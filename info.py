print(""" ______   ______ _____ _____ __  __
/ ___\ \ / / ___|_   _| ____|  \/  |
\___\ \ V /\___ \ | | |  _| | |\/| |
 ___) || |  ___) || | | |___| |  | |
|____/ |_| |____/ |_| |_____|_|  |_|

 ___ _   _ _____ ___  ____  __  __    _  _____ ___ ___  _   _
|_ _| \ | |  ___/ _ \|  _ \|  \/  |  / \|_   _|_ _/ _ \| \ | |
 | ||  \| | |_ | | | | |_) | |\/| | / _ \ | |  | | | | |  \| |
 | || |\  |  _|| |_| |  _ <| |  | |/ ___ \| |  | | |_| | |\  |
|___|_| \_|_|   \___/|_| \_\_|  |_/_/   \_\_| |___\___/|_| \_|""")




print("                     Tool By-- <<<DARK_CYBER_WEAPON>>>")



print("DATE AND TIME")
print(" ")


import datetime
e = datetime.datetime.now()
print ("Current date and time = %s" % e)
print("DATE>>>")
print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))
print("TIME>>>")
print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))
print("")








import platform

print("___DARK CYBER WEAPON SYSTEM INFORMATION___")

print(" ")
print(" ")
 
print("ANDROID SYSTEM")
my_system = platform.uname()
 
print("SYSTEM+>>>")
print(f"System: {my_system.system}")
print("NODE NAME+>>>")
print(f"Node Name: {my_system.node}")
print("SYSTEM RELEASE+>>>")
print(f"Release: {my_system.release}")
print("SYSTEM VERSION+>>>")
print(f"Version: {my_system.version}")
print("SYSTEM MACHINE+>>>")
print(f"Machine: {my_system.machine}")

print("")
print("<<<IP INFORMATION>>>")
print(" ")
print("YOUR IP ADDRESS IS")
print(" ")
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()

print("FINISHED!!!!!")
