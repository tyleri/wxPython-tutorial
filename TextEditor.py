#!/usr/bin/env python
import wx
import os

class MyFrame(wx.Frame):
    """ We simply derive a new class of Frame. """

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(200,100))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        # Setting up the menu
        filemenu = wx.Menu()

        menuAbout = filemenu.Append(wx.ID_ABOUT, "About", " Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT, "Exit", " Terminate the program")
        menuOpen = filemenu.Append(wx.ID_OPEN, "Open", " Open a file")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "File")
        self.SetMenuBar(menuBar)

        # Set events
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        #filemenu.AppendSeparator()
        
        self.Show(True)

    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, "A small text editor", "About sample editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, event):
        self.Close(True)

    def OnOpen(self, event):
        """ Open a file """
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

app = wx.App(False)
frame = MyFrame(None, 'Sample editor')
app.MainLoop()
