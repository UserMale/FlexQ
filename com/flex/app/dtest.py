#-*-coding=utf8-*-
import pexpect.popen_spawn as ps

# pro = ps.PopenSpawn(r"..\tools\bin\win32\imu_calibrator.exe")
# # t.sendline("help\r\n")
# #pro.sendline("\r\n")
# pro.expect("Lighthouse VrController HID opened")
# # print t.after
# print pro.before
# print "#" * 30
# #pro.flush()
# pro.sendline("\r\n")
# pro.expect("ACCEPTED")
# print pro.before
#
#
# pro.sendline("\r\n")
# pro.expect("REJECTED")
# print pro.before
#
# pro.sendline("\r\n")
# pro.expect("REJECTED")
# print pro.before
#
#
# pro.sendline("\r\n")
# pro.expect("REJECTED")
# print pro.before
#
#
# pro.sendline("q")
# pro.expect(ps.EOF)
# print pro.before
# pro.closed

pro1 = ps.PopenSpawn(r"..\tools\bin\win32\lighthouse_console.exe")
print pro1
# t.sendline("help\r\n")
#pro.sendline("\r\n")
pro1.expect("Lighthouse VrController HID opened")
print pro1.before
print "#" * 30
#pro.flush()
pro1.sendline("help")
pro1.expect("Many options are also allowed as command-line flags")
print pro1.before
pro1.sendline("help")
pro1.expect("Many options are also allowed as command-line flags")
print pro1.before

pro1.sendline("serial")
pro1.expect("Lighthouse VrController HID opened")
print pro1.before

pro1.sendline("downloadconfig demotestconfig")
pro1.expect("demotestconfig")
print pro1.before

pro1.sendline("quit")
#pro1.expect("demotestconfig")
print pro1.before

pro1.closed
