#! python3
#This is following along to a Python for *Nix Administrators - Noah Gift and Jeremy M.Jones - 2011
#Some modifications have been made to update from 2.5.1 to 3.7

import socket
import re
import sys

def check_server(address,port):
    #create a tcp socket
    s=socket.socket()
    print (" Checking the connection on "+str(port)+" at "+address+" .")
    try: 
        s.connect((address,port))
        print("Connected sucessfully.")
        return True
    except socket.error:
        print ("The connection failed.")
        return False
if __name__=='__main__':
    from optparse import OptionParser
    parser=OptionParser()

    parser.add_option("-a","--address",dest="address", default='localhost',help="ADDRESS for server",metavar="ADDRESS")
    parser.add_option("-p", "--port", dest="port",type="int",default=80, help="PORT for server",metavar="PORT")

    (options,args)=parser.parse_args()
    check=check_server(options.address,options.port)
    print("check_server returned "+str(check)+" .")
    sys.exit(not check)