import wx
import wx.xrc
from wx.lib.pdfviewer import pdfViewer, pdfButtonPanel
import os,stat
from PyPDF2 import PdfFileReader,PdfFileWriter
from PyPDF2.generic import NameObject, createStringObject
import json
from InForm import pdfCreateFrame
from encryptfs import EncryptFS
from encryptfs.encrypt_files import decrypt_file, encrypt_file, gen_key
import win32con, win32api
import shutil
import tempfile
import errno



class PdfViewer(pdfViewer):
	def __init__(self,parent):
		pdfViewer.__init__( self,parent, wx.NewId(), wx.DefaultPosition,
                                wx.DefaultSize, wx.HSCROLL|wx.VSCROLL|wx.SUNKEN_BORDER)
		self.UsePrintDirect = ``False``

	def openPdf(self,path):
	    self.LoadFile(path)

	

		
class Tree(wx.TreeCtrl):
	def __init__(self,parent):
		wx.TreeCtrl.__init__( self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )

	def add_root(self):
		self.root_tree=self.AddRoot('files')
	
	def addItem(self,filename,path):
		self.item=self.AppendItem(self.root_tree,filename)
		self.SetItemData(self.item,wx.TreeItemData(path))

	def getRoot(self):
		return self.root_tree
	
	def expandTree(self,expand):
		if expand:
			self.ExpandAll()

	def DeleteItems(self):
		self.DeleteAllItems()

		


class LoadFiles():
	def __init__(self,path):
		#decrypt from flash to temp
		self.pdfFiles=[]
		self.pdfPaths=[]
		self.cwd=os.getcwd()
		#self.directory=self.cwd+"\pdffiles"
                self.directory=path
                print self.directory
                if os.path.exists(self.directory):
                        self.temp_path=tempfile.mkdtemp()
                        print self.temp_path
                        os.chdir(self.directory)
                        self.encfs = EncryptFS('cool')
                        self.key=self.encfs.key
                        self.currentdir=self.encfs.current_dir
                        self.index=self.encfs.current_index
                        for file in self.index["files"]:
                                decrypt_file(self.key, os.path.join(self.currentdir, file["filename_enc"]), out_filename=os.path.join(self.temp_path, file["filename"]))
                        
                        for self.filename in os.listdir(self.temp_path):
							if self.filename.endswith('.pdf'):
								self.pdfPaths.append(os.path.join(self.temp_path,self.filename))
								self.pdfFiles.append(self.filename)


	def update(self):
		 self.pdfPaths=[]
		 self.pdfFiles=[]
		 for self.filename in os.listdir(self.temp_path):
				if self.filename.endswith('.pdf'):
					self.pdfPaths.append(os.path.join(self.temp_path,self.filename))
					self.pdfFiles.append(self.filename)

	def getFilesNameList(self):
		return self.pdfFiles

	def getFilesPathList(self):
		return self.pdfPaths



class MainFormFrame ( wx.Frame ):
	
	def __init__( self, parent, directory ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.flashdir=directory
		self.loadfiles=LoadFiles(directory)
		self.tempdir=self.loadfiles.temp_path
		self.fileobj=None
		print self.tempdir
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		self.menu = wx.MenuBar( 0 )
		self.file = wx.Menu()
		self.newMenuItem = wx.MenuItem( self.file, wx.ID_ANY, u"New", wx.EmptyString, wx.ITEM_NORMAL )
		self.file.AppendItem( self.newMenuItem )
		
		self.menu.Append( self.file, u"File" ) 
		
		self.SetMenuBar( self.menu )


		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.windowSplitter = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.windowSplitter.Bind( wx.EVT_IDLE, self.windowSplitterOnIdle )

		
		self.leftpanel = wx.Panel( self.windowSplitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
	

		#self.m_treeCtrl1 = wx.TreeCtrl( self.leftpanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		
		self.tree=Tree(self.leftpanel)
		#self. root_tree=self.m_treeCtrl1.AddRoot('files')
		self.tree.add_root()

		for self.path, self.filename in zip(self.loadfiles.getFilesPathList(),self.loadfiles.getFilesNameList()):
        	     self.tree.addItem(self.filename,self.path)
		self.tree.expandTree(True)
		#self.m_treeCtrl1.AppendItem(self.root_tree,'b')
		#self.m_treeCtrl1.ExpandAll()



		bSizer2.Add( self.tree, 1, wx.ALL|wx.EXPAND, 5 )


		self.searchCtrl = wx.SearchCtrl( self.leftpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER)
		self.searchCtrl.ShowSearchButton( True )
		self.searchCtrl.ShowCancelButton( False )
		bSizer2.Add( self.searchCtrl, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.leftpanel.SetSizer( bSizer2 )
		self.leftpanel.Layout()
		bSizer2.Fit( self.leftpanel )
		self.rightpanel = wx.Panel( self.windowSplitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		#self.buttonpanel = pdfButtonPanel(self.rightpanel, wx.NewId(),
        #                        wx.DefaultPosition, wx.DefaultSize, 0)
		#bSizer3.Add(self.buttonpanel, 0, wx.EXPAND, 5)

		self.pdf_Viewer = PdfViewer( self.rightpanel)
		#bSizer11.Add(self.viewer, 1, wx.GROW|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5)
		
		bSizer3.Add(self.pdf_Viewer, 1, wx.EXPAND, 5)
		#self.viewer.UsePrintDirect = ``False``
		#self.pdf_Viewer.openPdf(self.loadfiles.getFilesPathList[0])

		#self.buttonpanel.viewer = self.pdf_Viewer
		#self.pdf_Viewer.buttonpanel = self.buttonpanel
		
		
		self.rightpanel.SetSizer( bSizer3 )
		self.rightpanel.Layout()
		bSizer3.Fit( self.rightpanel )
		self.windowSplitter.SplitVertically( self.leftpanel, self.rightpanel,0)
		bSizer1.Add( self.windowSplitter, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )

		self.Bind( wx.EVT_MENU, self.newMenuItemSelected, id = self.newMenuItem.GetId() )
		self.tree.Bind( wx.EVT_TREE_SEL_CHANGED, self.m_treeCtrl1ItemSelection )
		
		#self.searchCtrl.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.searchOnTextEnter )
		self.searchCtrl.Bind( wx.EVT_TEXT_ENTER, self.searchOnTextEnter )
		self.Bind( wx.EVT_CLOSE, self.frameClosed )
	
	

	def __del__( self ):
		pass

	def frameClosed( self, event ):
		#self.pdf_Viewer=None
		#self.rightpanel.Destroy()
		#os.chdir(self.tempdir)
                #self.loadfiles.encfs.encrypt_all()
                #os.chmod(self.tempdir, stat.S_IWRITE)
                #print self.pdf_Viewer.have_file
		#shutil.rmtree(self.tempdir)
		if self.fileobj:
		   self.fileobj.close()
		shutil.rmtree(self.tempdir)
		event.Skip()


	def update_tree(self):
		self.tree.DeleteItems()
		self.loadfiles.update()
		print "update_tree"
		print self.loadfiles.getFilesNameList()
		self.tree.add_root()
		for self.path, self.filename in zip(self.loadfiles.getFilesPathList(),self.loadfiles.getFilesNameList()):
        	     self.tree.addItem(self.filename,self.path)
		self.tree.expandTree(True)
		print "ok"

	def update_tree_after_search(self,foundpath,foundfiles):
		if len(foundpath)>=1 and len(foundfiles)>=1:
			print "tree updated"
			self.tree.DeleteItems()
			self.tree.add_root()
			for self.path, self.filename in zip(foundpath,foundfiles):
	        	     self.tree.addItem(self.filename,self.path)
			self.tree.expandTree(True)


	def showMesssage(self,mesg):
		wx.MessageBox(mesg,'Info',wx.OK|wx.ICON_INFORMATION)




	def m_treeCtrl1ItemSelection( self, event ):
		
		self.item =  event.GetItem()
		if self.tree.GetItemData(self.item):
			self.pdfFilePath=self.tree.GetItemData(self.item).GetData()
			print self.pdfFilePath
			if self.fileobj:
		           self.fileobj.close()
			self.fileobj=file(self.pdfFilePath, 'rb')
			self.pdf_Viewer.openPdf(self.fileobj)
		event.Skip()


	def textChanged( self, event ):
		#print self.searchCtrl.GetValue()
		event.Skip()



	def searchOnTextEnter( self, event ):
	
		if self.searchCtrl.GetValue()!='':
			if ":" in self.searchCtrl.GetValue().lower():
				self.key_values=self.searchCtrl.GetValue().lower().split(";")
				print self.key_values
				self.keys=[]
				self.values=[]
				for self.key_value in self.key_values:
					print self.key_value.split(":")[0]
					self.keys.append(self.key_value.split(":")[0])
					self.values.append(self.key_value.split(":")[1])

				self.searchFoundPath=[]
				self.searchFoundFile=[]
				for self.path, self.filename in zip(self.loadfiles.getFilesPathList(),self.loadfiles.getFilesNameList()):
					self.found_state=[]
					print self.path
					self.input_file = file(self.path, 'rb')
					self.pdfFile=PdfFileReader(self.input_file)
					self.docInfo=self.pdfFile.getDocumentInfo()
					self.data= self.docInfo["/Description"]
					self.json_data=json.loads(self.data)

					#print not self.json_data.viewkeys()&self.keys

					if  not not self.json_data.viewkeys()&self.keys: #all keys present  http://stackoverflow.com/questions/16004593/python-what-is-best-way-to-check-multiple-keys-exists-in-a-dictionary
						#for self.key,self.value in zip(self.keys,self.values):
							#if self.value in self.json_data[self.key].split():
						print "found key"
						
						for self.key, self.value in zip(self.keys,self.values):
							if all (self.word in self.json_data[self.key] for self.word in self.value.split()):
								self.found_state.append(True)
							else:
								self.found_state.append(False)

						print self.found_state

						if all(self.found_state):
								self.searchFoundPath.append(self.path)
								self.searchFoundFile.append(self.filename)
				
                                if len(self.searchFoundPath)>0:
                                       self.showMesssage("Found")
                                       self.update_tree_after_search(self.searchFoundPath,self.searchFoundFile)
                                else:
                                       self.showMesssage("Not Found")
						

                        else:
                                self.showMesssage("Wrong format")
                                self.update_tree()
                else:
                        self.update_tree()
                

		event.Skip()


	def newMenuItemSelected( self, event ):
		print "menu item"
		###
		# new window opend
		###

		pdfcreateframe=pdfCreateFrame(None,self,self.flashdir,self.tempdir)
		pdfcreateframe.Show()
		pdfcreateframe.Maximize(True)
		print "new newMenuItem"

		event.Skip()
	

	
	def windowSplitterOnIdle( self, event ):
		#print self.GetSize()
		self.windowSplitter.SetSashPosition(self.GetSize()[0]/4)
		self.windowSplitter.Unbind( wx.EVT_IDLE )

	def getTempdir(self):
		return self.tempdir
	

'''
app=wx.App()
frame=MainFormFrame(None)
frame.Show()
frame.Maximize(True)
app.MainLoop()
'''
