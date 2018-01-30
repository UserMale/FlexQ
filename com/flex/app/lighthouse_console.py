#-*- coding = utf8-*-
import subprocess

class lighthouse_console():
    def __init__(self):
        pass
    def login(self):
        # #command_0 = ['cmd.exe /k ', shell = True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=None]
        # print "1"
        # handle_cmd = subprocess.Popen('cmd.exe /k ', shell = False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=None)
        # print "2"
        # handle_cmd.stdin.write(r"C:\Users\dell\Desktop\FlexQt\com\flex\tools\bin\win32\lighthouse_console.exe")
        # print "3"
        # output = handle_cmd.stdout.readlines()
        # print "4"
        # print output
        command_0 = [r"..\tools\bin\win32\lighthouse_console.exe"]
        result = subprocess.Popen(command_0, shell = False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=None)
        print result.stdout.readlines()
        print "1"
    def logout(self):
        pass
    def getSerialNum(self):
        pass
    def download(self):
        pass
    def upload(self):
        pass
    def getConnStatus(self):
        pass

if __name__ == "__main__":
    lConsole = lighthouse_console()
    lConsole.login()