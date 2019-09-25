#!/usr/bin/python

# CTF Documentor, the one stop shop tool for CTF's
# Created by Tyler Butler @butler_devsec & tylerbutler.info

# Import modules
from Tkinter import *
import ttk
import subprocess
import os
import sys
from datetime import datetime
from PIL import ImageTk, Image

# Define Global Variable
about = 'Welcome to the CTF Documentor\n\nThis tool is designed simplify your organization for CTF boot to root events. Creating a new project in CTF Documentor will create a new project direcory, and appropriate files. It allows you to perform your scans and dump them into neatly formatted txt files.\n\nWhen your ready to review the output of your scans, CTF Automtor provides an easy way to review what youve done.\n\nHelp Running CTF Documentor\n\nFor help, see the readme.me or the help infomrmation on this projects GitHub page.'
project_name = ""
target = ""
rawflag = []
path = ""
date = ""
adaptor = ""

#### Program Functions ####


# Quit the program
# Command fully implemented
def quit_command():
    sys.exit()
    return()

# Get a flag from the user, add it to the flag.txt file and the flag display
# Command fully implemented
def add_flag():
    global rawflag
    flag_buffer = ""
    if True:
        flag_buffer = flags_entry.get()
        with open(project_name+'/'+'flags.txt','a') as f:
            f.write('Flags found:  '+flag_buffer+'\n\n=================================\n\n')
            f.close()
        help_text.insert("1.0","Flag added\n\n")
        flags_text.insert("1.0","Flag Found:  "+flag_buffer+"\n\n")
    else:
        help_text.insert("1.0","{!} Error Adding Flag")
        return
    return

# Send a flag to a flag server for
# Function not implemented
def send_flag():
    help_text.insert("1.0","Send Flag not supported!\nIf you'd like, contribute to this project\n\n")
    return

# On user command, open a new window to enter a project name and directory location
# Function fully implemented
def popup_newproject():
    global project_name
    global date
    date = datetime.today().strftime('%y-%m-%d')
    def create():
        global project_name
        project_name = project_entry.get()
        if len(project_name) > 0 :
            help_text.insert("1.0","Creating Project...\n")
            os.mkdir(project_name)
            with open(project_name+'/scans.txt','w') as f:
                f.write('Date: '+date+'\nCTF Documentor\nNew Project: '+project_name+'\n\nScans\n\n')
                f.close()
            help_text.insert("1.0","Created output file\n")
            with open(project_name+'/'+'flags.txt','w') as f:
                f.write('Date'+date+'\nCTF Documentor\nNew Project: '+project_name+'\n\nFlags\n\n')
                f.close()
            help_text.insert("1.0","Created flag file\n")
            cmd =['pwd']
            directory = subprocess.check_output(cmd)
            help_text.insert("1.0","""Project located at """+directory+"""Project ''"""+project_name+"""' Created!\n""")
            new_project.destroy
            return
        else:
            help_text.tag_config('RED', foreground='red')
            help_text.insert("1.0","You must enter a project name\n","RED")
            return

    new_project = Toplevel(height=150,width=350)
    new_project.title('Create New Project')
    enter_project_label = Label(new_project, text='Enter Project Name')
    enter_project_label.place(x=5,y=5)
    project_entry= Entry(new_project)
    project_entry.place(x=155,y=5)
    enter_location_label= Label(new_project,text='Enter Save Location')
    enter_location_label.place(x=5,y=55)
    location_entry= Entry(new_project)
    location_entry.insert(END,'Default is current directory')
    location_entry.place(x=155,y=55)
    create_button= Button(new_project,text='Create Project',command=create)
    create_button.place(x=5,y=85)
    new_project.destroy
    return()

# On uper command, open a new window to choose an existing project to continue working on
# {!} ISSUE 
def popup_openproject():
	global path
	def open_project():
		global path
		path = open_entry.get()
		help_text.insert("1.0","Changing Directory....\n")
		os.chdir(path)
		help_text.insert("1.0","Directory changed to"+path+"\n")
		return

	openproject = Toplevel(height=150,width=350)
	openproject.title('Open Project')
	open_project_label = Label(openproject, text='Path to Project')
	open_project_label.place(x=5,y=5)
	open_entry= Entry(openproject)
	open_entry.place(x=115,y=5)
	open_button= Button(openproject,text='Open',command=open_project)
	open_button.place(x=85,y=40)
	return

# On button click, run arp-scan to find targets on network, print to display and text file
# Function fully implemented
def arp_scan():
	global project_name, adaptor
	help_text.insert("1.0","Running Arp-Scan...\n")
	cmd =['arp-scan','-I',adaptor,'-l']
	returned_value = subprocess.check_output(cmd)
	output_text.insert("1.0",returned_value.decode("utf-8"))
	write_value = str(returned_value.decode("utf-8"))
	print(write_value)
	if 1 == 1:
		with open(project_name+'/scans.txt','a') as f:
			f.write('\nARP Scan Results\n\n=============================\n\n')
			f.write(write_value)
			help_text.insert("1.0","Targets Acquire,Located in Outut\n")
			f.close()
		return()
	return()

# Get user input ipv4 address and set it to the target global variable
# Function fully implemented
def add_target():
    global target
    target = target_entry.get()
    if len(target) > 0 :
        help_text.insert("1.0","Setting Target...\n")
        os.mkdir(project_name)
        with open(project_name+'/scans.txt','w') as f:
            f.write('CTF Documentor\nNew Target Added:'+target)
            f.close()
        return()
    else:
        help_text.tag_config('RED', foreground='red')
        help_text.insert("1.0","You must enter a target\n","RED")
        return()

# Run an nmap scan against the target, if no target was selected, tell the user to enter a target or get help
# Function fully implemented
def nmap_target():
    global target
    help_text.insert("1.0","Running Nmap\n")
    target = target_entry.get()
    if len(target) > 0:
        cmd =['nmap',target]
        returned_value = subprocess.check_output(cmd)
        output_text.insert("1.0",returned_value.decode("utf-8"))
        write_value = str(returned_value.decode("utf-8"))
        with open(project_name+'/scans.txt','a') as f:
            f.write('\nNmap Scan Results\n=========================================\n\n')
            f.write(write_value)
            f.close()
        help_text.insert("1.0","Nmap done! Check Output Tab\n")
        return()
    else:
        help_text.tag_config('RED', foreground='red')
        help_text.insert("1.0","Enter a valid Target\n","RED")

# Run a more intense nmap scan
# Function fully implemented
def nmap_intense():
    global target
    help_text.insert("1.0","Running Intense Nmap\n")
    target = target_entry.get()
    st_target = str(target)
    cmd2 = ['nmap','-sS','-sV','-A',st_target]
    if len(target) > 0:
        returned_value = subprocess.check_output(cmd2)
        output_text.insert("1.0",returned_value.decode("utf-8"))
        write_value = str(returned_value.decode("utf-8"))
        with open(project_name+'/scans.txt','a') as f:
            f.write('\nIntense Nmap Scan Results\n=========================================\n\n')
            f.write(write_value)
            f.close()
        help_text.insert("1.0","Nmap done! Check Output Tab\n")
        return()
    else:
        help_text.tag_config('RED', foreground='red')
        help_text.insert("1.0","Enter a valid Target\n","RED")

# Run an nmap scan for UDP ports
# Function fully implemented
def nmap_udp():
    help_text.insert("1.0","Scanning UDP ports wth Nmap\n")
    target = target_entry.get()
    st_target = str(target)
    cmd2 = ['nmap','-sU','''-p-''',st_target]
    if len(target) > 0:
        returned_value = subprocess.check_output(cmd2)
        output_text.insert("1.0",returned_value.decode("utf-8"))
        write_value = str(returned_value.decode("utf-8"))
        with open(project_name+'/scans.txt','a') as f:
            f.write('\nUDP Nmap Scan Output\n=========================================\n\n')
            f.write(write_value)
            f.close()
        help_text.insert("1.0","UDP Ports Scanned!\n")
        return()
    else:
        help_text.tag_config('RED', foreground='red')
        help_text.insert("1.0","Enter a valid Target\n","RED")

# Print some helpful information
# Helpme.md has not been built out yet 
def helpme():
    help_text.insert("1.0","Open the readme file for more information. This is a pre-release version of ctf Documentor, not all features you see are currently supported. Consider making contributions to the project")
    return()

# Run dirb against a target to enumerate web servers, find hidden web directories
# Function fully implemented
# test
def dirb():
    global target
    help_text.insert("1.0","Running Dirb\n")
    target = target_entry.get()
    dirb_target = str('http://'+target)
    help_text.insert("1.0","Running Dirb Command: "+dirb_target)
    if len(target) > 0:
        cmd =['dirb',dirb_target, '-S']
        returned_value = subprocess.check_output(cmd)
        output_text.insert("1.0",returned_value.decode("utf-8"))
        write_value = str(returned_value.decode("utf-8"))
        with open(project_name+'/scans.txt','a') as f:
            f.write('\nDirb Results\n=========================================\n\n')
            f.write(write_value)
            f.close()
        help_text.insert("1.0","Dirb Complete! Check Output Tab\n")
        return()
    else:
        help_text.tag_config('RED', foreground='red')
        help_text.insert("1.0","Enter a valid Target\n","RED")
    return

# Run sparta, this just opens sparta and does not add to project files
# Function fully implemented
def sparta():

    help_text.insert("1.0","Opening Sparta\n")
    cmd =['sparta']
    subprocess.check_output(cmd)
    return

# use netdiscover for target discovery
# Function not built yet
def netdiscover():
	global project_name, adaptor
	help_text.insert("1.0","Running Netdiscover...\n")
	cmd =['netdiscover','-i',adaptor,'-f']
	returned_value = subprocess.check_output(cmd)
	output_text.insert("1.0",returned_value.decode("utf-8"))
	write_value = str(returned_value.decode("utf-8"))
	print(write_value)
	if 1 == 1:
		with open(project_name+'/scans.txt','a') as f:
			f.write('\nNetdiscover Scan Results\n\n=============================\n\n')
			f.write(write_value)
			help_text.insert("1.0","Targets Acquire,Located in Outut\n")
			f.close()
		return()
	return()

# Quit CTF Documentor
# Function fully implemented
def quit():
    sys.exit()

# Git Clone CTF Playbook
# {!} Function Not Tested
def git_playbook():
    cmd =['git clone https://github.com/tcbutler320/ctf-playbook']
    try:
        output = subprocess.check_output(cmd)
        cmd_2 = ['leafpad /ctf-playbook/README.md']
    except:
        print("{!} Exception: Could not connect to GitHub \n Check Internet Settings")

def get_myip():
    global target
    help_text.insert("1.0","Getting IP\n")
    try:
		cmd =['ifconfig']
		returned_value = subprocess.check_output(cmd)
		output_text.insert("1.0",returned_value.decode("utf-8"))
		write_value = str(returned_value.decode("utf-8"))
		with open(project_name+'/scans.txt','a') as f:
		    f.write('\nGet MyIp Scan Results\n=========================================\n\n')
		    f.write(write_value)
		    f.close()
		help_text.insert("1.0","IP Found! Its " + write_value + "\n")
		return
    except:
		print("{!} Exception")
    return

def set_adaptor():
	global adaptor
	adaptor = adaptor_entry.get()
	if len(adaptor) > 0 :
		help_text.insert("1.0","Setting Adaptor...\n")
		with open(project_name+'/scans.txt','w') as f:
			f.write('CTF Documentor\nNew Adaptor Set:'+adaptor)
			f.close()
			return()
	else:
		help_text.tag_config('RED', foreground='red')
		help_text.insert("1.0","You must enter a valid adaptor\n","RED")
	return()


#### Gui Configurations ####

# Main Gui
main = Tk()
main.title('CTF Documentor')
main.geometry('820x800')

# set style params
style = ttk.Style()
style.configure('My.TFrame', background='#e8e8e8')
style.configure('My.TButton', background='#e0e0e0',foreground='#000000')
style.configure('My.TLabel',background='#535353',foreground='#000000')

# create a menu bar
menubar = Menu(main)
project_menu = Menu(menubar, tearoff=0)
project_menu.add_command(label="Create New",command=popup_newproject)
project_menu.add_command(label="Open",command="open_command")
project_menu.add_command(label="Send Project",command="send_project")
menubar.add_cascade(label='Edit',menu=project_menu)
menubar.add_command(label='Quit',command=quit_command)
flags_menu = Menu(menubar,tearoff=0)
flags_menu.add_command(label='Add Flag',command=add_flag)
flags_menu.add_command(label='Send Flag',command=send_flag)
menubar.add_cascade(label='Flags',menu=flags_menu)
menubar.add_command(label='Help',command=helpme)
main.config(menu=menubar)

# Main Gui Window

# Main Left Frame
left_frame= Frame(main,width=200,height=800)
left_frame.place(x=0,y=0)
left_top_frame= Frame(left_frame,width=200,height=400)
left_top_frame.place(x=0,y=0)

# Help Output Text Bar and Label
help_text_label = Label(left_frame,text='Help Bar')
help_text_label.place(x=10,y=230)
help_text = Text(left_frame,bg='black',fg='white',height=20,width=20,wrap=WORD)
help_text.insert(INSERT,'Welcome to the CTF Documentor!\n\nStart by creating a new project.This is where useful information will be printed when you run commands.The useful output of scans will show up on your right.\n\n If you need help, click the help button or visit the readme at https://github.com/tcbutler320/ctf-documentor')
help_text.place(x=10,y=250)

# Add logo image to main window
path = 'logo2.png'
imgpath = 'logo2.png'
img = PhotoImage(file=imgpath)
img = img.subsample(3)
project_name_label = Label(left_frame, image=img)
project_name_label.config(font=("Courier", 20))
project_name_label.place(x=10 ,y=2)

# Set Adaptor Button
set_adaptor_button= ttk.Button(text='Set Adaptor',style='My.TButton',command=set_adaptor)
set_adaptor_button.place(x=10,y=610)
adaptor_entry = Entry(left_frame)
adaptor_entry.place(x=10, y=650)

# Main Buttons
new_project_button= ttk.Button(text='New Project',style='My.TButton',command=popup_newproject)
new_project_button.place(x=2,y=185)
open_project_button= ttk.Button(text='Open Project',style='My.TButton', command=popup_openproject)
open_project_button.place(x=100,y=185)

# Main Botton Frame
botton_title_frame= Frame(main,width=600,height=20)# bg='grey12',
botton_title_frame.place(x=200,y=425)

# Bottom Tools Label
tools_label= Label(botton_title_frame,text='Tools',fg='#000000')#,bg='grey12',
tools_label.place(x=0,y=0)

# This was from overstack, not sure why its needed, but it breaks if this isnt here lol
rows = 0
while rows < 50:
    main.rowconfigure(rows,weight=1)
    main.columnconfigure(rows,weight=1)
    rows += 1

# Configure the notebook Settings
# Top Output Notebook
nb = ttk.Notebook(main,width=600,height=400)
nb.place(x=200,y=0)

# Page 1:Home Page
home= ttk.Frame(nb,style='My.TFrame')
nb.add(home, text='Main')
output_text = Text(home,bg='black',fg='white',height=400,width=200,wrap=WORD)
output_text.insert(INSERT,"You'll see the output of your scans here\n")
output_text.place(x=0,y=0)

# Page 2: Flags
flags= ttk.Frame(nb)
nb.add(flags,text='Flags')
flags_text = Text(flags,bg='black',fg='white',height=400,width=600,wrap=WORD)
flags_text.insert(INSERT,'Found Flags will be added here\n')
flags_text.place(x=0,y=0)

# Page 3: Compromat
compromat = ttk.Frame(nb)
nb.add(compromat,text='Compromat')
compromat_text = Text(compromat,bg='black',fg='white',height=400,width=600,wrap=WORD)
compromat_text.insert(INSERT,"""The Compromat is a selection of all the compromising materials you've found. This includes things like vulnerabilities, backdoors, usernames and passwords, etc\n""")
compromat_text.place(x=0,y=0)

# Page 4: Chat
page4= ttk.Frame(nb)
nb.add(page4, text='Chat')
chat_text = Label(page4,text="To chat with other users of ctf-documentor, start listener\n")
chat_text.place(x=5,y=5)

lport_text = Label(page4, text="Set Listener Port")
lport_text.place(x=5, y=25)

lport_entry = Entry(page4)
lport_entry.place(x=175, y=25)

start_listener_button = Button(page4, text="Set Port")
start_listener_button.place(x=5,y=50)

start_listener_button = Button(page4, text="Start Listener")
start_listener_button.place(x=175,y=50)

# Page 5: About
about= ttk.Frame(nb)
nb.add(about, text='About')
about_text = Text(about,bg='black',fg='white',height=400,width=600,wrap=WORD)
about_text.insert(INSERT,"This is the about page\n")
about_text.place(x=0,y=0)

# Page 6: Settings
settings= ttk.Frame(nb)
nb.add(settings, text='Settings')

# Botton Tools Notebook
nb_tools = ttk.Notebook(main,width=600,height=380)
nb_tools.place(x=200,y=445)

# Target Discovery Tools Page for Bottom Notebook
# "Target Discovery" becomes "Reconnaissance 1" in this feature branch
discovery= ttk.Frame(nb_tools,style='My.TFrame')
nb_tools.add(discovery, text='Reconnaissance 1')
reconnaissance_1_frame= Frame(discovery,height=320,width=600)#bg='grey50'
reconnaissance_1_frame.place(x=0,y=0)
recon_label = Label(discovery, text= "Discover Target")
recon_label.place(x=5,y=5)
arp_button= Button(reconnaissance_1_frame, text='Arp Scan',command=arp_scan)
arp_button.place(x=5,y=55)
netdiscover_button= Button(reconnaissance_1_frame, text='Netdiscover')
netdiscover_button.place(x=5,y=105)
netstat_button= Button(reconnaissance_1_frame, text='Net Stat')
netstat_button.place(x=5,y=155)
getmyip_button= Button(reconnaissance_1_frame, text='Get MyIP',command=get_myip)
getmyip_button.place(x=5,y=205)


# Port and Service Scan for Bottom Notebook
# "Port and Service Scan" becomes "Reconnaissance 2" in this feature branch 
port_scan= ttk.Frame(nb_tools,style='My.TFrame')
nb_tools.add(port_scan, text='Reconnaissance 2')
reconnaissance_2_frame= Frame(port_scan,height=320,width=600)#bg='grey50'
reconnaissance_2_frame.place(x=0,y=0)
target_elable= Label(port_scan,text='Enter Target')
target_elable.place(x=1,y=5)
target_entry = Entry(port_scan)
target_entry.place(x=135,y=5)
set_target_button= Button(reconnaissance_2_frame,text='Set Target',command=add_target)
set_target_button.place(x=335,y=5)
nmap_op_label = Label(reconnaissance_2_frame, text = "Nmap Enumeration Options")
nmap_op_label.place(x=5,y=55)
nmap_button= Button(reconnaissance_2_frame, text='Nmap',command=nmap_target)
nmap_button.place(x=5,y=105)
nmap_button= Button(reconnaissance_2_frame, text='Nmap Intense',command=nmap_intense)
nmap_button.place(x=5,y=155)
nmap_button= Button(reconnaissance_2_frame, text='Nmap UDP', command=nmap_udp)
nmap_button.place(x=5,y=205)

nse_op_label = Label(reconnaissance_2_frame, text = "NSE Scripting Engine")
nse_op_label.place(x=200,y=55)
nse_discovery= Button(reconnaissance_2_frame, text='NSE Discovery') #command=nse_discovery
nse_discovery.place(x=200,y=105)

# Tools for Linux Enumeration
# "Enumeration" will now be "Reconnaissance 3" in this feature branch
reconnaissance_3 = ttk.Frame(nb_tools, style='My.TFrame')
nb_tools.add(reconnaissance_3,text= 'Reconnaissance 3')
reconnaissance_3_frame = Frame(reconnaissance_3, height= 320, width =600)
reconnaissance_3_frame.place(x=0,y=0)
enum1 = Button(reconnaissance_3_frame,text='Example',command='example')
enum1.place(x=5,y=5)
enum2 = Button(reconnaissance_3_frame,text='Dirb',command=dirb)
enum2.place(x=200,y=5)

# Added weaponization tool page for this feature branch
weaponization_tools = ttk.Frame(nb_tools, style='My.TFrame')
nb_tools.add(weaponization_tools,text= 'Weaponization')
other_frame = Frame(weaponization_tools, height= 320, width =600)
other_frame.place(x=0,y=0)
sparta_button = Button(weaponization_tools,text='Sparta',command=sparta)
sparta_button.place(x=5,y=5)


# Other random tools
other_tools = ttk.Frame(nb_tools, style='My.TFrame')
nb_tools.add(other_tools,text= 'Other Tools')
other_frame = Frame(other_tools, height= 320, width =600)
other_frame.place(x=0,y=0)
sparta_button = Button(other_tools,text='Sparta',command=sparta)
sparta_button.place(x=5,y=5)

# Flag tab for bottom notebook
flags = ttk.Frame(nb_tools,style='My.TFrame')
nb_tools.add(flags, text='Flags')
flags_frame = Frame(flags,height=320,width=600)#bg='grey50'
flags_frame.place(x=0,y=0)
flags_entry = Entry(flags)
flags_entry.place(x=100,y=30)
flags_lable= Label(flags,text='Enter flag')
flags_lable.place(x=1,y=30)
flags_button = Button(flags,text='Add Flag',command=add_flag)
flags_button.place(x=100,y=60)

# Start Gui
main.mainloop()