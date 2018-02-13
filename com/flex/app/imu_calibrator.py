#-*-coding=utf8-*-
import subprocess
class imu_calibrator():
    def __init__(self):
        self.consoleHandler = None
        self.serialNum = None
        self.connState = False

    def login(self):
        command_0 = [r"..\tools\bin\win32\imu_calibrator.exe"]
        self.consoleHandler = ps.PopenSpawn(r"..\tools\bin\win32\lighthouse_console.exe")
        index = self.consoleHandler.expect(["Lighthouse VrController HID opened", \
                                            "Error connecting or Lighthouse IMU"])
        if index == 0:
            strResult = self.consoleHandler.before
            serial_pattern = "lighthouse_console: Connected to receiver\s+(\w+-.*)"
            strSerial = re.search(serial_pattern, strResult)
            print "strSerial", strSerial
            self.serialNum = strSerial.group(1)
            print "\n%s\n" % self.serialNum
            logging.log(logging.INFO, strResult)
            return True
        else:
            return False

    def logout(self):
        if self.consoleHandler != None:
            print self.consoleHandler
            self.consoleHandler.sendline("q")
            # pro1.expect("demotestconfig")
            print self.consoleHandler.before

            self.consoleHandler.closed
        return True

    def getCurAxesResult(self):
        pass
    def getNextAxesResult(self):
        pass
    def genCalibJsonConfig(self):
        pass
    def uploadCalibConfig(self):
        pass
    def getConnStatus(self):
        pass

if  __name__ == "__main__":
    iCalibrator = imu_calibrator()
    iCalibrator.login()