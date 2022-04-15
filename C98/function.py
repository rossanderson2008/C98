
def countingwords ():
    filename=input("enter the file name- ")
    nowords=0
    file=open(filename,'r')
    for line in file:
        words=line.split( )
        nowords=nowords+len(words)
    print("number of words is equal to")
    print(nowords)
countingwords()