*Disclaimer: This application is under developement. Once a full, CTF-ready version is ready to be rolled out, it will be launched as v1.0. 

*Disclaimer 2: This application does not reflect on my employeer, as it is a personal project. 

# CTF Documentor Overview
Run and save common enumeration and vulnerability scans for CTF competitions. Built on python and designed for Kali Linux.

Home Dashboard: 
![alt text](/images/ctf-scans.png "Nmap Scans in CTF Documentor")

# Index
- [CTF Documentor Overview](#ctf-documentor-overview)
- [Index](#index)
  - [Overview](#overview)
  - [Getting Started](#getting-started)
  - [System Requirements Requirements](#system-requirements-requirements)
  - [Installation](#installation)
  - [Running for the First Time](#running-for-the-first-time)
  - [Use](#use)
  - [Limitations](#limitations)
  - [Dev Roadmap](#dev-roadmap)
  - [Contributing](#contributing)

## Overview
CTF Documentor is a central hub for simple scanning and documentation often used during CTF boot2root competitions. It helps you organize your scans and places all enumeration information in an easy to use format.

## Getting Started
CTF Documentor was built and intended to be used on the latest version of Kali Linux for virtualbox. At the time of this release you can download this image [here](https://www.offensive-security.com/kali-linux-vm-vmware-virtualbox-image-download/)

## System Requirements Requirements

1) Kali Linux for Virtual Box and the following programs
    A) Nmap, Dirb, arp-scan, dirb, sparta, netdiscover

## Installation
To get started, launch your kali linux machine in Virtualbox. Make sure to give your machine an internet connection by enabling the NAT adaptor and having internet conmnection to your local machine. 

In the terminal of your linux machine change directories to your desktop by entering,

        cd Desktop

Then, clone the repository to your desktop with the command,

        git clone https://github.com/tcbutler320/CTF-Documentor

## Running for the First Time
To open and run the application, navigate inside the directory with the terminal command 

        cd CTF-Documentor 

Run the program with 

        python ./automator-gui.py

The program is up and running properly if you are greeted with this home dashboard 

Home Dashboard: 
![alt text](/images/home-dashboard.png "Nmap Scans in CTF Documentor")

## Use
Before launching enumeration or vulnerability scans,you first must create a project using the new project button. 

Creating a Project: 
![alt text](/images/create-project.png "Creating a project")

After creating a project, you will need to add a target to the project scope in order to conduct any scanning. There are two ways to do this. Navigate over to the target discvory tab on the tools bar in the bottom of the dashboard. Using the arp-scan button will search your connected network for IP's found in address resolution protocol communications. You can add one of these IP's to the project scope by navigating to the port scan tab, and entering the ip into the feild below and clicking set target

Adding a Target to Scope: 
![alt text](/images/ctf-scans.png "Adding an IP to scope")

With a target set, you are now able to use the pre-set enuneration buttons for a variety of scans. Nmap, Nmap Intense, and Nmap UDP are pre-defined nmap scans which can be activated by presses the button.


## Limitations
For the time being, the CTF Documentor only runs in Kali Linux.

## Dev Roadmap
Check back often for updated informaiton about the development roadmap for this project. I am using this project as a template and repository for learning software design, devops, penetration testing, and CTFs

## Contributing 
If your interested in contributing to the project, feel free to do so on your on terms. You may reach out on twitter or other platforms for questions or ideas for enhancements.