#-*- coding=utf8-*-
import re
import time
import subprocess
import pexpect
import pexpect.popen_spawn as ps
import logging
class vrtrackingcalib():
    def __init__(self):
        self.consoleHandler = None
        self.serialNum = None
        self.connState = False

    def login(self, fileJsonConfigure, intMinimumReadings, intMinimumHits, intTimeout):
        # command_0 = [r"..\tools\bin\win32\vrtrackingcalib.exe", r"/usedisambiguation", "framer", \
        #              r"/bodycal", fileJsonConfigure, intMinimumReadings, intMinimumHits]
        # result = subprocess.Popen(command_0, shell = False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=None)
        # print result.stdout.readlines()
        command_0 = r"..\tools\bin\win32\vrtrackingcalib.exe /usedisambiguation framer /bodycal " +\
            fileJsonConfigure + ' ' + str(intMinimumReadings) + ' ' + str(intMinimumHits)
        print command_0
        ##r"..\tools\bin\win32\vrtrackingcalib.exe /usedisambiguation framer /bodycal imu_updated.json 800 200 "
        self.consoleHandler = ps.PopenSpawn(command_0, timeout=int(intTimeout)*60)
        index = self.consoleHandler.expect(["Ready to run capture position number 0", \
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
        '''
        C:\Users\dell>taskkill /F /IM vrtrackingcalib.exe /T
        成功: 已终止 PID 11360 (属于 PID 12936 子进程)的进程。
        :return:
        '''
        command_0 = [r'taskkill', r'/F', r'/IM', r'vrtrackingcalib.exe', r'/T']
        result = subprocess.call(command_0)
        if result:
            logging.log(logging.INFO, "logout suc !!!")

    def getCapture(self, msg):
        self.consoleHandler.expect(['Calibration capture complete.', pexpect.EOF, pexpect.TIMEOUT])
        self.consoleHandler.sendline('\r\n')
        # consoleHandler.expect('base 00000000')
        # print consoleHandler.before
        index = self.consoleHandler.expect(['Calibration capture complete.', pexpect.EOF, pexpect.TIMEOUT])
        if index == 0:
            print '0000000000000000'
            print self.consoleHandler.before
            msg[0] = False
            return msg
        elif index == 1:
            print '1111111111111111'
            print self.consoleHandler.before
            msg[0] = False
            return msg
        elif index == 2:
            print '2222222222222222'
            print self.consoleHandler.before
            msg[0] = True
            return msg

    def getConnStatus(self):
        pass

if __name__ == "__main__":
    vCalib = vrtrackingcalib()
    vCalib.login('imu_updated.json','800','200')
    time.sleep(10)
    vCalib.logout()