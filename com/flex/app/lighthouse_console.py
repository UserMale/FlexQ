#-*- coding = utf8-*-
import subprocess
import logging
import pexpect.popen_spawn as ps
logger = logging.getLogger()
#print __name__
print "logger=",logger


class lighthouse_console():

    def __init__(self):
        self.consoleHandler = None

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
        #command_0 = [r"..\tools\bin\win32\lighthouse_console.exe",">","2>&1 &"]
        #command_0 = [r"..\tools\bin\win32\lighthouse_console.exe",">NUL"]
        self.consoleHandler = ps.PopenSpawn(r"..\tools\bin\win32\lighthouse_console.exe")
        self.consoleHandler.expect("Lighthouse VrController HID opened")
        strResult = self.consoleHandler.before
        logging.log(logging.INFO,strResult)
        #t.sendline("help\r\n")

        # t.expect("lh>")
        # #print t.after
        # #print t.before
        # print "#"*30
        # t.flush()
        # t.sendline("imu\r\n")
        # t.expect("lh>")
        # #print t.before
        # #print t.before
        # #t.read_nonblocking()
        # print "#" * 30
        # t.sendline("imu\r\n")
        # t.expect("lh>")
        # print t.before
        # t.sendline("quit\r\n")
        # #t.expect("lh>")
        # print t.before
        # t.closed
        #command_0 = [r"ipconfig"]
        #command_0 = [r"ping","www.baidu.com"]
        # self.consoleHandler = subprocess.Popen(command_0, shell = False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # self.consoleHandler.wait()
        # print self.consoleHandler.returncode
        # self.consoleHandler.stdin.write("quit")
        # print self.consoleHandler.returncode
        #print self.consoleHandler.communicate("help\r\n")
        #self.consoleHandler.stdin.write("help \r\n")
        #self.consoleHandler.stdin.flush()
        #print self.consoleHandler.stdout.read(500)
        #print self.consoleHandler.stdout.readlines()
        #logging.log(logging.INFO,"".join(self.consoleHandler.stdout.readlines()))
        #self.consoleHandler.stdout.flush()
        return True

    def logout(self):
        if self.consoleHandler != None:
            print self.consoleHandler
            self.consoleHandler.sendline("quit")
            # pro1.expect("demotestconfig")
            print self.consoleHandler.before

            self.consoleHandler.closed
        return True

            #self.consoleHandler.stdin.write("quit")

    def getSerialNum(self):
        pass

    def download(self,dirfilename):
        if self.consoleHandler != None:
            print self.consoleHandler
            self.consoleHandler.sendline("downloadconfig {0}".format(filename))
            pro1.expect(filename)
            logging.log(logging.INFO, self.consoleHandler.before)

            #self.consoleHandler.closed
        return True

    def upload(self):
        pass

    def getConnStatus(self):
        pass


if __name__ == "__main__":
    lConsole = lighthouse_console()
    lConsole.login()
    lConsole.logout()