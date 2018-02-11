#-*-coding=utf8-*-
import logging

import os
import sys
import time
import logging
from com.flex.utils.Singleton import Singleton


@Singleton
class Logger(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        logging.debug('PhontomLOG OPEN')
        self._currentDir = os.path.dirname(os.path.realpath(__file__))
        self._logDir = self._currentDir + '../../log'
        self._logFileName = self._logDir + '/PhontomLOG.txt'
        self._timeFormat = '%Y-%m-%d %H:%M:%S'
        self._logFile = None
        self._decorate = '******'
        self._fileMaxSize = 10000000

    def _open_log_file(self):
        if self._logFile is None:
            self._judge_log_file_size()
            self._logFile = open(self._logFileName, "a")
        return self._logFile

    def _judge_log_file_size(self):
        if os.path.exists(self._logFileName):
            if self._get_file_size(self._logFileName) > self._fileMaxSize:
                os.remove(self._logFileName)

    def _write(self, s):
        try:
            s = s.encode('utf-8')
            f = self._open_log_file()
            f.write(s + '\n')
        except Exception, e:
            logging.debug(e)

    def _write_header_information(self):
        self._write(self._decorate * 10)
        self._write(self._decorate + 'TIME: ' + self._get_current_time())
#         self._write(self._decorate + 'FUNCTION_NAME: ' + self._get_function_name())
#         self._write(self._decorate + 'LINE_NUNBER: ' + self._get_line_number())

    def _get_current_time(self):
        return str(time.strftime(self._timeFormat, time.localtime()))

    def _get_function_name(self):
        return sys.argv[0]

    def _get_line_number(self):
        return str(sys._getframe().f_back.f_lineno)

    def __del__(self):
        try:
            if self._logFile is not None:
                self._logFile.close()
            self._logFile = None
        except Exception:
            pass

    def _get_file_size(self, logFileName):
        try:
            return os.path.getsize(logFileName)
        except Exception, e:
            logging.warn(e)
            return 0

    def _log(self, level, s):
        self._write_header_information()
        self._write(self._decorate + level + ' :')
        self._write(s)
        self._write(self._decorate * 10)
        self._write('\n')

    def warn(self, s, flag=True):
        self._log('WARN', s)
        if flag:
            logging.warn(s)

    def info(self, s, flag=True):
        self._log('INFO', s)
        if flag:
            logging.info(s)

    def debug(self, s, flag=True):
        self._log('DEBUG', s)
        if flag:
            logging.debug(s)

    def error(self, s, flag=True):
        self._log('ERROR', s)
        if flag:
            logging.error(s)


if __name__ == '__main__':

    for i in range(10):
        Logger().info('xiongxiongxiongxiongxiong')
        Logger().error('xiongxiongxiongxiongxiong')