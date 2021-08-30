# subprocess module will help us to execute commands on device and optparse will help us to use arguments like --help in our program
import subprocess
import optparse
import re

print('''
                           


░█▀▄▀█ █▀▀█ █▀▀ 　 █▀▀█ █▀▀▄ █▀▀▄ █▀▀█ █▀▀ █▀▀ █▀▀ 　 
░█░█░█ █▄▄█ █── 　 █▄▄█ █──█ █──█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 　
░█──░█ ▀──▀ ▀▀▀ 　 ▀──▀ ▀▀▀─ ▀▀▀─ ▀─▀▀ ▀▀▀ ▀▀▀ ▀▀▀ 　 

█▀▀ █──█ █▀▀█ █▀▀▄ █▀▀▀ █▀▀ █▀▀█ 
█── █▀▀█ █▄▄█ █──█ █─▀█ █▀▀ █▄▄▀ 
▀▀▀ ▀──▀ ▀──▀ ▀──▀ ▀▀▀▀ ▀▀▀ ▀─▀▀ 

''')
print("Made by akshay-cybersec")
print("Github link - https://github.com/Akshay-cybersec")
print("\n")

def get_arguments():
    parser = optparse.OptionParser() # this line will make a parser so that we cann add option in it like -i -m --help
    # adding option and sending it in destination so that we can use it letter by typing variable.interface and variable.macaddr
    parser.add_option("-i","--interface",dest="interface",help="Interface to change mac_address")
    parser.add_option("-m","--mac",dest="macaddr",help="New mac_address to change")
    # parser.parse_args() will put all the above args in our progtam and return us two value becuz 
    # we have added 2 options in our program and we stored it in variable called options and arguments
    (options,arguments)= parser.parse_args()
    # if user did not specify mac or interface then this error will be showned
    if not options.interface:
        parser.error("Please specify interface , use --help for information")
    elif not options.macaddr:
        parser.error("Please specify macaddress , use --help for information")
    else:
        # if user entered all values we needed to change mac then it will return that options provided by user
        return options

def change_mac(interface,macaddr):
    # this will run commands in system
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",macaddr])
    subprocess.call(["ifconfig",interface,"up"])

def mac_check(interface):
    # .check_output will run command and return output which system has given
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # re.search will find string in ifconfig_result variable
    # \w:\w is pattern of regular expression which find string using its rule
    # https://pythex.org/   here we can make rules as per requirement
    current_mac = re.search(b"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
    if current_mac:
        curmac = str(current_mac.group(0),'utf-8')
        return curmac
    else:
        return "None"

options = get_arguments() # the options which get_arguments() has written are stored in options 
currentmac = mac_check(options.interface)
if currentmac == "None":
    print("THe device you specified does not contain mac address so unable to change")
else:
    print("Current mac = "+ currentmac)
change_mac(options.interface,options.macaddr) # change_mac() function is run and options.interface will contain interface name and so on

new_mac = mac_check(options.interface)
if new_mac == options.macaddr:
    print("Mac changed successfully")
    print("New mac = "+ new_mac)
else:
    print("error")


