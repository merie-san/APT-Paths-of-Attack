# APT-Paths-of-Attack
Degree thesis for the Bachelor in Computer Science University of Florence. <br>
Thesis' Supervisors: prof. Andrea Ceccarelli, Tommaso Puccetti. <br>
Note: some attack scripts like the qos_mid_dos.py were not finished. <br>
For more information see the main pdf file on the thesis.
## Updates
Updated and added new scripts for the paper "create and use a representative dataset for APT detection" in "new_src" folder. <br>
The new module "APT" allows for higher efficiency, simplicity and customizability when building and running APT attacks: <br>
- APT allows you to define new tipes of Reconnaissance and Discovery steps dinamically by creating RecStep and DiscStep objects
- high number of already implemented Reconnaissance and Discovery steps
- easily extendable with new exploit types by extending the abstract class ExploitStep and implementing the required abstract methods
- dinamically configurable by allowing to chain the steps in different ways, to repeat each step and the entire attack any number of times.
- presence of special steps like the PauseStep or the DistributedExploit which allow for further customization of the attack paths <br>
For more information see the APT.py file and the usage showcase in example_APT_usage.py
