#-*-coding=utf8-*-
import subprocess
import re
import os
import wx
import errno
import time
import logging
import pexpect
import pexpect.popen_spawn as ps

print os.path.realpath(__file__)
print os.path.split(os.path.realpath(__file__))
g_DownloadPath = os.path.split(os.path.realpath(__file__))[0]
print g_DownloadPath


class imu_calibrator():
    def __init__(self):
        self.consoleHandler = None
        self.serialNum = None
        self.connState = False
        self.logoutFlag = False

    def login(self):
        command_0 = [r"..\tools\bin\win32\imu_calibrator.exe"]
        self.consoleHandler = ps.PopenSpawn(r"..\tools\bin\win32\imu_calibrator.exe")
        index = self.consoleHandler.expect(["Lighthouse VrController HID opened", \
                                            "Error connecting or Lighthouse IMU", \
                                            pexpect.EOF, \
                                            pexpect.TIMEOUT])
        if index == 0:
            strResult = self.consoleHandler.before
            serial_pattern = "Attempting HID Open IMU:\s+(\w+-.*)"
            strSerial = re.search(serial_pattern, strResult)
            print "strSerial", strSerial
            self.serialNum = strSerial.group(1)
            print "\n%s\n" % self.serialNum
            logging.log(logging.INFO, strResult)
            return True
        else:
            return False

    def getSerialNum(self):
        print "serial num %s"%(self.serialNum)
        return self.serialNum

    def logout(self):
        # command_0 = [r'taskkill', r'/F', r'/IM', r'imu_calibrator.exe', r'/T']
        # result = subprocess.call(command_0)
        # if result:
        #     logging.log(logging.INFO, "logout suc !!!")
        if self.logoutFlag:
            print "OKKK"
            command_0 = [r'taskkill', r'/F', r'/IM', r'imu_calibrator.exe', r'/T']
            result = subprocess.call(command_0)
            if result:
                logging.log(logging.INFO, "logout suc !!!")

        else:
            print "OKKK1111"
            print self.consoleHandler
            self.consoleHandler.sendline("q")
            # pro1.expect("demotestconfig")
            print self.consoleHandler.before
            self.consoleHandler.closed


    def getCurAxesResult(self):
        pass

    def getNextAxesResult(self):

        #global g_DownloadPath
        stateDict = {}
        if self.consoleHandler != None:
           # print self.consoleHandler
            try:
                #self.consoleHandler.buffer = ""
                print '1111', self.consoleHandler.before

                self.consoleHandler.expect(["Press enter to sample, 'q' to quit", pexpect.EOF])
                print '2222'
                self.consoleHandler.sendline("\r\n")
                print '3333'
                # pro1.expect("demotestconfig")
                # self.consoleHandler.expect("Press enter to sample, 'q' to quit")
                # time.sleep(2)
                # self.consoleHandler.sendline("q")
                # self.consoleHandler.expect(ps.EOF)
                #time.sleep(2)
                #print 'test===', self.consoleHandler.before
                index = self.consoleHandler.expect(["Press enter to sample, 'q' to quit", pexpect.EOF])
                #print 'test===', self.consoleHandler.before
                if index == 0:
                    strResult = self.consoleHandler.before
                    #print strResult
                    logging.log(logging.INFO, strResult)
                    iResult = strResult.find("ACCEPTED")
                    if iResult != -1:
                        print str(re.findall(r"ACCEPTED.*", strResult, re.MULTILINE)[0]).strip()
                        stateDict["ACCEPTED"] = str(re.findall(r"ACCEPTED.*", strResult, re.MULTILINE)[0]).strip()
                        #print stateDict
                        #return stateDict
                    else:
                        '''
                        REJECTED. Duplicate orientation (alignment 1)
                        REJECTED. Please hold sensor still.
                        '''
                        stateDict["REJECTED"] = str(re.findall(r"REJECTED.*", strResult, re.MULTILINE)[0]).strip()
                        #return "REJECTED"
                        #return stateDict

                elif index == 1:
                    print "I am here 1"
                    strResult = self.consoleHandler.before
                    strResult = str(strResult).split('DONE.')[-1]
                    stateDict["DONE"] = str(strResult).strip()
                    self.logoutFlag = True

                #return stateDict
            except pexpect.EOF:
                print 'r'
                raise  "Exception Happend, EOF!!! "

            except pexpect.TIMEOUT:
                print 'w'
                raise "Exception Happend, pls re-connect!!! "
                #wx.MessageBox("Exception Happend, pls re-connect!!!", 'Error',
                #              wx.OK | wx.ICON_ERROR)
            # finally:
            #     print 'test finnally1===', self.consoleHandler.before
            #     print 'test finnally2===', self.consoleHandler.after
            #     return stateDict
        return stateDict


            #self.consoleHandler.closed
        #return True
    def genCalibJsonConfig(self):
        pass
    def uploadCalibConfig(self):
        pass
    def getConnStatus(self):
        pass

if  __name__ == "__main__":
    iCalibrator = imu_calibrator()
    iCalibrator.login()