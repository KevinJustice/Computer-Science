# Echo client program
import socket
from time import *
from graphics import *
from kev import *
from datetime import *

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


def Open():
    win = GraphWin('Welcome to Callxr IM!', 300,300)
    win.setCoords(0,0,10,10)

    Background = Image(Point(5,5), 'IMG/OpenBG.gif')
    Background.draw(win)

    YourIP = getIPv4('ip.txt')
    YourAddress = Text(Point(2.5,6), 'Your Address')
    YourAddress.setStyle('bold italic')
    YourAddress.draw(win)
    YourIPAddress = Text(Point(2.5,5.25), YourIP)    
    YourIPAddress.draw(win)

    TheirAddress = Text(Point(2.5, 4), 'Friends Address')
    TheirAddress.setStyle('bold italic')
    TheirAddress.draw(win)
    TheirIPAddress = Entry(Point(2.5, 3.25), 15)
    TheirIPAddress.setFill('White')
    TheirIPAddress.draw(win)

    GoButt = Button(win, Point(7.5, 2.5), 1.5, 1, 'Go!', 'Gray')
    GoButt.activate()

    if GoButt.clicked(win.getMouse()) is True:
        GoButt.deactivate()
        SERVIP = str(TheirIPAddress.getText())
        win.close()
        return(SERVIP)
    else:
        GoButt.deactivate()
        win.close()
        return(Open())

def MainScreen():
    global TextList
    win = GraphWin('Callxr IM', 600, 600)
    win.setCoords(0,0,10,10)

    BGIMG = Image(Point(5,5), 'IMG/ClientBG.gif')
    BGIMG.draw(win)
    
    for i in TextList:
        i.draw(win)

    InputPanel = Entry(Point(3.4, .5), 40)
    InputPanel.setFill('white')
    InputPanel.draw(win)
    try:
        while 1:
            InputPanel.setText('')
            win.getMouse()
            SelectedSentence = str(InputPanel.getText())
            InputPanel.setText('Sending. Please Wait......')
            Tym = str(strftime("%X"))
            Time = '['
            for j in range(0,5,1):
                Time = Time + Tym[j]
            Mark(Time+"]"+"You: "+SelectedSentence, win)
            SelectedSentence = SelectedSentence + '`'
            for Dissect in SelectedSentence:
                for Compare in range(94):
                    if Letters[Compare] is Dissect: 
                        s.sendall(bytes(Compare))
                        sleep(1)
                    else:
                        x = 1
    except GraphicsError:
        win.close()


    
    
    

HOST = Open()   # The remote host
print(HOST)
PORT = 5007             # The same port as used by the server
Letters = ['~','`','A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z',' ','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','-','_','+','=',':',';','\'','"','{','}','[',']','\\','|','<','>','?','/','.',',']
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
MainScreen()
#Send()

#data = s.recv(1024)
#s.close()
#print('Received', repr(data))
