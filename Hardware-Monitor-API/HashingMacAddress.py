#from uuid import getnode as get_mac
from getmac import get_mac_address as gma
import hashlib
import os

def getHash256MAC():
    #mac = get_mac()
    mac = gma()
    mac = str(mac).encode('utf8')
    machash = hashlib.sha256()
    machash.update(mac)
    
    #print(machash.hexdigest())
    arquivoHash = open("hashmac","w+")
    arquivoHash.write(machash.hexdigest())

def readHashMAC():
    getHash256MAC()
    f = open("hashmac", "r")
    from sys import platform
    if f.mode == 'r':
        conteudo = f.read()
        if platform != 'win32':
            os.remove("hashmac")
        else:
            import subprocess
            subprocess.Popen('del hashmac', shell=True, stdout = subprocess.PIPE, stderr= subprocess.PIPE)
        return conteudo

#getHashMAC()
if __name__ == '__main__':
    print(readHashMAC())
