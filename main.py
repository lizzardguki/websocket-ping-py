import websocket-ping
from subprocess import Popen
import sys
import os
import psutil
import logging 

def restart_program():
    """Restarts the current program, with file objects and descriptors
       cleanup
    """

    try:
        p = psutil.Process(os.getpid())
        for handler in p.get_open_files() + p.connections():
            os.close(handler.fd)
    except Exception  :
        print("")

    python = sys.executable
    os.execl(python, python, *sys.argv)

def __main__():
    try:
        print ("ALL OK!")
        websocket-ping.sendonline()
        while True:
            while websocket-ping.checktime() == False :
                print("Checking time")
            else:
                websocket-ping.sendonline()
    except: 
        restart_program()
    
    return

if __name__ == "__main__":
    if websocket-ping.__main__() == True:
        __main__()
    pass
        
