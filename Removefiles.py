import os
import shutil
def findShouldDeleteFile(whichFile):
    isExist = os.path.exists(whichFile)
    print(isExist)
    if(isExist==True):
        time= os.stat(whichFile.st)
        if(time>30):
            os.remove(whichFile)
        return time
        
    else:
        print("File cannot be found please try again")

keepGoing =0
while  keepGoing<1:
    n=input("which file do you want scanned: " )
    print(n)
    findShouldDeleteFile(n)
    n=input("do you want to end y/n: " )
    if(n=="y"):
        keepGoing=1
    
#"c:/Users/defau/sampleText.txt"
#
