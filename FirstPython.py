

print("""
##################################################

# Python3
# Made By Adkali With Love                   A    #
# Need Help? Learn Python!                   D    #
# This Challenge Made For Beginners          K    #
#  H            N                            A    #
#    A        U                              L    #
#      V    F                                I    #
         E
##################################################

""")
import hashlib
import datetime
import time
import base64
import getpass
import sys

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.050)
 
Work = input("\nPlease, Enter your Worker Name (a-z/A-z): ")
time.sleep(1.5)
print_slow("\nChecking Worker Named " + Work)
Wolf = hashlib.md5(b"\n\n\n\n\n.syslog").hexdigest()
time.sleep(1.5)
print_slow("\nAre You Authorized? Cheking Worker Name Permissions, Please Wait...")
time.sleep(2.0)
print("\n")
LoginPage = {

"User:": "Unknow/Anonymous........................",
"Access:": "Denied..............................",
"Proxy:": "Not Detected....................",

}

for x, y in LoginPage.items():
 print(x,y)
time.sleep(2.0)

for _ in range(2):
    for x in range(4):
      string = "A Suspicious Attempt Identified! Logout"+"."*x+""
      print("\033[K", string, end="\r")
      time.sleep(1.0)

time.sleep(2.0)
print("\n")
print("\033[0;31;47m Recording Everything: Event Number 3 \033[0;0m")
print("The Time And Date Now Are")
time.sleep(0.5)
x = datetime.datetime.now()
print(x)

time.sleep(1.2)
print("\nSystem Made Hard Reset!\nTry To Log In Again Please...") 

time.sleep(1.2)
print("\n")
Authorized = ['Admin', 'Jordan', 'BlackAuth', 'Shell', 'Guest', 'James.B']
print(Authorized)

NTUser = "Le0nard0"
OK = "Belf0rt" + str(Wolf)

loop = 'true'
while (loop == 'true'):

    access = input("Username Please: ")
    if access == NTUser:
        loop1 = 'true'
        while (loop1 == 'true'):
            Shell = getpass.getpass("Please enter your password: ")
            if Shell == "W0lf" + OK:
                print ("Welcome Back To WallStreet " + access)
                loop = 'false'
                loop1 = 'false'
            else:
                print ("Password incorrect!")

    else:
        print("Username incorrect!")
