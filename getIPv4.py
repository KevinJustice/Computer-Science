def getIPv4(textFile):
    def listLength(List):
        counter = 0
        for i in List:
            counter = counter + 1
        return counter
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
                    
print(getIPv4('ip.txt'))
