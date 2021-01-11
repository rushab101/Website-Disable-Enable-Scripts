import ctypes
import sys
import os


def isAdmin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def blockIt(website):

    try:

        f = open("C:\\Windows\\System32\\drivers\\etc\\hosts", 'a+')

        f.seek(0)
        contents = f.read()

        if(website in contents):
            print("Website Already Blocked!")
        else:
            local_host = "127.0.0.1"
            f.write("\n")

            if('www' in website):
                domain = website.replace('www.', '')
                f.write(local_host + " " + website + "\n")
                f.write(local_host + " " + domain + "\n")
            else:
                f.write(local_host + " " + website + "\n")
                f.write(local_host + " www." + website + "\n")

            print("Blocked")

        f.close()
        return True
    except:
        return False




def main():

    if(not isAdmin()):
        print("Access Denied, Asking for permission")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()
    print("##############################################################")
    print("##############################################################")
    print("##################WEBSITE BLOCKER TEST########################")
    print("##############################################################")
    print("##############################################################")
    while(True):
        web = input("Enter a website link to Unblock, press q to exit:")
        if (web == 'q' or web == 'Q'):
            sys.exit()
        if(not blockIt(web)):
            print("Error in blocking the website!")
    os.system("pause")


if(__name__ == '__main__'):
    main()