#-*- coding = utf8-*-
import re
import subprocess
import logging
import pexpect.popen_spawn as ps
logger = logging.getLogger()
#print __name__
print "logger=",logger
##########################################################
##lh> downloadconfig LHR-4F322C04
##LHR-4F322C04: Unable to request config start from device
##Unable to read config from device
##########################################################

##########################################################
##lh> serial
##Attached lighthouse receiver devices: 0
##No connected lighthouse device found.
##########################################################
class lighthouse_console():

    def __init__(self):
        self.consoleHandler = None
        self.serialNum = None
        self.connState = False

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
        index = self.consoleHandler.expect(["Lighthouse VrController HID opened", \
                                            "No connected lighthouse device found"])
        if index == 0:
            strResult = self.consoleHandler.before
            serial_pattern = "lighthouse_console: Connected to receiver\s+(\w+-.*)"
            strSerial = re.search(serial_pattern, strResult)
            print "strSerial", strSerial
            self.serialNum = (strSerial.group(1)).strip("\r")
            print "\n%s\n" % self.serialNum
            logging.log(logging.INFO, strResult)
            return True
        else:
            return False

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
        #return True

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
        print "serial num %s"%(self.serialNum)
        return self.serialNum

    def download(self,dirDownload):
        '''
        case1:
          lh> downloadconfig LHR-4F322C04
            LHR-4F322C04: Read config of 1810 bytes from [vid:28de, pid:2300] (LHR-4F322C04) and inflated to 9007 bytes
            Wrote 9007 bytes to LHR-4F322C04
        case2:
        lh> LHR-4F322C04: Read config of 1810 bytes from [vid:28de, pid:2300] (LHR-4F322C04) and inflated to 9007 bytes
            Unable to write to LHR-4F322C04
        :param dirDownload:
        :return:
        '''
        if self.consoleHandler != None:
            try:
                #cmd = "downloadconfig auto_"+self.serialNum+".json"
                #print("hhh",cmd)
                #print type(cmd)
                serialnum  = self.getSerialNum()
                print "serial num= %s"%(serialnum)
                print type(serialnum)
                self.consoleHandler.sendline("downloadconfig auto_{0}.json"\
                                             .format(serialnum))
                self.consoleHandler.expect("auto_{0}.json".format(serialnum))
                strResult = self.consoleHandler.before
                ##log
                logging.log(logging.INFO, strResult)

            except ps.EOF:
                pass
            except ps.TIMEOUT:
                pass

            #self.consoleHandler.close
            #return True

    def upload(self):
        """
        case1:
            lh> uploadconfig auto_LHR-4F322C04.json
                Compressed config size is 1810
                Wrote the contents of auto_LHR-4F322C04.json as the config on the device
        case2:
            lh> uploadconfig auto_LHR-4F322C0.json
                Could not load config file auto_LHR-4F322C0.json
        :return:
        """
        if self.consoleHandler != None:
            try:
                #cmd = "downloadconfig auto_"+self.serialNum+".json"
                #print("hhh",cmd)
                #print type(cmd)
                serialnum  = self.getSerialNum()
                print "serial num= %s"%(serialnum)
                print type(serialnum)
                self.consoleHandler.sendline("uploadconfig auto_{0}.json"\
                                             .format(serialnum))
                index = self.consoleHandler.expect(["Wrote the contents of",\
                                                    "Could not load config file"])
                if index == 0:
                    strResult = self.consoleHandler.before
                    print "suc"
                    logging.log(logging.INFO, strResult)
                elif index == 1:
                    print "fail"

            except ps.EOF:
                pass
            except ps.TIMEOUT:
                pass


    def getConnStatus(self):

        if self.consoleHandler != None:
            try:
                self.consoleHandler.sendline("serial")
                index = self.consoleHandler.expect(["Lighthouse VrController HID opened",\
                                                    "No connected lighthouse device found"])
                if index == 0:
                    self.connState = True
                else:
                    self.connState = False

            except ps.EOF:
                pass

            except ps.TIMEOUT:
                pass


if __name__ == "__main__":
    lConsole = lighthouse_console()
    lConsole.login()
    lConsole.download("11")
    lConsole.upload()
    lConsole.logout()
