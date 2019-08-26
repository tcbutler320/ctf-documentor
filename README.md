*Disclaimer: This is under developement. Once a full, CTF-ready version is ready to be rolled out, it will be launched as v1.0.

# ctf-automator
One stop application for CTF's, create a project directory, run common pen-test scans, all in one place

<img src="/images/ctf-scans.png" alt="drawing" width="800"/>

## Overview
CTF Automator is a central hub for simple scanning and documentation often used during CTF boot2root competitions. It helps you organize your scans and places all enumeration information in an easy to use format. The CTF Automator includes, or will include the following features...

1. Create CTF Project folder and txt files for important information like the output of scans, flags, found vulnerabilities, etc.
2. Use pre-configured buttons to simply run automated scans for target discovery, port and service scanning, vulnerability mapping, exploits, etc.
3. Parse output of commonly used tools with python for keywords/phrases
4. Create a uniformed system of operations to simplify team sharing when competing with groups

## Requirements
CTF Automator is designed to be run on Kali Linux. It's been tested on Kali and should work fine. While it will work on other unix distributions, be aware that the layout and UI will be very different. This tool was not intended to be run outside of Kali Linux, and its capabilities and ease of use will vary greatly depending on which version its run in. I will add os handling in later versions.

## Use
Clone the repository to your local machine. To run, navigate inside the folder and type (python automator-gui.py). The first thing you should do is create a project using the button on the left frame. Enter a project name in the popup window (keep in mind this is the only way to get started, as the import project function is not finished yet). After you click create, exit out of the popup window.

The first time to do is use the target discovery tools located on the bottom tool panel. The only tool currently set up is the arp-scan function. Run arp-scan to get a list of targets on your local network. Keep in mind that if you have several network interfaces up and running, arp-scan might not give you the targets your looking for. The output of the scan will be placed in the main output panel above. All scan output will also be saved in a text file in your project directory for later reference.

Navigate over to the port scan tab. Enter one of the targets above into the "set target" entry box. Click add targets to add the target to your scope. Now you can run an nmap scan. The two functions currently working are nmap and intense nmap. Click on these to run.

## Limitations
Not all functions or buttons are currently running. This project is being developed in an ad-hoc manner, and I am not only learning the basics of python, but also UI design and software developement.

## What works vs What Doesn't
Not every feature you see on CTF automator is currently supported.

### What Works
Create project : Create a project folder and a scans and flag txt files.
Arp-scan : Arp scan network for potential targets
Set Target : Choose an IPv4 address to set as a target machine
Nmap Scan : Run a quick nmap scan of the target (nmap -T 5 [target])
Nmap Intense: Run an intense nmap scan of the target for all ports, service and version discovery (nmap -sS -sV -A -O -p- [target])
Add Flag: Enter a flag, add to flag.txt
Help Output: A text output on the lefthand panel to tell you the status of commands
Home Output: A text output on the middle page to display usefull output of scans

### What doesn't work
Open a project : Almost complete
Netdiscover : Not started
Net Stat : Not started
Nmap UDP : Not started
Linux Enumeration : Not started
Chat : Not started
Settings: Not started
Compromat : Not started
About : Not started


## Contributions
Feel free to contribute as desired. Looking for issues and feature requests.

## Dev Roadmap
The first working branch of this project (v1.0), should be released in early June 2019. Below is a list of known features and issues to be included.
1. Separate GUI and logic.py files
2. Add error handling and exception for functions
3. Add multiple OS support with sys module
4. Add tkinter menu
5. Update UI with branding/color
6. Create config file for custom user settings
7. Add support for more scanning tools

## UI application
See the below rough sketch of what the final UI will look like
<img src="/images/UI-plan" alt="drawing" width="800"/>
