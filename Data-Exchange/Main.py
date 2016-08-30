# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os,stat,shutil
import win32file
import win32con, win32api
from MainForm import MainFormFrame
import errno

###########################################################################
## Class MainFrame
###########################################################################

def USB_Flashes():
	USB_flashes=[]
	dv = win32api.GetLogicalDriveStrings()
	dv = dv.split('\000')[:-1]
	for p in dv:
		if win32file.GetDriveType(p)==win32file.DRIVE_REMOVABLE:
			USB_flashes.append(p)
	return USB_flashes


class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.tempdir=None
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.readText = wx.StaticText( self, wx.ID_ANY, u"Click read button to read data (USB FLASH must be inserted)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.readText.Wrap( -1 )
		self.readText.SetFont( wx.Font( 10, 74, 90, 92, False, "Arial" ) )
		
		bSizer1.Add( self.readText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.readButton = wx.Button( self, wx.ID_ANY, u"Read", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.readButton.SetFont( wx.Font( 10, 74, 90, 92, False, "Arial" ) )
		
		bSizer1.Add( self.readButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.createTxt = wx.StaticText( self, wx.ID_ANY, u"Click create to create new device (Formated USB FLASH must be inserted)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.createTxt.Wrap( -1 )
		self.createTxt.SetFont( wx.Font( 10, 74, 90, 92, False, "Arial" ) )
		
		bSizer1.Add( self.createTxt, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.createButton = wx.Button( self, wx.ID_ANY, u"Create", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.createButton.SetFont( wx.Font( 10, 74, 90, 92, False, "Arial" ) )
		
		bSizer1.Add( self.createButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.readButton.Bind( wx.EVT_BUTTON, self.readView )
		self.createButton.Bind( wx.EVT_BUTTON, self.createDevice )
		self.Bind( wx.EVT_CLOSE, self.frameClosed )
	
		

	def frameClosed( self, event ):
		#shutil.rmtree(self.tempdir)
		event.Skip()
		
	
	def __del__( self ):
		pass


	def showMesssage(self,mesg):
		wx.MessageBox(mesg,'Info',wx.OK|wx.ICON_INFORMATION)


	
	# Virtual event handlers, overide them in your derived class
	def readView( self, event ):
		if len(USB_Flashes())>0:
			print USB_Flashes()
			self.directory=USB_Flashes()[0]+"pdfencyptedfiles"
			if not os.path.exists(self.directory):
				self.showMesssage("Insert right Flash")
			else:
				###
				# new window 
				###
				'''
				if self.tempdir!=None and os.path.exists(self.tempdir):
					shutil.rmtree(self.tempdir)
                '''
				frame=MainFormFrame(None,self.directory)
				frame.Show()
				frame.Maximize(True)
				#self.tempdir=frame.getTempdir()
				self.Close()
		else:
			print "no flash"
			self.showMesssage("No USB flash, Insert USB")
		event.Skip()

	
	def createDevice( self, event ):
		if len(USB_Flashes())>0:
			print USB_Flashes()
			self.directory=USB_Flashes()[0]+"pdfencyptedfiles"
			if not os.path.exists(self.directory):
			    os.makedirs(self.directory)
			    win32api.SetFileAttributes(self.directory,win32con.FILE_ATTRIBUTE_HIDDEN)
			    if os.path.exists(self.directory):
			    	self.showMesssage("USB flash is ready for data")
		else:
			print "no flash"
			self.showMesssage("No USB flash, Insert USB")
		event.Skip()


	

app=wx.App()
frame=MainFrame(None)
frame.Show() 
app.MainLoop()
