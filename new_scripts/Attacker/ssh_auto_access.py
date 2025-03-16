import paramiko
import argparse
import time
import random


def execute_command(client, command, password):
    """Execute a command on the remote server, handling sudo prompts."""
    # Start the command execution
    stdin, stdout, stderr = client.exec_command(command)

    # If the command requires sudo, provide the password
    if "sudo" in command:
        stdin.write(password + "\n")  # Send the password
        stdin.flush()  # Ensure the command is sent

    # Wait for the command to finish and capture the output
    exit_status = stdout.channel.recv_exit_status()  # This will block until the command finishes

    output = stdout.read().decode('utf-8')
    error_output = stderr.read().decode('utf-8')

    return exit_status, output, error_output
    

def ssh_commands(hostname, username, password, commands, inf_wait_time, sup_wait_time, logfile):
    # Create an SSH client
    client = paramiko.SSHClient()
    # Automatically add untrusted hosts (make sure okay for your use case)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Connect to the host
        client.connect(hostname, port=22, username=username, password=password)
        print(f"Connected to {hostname}")

        with open(logfile, 'w') as log:
            # Execute each command
            for command in commands:
                print(f"Executing command: {command}")
                log.write(f"Executing command: {command}\n")

                # Execute the command and wait for it to complete
                exit_status, output, error_output = execute_command(client, command, password)
                
                if exit_status == 0:
                    print(f"Command '{command}' completed successfully.")
                    log.write(output + "\n")
                else:
                    print(f"Command '{command}' failed with exit status {exit_status}.")
                    print(error_output)
                    log.write(f"Error: {error_output}\n")
                
                # Print output to the console as well
                print(output)
                
                # Random wait between inf_wait_time and sup_wait_time seconds
                wait_time = random.randint(inf_wait_time, sup_wait_time)
                print(f"Waiting for {wait_time} seconds before next command.")
                time.sleep(wait_time)

    finally:
        # Close the connection
        client.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='SSH into a server and run commands')
    parser.add_argument('hostname', help='The hostname or IP address of the remote server')
    parser.add_argument('username', help='The username to authenticate as')
    parser.add_argument('password', help='The password to authenticate with')
    parser.add_argument('commands', help='The commands to run on the remote server, separated by semicolons')
    parser.add_argument('inf_wait_time', type=int, help='First number for random wait time range')
    parser.add_argument('sup_wait_time', type=int, help='Second number for random wait time range')
    parser.add_argument('logfile', help='Path to the logfile')
    parser.add_argument('redirect_port', type=int, help='The port to redirect traffic to')

    args = parser.parse_args()
    
    # Split the commands string by semicolons to get a list of commands
    commands_list = args.commands.split(';')
    
    ssh_commands(args.hostname, args.username, args.password, commands_list, args.int_1, args.int_2, args.logfile, args.redirect_port)
