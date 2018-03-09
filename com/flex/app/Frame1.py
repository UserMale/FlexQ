#Boa:Frame:Frame1

import logging
import random
# import thread
# import sys

import os
import wx
import re
import json
import time
import subprocess
from threading import Thread
from wx.lib.pubsub import Publisher
import wx.richtext
import wx.lib.intctrl
import wx.lib.filebrowsebutton
import win32com.client
from com.flex.app.lighthouse_console import lighthouse_console
from com.flex.app.imu_calibrator import imu_calibrator
from com.flex.app.vrtrackingcalib import vrtrackingcalib

logger = logging.getLogger()
print "logger=", logger
print "__name__", __name__
gBtn1ConnFlag = False
gBtn2ConnFlag = False
gBtn5ConnFlag = False
print os.path.realpath(__file__)
print os.path.split(os.path.realpath(__file__))
g_DownloadPath = os.path.split(os.path.realpath(__file__))[0]
print g_DownloadPath

logging.getLogger()
#############################################################
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

gcounts_sample = 0

def setup_logger(name, log_file, level=logging.INFO):
    """Function setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
#############################################################
loggers = {}

def myLogger(name):
    global loggers

    if loggers.get(name):
        return loggers.get(name)
    else:
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        now = datetime.datetime.now()
        handler = logging.FileHandler(
            '/root/credentials/Logs/ProvisioningPython'
            + now.strftime("%Y-%m-%d")
            + '.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        loggers.update(dict(name=logger))

        return logger
#############################################################

#print "__name__=",__name__

class WxTextCtrlHandle(logging.Handler):

    def __init__(self,ctrl):
        logging.Handler.__init__(self)
        self.ctrl = ctrl
        print "Init Position ,", self.ctrl

    def emit(self, record):
        s = self.format(record) + '\n'
        print "s=", s
        wx.CallAfter(self.ctrl.WriteText, s)

LEVELS = [
    logging.DEBUG,
    logging.INFO,
    logging.WARNING,
    logging.ERROR,
    logging.CRITICAL
]



def isPnpDeviceExist(strSerialNum):

    strComputer = "."
    objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    objSWbemServices = objWMIService.ConnectServer(strComputer, "root\cimv2")
    colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_PnPDevice")
    boolFlag = False
    for objItem in colItems:

        if objItem.SameElement != None:
            #print "SameElement:" + ` objItem.SameElement`
            if str(objItem.SameElement).find(strSerialNum) != -1:
                #logging.log(logging.INFO, 'Detected, there it is !!!')
                boolFlag = True
                break

        # if objItem.SystemElement != None:
        #     print "SystemElement:" + ` objItem.SystemElement`

    return boolFlag


def InitTestToolEnv():
    command_0 = [r'taskkill', r'/F', r'/IM', r'lighthouse_console.exe', r'/T']
    command_1 = [r'taskkill', r'/F', r'/IM', r'imu_calibrator.exe', r'/T']
    command_2 = [r'taskkill', r'/F', r'/IM', r'vrtrackingcalib.exe', r'/T']
    result = subprocess.call(command_0)
    if result:
        logging.log(logging.INFO, "clean lighthouse_console suc !!!")

    result = subprocess.call(command_1)
    if result:
        logging.log(logging.INFO, "clean imu_calibrator suc !!!")

    result = subprocess.call(command_2)
    if result:
        logging.log(logging.INFO, "clean vrtrackingcalib suc !!!")


def call_after(func):
    def _wrapper(*args, **kwargs):
        return wx.CallAfter(func, *args, **kwargs)
    return _wrapper()


def create(parent):

    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3, 
 wxID_FRAME1BUTTON4, wxID_FRAME1BUTTON5, wxID_FRAME1BUTTON6, 
 wxID_FRAME1BUTTON7, wxID_FRAME1BUTTON8, wxID_FRAME1CHECKBOX1, 
 wxID_FRAME1CHECKBOX2, wxID_FRAME1CHECKBOX3, wxID_FRAME1CHECKBOX4, 
 wxID_FRAME1CHECKBOX5, wxID_FRAME1CHECKBOX6, wxID_FRAME1DIRBROWSEBUTTON1, 
 wxID_FRAME1FILEBROWSEBUTTONWITHHISTORY1, 
 wxID_FRAME1FILEBROWSEBUTTONWITHHISTORY2, wxID_FRAME1INTCTRL1, 
 wxID_FRAME1INTCTRL2, wxID_FRAME1INTCTRL3, wxID_FRAME1NOTEBOOK1, 
 wxID_FRAME1PANEL1, wxID_FRAME1PANEL2, wxID_FRAME1PANEL3, wxID_FRAME1PANEL4, 
 wxID_FRAME1PANEL5, wxID_FRAME1RICHTEXTCTRL1, wxID_FRAME1RICHTEXTCTRL2, 
 wxID_FRAME1STATICBOX1, wxID_FRAME1STATICBOX2, wxID_FRAME1STATICBOX3, 
 wxID_FRAME1STATICBOX4, wxID_FRAME1STATICBOX5, wxID_FRAME1STATICBOX6, 
 wxID_FRAME1STATICBOX7, wxID_FRAME1STATICBOX9, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, 
 wxID_FRAME1STATICTEXT5, wxID_FRAME1STATICTEXT6, wxID_FRAME1STATUSBAR1, 
 wxID_FRAME1STATUSBAR2, wxID_FRAME1STATUSBAR3, 
] = [wx.NewId() for _init_ctrls in range(46)]

[wxID_FRAME1MENU1ITEMS0] = [wx.NewId() for _init_coll_menu1_Items in range(1)]

[wxID_FRAME1TIMER1] = [wx.NewId() for _init_utils in range(1)]

class Frame1(wx.Frame):
    def _init_coll_FlexQ_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=wx.Menu(), title=u'Exit')

    def _init_coll_menu1_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_FRAME1MENU1ITEMS0, kind=wx.ITEM_NORMAL,
              text=u'Exit')

    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel1, select=False,
              text=u'lighthouse_console')
        parent.AddPage(imageId=-1, page=self.panel2, select=True,
              text=u'imu_calibrator')
        parent.AddPage(imageId=-1, page=self.panel3, select=False,
              text=u'vrtrackingcalib')
        parent.AddPage(imageId=-1, page=self.panel4, select=False, text=u'help')

    def _init_utils(self):
        # generated method, don't edit
        self.FlexQ = wx.MenuBar()
        self.FlexQ.SetThemeEnabled(True)

        self.menu1 = wx.Menu(title='')

        self.timer1 = wx.Timer(id=wxID_FRAME1TIMER1, owner=self)
        self.Bind(wx.EVT_TIMER, self.OnTimer1Timer, id=wxID_FRAME1TIMER1)

        self._init_coll_FlexQ_Menus(self.FlexQ)
        self._init_coll_menu1_Items(self.menu1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(643, 299), size=wx.Size(1018, 663),
              style=wx.MAXIMIZE_BOX | wx.DEFAULT_FRAME_STYLE,
              title='Phantom Test Tool')
        self._init_utils()
        self.SetClientSize(wx.Size(1002, 624))
        self.Enable(True)
        self.SetCursor(wx.STANDARD_CURSOR)
        self.SetAutoLayout(True)
        self.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              u'Arial'))

        self.notebook1 = wx.Notebook(id=wxID_FRAME1NOTEBOOK1, name='notebook1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(1000, 272),
              style=0)
        self.notebook1.SetThemeEnabled(True)
        self.notebook1.SetAutoLayout(True)
        self.notebook1.SetFitToCurrentPage(True)
        self.notebook1.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Calibri'))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(992, 241),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetAutoLayout(True)

        self.panel2 = wx.Panel(id=wxID_FRAME1PANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(992, 241),
              style=wx.TAB_TRAVERSAL)

        self.panel3 = wx.Panel(id=wxID_FRAME1PANEL3, name='panel3',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(992, 241),
              style=wx.TAB_TRAVERSAL)

        self.panel4 = wx.Panel(id=wxID_FRAME1PANEL4, name='panel4',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(992, 241),
              style=wx.TAB_TRAVERSAL)
        self.panel4.SetHelpText(u'')

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'Connect',
              name='button1', parent=self.panel1, pos=wx.Point(24, 72),
              size=wx.Size(88, 32), style=0)
        self.button1.SetThemeEnabled(True)
        self.button1.SetAutoLayout(True)
        self.button1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Arial'))
        self.button1.Bind(wx.EVT_BUTTON, self.OnBtn1Conn, id=wxID_FRAME1BUTTON1)

        self.statusBar1 = wx.StatusBar(id=wxID_FRAME1STATUSBAR1,
              name='statusBar1', parent=self.panel1, style=0)
        self.statusBar1.SetStatusText(u'Current Status:   Disconnect')
        self.statusBar1.SetToolTipString(u'statusBar1')
        self.statusBar1.SetThemeEnabled(True)
        self.statusBar1.SetAutoLayout(True)
        self.statusBar1.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Calibri'))

        self.statusBar2 = wx.StatusBar(id=wxID_FRAME1STATUSBAR2,
              name='statusBar2', parent=self.panel2, style=0)
        self.statusBar2.SetStatusText(u'Current Status:   Disconnect')
        self.statusBar2.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Calibri'))

        self.statusBar3 = wx.StatusBar(id=wxID_FRAME1STATUSBAR3,
              name='statusBar3', parent=self.panel3, style=0)
        self.statusBar3.SetStatusText(u'Current Status:   Disconnect')
        self.statusBar3.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Calibri'))

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label=u'Connect',
              name='button2', parent=self.panel2, pos=wx.Point(16, 80),
              size=wx.Size(160, 32), style=0)
        self.button2.SetAutoLayout(True)
        self.button2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u''))
        self.button2.Bind(wx.EVT_BUTTON, self.OnBtn2Conn, id=wxID_FRAME1BUTTON2)

        self.checkBox1 = wx.CheckBox(id=wxID_FRAME1CHECKBOX1, label=u'Sample1',
              name='checkBox1', parent=self.panel2, pos=wx.Point(240, 88),
              size=wx.Size(80, 14), style=0)
        self.checkBox1.SetValue(False)
        self.checkBox1.Show(True)
        self.checkBox1.Enable(False)

        self.checkBox2 = wx.CheckBox(id=wxID_FRAME1CHECKBOX2, label=u'Sample2',
              name='checkBox2', parent=self.panel2, pos=wx.Point(352, 88),
              size=wx.Size(79, 14), style=0)
        self.checkBox2.SetValue(False)
        self.checkBox2.Enable(False)

        self.checkBox3 = wx.CheckBox(id=wxID_FRAME1CHECKBOX3, label=u'Sample3',
              name='checkBox3', parent=self.panel2, pos=wx.Point(448, 88),
              size=wx.Size(79, 14), style=0)
        self.checkBox3.SetValue(False)
        self.checkBox3.Enable(False)
        self.checkBox3.SetToolTipString(u'checkBox3')

        self.checkBox4 = wx.CheckBox(id=wxID_FRAME1CHECKBOX4, label=u'Sample4',
              name='checkBox4', parent=self.panel2, pos=wx.Point(240, 120),
              size=wx.Size(79, 14), style=0)
        self.checkBox4.SetValue(False)
        self.checkBox4.Enable(False)
        self.checkBox4.SetToolTipString(u'checkBox4')

        self.checkBox5 = wx.CheckBox(id=wxID_FRAME1CHECKBOX5, label=u'Sample5',
              name='checkBox5', parent=self.panel2, pos=wx.Point(352, 120),
              size=wx.Size(79, 14), style=0)
        self.checkBox5.SetValue(False)
        self.checkBox5.Enable(False)

        self.checkBox6 = wx.CheckBox(id=wxID_FRAME1CHECKBOX6, label=u'Sample6',
              name='checkBox6', parent=self.panel2, pos=wx.Point(448, 120),
              size=wx.Size(79, 14), style=0)
        self.checkBox6.SetValue(False)
        self.checkBox6.Enable(False)
        self.checkBox6.SetToolTipString(u'checkBox6')

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label=u'Next',
              name='button3', parent=self.panel2, pos=wx.Point(16, 128),
              size=wx.Size(75, 32), style=0)
        self.button3.Enable(False)
        self.button3.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u''))
        self.button3.Bind(wx.EVT_BUTTON, self.OnBtn3Next, id=wxID_FRAME1BUTTON3)

        self.button4 = wx.Button(id=wxID_FRAME1BUTTON4, label=u'Finish',
              name='button4', parent=self.panel2, pos=wx.Point(104, 128),
              size=wx.Size(75, 32), style=0)
        self.button4.Enable(False)
        self.button4.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u''))
        self.button4.Bind(wx.EVT_BUTTON, self.OnBtn4Finish,
              id=wxID_FRAME1BUTTON4)

        self.button5 = wx.Button(id=wxID_FRAME1BUTTON5, label=u'Connect',
              name='button5', parent=self.panel3, pos=wx.Point(752, 80),
              size=wx.Size(88, 32), style=0)
        self.button5.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u''))
        self.button5.Bind(wx.EVT_BUTTON, self.OnBtn5Conn, id=wxID_FRAME1BUTTON5)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'Six Axes State', name='staticBox1', parent=self.panel2,
              pos=wx.Point(224, 48), size=wx.Size(312, 120), style=0)
        self.staticBox1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Calibri'))

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label=u'Download Save Path ', name='staticBox2',
              parent=self.panel1, pos=wx.Point(8, 128), size=wx.Size(440, 100),
              style=0)
        self.staticBox2.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Calibri'))

        self.staticBox3 = wx.StaticBox(id=wxID_FRAME1STATICBOX3,
              label=u'Upload Json File Path', name='staticBox3',
              parent=self.panel1, pos=wx.Point(520, 40), size=wx.Size(400, 100),
              style=0)
        self.staticBox3.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Calibri'))

        self.staticBox4 = wx.StaticBox(id=wxID_FRAME1STATICBOX4,
              label=u'Operate', name='staticBox4', parent=self.panel1,
              pos=wx.Point(8, 40), size=wx.Size(440, 72), style=0)
        self.staticBox4.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Calibri'))

        self.dirBrowseButton1 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Browse',
              dialogTitle='', id=wxID_FRAME1DIRBROWSEBUTTON1,
              labelText='Select a directory:', newDirectory=False,
              parent=self.panel1, pos=wx.Point(16, 160), size=wx.Size(424, 48),
              startDirectory='.', style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.dirBrowseButton1.SetValue(u'C:')
        self.dirBrowseButton1.SetLabel(u'Select a directory:')
        self.dirBrowseButton1.SetToolTipString(u'dirBrowseButton1')
        self.dirBrowseButton1.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, u'Calibri'))

        self.fileBrowseButtonWithHistory1 = wx.lib.filebrowsebutton.FileBrowseButtonWithHistory(buttonText='Browse',
              dialogTitle=u'Choose a file', fileMask=u'*.json',
              id=wxID_FRAME1FILEBROWSEBUTTONWITHHISTORY1, initialValue='',
              labelText='File Entry:', parent=self.panel1, pos=wx.Point(528,
              72), size=wx.Size(392, 48), startDirectory='.',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type filename or click browse to choose file')
        self.fileBrowseButtonWithHistory1.SetValue(u'C:')
        self.fileBrowseButtonWithHistory1.SetLabel(u'File Entry:')
        self.fileBrowseButtonWithHistory1.SetToolTipString(u'fileBrowseButtonWithHistory1')
        self.fileBrowseButtonWithHistory1.SetFont(wx.Font(9, wx.SWISS,
              wx.NORMAL, wx.NORMAL, False, u'Calibri'))

        self.staticBox5 = wx.StaticBox(id=wxID_FRAME1STATICBOX5,
              label=u'Operate', name='staticBox5', parent=self.panel2,
              pos=wx.Point(0, 48), size=wx.Size(200, 120), style=0)
        self.staticBox5.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Calibri'))

        self.staticBox6 = wx.StaticBox(id=wxID_FRAME1STATICBOX6,
              label=u'Operate', name='staticBox6', parent=self.panel3,
              pos=wx.Point(744, 40), size=wx.Size(216, 128), style=0)
        self.staticBox6.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Calibri'))

        self.staticBox7 = wx.StaticBox(id=wxID_FRAME1STATICBOX7,
              label=u'Params', name='staticBox7', parent=self.panel3,
              pos=wx.Point(8, 40), size=wx.Size(296, 128), style=0)
        self.staticBox7.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Calibri'))

        self.button6 = wx.Button(id=wxID_FRAME1BUTTON6, label=u'Download',
              name='button6', parent=self.panel1, pos=wx.Point(168, 72),
              size=wx.Size(96, 32), style=0)
        self.button6.Enable(False)
        self.button6.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u''))
        self.button6.Bind(wx.EVT_BUTTON, self.OnBtn6Download,
              id=wxID_FRAME1BUTTON6)

        self.button7 = wx.Button(id=wxID_FRAME1BUTTON7, label=u'Upload',
              name='button7', parent=self.panel1, pos=wx.Point(312, 72),
              size=wx.Size(88, 32), style=0)
        self.button7.Enable(False)
        self.button7.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u''))
        self.button7.Bind(wx.EVT_BUTTON, self.OnBtn7Upload,
              id=wxID_FRAME1BUTTON7)

        self.intCtrl1 = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_FRAME1INTCTRL1,
              limited=False, max=None, min=None, name='intCtrl1',
              oob_color=wx.RED, parent=self.panel3, pos=wx.Point(160, 72),
              size=wx.Size(100, 22), style=0, value=800)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Minimum Readings:', name='staticText1',
              parent=self.panel3, pos=wx.Point(24, 72), size=wx.Size(124, 18),
              style=0)
        self.staticText1.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Calibri'))

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Minimum Hits:', name='staticText2', parent=self.panel3,
              pos=wx.Point(56, 104), size=wx.Size(92, 18), style=0)
        self.staticText2.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Calibri'))

        self.intCtrl2 = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_FRAME1INTCTRL2,
              limited=False, max=None, min=None, name='intCtrl2',
              oob_color=wx.RED, parent=self.panel3, pos=wx.Point(160, 104),
              size=wx.Size(100, 22), style=0, value=200)

        self.staticBox9 = wx.StaticBox(id=wxID_FRAME1STATICBOX9,
              label=u'Imu Updated Json File', name='staticBox9',
              parent=self.panel3, pos=wx.Point(320, 40), size=wx.Size(400, 128),
              style=0)
        self.staticBox9.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Calibri'))

        self.fileBrowseButtonWithHistory2 = wx.lib.filebrowsebutton.FileBrowseButtonWithHistory(buttonText='Browse',
              dialogTitle='Choose a file', fileMask=u'*.json',
              id=wxID_FRAME1FILEBROWSEBUTTONWITHHISTORY2, initialValue=u'',
              labelText=u'File Entry:', parent=self.panel3, pos=wx.Point(328,
              80), size=wx.Size(384, 48), startDirectory='.',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type filename or click browse to choose file')
        self.fileBrowseButtonWithHistory2.SetValue(u'C:')
        self.fileBrowseButtonWithHistory2.SetLabel(u'File Entry:')
        self.fileBrowseButtonWithHistory2.SetToolTipString(u'fileBrowseButtonWithHistory2')
        self.fileBrowseButtonWithHistory2.SetFont(wx.Font(8, wx.SWISS,
              wx.NORMAL, wx.BOLD, False, u'Calibri'))

        self.button8 = wx.Button(id=wxID_FRAME1BUTTON8, label=u'Capture',
              name='button8', parent=self.panel3, pos=wx.Point(864, 80),
              size=wx.Size(83, 32), style=0)
        self.button8.Enable(False)
        self.button8.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u''))
        self.button8.Bind(wx.EVT_BUTTON, self.OnBtn8Start,
              id=wxID_FRAME1BUTTON8)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Console Output', name='staticText3', parent=self.panel1,
              pos=wx.Point(360, 392), size=wx.Size(86, 14), style=0)

        self.panel5 = wx.Panel(id=wxID_FRAME1PANEL5, name='panel5', parent=self,
              pos=wx.Point(0, 280), size=wx.Size(1000, 376),
              style=wx.TAB_TRAVERSAL)

        self.richTextCtrl1 = wx.richtext.RichTextCtrl(id=wxID_FRAME1RICHTEXTCTRL1,
              parent=self.panel5, pos=wx.Point(8, 8), size=wx.Size(984, 328),
              style=wx.richtext.RE_MULTILINE|wx.richtext.RE_READONLY|wx.HSCROLL|wx.VSCROLL|wx.EXPAND|wx.TE_RICH2,
              value=u'')

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'Generate Imu Infos', name='staticText4',
              parent=self.panel2, pos=wx.Point(576, 32), size=wx.Size(120, 18),
              style=0)
        self.staticText4.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Calibri'))

        self.richTextCtrl2 = wx.richtext.RichTextCtrl(id=wxID_FRAME1RICHTEXTCTRL2,
              parent=self.panel2, pos=wx.Point(576, 56), size=wx.Size(384, 112),
              style=wx.richtext.RE_MULTILINE, value=u'')
        self.richTextCtrl2.SetLabel(u'richText')

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'Set Timeout(min):', name='staticText5',
              parent=self.panel3, pos=wx.Point(32, 136), size=wx.Size(113, 18),
              style=0)
        self.staticText5.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Calibri'))

        self.intCtrl3 = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_FRAME1INTCTRL3,
              limited=False, max=None, min=None, name='intCtrl3',
              oob_color=wx.RED, parent=self.panel3, pos=wx.Point(160, 136),
              size=wx.Size(100, 24), style=0, value=3)

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label='staticText6', name='staticText6', parent=self.panel2,
              pos=wx.Point(24, 184), size=wx.Size(67, 18), style=0)
        self.staticText6.Show(False)
        self.staticText6.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD, True,
              u'Calibri'))

        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        handler = WxTextCtrlHandle(self.richTextCtrl1)
        print("handler=", handler)
        logger.addHandler(handler)
        strFormat = "%(asctime)s %(levelname)s %(message)s"
        handler.setFormatter(logging.Formatter(strFormat))
        logger.setLevel(logging.NOTSET)
        #self.lighthouse_console = lighthouse_console()
        #self.richTextCtrl1.MoveToLineEnd()
        self.handler_lighthouseconsole = None
        self.handler_imucalibrator = None
        self.handler_vrtrackingcalib = None
        self.serialNum = None
        self.onTimeFlag = False
        self.dirBrowseButton1.SetValue(g_DownloadPath)
        InitTestToolEnv()
        self.result1 = 0
        self.vrTrackCapture = [False]
        self._thread = Thread(target=self.run, args=())
        self._thread1 = Thread(target=self.run1, args=())
        self._thread2 = Thread(target=self.run2, args=())
        self._thread.daemon = True
        self._thread1.daemon = True
        self._thread2.daemon = True
        logging.log(logging.INFO, " Initial Setting Finish")

    def Onstart(self):
        self.onTimeFlag = True
        self.timer1.Start(3000)

    def OnStop(self):
        self.onTimeFlag = False
        self.timer1.Stop()


    def OnBtn1Conn(self, event):

        global gBtn1ConnFlag
        gBtn1ConnFlag = ~gBtn1ConnFlag
        if gBtn1ConnFlag:
            logging.log(logging.INFO, " Click Connect")
            self.button1.SetLabel(u'Connecting')
            #self.lighthouse_console.login()
            self.handler_lighthouseconsole = lighthouse_console()
            boolResult = self.handler_lighthouseconsole.login()
            if boolResult:
                self.onTimeFlag = True
                self.statusBar1.SetStatusText(u'Current Status:   Connected')
                self.button1.SetLabel(u'Disconnect')
                self.button6.Enable(True)
                self.button7.Enable(True)
                self.serialNum = self.handler_lighthouseconsole.getSerialNum()
            else:
                self.button1.SetLabel(u'Connect')
                gBtn1ConnFlag = ~gBtn1ConnFlag
            self.Onstart()

        else:
            self.onTimeFlag = False
            self.statusBar1.SetStatusText(u'Current Status:   Disconnect')
            self.button1.SetLabel(u'Connect')
            self.button6.Enable(False)
            self.button7.Enable(False)
            #self.OnStop()
            self.handler_lighthouseconsole.logout()
            logging.log(logging.INFO, " Click Disconnect")
        event.Skip()

    def OnListBox1Listbox(self, event):
        event.Skip()

    def OnBtn2Conn(self, event):
        global gBtn2ConnFlag
        global gcounts_sample
        gBtn2ConnFlag = ~gBtn2ConnFlag
        gcounts_sample = 0
        if gBtn2ConnFlag:
            logging.log(logging.INFO, " Click Connect")
            self.button2.SetLabel(u'Connecting')
            self.handler_imucalibrator = imu_calibrator()
            boolResult = self.handler_imucalibrator.login()
            if boolResult:
                self.statusBar2.SetStatusText(u'Current Status:   Connected')
                self.button2.SetLabel(u'Disconnect')
                self.button3.Enable(True)
                self.serialNum = self.handler_imucalibrator.getSerialNum()
            else:
                self.button2.SetLabel(u'Connect')
                gBtn2ConnFlag = ~gBtn2ConnFlag
            self.Onstart()
        else:
            self.statusBar2.SetStatusText(u'Current Status:   Disconnect')
            self.button2.SetLabel(u'Connect')
            self.button3.Enable(False)
            self.button4.Enable(False)
            for index in range(1, 7):
                #strCheckBox = "self.checkBox" + str(index)
                #print eval("self.checkBox" + str(index))
                eval("self.checkBox" + str(index)).SetValue(False)

            self.handler_imucalibrator.logout()

        event.Skip()

    def OnBtn3Next(self, event):
        #global gcounts_sample

        if self.button3.GetLabel() == u'Processing':
            pass

        else:
            self.button3.SetLabel(u'Processing')
            strResult = self.handler_imucalibrator.getNextAxesResult()
            #strResult = "ACCEPTED"
            print "strResult", strResult
            strResult = dict(strResult)
            if strResult.has_key("ACCEPTED"):
                global gcounts_sample
                gcounts_sample += 1
                print "self.checkBox"+str(gcounts_sample)
                print eval("self.checkBox"+str(gcounts_sample))
                eval("self.checkBox"+str(gcounts_sample)).SetValue(True)
                gcounts_sample = gcounts_sample % 6

            elif strResult.has_key("REJECTED"):
                wx.MessageBox(strResult["REJECTED"]+", pls switch another orientation.",\
                              'Warning', wx.OK | wx.ICON_WARNING)
                #dlg.ShowModal()
                #dlg.Destroy()
            elif strResult.has_key("DONE"):
                self.button3.Enable(False)
                self.button4.Enable(True)
                self.checkBox6.SetValue(True)
                self.richTextCtrl2.SetValue(strResult["DONE"])
            else:
                wx.MessageBox("Exception Happend, pls re-connect!!!", 'Error',
                              wx.OK | wx.ICON_ERROR)

            self.button3.SetLabel(u'Next')
            #self.button4.Enable(True)
            print "global gcounts_sample = %s"%(gcounts_sample)
        event.Skip()

    def OnBtn4Finish(self, event):
        dictKey = {}
        boolResult = os.path.isfile(self.fileBrowseButtonWithHistory1.GetValue())
        if boolResult:
            updatedFilename = os.path.split(os.path.realpath(self.fileBrowseButtonWithHistory1.GetValue()))[1]
            print updatedFilename
            strImuConfigureInfo = self.richTextCtrl2.GetValue()
            if strImuConfigureInfo != "":
                listImuConfigureInfo = re.findall('.*\[\s+(-?\d+.\d+),\s+(-?\d+.\d+),\s+(-?\d+.\d+)\s+\]', \
                                                  strImuConfigureInfo)
                if listImuConfigureInfo != []:
                    dictKey['acc_scale'] = [float(listImuConfigureInfo[0][i]) for i in range(0, 3)]
                    dictKey['acc_bias'] = [float(listImuConfigureInfo[1][i]) for i in range(0, 3)]
                    dictKey['gyro_scale'] = [float(listImuConfigureInfo[2][i]) for i in range(0, 3)]
                    dictKey['gyro_bias'] = [float(listImuConfigureInfo[3][i]) for i in range(0, 3)]
                    print dictKey['acc_scale'], type(dictKey['acc_scale'][0])
                    print dictKey['acc_bias'], type(dictKey['acc_scale'][0])
                    print dictKey['gyro_scale'], type(dictKey['acc_scale'][0])
                    print dictKey['gyro_bias'], type(dictKey['acc_scale'][0])
                    with open(updatedFilename, 'r') as jsonFile:
                        data = json.load(jsonFile)
                    data['imu']['acc_scale'] = dictKey['acc_scale']
                    data['imu']['acc_bias'] = dictKey['acc_bias']
                    data['imu']['gyro_scale'] = dictKey['gyro_scale']
                    data['imu']['gyro_bias'] = dictKey['gyro_bias']
                    with open(updatedFilename, 'w') as jsonFile:
                        json.dump(data, jsonFile)
                self.staticText6.SetLabel("Updated Imu Json File Path :\n  {0}\nNote: Pls Click Button 'Upload' In Lighthouse UI"\
                                          .format(self.fileBrowseButtonWithHistory1.GetValue()))
                self.staticText6.Shown = True
        else:
            wx.MessageBox("Pls Input Upload Json File In Lighthouse UI !!!", \
                          'Params Check', wx.OK | wx.ICON_INFORMATION)
        #logging.log(logging.INFO, 'ww')
        # self.staticText4.SetLabel('''Calibrating to gravity sphere, radius 9.8066
        # 0.409 accelerometer fit error (6 sample vectors x 8 subsamples per vector)
        # "acc_scale" : [ 0.9977, 0.9991, 0.9944 ],
        # "acc_bias" : [ 0.1842, 0.04925, 0.6027 ],
        # "gyro_scale" : [ 1.0, 1.0, 1.0 ],
        # "gyro_bias" : [ -0.007314, 0.01486, 0.01087 ],
        #
        # ''')
        event.Skip()

    def OnBtn5Conn(self, event):
        global gBtn5ConnFlag

        boolResult = os.path.isfile(self.fileBrowseButtonWithHistory2.GetValue())
        if boolResult:
            gBtn5ConnFlag = ~gBtn5ConnFlag
            if gBtn5ConnFlag:

                logging.log(logging.INFO, " Click Connect")
                self.button5.SetLabel(u'Connecting')
                #self.lighthouse_console.login()
                self.handler_vrtrackingcalib = vrtrackingcalib()
                #os.path.self.fileBrowseButtonWithHistory2.GetValue()
                boolResult = self.handler_vrtrackingcalib.login(self.fileBrowseButtonWithHistory2.GetValue(), \
                                                                self.intCtrl1.GetValue(), \
                                                                self.intCtrl2.GetValue(), \
                                                                self.intCtrl3.GetValue())
                if boolResult:
                    self.statusBar3.SetStatusText(u'Current Status:   Connected')
                    self.button5.SetLabel(u'Disconnect')
                    self.button8.Enable(True)
                    self.serialNum = self.handler_vrtrackingcalib.getSerialNum()
                else:
                    self.button5.SetLabel(u'Connect')
                    gBtn5ConnFlag = ~gBtn5ConnFlag
                self.Onstart()
            else:
                self.statusBar3.SetStatusText(u'Current Status:   Disconnect')
                self.button5.SetLabel(u'Connect')
                self.button8.Enable(False)
                self.handler_vrtrackingcalib.logout()
        else:
            wx.MessageBox("Pls Input Imu Updated Json File !!!", 'Params Check', wx.OK | wx.ICON_INFORMATION)
        event.Skip()

    def OnBtn6Download(self, event):
        logging.log(logging.INFO, " Click Download")
        strDownloadPath = self.dirBrowseButton1.GetValue()
        print "strDownloadPath = ", strDownloadPath
        filename = self.handler_lighthouseconsole.download(strDownloadPath)
        if filename != "":
            self.fileBrowseButtonWithHistory1.SetValue(strDownloadPath + "\\" + filename)
            wx.MessageBox("Download Suc !!!", 'Download Result', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("Download Fail !!!", 'Download Result', wx.OK | wx.ICON_WARNING)
        event.Skip()

    def OnBtn7Upload(self, event):
        logging.log(logging.INFO, " Click Upload")
        strUploadFilename = self.fileBrowseButtonWithHistory1.GetValue()
        boolResult = os.path.isfile(strUploadFilename)
        if boolResult:
            print "strUploadFilename = ", strUploadFilename
            result = self.handler_lighthouseconsole.upload(strUploadFilename)
            if result:
                wx.MessageBox("Upload Suc !!!", 'Upload Result', wx.OK | wx.ICON_INFORMATION)
                self.staticText6.Shown = False
            else:
                wx.MessageBox("Upload Fail !!!", 'Upload Result', wx.OK | wx.ICON_WARNING)
        else:
            wx.MessageBox("Pls Input Upload Json File !!!", 'Params Check', wx.OK | wx.ICON_INFORMATION)

        event.Skip()


    def OnBtn8Start(self, event):



        self._thread.start()
        self._thread1.start()
        self._thread2.start()



        event.Skip()

    def OnTimer1Timer(self, event):
        #print 'self.serialNum =', self.serialNum
        self.updateLoggerShowMode()
        if self.serialNum != None:

            bPnpDeviceConnFlag = isPnpDeviceExist(str(self.serialNum).rstrip())
            #print 'bPnpDeviceConnFlag', bPnpDeviceConnFlag
            if bPnpDeviceConnFlag:
                pass
            else:
                self.statusBar1.SetStatusText(u'Current Status:   Disconnect')
                self.statusBar2.SetStatusText(u'Current Status:   Disconnect')
                self.statusBar3.SetStatusText(u'Current Status:   Disconnect')
                self.button1.SetLabel(u'Connect')
                self.button2.SetLabel(u'Connect')
                self.button5.SetLabel(u'Connect')
                self.button3.Enable(False)
                self.button4.Enable(False)
                self.button6.Enable(False)
                self.button7.Enable(False)
                self.button8.Enable(False)
                # self.button1.RemoveEventHandler()
                # self.button2.RemoveEventHandler()
                # self.button5.RemoveEventHandler()
                #self.handler_lighthouseconsole.logout()
                #InitTestToolEnv()
                self.OnStop()
                #if boolFlag == False:
                logging.log(logging.ERROR, " Pnp Device not plugin")
                wx.MessageBox("Detected, There it is not, pls check connnectivity !!!", \
                              'Error', wx.OK | wx.ICON_ERROR)

        else:
            #wx.MessageBox("Pls test connectivity by using lighthouse_console!!!",'Warning', wx.OK | wx.ICON_WARNING)
            #self.OnStop()
            #print "111== ", self.button1.GetEventHandler()
            #print "222== ", self.button2.GetEventHandler()
            #print "555== ", self.button5.GetEventHandler()
            pass
        event.Skip()

    def updateLoggerShowMode(self):
        # # Resart the timer
        # # t = Timer(0.25, self.AddText)
        # # t.start()
        #
        #
        # holdingBack = True
        # # Work out if we're at the end of the file
        # currentCaretPosition = self.richTextCtrl1.GetInsertionPoint()
        # currentLengthOfText = self.richTextCtrl1.GetLastPosition()
        # if currentCaretPosition != currentLengthOfText:
        #     holdingBack = True
        # else:
        #     holdingBack = False
        #
        # #timeStamp = str(time.time())
        #
        # # If we're not at the end of the file, we're holding back
        # if holdingBack:
        #     #print "%s FROZEN" % (timeStamp)
        #     self.richTextCtrl1.Freeze()
        #     (currentSelectionStart, currentSelectionEnd) = self.richTextCtrl1.GetSelection()
        #     #self.richTextCtrl1.AppendText(timeStamp + "\n")
        #     self.richTextCtrl1.SetInsertionPoint(currentCaretPosition)
        #     self.richTextCtrl1.SetSelection(currentSelectionStart, currentSelectionEnd)
        #     self.richTextCtrl1.Thaw()
        # else:
        #     pass
        #     #print "%s THAWED" % (timeStamp)
        #     #self.richTextCtrl1.AppendText(timeStamp + "\n")


        # curPos = self.richTextCtrl1.GetInsertionPoint()
        # print 'curPos=', curPos
        # curCol, curRow = self.richTextCtrl1.PositionToXY(curPos)
        # print 'curCol=%s curRow=%s'%(curCol, curRow)
        # lineNum = curRow
        # print "lineNum=",lineNum
        # lineText = self.richTextCtrl1.GetLineText(lineNum)
        # newPos = self.richTextCtrl1.XYToPosition(len(lineText), curRow)
        # print 'newPos = ',newPos
        # self.richTextCtrl1.SetInsertionPoint(newPos)
        self.richTextCtrl1.ShowPosition(self.richTextCtrl1.GetLastPosition())

    def run(self):
        self.handler_vrtrackingcalib.getCapture(self.vrTrackCapture)

    def run1(self):
        for i in range(int(self.intCtrl3.GetValue())*60-1, 0, -1):
            print i
            time.sleep(1)
            self.showOnTime(str(i))
        # self._thread.join()
        # print("thread = ", self.bResult)
        self.result1 = 1

    def run2(self):
        while True:
            time.sleep(1)
            if self.result1 == 1:
                self.button8.SetLabel("Capture")
                # self._thread.
                # self._thread1.stop()


            if self.vrTrackCapture[0]:
                self.button8.SetLabel("TIMEOUT")

    # @call_after
    def showOnTime(self, msg):
        self.button8.SetLabel(msg)
