#-*- coding=utf8-*-
import subprocess
class vrtrackingcalib():
    def __init__(self):
        pass
    def login(self):
        command_0 = [r"..\tools\bin\win32\vrtrackingcalib.exe"]
        result = subprocess.Popen(command_0, shell = False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=None)
        print result.stdout.readlines()


    def logout(self):
        pass
    def getStart(self):
        pass
    def getConnStatus(self):
        pass

if __name__ == "__main__":
    vCalib = vrtrackingcalib()
    vCalib.login()