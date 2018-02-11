#-*-coding=utf8-*-
import subprocess
class imu_calibrator():
    def __init__(self):
        pass
    def login(self):
        command_0 = [r"..\tools\bin\win32\imu_calibrator.exe"]
        result = subprocess.Popen(command_0, shell = False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=None)
        print result.stdout.readlines()

    def logout(self):
        pass
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