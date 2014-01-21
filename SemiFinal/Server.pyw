# Echo server program
import socket
from time import *
from graphics import *
from kev import *

global TextList
TextList = [Text(Point(2.5, 9.25), ''),
Text(Point(2.5, 8.75), ''),
Text(Point(2.5, 8.25), ''),
Text(Point(2.5, 7.75), ''),
Text(Point(2.5, 7.25), ''),
Text(Point(2.5, 6.75), ''),
Text(Point(2.5, 6.25), ''),
Text(Point(2.5, 5.75), ''),
Text(Point(2.5, 5.25), ''),
Text(Point(2.5, 4.75), ''),
Text(Point(2.5, 4.25), ''),
Text(Point(2.5, 3.75), ''),
Text(Point(2.5, 3.25), ''),
Text(Point(2.5, 2.75), ''),
Text(Point(2.5, 2.25), ''),
Text(Point(2.5, 1.75), '')]

def getIPv4(textFile):
    x = open(textFile, 'r')
    x = x.read()
    x = list(x)
    for i in range(listLength(x)):
        if x[i] is 'I':
            if x[i+1] is 'P':
                if x[i+2] is 'v':
                    if x[i+3] is '4':
                        empty = ''
                        for j in range(36, 57, 1):
                            if x[i+j] != '\n':
                                empty = empty + x[i+j]
                            else:
                                empty = empty
                                break
                        return(empty)

def Inbox():
    win = GraphWin("Callxr Inbox", 600, 400)
    win.setCoords(0,0,10,10)

    BG = Image(Point(5,5), 'IMG/ServerBG.gif')
    BG.draw(win)
    return(win)

def Mark(new, win):
    global TextList
    for i in TextList:
        i.undraw()
    TLine = Text(Point(3.4,1.25), new)
    TextList.append(TLine)
    for j in TextList:
        j.move(0,.5)
    for k in range(listLength(TextList) - 16, listLength(TextList), 1):
        TextList[k].draw(win)

def Recieve():    
    dataappender = ''
    while 1:
        #conn[Talker].sendall(data)
        def LetterConvert(data):
            Indexer = 0
            for qwerty in data:
                if qwerty == 'x':
                    Indexer = Indexer + 1
            return(Letters[Indexer])
        
        recvddata = conn.recv(1024)
        data = LetterConvert(str(recvddata))
        
        """one = (conn[1].recv(1024))"""
        if data != '`':
            dataappender = dataappender+data
            """Refresh()"""
            
        else:
            Mark(dataappender, win)
            dataappender = ''

win = Inbox()
HOST = getIPv4('ip.txt')    # The remote host
PORT = 5007       # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
Letters = ['~','`','A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z',' ','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','-','_','+','=',':',';','\'','"','{','}','[',']','\\','|','<','>','?','/','.',',']
s.listen(1)
conn, addr = s.accept()
Mark((addr," has Joined the Server"), win)
Recieve()

#conn.close()
