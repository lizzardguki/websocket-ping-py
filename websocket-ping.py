
import asyncio 
import websockets
import urllib.request
import time
import sys
import os
remotetime = ''
def internet_on():
    try:
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlopen("http://google.com")
        print("Connection available!")
        return True
    except: 
        print("Connection unavailable!")
        time.sleep(5)
        return False
 

def checkcfg():
    if os.path.isfile("config.cfg") == True :
      print("Config file exist!")
      return True
    else:
        print("Please create config.cfg")
        time.sleep(2)
        return False
    
async def connect(msg):
    try:
        async with websockets.connect(opencfg(1)) as socket:
         await socket.send(msg)
         result = await socket.recv()
         return result
    except:
        return result        

def get_command(command):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(connect(command)))
    return result

def synced():
    global remotetime

    try:
        remotetime = asyncio.get_event_loop().run_until_complete(asyncio.gather(connect("gettime")))
    except:
        internet_on()
        print(opencfg(1))

    for i in range(0, len(remotetime)): 
        
        remotetime[i] = int(remotetime[i]) 
        remotetime2 = (str(remotetime))
        remotetime2 = remotetime2.replace("[","")
        remotetime2 = remotetime2.replace("]","")
        if int(remotetime2) == int(time.time()) or (int(remotetime2) + 1) == int(time.time()) or  (int(remotetime2) - 1) == int(time.time()) or (int(remotetime2) + 2) == int(time.time()) or  (int(remotetime2) - 2) == int(time.time()) or (int(remotetime2) + 3) == int(time.time()) or  (int(remotetime2) - 3) == int(time.time()):
            print ("SYNCED!")
            print (remotetime2 + "   |    " + str(int(time.time())))
            return True
        else:
            print("Not synced")
            print (remotetime2 + "   |    " + str(int(time.time())))
            time.sleep(2)
            return False
            

def opencfg (x) : # Open a certain line of config.cfg
    f=open('config.cfg')
    line=f.readlines()
    return (line[x].replace("\n", ""))
def savecfg(edit,x) :
    with open('config.cfg', 'r') as file: # read a file
        data = file.readlines() # read files
        data[x] = (edit + "\n") #edit a certain line ([X] line number, [edit] text to write)
        with open('config.cfg', 'w') as file:
            file.writelines( data ) # saves the edited file
    return

def sendonline():
    try:
        result = asyncio.get_event_loop().run_until_complete(asyncio.gather(connect(opencfg(0) +"|online")))
    except:
        internet_on()
        return
    result2=str(result[0])
    savecfg(str(int(result2)),2 )
    return (str(result2))

def checktime():
    while int(opencfg(2)) > int(time.time())  :
        print (str(opencfg(2)) + "  |  " + str(int(time.time())))
        time.sleep(1)
        return False
    else:
        if int(opencfg(2)) == int(time.time())  :
            print("I should send online" + " " + str(int(time.time())))
        return True

def __main__():
    if internet_on() == True and checkcfg() == True and synced() == True:
        return True
    else:
        return False

if __name__ == "__main__":
    __main__()
        
    pass
