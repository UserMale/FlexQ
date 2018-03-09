#-*- coding = utf8-*-
import re
import os
import errno
import subprocess
import logging
import shutil
import pexpect
import pexpect.popen_spawn as ps
logger = logging.getLogger()
#print __name__
print "logger=",logger

#print os.path.realpath(__file__)
# print os.path.split(os.path.realpath(__file__))
# g_DownloadPath = os.path.split(os.path.realpath(__file__))[0]
# print g_DownloadPath

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
class lighthouse_console(object) :

    def __init__(self):
        self.consoleHandler = None
        self.serialNum = None
        self.connState = False

    def login(self):

        self.consoleHandler = ps.PopenSpawn(r"..\tools\bin\win32\lighthouse_console.exe")
        index = self.consoleHandler.expect(["Lighthouse VrController HID opened", \
                                            "No connected lighthouse device found", \
                                            pexpect.EOF, \
                                            pexpect.TIMEOUT])
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

    def logout(self):

        if self.consoleHandler != None:
            print self.consoleHandler
            self.consoleHandler.sendline("quit")
            # pro1.expect("demotestconfig")
            print self.consoleHandler.before
            self.consoleHandler.closed

        else:

            command_0 = [r'taskkill', r'/F', r'/IM', r'lighthouse_console.exe', r'/T']
            result = subprocess.call(command_0)
            if result:
                logging.log(logging.INFO, "logout suc !!!")

            #self.consoleHandler.stdin.write("quit")

    def getSerialNum(self):
        print "serial num %s"%(self.serialNum)
        return self.serialNum

    def download(self, strDownloadPath):
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
        filename = ""
        if self.consoleHandler != None:
            try:
                # global g_DownloadPath
                # print g_DownloadPath
                #cmd = "downloadconfig auto_"+self.serialNum+".json"
                serialnum  = self.getSerialNum()
                print "serial num= %s"%(serialnum)
                print type(serialnum)
                self.consoleHandler.sendline("downloadconfig ptt_{0}.json"\
                                             .format(serialnum))
                self.consoleHandler.expect("ptt_{0}.json".format(serialnum))
                strResult = self.consoleHandler.before
                print strResult
                try:
                    print "osgetwcd = ",os.getcwd()
                    print "strDownloadPath = ",strDownloadPath
                    if os.getcwd() != strDownloadPath:
                        shutil.move(os.getcwd() + "\\" + "ptt_{0}.json".format(serialnum),\
                                    strDownloadPath + "\\" +"ptt_{0}.json".format(serialnum))
                    filename = "ptt_{0}.json".format(serialnum)
                    # result = os.path.exists(g_DownloadPath+"\\"+"auto_{0}.json"\
                    #                         .format(serialnum))
                    # print 'result = ', result
                    # if result == True:
                    #     shutil.copyfile("auto_{0}.json".format(serialnum), strDownloadPath+"\\"+\
                    #                     "auto_{0}.json".format(serialnum))
                    #
                    # logging.log(logging.INFO, strResult)
                except OSError as e:
                    if e.errno != errno.ENOENT:
                        raise "Exception "

            except ps.EOF:
                pass
            except pexpect.TIMEOUT:
                pass
            finally:
                return filename

            #self.consoleHandler.close
            #return True

    def upload(self, strUploadFilename):
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
        result = False
        if self.consoleHandler != None:

            targetDir = os.path.split(os.path.realpath(strUploadFilename))[0]
            targetFile = os.path.split(os.path.realpath(strUploadFilename))[1]

            if os.getcwd() == targetDir:
                pass
            else:
                try:
                    shutil.move(strUploadFilename, os.getcwd() + "\\" + targetFile)
                except IOError as e:
                    if e.errno != errno.ENOENT:
                        raise "Exception "
            try:
                #cmd = "downloadconfig auto_"+self.serialNum+".json"
                #print("hhh",cmd)
                #print type(cmd)
                # serialnum  = self.getSerialNum()
                # print "serial num= %s"%(serialnum)
                # print type(serialnum)
                #auto_{0}.json
                self.consoleHandler.sendline("uploadconfig {0}"\
                                             .format(targetFile))
                index = self.consoleHandler.expect(["Wrote the contents of",\
                                                    "Could not load config file"])
                if index == 0:
                    strResult = self.consoleHandler.before
                    print "suc"
                    result = True
                    logging.log(logging.INFO, strResult)
                elif index == 1:
                    print "fail"

            except ps.EOF:
                pass
            except pexpect.TIMEOUT:
                pass
            finally:
                return result


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
