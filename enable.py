import ctypes
import sys
import os


def isAdmin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def unblockIt(website):

    try:
        f = open("C:\\Windows\\System32\\drivers\\etc\\hosts", "r+")
        content = f.read()
        f.close()

        if website in content:
            elem = content.split("\n")
            newElem = []

            for line in elem:
                if(website not in line):
                    newElem.append(line)

            finalContent = "\n".join(newElem)

            f = open("C:\\Windows\\System32\\drivers\\etc\\hosts", "w+")
            f.write(finalContent)
            f.close()

            print("Website Unblocked Successfully\n")
        else:
            print("website is not in blocked list\n")

        return True

    except:
        return False


def main():

    print("##############################################################")
    print("##############################################################")
    print("##################WEBSITE BLOCKER Re-Enabler###################")
    print("##############################################################")
    print("##############################################################")
    if(not isAdmin()):
        print("Access Denied, Asking for permission")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()
    else:
        while(1):
            web = input("Enter a website link to Unblock, press q to exit:")
            if (web == 'q' or web == 'Q'):
                sys.exit()
            if(not unblockIt(web)):
                print("Error in unblocking the website!")
    os.system("pause")


if(__name__ == '__main__'):
    main()

 
