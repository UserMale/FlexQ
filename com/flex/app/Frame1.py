#Boa:Frame:Frame1

import wx
import wx.lib.intctrl
import wx.lib.filebrowsebutton

gBtn1ConnFlag = False
gBtn2ConnFlag = False
gBtn5ConnFlag = False

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3, 
 wxID_FRAME1BUTTON4, wxID_FRAME1BUTTON5, wxID_FRAME1BUTTON6, 
 wxID_FRAME1BUTTON7, wxID_FRAME1BUTTON8, wxID_FRAME1CHECKBOX1, 
 wxID_FRAME1CHECKBOX2, wxID_FRAME1CHECKBOX3, wxID_FRAME1CHECKBOX4, 
 wxID_FRAME1CHECKBOX5, wxID_FRAME1CHECKBOX6, wxID_FRAME1DIRBROWSEBUTTON1, 
 wxID_FRAME1FILEBROWSEBUTTONWITHHISTORY1, 
 wxID_FRAME1FILEBROWSEBUTTONWITHHISTORY2, wxID_FRAME1INTCTRL1, 
 wxID_FRAME1INTCTRL2, wxID_FRAME1LISTBOX1, wxID_FRAME1NOTEBOOK1, 
 wxID_FRAME1PANEL1, wxID_FRAME1PANEL2, wxID_FRAME1PANEL3, wxID_FRAME1PANEL4, 
 wxID_FRAME1STATICBOX1, wxID_FRAME1STATICBOX2, wxID_FRAME1STATICBOX3, 
 wxID_FRAME1STATICBOX4, wxID_FRAME1STATICBOX5, wxID_FRAME1STATICBOX6, 
 wxID_FRAME1STATICBOX7, wxID_FRAME1STATICBOX9, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1STATUSBAR1, 
 wxID_FRAME1STATUSBAR2, wxID_FRAME1STATUSBAR3, 
] = [wx.NewId() for _init_ctrls in range(40)]

[wxID_FRAME1MENU1ITEMS0] = [wx.NewId() for _init_coll_menu1_Items in range(1)]

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

        parent.AddPage(imageId=-1, page=self.panel1, select=True,
              text=u'lighthouse_console')
        parent.AddPage(imageId=-1, page=self.panel2, select=False,
              text=u'imu_calibrator')
        parent.AddPage(imageId=-1, page=self.panel3, select=False,
              text=u'vrtrackingcalib')
        parent.AddPage(imageId=-1, page=self.panel4, select=False, text=u'help')

    def _init_utils(self):
        # generated method, don't edit
        self.FlexQ = wx.MenuBar()
        self.FlexQ.SetThemeEnabled(True)

        self.menu1 = wx.Menu(title='')

        self._init_coll_FlexQ_Menus(self.FlexQ)
        self._init_coll_menu1_Items(self.menu1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(656, 294), size=wx.Size(981, 568),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self._init_utils()
        self.SetClientSize(wx.Size(965, 529))

        self.notebook1 = wx.Notebook(id=wxID_FRAME1NOTEBOOK1, name='notebook1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(965, 529), style=0)
        self.notebook1.SetThemeEnabled(True)
        self.notebook1.SetAutoLayout(True)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(957, 502),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetAutoLayout(True)

        self.panel2 = wx.Panel(id=wxID_FRAME1PANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(957, 502),
              style=wx.TAB_TRAVERSAL)

        self.panel3 = wx.Panel(id=wxID_FRAME1PANEL3, name='panel3',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(957, 502),
              style=wx.TAB_TRAVERSAL)

        self.panel4 = wx.Panel(id=wxID_FRAME1PANEL4, name='panel4',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(957, 502),
              style=wx.TAB_TRAVERSAL)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'Connect',
              name='button1', parent=self.panel1, pos=wx.Point(16, 72),
              size=wx.Size(75, 24), style=0)
        self.button1.SetThemeEnabled(True)
        self.button1.SetAutoLayout(True)
        self.button1.Bind(wx.EVT_BUTTON, self.OnBtn1Conn, id=wxID_FRAME1BUTTON1)

        self.statusBar1 = wx.StatusBar(id=wxID_FRAME1STATUSBAR1,
              name='statusBar1', parent=self.panel1, style=0)
        self.statusBar1.SetStatusText(u'Connect Status')
        self.statusBar1.SetToolTipString(u'statusBar1')
        self.statusBar1.SetThemeEnabled(True)
        self.statusBar1.SetAutoLayout(True)

        self.listBox1 = wx.ListBox(choices=[], id=wxID_FRAME1LISTBOX1,
              name='listBox1', parent=self.panel1, pos=wx.Point(544, 64),
              size=wx.Size(408, 416), style=0)
        self.listBox1.SetThemeEnabled(False)
        self.listBox1.SetAutoLayout(True)
        self.listBox1.SetLabel(u'Console Output')
        self.listBox1.SetStringSelection(u'1')
        self.listBox1.Bind(wx.EVT_LISTBOX, self.OnListBox1Listbox,
              id=wxID_FRAME1LISTBOX1)

        self.statusBar2 = wx.StatusBar(id=wxID_FRAME1STATUSBAR2,
              name='statusBar2', parent=self.panel2, style=0)
        self.statusBar2.SetStatusText(u'Connect Status')

        self.statusBar3 = wx.StatusBar(id=wxID_FRAME1STATUSBAR3,
              name='statusBar3', parent=self.panel3, style=0)
        self.statusBar3.SetStatusText(u'Connect Status')

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label=u'Connect',
              name='button2', parent=self.panel2, pos=wx.Point(8, 96),
              size=wx.Size(75, 24), style=0)
        self.button2.SetAutoLayout(True)
        self.button2.Bind(wx.EVT_BUTTON, self.OnBtn2Conn, id=wxID_FRAME1BUTTON2)

        self.checkBox1 = wx.CheckBox(id=wxID_FRAME1CHECKBOX1, label=u'Sample1',
              name='checkBox1', parent=self.panel2, pos=wx.Point(240, 88),
              size=wx.Size(80, 14), style=0)
        self.checkBox1.SetValue(False)
        self.checkBox1.Show(True)

        self.checkBox2 = wx.CheckBox(id=wxID_FRAME1CHECKBOX2, label=u'Sample2',
              name='checkBox2', parent=self.panel2, pos=wx.Point(240, 128),
              size=wx.Size(79, 14), style=0)
        self.checkBox2.SetValue(False)

        self.checkBox3 = wx.CheckBox(id=wxID_FRAME1CHECKBOX3, label=u'Sample3',
              name='checkBox3', parent=self.panel2, pos=wx.Point(240, 168),
              size=wx.Size(79, 14), style=0)
        self.checkBox3.SetValue(True)

        self.checkBox4 = wx.CheckBox(id=wxID_FRAME1CHECKBOX4, label=u'Sample4',
              name='checkBox4', parent=self.panel2, pos=wx.Point(240, 208),
              size=wx.Size(79, 14), style=0)
        self.checkBox4.SetValue(True)

        self.checkBox5 = wx.CheckBox(id=wxID_FRAME1CHECKBOX5, label=u'Sample5',
              name='checkBox5', parent=self.panel2, pos=wx.Point(240, 248),
              size=wx.Size(79, 14), style=0)
        self.checkBox5.SetValue(True)

        self.checkBox6 = wx.CheckBox(id=wxID_FRAME1CHECKBOX6, label=u'Sample6',
              name='checkBox6', parent=self.panel2, pos=wx.Point(240, 288),
              size=wx.Size(79, 14), style=0)
        self.checkBox6.SetValue(True)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label=u'Next',
              name='button3', parent=self.panel2, pos=wx.Point(240, 328),
              size=wx.Size(75, 24), style=0)
        self.button3.Enable(False)
        self.button3.Bind(wx.EVT_BUTTON, self.OnBtn3Next, id=wxID_FRAME1BUTTON3)

        self.button4 = wx.Button(id=wxID_FRAME1BUTTON4, label=u'Finish',
              name='button4', parent=self.panel2, pos=wx.Point(424, 328),
              size=wx.Size(75, 24), style=0)
        self.button4.Enable(False)
        self.button4.Bind(wx.EVT_BUTTON, self.OnBtn4Finish,
              id=wxID_FRAME1BUTTON4)

        self.button5 = wx.Button(id=wxID_FRAME1BUTTON5, label=u'Connect',
              name='button5', parent=self.panel3, pos=wx.Point(40, 344),
              size=wx.Size(75, 24), style=0)
        self.button5.Bind(wx.EVT_BUTTON, self.OnBtn5Conn, id=wxID_FRAME1BUTTON5)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1, label=u'Steps',
              name='staticBox1', parent=self.panel2, pos=wx.Point(192, 64),
              size=wx.Size(336, 328), style=0)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label=u'Download Save Path ', name='staticBox2',
              parent=self.panel1, pos=wx.Point(8, 184), size=wx.Size(400, 100),
              style=0)

        self.staticBox3 = wx.StaticBox(id=wxID_FRAME1STATICBOX3,
              label=u'Upload Json File Path', name='staticBox3',
              parent=self.panel1, pos=wx.Point(8, 312), size=wx.Size(400, 100),
              style=0)

        self.staticBox4 = wx.StaticBox(id=wxID_FRAME1STATICBOX4,
              label=u'Operate', name='staticBox4', parent=self.panel1,
              pos=wx.Point(8, 48), size=wx.Size(400, 112), style=0)

        self.dirBrowseButton1 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Browse',
              dialogTitle='', id=wxID_FRAME1DIRBROWSEBUTTON1,
              labelText='Select a directory:', newDirectory=False,
              parent=self.panel1, pos=wx.Point(16, 216), size=wx.Size(392, 48),
              startDirectory='.', style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.dirBrowseButton1.SetValue(u'C:')
        self.dirBrowseButton1.SetLabel(u'Select a directory:')
        self.dirBrowseButton1.SetToolTipString(u'dirBrowseButton1')

        self.fileBrowseButtonWithHistory1 = wx.lib.filebrowsebutton.FileBrowseButtonWithHistory(buttonText='Browse',
              dialogTitle=u'Choose a file', fileMask=u'*.json',
              id=wxID_FRAME1FILEBROWSEBUTTONWITHHISTORY1, initialValue='',
              labelText='File Entry:', parent=self.panel1, pos=wx.Point(16,
              344), size=wx.Size(392, 48), startDirectory='.',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type filename or click browse to choose file')
        self.fileBrowseButtonWithHistory1.SetValue(u'C:')
        self.fileBrowseButtonWithHistory1.SetLabel(u'File Entry:')
        self.fileBrowseButtonWithHistory1.SetToolTipString(u'fileBrowseButtonWithHistory1')

        self.staticBox5 = wx.StaticBox(id=wxID_FRAME1STATICBOX5,
              label=u'Operate', name='staticBox5', parent=self.panel2,
              pos=wx.Point(0, 64), size=wx.Size(184, 328), style=0)

        self.staticBox6 = wx.StaticBox(id=wxID_FRAME1STATICBOX6,
              label=u'Operate', name='staticBox6', parent=self.panel3,
              pos=wx.Point(16, 320), size=wx.Size(304, 160), style=0)

        self.staticBox7 = wx.StaticBox(id=wxID_FRAME1STATICBOX7,
              label=u'Params', name='staticBox7', parent=self.panel3,
              pos=wx.Point(16, 56), size=wx.Size(304, 128), style=0)

        self.button6 = wx.Button(id=wxID_FRAME1BUTTON6, label=u'Download',
              name='button6', parent=self.panel1, pos=wx.Point(152, 72),
              size=wx.Size(75, 24), style=0)
        self.button6.Enable(False)
        self.button6.Bind(wx.EVT_BUTTON, self.OnBtn6Download,
              id=wxID_FRAME1BUTTON6)

        self.button7 = wx.Button(id=wxID_FRAME1BUTTON7, label=u'Upload',
              name='button7', parent=self.panel1, pos=wx.Point(288, 72),
              size=wx.Size(75, 24), style=0)
        self.button7.Enable(False)
        self.button7.Bind(wx.EVT_BUTTON, self.OnBtn7Upload,
              id=wxID_FRAME1BUTTON7)

        self.intCtrl1 = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_FRAME1INTCTRL1,
              limited=False, max=None, min=None, name='intCtrl1',
              oob_color=wx.RED, parent=self.panel3, pos=wx.Point(152, 88),
              size=wx.Size(100, 22), style=0, value=800)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Minimum Readings:', name='staticText1',
              parent=self.panel3, pos=wx.Point(32, 88), size=wx.Size(103, 14),
              style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Minimum Hits:', name='staticText2', parent=self.panel3,
              pos=wx.Point(32, 144), size=wx.Size(75, 14), style=0)

        self.intCtrl2 = wx.lib.intctrl.IntCtrl(allow_long=False,
              allow_none=False, default_color=wx.BLACK, id=wxID_FRAME1INTCTRL2,
              limited=False, max=None, min=None, name='intCtrl2',
              oob_color=wx.RED, parent=self.panel3, pos=wx.Point(152, 136),
              size=wx.Size(100, 22), style=0, value=200)

        self.staticBox9 = wx.StaticBox(id=wxID_FRAME1STATICBOX9,
              label=u'Imu Updated Json File', name='staticBox9',
              parent=self.panel3, pos=wx.Point(16, 208), size=wx.Size(304, 100),
              style=0)

        self.fileBrowseButtonWithHistory2 = wx.lib.filebrowsebutton.FileBrowseButtonWithHistory(buttonText='Browse',
              dialogTitle='Choose a file', fileMask=u'*.json',
              id=wxID_FRAME1FILEBROWSEBUTTONWITHHISTORY2, initialValue=u'',
              labelText=u'File Entry:', parent=self.panel3, pos=wx.Point(16,
              248), size=wx.Size(296, 48), startDirectory='.',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type filename or click browse to choose file')
        self.fileBrowseButtonWithHistory2.SetValue(u'C:')
        self.fileBrowseButtonWithHistory2.SetLabel(u'File Entry:')
        self.fileBrowseButtonWithHistory2.SetToolTipString(u'fileBrowseButtonWithHistory2')

        self.button8 = wx.Button(id=wxID_FRAME1BUTTON8, label=u'Start',
              name='button8', parent=self.panel3, pos=wx.Point(224, 432),
              size=wx.Size(75, 24), style=0)
        self.button8.Enable(False)
        self.button8.Bind(wx.EVT_BUTTON, self.OnBtn8Start,
              id=wxID_FRAME1BUTTON8)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Console Output', name='staticText3', parent=self.panel1,
              pos=wx.Point(544, 48), size=wx.Size(86, 14), style=0)

        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBtn1Conn(self, event):
        global gBtn1ConnFlag
        gBtn1ConnFlag = ~gBtn1ConnFlag
        if gBtn1ConnFlag :
            self.button1.SetLabel(u'Disconnect')
            self.button6.Enable(True)
            self.button7.Enable(True)
        else:
            self.button1.SetLabel(u'Connect')
            self.button6.Enable(False)
            self.button7.Enable(False)

        event.Skip()

    def OnListBox1Listbox(self, event):
        event.Skip()

    def OnBtn2Conn(self, event):
        global gBtn2ConnFlag
        gBtn2ConnFlag = ~gBtn2ConnFlag
        if gBtn2ConnFlag :
            self.button3.Enable(True)
        else:
            self.button3.Enable(False)

        event.Skip()

    def OnBtn3Next(self, event):
        event.Skip()

    def OnBtn4Finish(self, event):
        event.Skip()

    def OnBtn5Conn(self, event):
        global gBtn5ConnFlag
        gBtn5ConnFlag = ~gBtn5ConnFlag
        if gBtn5ConnFlag :
            self.button8.Enable(True)
        else:
            self.button8.Enable(False)
        event.Skip()

    def OnBtn6Download(self, event):
        event.Skip()

    def OnBtn7Upload(self, event):
        event.Skip()

    def OnBtn8Start(self, event):
        event.Skip()
