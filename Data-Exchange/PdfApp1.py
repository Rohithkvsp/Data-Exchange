
import wx
import wx.xrc
from wx.lib.pdfviewer import pdfViewer, pdfButtonPanel
import os
import PyPDF2




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
		self.root_tree=self.AddRoot('files')
	
	def addItem(self,filename,path):
		self.item=self.AppendItem(self.root_tree,filename)
		self.SetItemData(self.item,wx.TreeItemData(path))

	def getRoot(self):
		return self.root_tree
	
	def expandTree(self,expand):
		if expand:
			self.ExpandAll()



class LoadFiles():
	def __init__(self):
		self.pdfFiles=[]
		self.pdfPaths=[]
		self.cwd=os.getcwd()
		self.directory=self.cwd+"\pdffiles"
		for self.filename in os.listdir(self.directory):
			if self.filename.endswith('.pdf'):
				self.pdfPaths.append(os.path.join(self.directory,self.filename))
				self.pdfFiles.append(self.filename)

	def getFilesNameList(self):
		return self.pdfFiles

	def getFilesPathList(self):
		return self.pdfPaths




class Frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.loadfiles=LoadFiles()
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.windowSplitter = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.windowSplitter.Bind( wx.EVT_IDLE, self.windowSplitterOnIdle )
		
		self.leftpanel = wx.Panel( self.windowSplitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
	

		#self.m_treeCtrl1 = wx.TreeCtrl( self.leftpanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		
		self.tree=Tree(self.leftpanel)
		#self. root_tree=self.m_treeCtrl1.AddRoot('files')
		for self.path, self.filename in zip(self.loadfiles.getFilesPathList(),self.loadfiles.getFilesNameList()):
        	     self.tree.addItem(self.filename,self.path)
		self.tree.expandTree(True)
		#self.m_treeCtrl1.AppendItem(self.root_tree,'b')
		#self.m_treeCtrl1.ExpandAll()



		bSizer2.Add( self.tree, 1, wx.ALL|wx.EXPAND, 5 )


		self.searchCtrl = wx.SearchCtrl( self.leftpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.searchCtrl.ShowSearchButton( True )
		self.searchCtrl.ShowCancelButton( False )
		bSizer2.Add( self.searchCtrl, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.leftpanel.SetSizer( bSizer2 )
		self.leftpanel.Layout()
		bSizer2.Fit( self.leftpanel )
		self.rightpanel = wx.Panel( self.windowSplitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		self.buttonpanel = pdfButtonPanel(self.rightpanel, wx.NewId(),
                                wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer3.Add(self.buttonpanel, 0, wx.EXPAND, 5)

		self.pdf_Viewer = PdfViewer( self.rightpanel)
		#bSizer11.Add(self.viewer, 1, wx.GROW|wx.LEFT|wx.RIGHT|wx.BOTTOM, 5)
		
		bSizer3.Add(self.pdf_Viewer, 1, wx.EXPAND, 5)
		#self.viewer.UsePrintDirect = ``False``
		#self.pdf_Viewer.openPdf(self.loadfiles.getFilesPathList[0])

		self.buttonpanel.viewer = self.pdf_Viewer
		self.pdf_Viewer.buttonpanel = self.buttonpanel
		
		
		self.rightpanel.SetSizer( bSizer3 )
		self.rightpanel.Layout()
		bSizer3.Fit( self.rightpanel )
		self.windowSplitter.SplitVertically( self.leftpanel, self.rightpanel,0)
		bSizer1.Add( self.windowSplitter, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		self.tree.Bind( wx.EVT_TREE_SEL_CHANGED, self.m_treeCtrl1ItemSelection )
		self.searchCtrl.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.searchButtonPressed )
	
	

	def __del__( self ):
		pass

	def m_treeCtrl1ItemSelection( self, event ):
		event.Skip()
		self.item =  event.GetItem()
		if self.tree.GetItemData(self.item):
			self.pdfFilePath=self.tree.GetItemData(self.item).GetData()
			print self.pdfFilePath
			self.pdf_Viewer.openPdf(self.pdfFilePath)

	def searchButtonPressed( self, event ):
		if self.searchCtrl.GetValue()!='':
			#for self.path, self.filename in zip(self.loadfiles.getFilesPathList(),self.loadfiles.getFilesNameList()):
        	             #self.pdfFileObj = open(self.path, 'rb')
        	     self.rootitem = self.tree.getRoot()
        	     (self.child,self.cookie) = self.tree.GetFirstChild(self.rootitem)
        	     while self.child.IsOk():
        	     	self.pdffilename = self.tree.GetItemText(self.child)
        	     	self.pdffilepath = self.tree.GetItemData(self.child).GetData()
        	     	self.pdfFileObj = open(self.pdffilepath, 'rb')
        	     	self.pdfReader = PyPDF2.PdfFileReader(self.pdfFileObj)
        	     	for self.pageNum in range(0, self.pdfReader.numPages):
        	     		self.pageObj = self.pdfReader.getPage(self.pageNum)
        	     		self.Data=self.pageObj.extractText().lower()
        	     		print self.Data
			        if self.Data.find(self.searchCtrl.GetValue(),0,len(self.Data))!= -1:
                                        self.tree.SetItemBackgroundColour(self.child,wx.Colour(255,0,0))
                                        print self.pdffilename
                                elif self.Data.find(self.searchCtrl.GetValue(),0,len(self.Data))== -1:
                    	                self.tree.SetItemBackgroundColour(self.child,wx.Colour(255,0,255))

                        self.pdfFileObj.close() 

        	     	(self.child,self.cookie) = self.tree.GetNextChild(self.rootitem,self.cookie)

			     
		event.Skip()

	
	def windowSplitterOnIdle( self, event ):
		self.windowSplitter.SetSashPosition( 0 )
		self.windowSplitter.Unbind( wx.EVT_IDLE )
	


app=wx.App()
frame=Frame(None)
frame.Show()
app.MainLoop()

