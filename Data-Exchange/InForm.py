# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph,Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from PyPDF2 import PdfFileReader,PdfFileWriter
from PyPDF2.generic import NameObject, createStringObject
from encryptfs import EncryptFS
from encryptfs.encrypt_files import decrypt_file, encrypt_file, gen_key
import os
import datetime
import json



###########################################################################
## Class Frame
###########################################################################



class PdfBuilder():

	def __init__ (self,inpath,outpath,lastname):
		print lastname
		self.flash_directory=inpath
		self.temp_directory=outpath
		print self.flash_directory
		self.filename=lastname+"_"+datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
		self.cwd=os.getcwd()
		#self.directory=self.cwd+"\pdffiles"
		if os.path.exists(self.flash_directory):
			self.path=str(self.flash_directory+"\\"+self.filename+'.pdf')
			self.doc = SimpleDocTemplate(self.path,pagesize = letter)
			self.story=[]
			self.styles = getSampleStyleSheet()
			self.styleN = self.styles['Normal']
			self.styles.leading = 40
			self.spacer=Spacer(0,0.2*inch)
			

	def getDataList(self,data_list):
		for data in data_list:
			self.data_table = [[Paragraph(cell, self.styleN) for cell in row] for row in data]
			self.t=Table(self.data_table)
			self.story.append(self.t)
			self.story.append(self.spacer)
		self.doc.build(self.story)
		print data_list

	def addMetadata(self,description):
		#self.inputfile=file(str(self.filename+'.pdf'),'rb')
		self.inputfile=file(str(self.path),'rb')
		self.pdfFile=PdfFileReader(self.inputfile)
		self.writer=PdfFileWriter()
		for page in range(self.pdfFile.getNumPages()):
			self.writer.addPage(self.pdfFile.getPage(page))
		self.infoDict=self.writer._info.getObject()
		self.infoDict.update({NameObject('/Description'):createStringObject(description)})
		#self.outputfile=open(str(self.filename+'out.pdf'),'wb')
		self.outputfile=open(str(self.path[:-4]+'out.pdf'),'wb')
		self.writer.write(self.outputfile)
		self.inputfile.close()
		self.outputfile.close()
		#os.unlink(str(self.filename+'.pdf'))
		#os.rename(str(self.filename+'out.pdf'), str(self.filename+'.pdf'))
		os.unlink(str(self.path))
		os.rename(str(self.path[:-4]+'out.pdf'),str(self.path))

	def check_file_exists(self):
		if os.path.exists(str(self.path)):
			return True
		else:
		    return False
		
        def encrypt_decrypt_file_to_temp(self):
               os.chdir(self.flash_directory)
               self.encfs = EncryptFS('cool')
               self.encfs.encrypt_all()
               #os.chdir(self.flash_directory)
              # self.encfs = EncryptFS('cool')
               self.key=self.encfs.key
               self.currentdir=self.encfs.current_dir
               self.index=self.encfs.current_index
               for file in self.index["files"]:
                       decrypt_file(self.key, os.path.join(self.currentdir, file["filename_enc"]), out_filename=os.path.join(self.temp_directory, file["filename"]))
                







class pdfCreateFrame ( wx.Frame ):

	def __init__( self, parent, MainFormFrame,inpath,outpath):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Report of Physical or Mental Examination", pos = wx.DefaultPosition, size = wx.Size( 919,890 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.json_build_data={}
		self.MainForm=MainFormFrame
		self.flash_directory=inpath
		self.temp_directory=outpath
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		self.m_scrolledWindow1.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizerScrolled = wx.BoxSizer( wx.VERTICAL )

        
                bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer2_1 = wx.BoxSizer( wx.VERTICAL )
		
		self.fistName = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fistName.Wrap( -1 )
		self.fistName.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer2_1.Add( self.fistName, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 10 )
		
		self.street = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Street", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.street.Wrap( -1 )
		self.street.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer2_1.Add( self.street, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 10 )
		
		self.caseid = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Case Id", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.caseid.Wrap( -1 )
		self.caseid.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer2_1.Add( self.caseid, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 10 )
		
		
		bSizer2.Add( bSizer2_1, 0, wx.EXPAND, 5 )
		
		bSizer2_2 = wx.BoxSizer( wx.VERTICAL )
		
		self.firstNameTextCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2_2.Add( self.firstNameTextCtrl, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 10 )
		
		self.streetTextCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer2_2.Add( self.streetTextCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 10 )
		
		self.caseIdtxtCrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2_2.Add( self.caseIdtxtCrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 10 )
		
		
		bSizer2.Add( bSizer2_2, 1, wx.EXPAND, 5 )
		
		bSizer2_3 = wx.BoxSizer( wx.VERTICAL )
		
		self.lastname = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lastname.Wrap( -1 )
		self.lastname.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer2_3.Add( self.lastname, 1, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 10 )
		
		self.city = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"City", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.city.Wrap( -1 )
		self.city.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer2_3.Add( self.city, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 10 )
		
		self.category = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Category", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.category.Wrap( -1 )
		self.category.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer2_3.Add( self.category, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 10 )
		
		
		bSizer2.Add( bSizer2_3, 0, wx.EXPAND, 5 )
		
		bSizer2_4 = wx.BoxSizer( wx.VERTICAL )
		
		self.lastNameTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2_4.Add( self.lastNameTxtCtrl, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 10 )
		
		self.cityTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2_4.Add( self.cityTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 10 )
		
		self.categoryTextCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2_4.Add( self.categoryTextCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 10 )
		
		
		bSizer2.Add( bSizer2_4, 1, wx.EXPAND, 5 )
		
		bSizer2_5 = wx.BoxSizer( wx.VERTICAL )
		
		self.dataOfBirth = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Date of Birth", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dataOfBirth.Wrap( -1 )
		self.dataOfBirth.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer2_5.Add( self.dataOfBirth, 0, wx.ALIGN_CENTER|wx.EXPAND|wx.ALL, 10 )
		
		self.state = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"State", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.state.Wrap( -1 )
		self.state.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer2_5.Add( self.state, 1, wx.ALL|wx.EXPAND, 10 )
		
		
		bSizer2.Add( bSizer2_5, 0, wx.EXPAND, 5 )
		
		bSizer2_6 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer44 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.monthspinCtrl = wx.SpinCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 12, 1 )
		self.monthspinCtrl.SetMinSize( wx.Size( 50,-1 ) )
		
		bSizer44.Add( self.monthspinCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.datespinCtrl = wx.SpinCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 31, 1 )
		self.datespinCtrl.SetMinSize( wx.Size( 50,-1 ) )
		
		bSizer44.Add( self.datespinCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.yearspinCtrl = wx.SpinCtrl( self.m_scrolledWindow1, wx.ID_ANY, u"1990", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1950, 2030, 1989 )
		self.yearspinCtrl.SetMinSize( wx.Size( 70,-1 ) )
		
		bSizer44.Add( self.yearspinCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer2_6.Add( bSizer44, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.stateTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2_6.Add( self.stateTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 10 )
		
		
		bSizer2.Add( bSizer2_6, 1, wx.EXPAND, 5 )
		
		bSizer2_7 = wx.BoxSizer( wx.VERTICAL )
		
		self.gender = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Gender", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gender.Wrap( -1 )
		self.gender.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer2_7.Add( self.gender, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 10 )
		
		self.zip = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Zip", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.zip.Wrap( -1 )
		self.zip.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer2_7.Add( self.zip, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 10 )
		
		
		bSizer2.Add( bSizer2_7, 0, wx.EXPAND, 5 )
		
		bSizer2_8 = wx.BoxSizer( wx.VERTICAL )
		
		self.genderChoiceBoxChoices = [ u"male", u"female" ]
		self.genderChoiceBox = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.genderChoiceBoxChoices, 0 )
		self.genderChoiceBox.SetSelection( 0 )
		bSizer2_8.Add( self.genderChoiceBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.zipTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2_8.Add( self.zipTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer2_8, 1, wx.EXPAND, 5 )
		
		
		bSizerScrolled.Add( bSizer2, 0, wx.EXPAND|wx.SHAPED, 5 )
		

		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizerScrolled.Add( bSizer3, 0, 0, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer4_1 = wx.BoxSizer( wx.VERTICAL )
		
		self.enterByTxt = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Entered By", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.enterByTxt.Wrap( -1 )
		bSizer4_1.Add( self.enterByTxt, 0, wx.ALL, 10 )
		
		
		bSizer4.Add( bSizer4_1, 0, 0, 5 )
		
		bSizer4_2 = wx.BoxSizer( wx.VERTICAL )
		
		self.enteredByTextCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4_2.Add( self.enteredByTextCtrl, 0, wx.ALL, 10 )
		
		
		bSizer4.Add( bSizer4_2, 0, wx.EXPAND, 5 )
		
		bSizer4_3 = wx.BoxSizer( wx.VERTICAL )
		
		self.clinicAddressTxt = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Clinic Address", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.clinicAddressTxt.Wrap( -1 )
		bSizer4_3.Add( self.clinicAddressTxt, 0, wx.ALL, 10 )
		
		
		bSizer4.Add( bSizer4_3, 0, wx.EXPAND, 5 )
		
		bSizer4_4 = wx.BoxSizer( wx.VERTICAL )
		
		self.clinicAddressTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4_4.Add( self.clinicAddressTxtCtrl, 0, wx.ALL, 10 )
		
		
		bSizer4.Add( bSizer4_4, 0, wx.EXPAND, 5 )
		
		bSizer4_5 = wx.BoxSizer( wx.VERTICAL )
		
		self.physicianNameTxt = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Physician Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.physicianNameTxt.Wrap( -1 )
		bSizer4_5.Add( self.physicianNameTxt, 0, wx.ALL, 10 )
		
		
		bSizer4.Add( bSizer4_5, 0, wx.EXPAND, 5 )
		
		bSizer4_6 = wx.BoxSizer( wx.VERTICAL )
		
		self.physicianNameTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4_6.Add( self.physicianNameTxtCtrl, 0, wx.ALL, 10 )
		
		
		bSizer4.Add( bSizer4_6, 0, wx.EXPAND, 5 )
		
		
		bSizerScrolled.Add( bSizer4, 0, wx.EXPAND, 5 )

		
		
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.tobecompletedbyphysician = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"TO BE COMPLETED BY EXAMINING PHYSICIAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tobecompletedbyphysician.Wrap( -1 )
		self.tobecompletedbyphysician.SetFont( wx.Font( 11, 74, 90, 92, False, "Arial" ) )
		
		bSizer6.Add( self.tobecompletedbyphysician, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		
		bSizerScrolled.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer7.SetMinSize( wx.Size( -1,90 ) ) 
		self.medicalhistory = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Medical History", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.medicalhistory.Wrap( -1 )
		self.medicalhistory.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer7.Add( self.medicalhistory, 0, wx.ALL|wx.EXPAND, 15 )
		
		self.medicalHistoryTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer7.Add( self.medicalHistoryTxtCtrl, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		bSizerScrolled.Add( bSizer7, 0, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.height = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Height", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.height.Wrap( -1 )
		self.height.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer8.Add( self.height, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.heightTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.heightTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.weight = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Weight", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.weight.Wrap( -1 )
		self.weight.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer8.Add( self.weight, 0, wx.ALL, 15 )
		
		self.weightTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.weightTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.bloodpressure = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Blood Pressure", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bloodpressure.Wrap( -1 )
		self.bloodpressure.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer8.Add( self.bloodpressure, 0, wx.ALL, 15 )
		
		self.bloodPressureTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.bloodPressureTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.pulse  = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Pulse", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pulse .Wrap( -1 )
		self.pulse .SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer8.Add( self.pulse , 0, wx.ALL, 15 )
		
		self.pulseTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.pulseTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.generalappearance = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"General Appearance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.generalappearance.Wrap( -1 )
		self.generalappearance.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer8.Add( self.generalappearance, 0, wx.ALL, 15 )
		
		self.generalAppearanceTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.generalAppearanceTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.headscalp = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Head, Scalp", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.headscalp.Wrap( -1 )
		self.headscalp.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer8.Add( self.headscalp, 0, wx.ALL, 15 )
		
		self.headScalpTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.headScalpTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizerScrolled.Add( bSizer8, 0, 0, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ears = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Ears", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ears.Wrap( -1 )
		self.ears.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( self.ears, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.earsTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.earsTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.hearingleft = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Hearing Left", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hearingleft.Wrap( -1 )
		self.hearingleft.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( self.hearingleft, 0, wx.ALL, 15 )
		
		self.hearingLeftTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.hearingLeftTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.hearingright = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Hearing Right", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hearingright.Wrap( -1 )
		self.hearingright.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( self.hearingright, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.hearingRightTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.hearingRightTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.nose = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Nose", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nose.Wrap( -1 )
		self.nose.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( self.nose, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.noseTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.noseTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.throat = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Throat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.throat.Wrap( -1 )
		self.throat.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( self.throat, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.throatTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.throatTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.mouth = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Mouth", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mouth.Wrap( -1 )
		self.mouth.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( self.mouth, 0, wx.ALL, 15 )
		
		self.mouthTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.mouthTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizerScrolled.Add( bSizer9, 0, 0, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer10_1 = wx.BoxSizer( wx.VERTICAL )
		
		self.visualacuity = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Visual Acuity ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.visualacuity.Wrap( -1 )
		self.visualacuity.SetFont( wx.Font( 10, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_1.Add( self.visualacuity, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 35 )
		
		self.righteye1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"RIGHT EYE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.righteye1.Wrap( -1 )
		self.righteye1.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_1.Add( self.righteye1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )
		
		self.lefteye1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"LEFT EYE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lefteye1.Wrap( -1 )
		self.lefteye1.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_1.Add( self.lefteye1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10 )
		
		
		bSizer10.Add( bSizer10_1, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer10_2 = wx.BoxSizer( wx.VERTICAL )
		
		self.withoutglasses = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"WITHOUT GLASSES", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.withoutglasses.Wrap( -1 )
		self.withoutglasses.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_2.Add( self.withoutglasses, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 15 )
		
		bSizer10_2_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer10_2_1_1 = wx.BoxSizer( wx.VERTICAL )
		
		self.distancewithoutglases = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Distance (20 ft.) ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.distancewithoutglases.Wrap( -1 )
		self.distancewithoutglases.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_2_1_1.Add( self.distancewithoutglases, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 15 )
		
		self.rightEyeDistanceWithOutGlassesTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10_2_1_1.Add( self.rightEyeDistanceWithOutGlassesTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.leftEyeDistanceWithOutGlassesTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10_2_1_1.Add( self.leftEyeDistanceWithOutGlassesTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer10_2_1.Add( bSizer10_2_1_1, 1, wx.EXPAND, 5 )
		
		bSizer10_2_1_2 = wx.BoxSizer( wx.VERTICAL )
		
		self.nearwithoutglases = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Near (14 in.)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nearwithoutglases.Wrap( -1 )
		self.nearwithoutglases.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_2_1_2.Add( self.nearwithoutglases, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 15 )
		
		self.rightEyeNearWithOutGlassesTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10_2_1_2.Add( self.rightEyeNearWithOutGlassesTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.leftEyeNearWithOutGlassesTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10_2_1_2.Add( self.leftEyeNearWithOutGlassesTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer10_2_1.Add( bSizer10_2_1_2, 1, wx.EXPAND, 5 )
		
		
		bSizer10_2.Add( bSizer10_2_1, 1, wx.EXPAND, 5 )
		
		
		bSizer10.Add( bSizer10_2, 1, wx.EXPAND, 5 )
		
		bSizer10_3 = wx.BoxSizer( wx.VERTICAL )
		
		self.withglasess = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"WITH GLASSES", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.withglasess.Wrap( -1 )
		self.withglasess.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_3.Add( self.withglasess, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 15 )
		
		bSizer10_3_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer10_3_1_1 = wx.BoxSizer( wx.VERTICAL )
		
		self.distancewithglases = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Distance (20 ft.) ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.distancewithglases.Wrap( -1 )
		self.distancewithglases.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_3_1_1.Add( self.distancewithglases, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 15 )
		
		self.rightEyeDistanceWithGlassesTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10_3_1_1.Add( self.rightEyeDistanceWithGlassesTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.leftEyeDistanceWithGlassesTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10_3_1_1.Add( self.leftEyeDistanceWithGlassesTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer10_3_1.Add( bSizer10_3_1_1, 1, wx.EXPAND, 5 )
		
		bSizer10_3_1_2 = wx.BoxSizer( wx.VERTICAL )
		
		self.neardwithglases = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Near (14 in.)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.neardwithglases.Wrap( -1 )
		self.neardwithglases.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_3_1_2.Add( self.neardwithglases, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 15 )
		
		self.rightEyeNearWithGlassesTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10_3_1_2.Add( self.rightEyeNearWithGlassesTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.leftEyeNearWithGlassesTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10_3_1_2.Add( self.leftEyeNearWithGlassesTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer10_3_1.Add( bSizer10_3_1_2, 1, wx.EXPAND, 5 )
		
		
		bSizer10_3.Add( bSizer10_3_1, 1, wx.EXPAND, 5 )
		
		
		bSizer10.Add( bSizer10_3, 1, wx.EXPAND, 5 )
		
		
		bSizerScrolled.Add( bSizer10, 0, 0, 5 )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer11_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.fieldofvision = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Field of Vision", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fieldofvision.Wrap( -1 )
		self.fieldofvision.SetFont( wx.Font( 11, 74, 90, 92, False, "Arial" ) )
		
		bSizer11_1.Add( self.fieldofvision, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		
		bSizer11.Add( bSizer11_1, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer11_2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.limitationfieldofvision = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Is there any limitation in the field of vision?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.limitationfieldofvision.Wrap( -1 )
		self.limitationfieldofvision.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer11_2.Add( self.limitationfieldofvision, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.righteye = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Right Eye:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.righteye.Wrap( -1 )
		self.righteye.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer11_2.Add( self.righteye, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.righteyeCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Yes/No", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.righteyeCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer11_2.Add( self.righteyeCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.lefteye = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Left Eye:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lefteye.Wrap( -1 )
		self.lefteye.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer11_2.Add( self.lefteye, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.lefteyeCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Yes/No", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lefteyeCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer11_2.Add( self.lefteyeCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer11.Add( bSizer11_2, 1, wx.EXPAND, 5 )
		
		
		bSizerScrolled.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer12_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer12_1.SetMinSize( wx.Size( -1,90 ) ) 
		self.neck = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Neck", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.neck.Wrap( -1 )
		self.neck.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer12_1.Add( self.neck, 0, wx.ALL|wx.EXPAND, 15 )
		
		self.neckTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer12_1.Add( self.neckTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer12.Add( bSizer12_1, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer12_2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer12_2.SetMinSize( wx.Size( -1,90 ) ) 
		self.chest = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Chest", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chest.Wrap( -1 )
		self.chest.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer12_2.Add( self.chest, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 15 )
		
		self.chestTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer12_2.Add( self.chestTxtCtrl, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		bSizer12.Add( bSizer12_2, 0, wx.EXPAND, 5 )
		
		
		bSizerScrolled.Add( bSizer12, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer13_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer13_1.SetMinSize( wx.Size( -1,90 ) ) 
		self.cardiovascularsystem = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Cardiovascular System", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cardiovascularsystem.Wrap( -1 )
		self.cardiovascularsystem.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_1.Add( self.cardiovascularsystem, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 15 )
		
		self.cardiovascularSystemTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer13_1.Add( self.cardiovascularSystemTxtCtrl, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer13.Add( bSizer13_1, 0, wx.EXPAND, 5 )
		
		bSizer13_2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer13_2_1 = wx.BoxSizer( wx.VERTICAL )
		
		self.cardiacstatus = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Cardiac Status", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cardiacstatus.Wrap( -1 )
		self.cardiacstatus.SetFont( wx.Font( 11, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_1.Add( self.cardiacstatus, 0, wx.ALL, 15 )
		
		bSizer13_2_1_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.uncompromisedCardiacStatusCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Uncompromised", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.uncompromisedCardiacStatusCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_1_1.Add( self.uncompromisedCardiacStatusCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.slightlyCompromisedCardiacStatusCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Slightly Compromised", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.slightlyCompromisedCardiacStatusCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_1_1.Add( self.slightlyCompromisedCardiacStatusCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.moderatelyCompromisedCardiacStatusCardiacStatusCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Moderately Compromised", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.moderatelyCompromisedCardiacStatusCardiacStatusCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_1_1.Add( self.moderatelyCompromisedCardiacStatusCardiacStatusCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.severelyCompromisedCardiacStatusCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Severely Compromised", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.severelyCompromisedCardiacStatusCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_1_1.Add( self.severelyCompromisedCardiacStatusCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		
		bSizer13_2_1.Add( bSizer13_2_1_1, 1, wx.EXPAND, 5 )
		
		
		bSizer13_2.Add( bSizer13_2_1, 1, wx.EXPAND, 5 )
		
		bSizer13_2_2 = wx.BoxSizer( wx.VERTICAL )
		
		self.prognosis1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Prognosis", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.prognosis1.Wrap( -1 )
		self.prognosis1.SetFont( wx.Font( 11, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_2.Add( self.prognosis1, 0, wx.ALL, 15 )
		
		bSizer13_2_2_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.goodPrognsisCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Good", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.goodPrognsisCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_2_1.Add( self.goodPrognsisCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.goodWithTherapyPrognsisCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Good With Therapy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.goodWithTherapyPrognsisCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_2_1.Add( self.goodWithTherapyPrognsisCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.fairWithTherapyPrognsisCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Fair With Therapy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fairWithTherapyPrognsisCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_2_1.Add( self.fairWithTherapyPrognsisCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.guardedDespiteTherapyCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Guarded Despite Therapy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.guardedDespiteTherapyCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_2_1.Add( self.guardedDespiteTherapyCheckBox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		
		bSizer13_2_2.Add( bSizer13_2_2_1, 1, wx.EXPAND, 5 )
		
		
		bSizer13_2.Add( bSizer13_2_2, 1, wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer13_2, 1, wx.EXPAND, 5 )
		
		
		bSizerScrolled.Add( bSizer13, 0, wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14_1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14_1_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14_1_1.SetMinSize( wx.Size( -1,90 ) ) 
		self.vascularsystem = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Vascular System", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vascularsystem.Wrap( -1 )
		self.vascularsystem.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14_1_1.Add( self.vascularsystem, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		bSizer14_1.Add( bSizer14_1_1, 1, wx.EXPAND, 5 )
		
		bSizer14_1_2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14_1_2.SetMinSize( wx.Size( -1,90 ) ) 
		self.gastrointestinal = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Gastro Intestinal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gastrointestinal.Wrap( -1 )
		self.gastrointestinal.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14_1_2.Add( self.gastrointestinal, 0, wx.TOP|wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		bSizer14_1.Add( bSizer14_1_2, 1, wx.EXPAND, 5 )
		
		bSizer14_1_3 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14_1_3.SetMinSize( wx.Size( -1,90 ) ) 
		self.genitourinary = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Genitourinary", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.genitourinary.Wrap( -1 )
		self.genitourinary.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14_1_3.Add( self.genitourinary, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		bSizer14_1.Add( bSizer14_1_3, 1, wx.EXPAND, 5 )
		
		bSizer14_1_4 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14_1_4.SetMinSize( wx.Size( -1,90 ) ) 
		self.hernia = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Hernia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hernia.Wrap( -1 )
		self.hernia.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14_1_4.Add( self.hernia, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 15 )
		
		
		bSizer14_1.Add( bSizer14_1_4, 1, wx.EXPAND, 5 )
		
		bSizer14_1_5 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14_1_5.SetMinSize( wx.Size( -1,90 ) ) 
		self.musculoskeletal = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Musculoskeletal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.musculoskeletal.Wrap( -1 )
		self.musculoskeletal.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14_1_5.Add( self.musculoskeletal, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 15 )
		
		
		bSizer14_1.Add( bSizer14_1_5, 1, wx.EXPAND, 5 )
		
		bSizer14_1_6 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14_1_6.SetMinSize( wx.Size( -1,90 ) ) 
		self.neurological = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Neurological", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.neurological.Wrap( -1 )
		self.neurological.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14_1_6.Add( self.neurological, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 15 )
		
		
		bSizer14_1.Add( bSizer14_1_6, 1, wx.EXPAND, 5 )
		
		bSizer14_1_7 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14_1_7.SetMinSize( wx.Size( -1,90 ) ) 
		self.skin = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Skin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.skin.Wrap( -1 )
		self.skin.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14_1_7.Add( self.skin, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 15 )
		
		
		bSizer14_1.Add( bSizer14_1_7, 1, wx.EXPAND, 5 )
		
		bSizer14_1_8 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14_1_8.SetMinSize( wx.Size( -1,90 ) ) 
		self.estimateofmentalcondition = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Estimate of Mental Condition", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.estimateofmentalcondition.Wrap( -1 )
		self.estimateofmentalcondition.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14_1_8.Add( self.estimateofmentalcondition, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 15 )
		
		
		bSizer14_1.Add( bSizer14_1_8, 1, wx.EXPAND, 5 )
		
		bSizer14_1_9 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14_1_9.SetMinSize( wx.Size( -1,90 ) ) 
		self.diagnosis = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"DIAGNOSIS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.diagnosis.Wrap( -1 )
		self.diagnosis.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14_1_9.Add( self.diagnosis, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 15 )
		
		
		bSizer14_1.Add( bSizer14_1_9, 1, wx.EXPAND, 5 )
		
		bSizer14_1_10 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14_1_10.SetMinSize( wx.Size( -1,90 ) ) 
		self.prognosis = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"PROGNOSIS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.prognosis.Wrap( -1 )
		self.prognosis.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14_1_10.Add( self.prognosis, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 15 )
		
		
		bSizer14_1.Add( bSizer14_1_10, 1, wx.EXPAND, 5 )
		
		bSizer14_1_11 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14_1_11.SetMinSize( wx.Size( -1,90 ) ) 
		self.vacination = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Vacination", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vacination.Wrap( -1 )
		bSizer14_1_11.Add( self.vacination, 0, wx.ALL, 15 )
		
		
		bSizer14_1.Add( bSizer14_1_11, 1, wx.EXPAND, 5 )
		
		
		bSizer14.Add( bSizer14_1, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		bSizer14_2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14_2_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14_2_1.SetMinSize( wx.Size( -1,90 ) ) 
		self.vascularSystemTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_1.Add( self.vascularSystemTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_1, 1, wx.EXPAND, 5 )
		
		bSizer14_2_2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14_2_2.SetMinSize( wx.Size( -1,-90 ) ) 
		self.gastroIntestinalTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_2.Add( self.gastroIntestinalTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_2, 1, wx.EXPAND, 5 )
		
		bSizer14_2_3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14_2_3.SetMinSize( wx.Size( -1,90 ) ) 
		self.genitourinaryTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_3.Add( self.genitourinaryTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_3, 1, wx.EXPAND, 5 )
		
		bSizer14_2_4 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14_2_4.SetMinSize( wx.Size( -1,90 ) ) 
		self.herniaTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_4.Add( self.herniaTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_4, 1, wx.EXPAND, 5 )
		
		bSizer14_2_5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14_2_5.SetMinSize( wx.Size( -1,90 ) ) 
		self.musculoskeletalTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_5.Add( self.musculoskeletalTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_5, 1, wx.EXPAND, 5 )
		
		bSizer14_2_6 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14_2_6.SetMinSize( wx.Size( -1,90 ) ) 
		self.neurologicalTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_6.Add( self.neurologicalTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_6, 1, wx.EXPAND, 5 )
		
		bSizer14_2_7 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14_2_7.SetMinSize( wx.Size( -1,90 ) ) 
		self.skinTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_7.Add( self.skinTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_7, 1, wx.EXPAND, 5 )
		
		bSizer14_2_8 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14_2_8.SetMinSize( wx.Size( -1,90 ) ) 
		self.estimateofMentalConditionTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_8.Add( self.estimateofMentalConditionTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_8, 1, wx.EXPAND, 5 )
		
		bSizer14_2_9 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14_2_9.SetMinSize( wx.Size( -1,90 ) ) 
		self.diagnosisTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_9.Add( self.diagnosisTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_9, 1, wx.EXPAND, 5 )
		
		bSizer14_2_10 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14_2_10.SetMinSize( wx.Size( -1,90 ) ) 
		self.prognosisTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_10.Add( self.prognosisTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_10, 1, wx.EXPAND, 5 )
		
		bSizer14_2_11 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14_2_11.SetMinSize( wx.Size( -1,90 ) ) 
		self.vacinationTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14_2_11.Add( self.vacinationTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer14_2.Add( bSizer14_2_11, 1, wx.EXPAND, 5 )
		
		
		bSizer14.Add( bSizer14_2, 1, 0, 5 )
		
		
		bSizerScrolled.Add( bSizer14, 0, wx.EXPAND, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.submit = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.submit.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer15.Add( self.submit, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer15, 0, wx.EXPAND, 5 )
		
		
		self.m_scrolledWindow1.SetSizer( bSizerScrolled )
		self.m_scrolledWindow1.Layout()
		bSizerScrolled.Fit( self.m_scrolledWindow1 )
		bSizer1.Add( self.m_scrolledWindow1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.frameClosed )
		self.submit.Bind( wx.EVT_BUTTON, self.Submitted )
		self.dataList=[]


	
	def __del__( self ):
		pass

	def showMesssage(self,mesg):
		wx.MessageBox(mesg,'Info',wx.OK|wx.ICON_INFORMATION)

	def frameClosed( self, event ):
		self.MainForm.update_tree()
		event.Skip()
	
	
	
	def Submitted( self, event ):
		print self.monthspinCtrl.GetValue()
		print self.datespinCtrl.GetValue()
		print self.yearspinCtrl.GetValue()
		print self.genderChoiceBoxChoices[self.genderChoiceBox.GetSelection()]
		event.Skip()
		self.dataList.append([['<font size=12><b>First Name</b></font> ',"<font size=11>"+self.firstNameTextCtrl.GetValue()+"</font>",'<font size=12><b>Last Name</b></font> ',"<font size=11>"+self.lastNameTxtCtrl.GetValue()+"</font>",'<font size=12><b>Date of Birth</b></font> ',"<font size=11>"+str(self.monthspinCtrl.GetValue())+" / "+str(self.datespinCtrl.GetValue())+" / "+str(self.yearspinCtrl.GetValue())+"</font>",
			'<font size=12><b>Gender</b></font> ',"<font size=11>"+self.genderChoiceBoxChoices[self.genderChoiceBox.GetSelection()]+"</font>"]])
		#self.dataList.append([['']])
		self.json_build_data["First Name".lower()]=self.firstNameTextCtrl.GetValue().lower()
		self.json_build_data["Last Name".lower()]=self.lastNameTxtCtrl.GetValue().lower()
		self.json_build_data["Date of Birth".lower()]=str(self.monthspinCtrl.GetValue())+" / "+str(self.datespinCtrl.GetValue())+" / "+str(self.yearspinCtrl.GetValue()).lower()
		self.json_build_data["Gender".lower()]=self.genderChoiceBoxChoices[self.genderChoiceBox.GetSelection()].lower()
		
		self.dataList.append([['<font size=12><b>Street</b></font> ',"<font size=11>"+self.streetTextCtrl.GetValue()+"</font>",'<font size=12><b>City</b></font> ',"<font size=11>"+self.cityTxtCtrl.GetValue()+"</font>",
			'<font size=12><b>State</b></font> ',"<font size=11>"+self.stateTxtCtrl.GetValue()+"</font>",'<font size=12><b>Zipcode</b></font> ',"<font size=11>"+self.zipTxtCtrl.GetValue()+"</font>"]])
		#self.dataList.append([['']])
		self.json_build_data["Street".lower()]=self.streetTextCtrl.GetValue().lower()
		self.json_build_data["City".lower()]=self.cityTxtCtrl.GetValue().lower()
		self.json_build_data["State".lower()]=self.stateTxtCtrl.GetValue().lower()
		self.json_build_data["Zipcode".lower()]=self.zipTxtCtrl.GetValue().lower()

		
		self.dataList.append([['<font size=12><b>Case Id</b></font> ',"<font size=11>"+self.caseIdtxtCrl.GetValue()+"</font>",'<font size=12><b>Category</b></font>',"<font size=11>"+self.categoryTextCtrl.GetValue()+"</font>"]])
		self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Entered By </b></font> ',"<font size=11>"+self.enteredByTextCtrl.GetValue()+"</font>",'<font size=12><b>Clinic Address </b></font> ',"<font size=11>"+self.clinicAddressTxtCtrl.GetValue()+"</font>",
			'<font size=12><b>Physician Name </b></font> ',"<font size=11>"+self.physicianNameTxtCtrl.GetValue()+"</font>"]])
		#self.dataList.append([['']])
		self.dataList.append([['']])
		
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>TO BE COMPLETED BY EXAMINING PHYSICIAN</b></font>']])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Medical History</b></font> ',"<font size=11>"+self.medicalHistoryTxtCtrl.GetValue()+"</font>"]])
		#self.dataList.append([['']])
		self.json_build_data["Case Id".lower()]=self.caseIdtxtCrl.GetValue().lower()
		self.json_build_data["Category".lower()]=self.categoryTextCtrl.GetValue().lower()

		self.json_build_data["Entered By".lower()]=self.enteredByTextCtrl.GetValue().lower()
		self.json_build_data["Clinic Address".lower()]=self.clinicAddressTxtCtrl.GetValue().lower()
		self.json_build_data["Physician Name".lower()]=self.physicianNameTxtCtrl.GetValue().lower()
		
		

		self.json_build_data["Medical History".lower()]=self.medicalHistoryTxtCtrl.GetValue().lower()
		

		self.dataList.append([['<font size=12><b>Height</b></font> ',"<font size=11>"+self.heightTxtCtrl.GetValue()+"</font>",'<font size=12><b>Weight</b></font> ',"<font size=11>"+self.weightTxtCtrl.GetValue()+"</font>",
		'<font size=12><b>Blood Pressure</b></font> ',"<font size=11>"+self.bloodPressureTxtCtrl.GetValue()+"</font>"]])
		self.dataList.append([['<font size=12><b>Pulse</b></font> ',"<font size=11>"+self.pulseTxtCtrl.GetValue()+"</font>",
		'<font size=12><b>General Appearance</b></font> ',"<font size=11>"+self.generalAppearanceTxtCtrl.GetValue()+"</font>",'<font size=12><b>Head, Scalp</b></font> ',"<font size=11>"+self.headScalpTxtCtrl.GetValue()+"</font>"]])

		self.json_build_data["Height".lower()]=self.heightTxtCtrl.GetValue().lower()
		self.json_build_data["Weight".lower()]=self.weightTxtCtrl.GetValue().lower()
		self.json_build_data["Blood Pressure".lower()]=self.bloodPressureTxtCtrl.GetValue().lower()
		self.json_build_data["Pulse".lower()]=self.pulseTxtCtrl.GetValue().lower()
		self.json_build_data["General Appearance".lower()]=self.generalAppearanceTxtCtrl.GetValue().lower()
		self.json_build_data["Head, Scalp".lower()]=self.headScalpTxtCtrl.GetValue().lower()
		
		
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Ears</b></font> ',"<font size=11>"+self.earsTxtCtrl.GetValue()+"</font>",'<font size=12><b>Hearing Left</b></font> ',"<font size=11>"+self.hearingLeftTxtCtrl.GetValue()+"</font>",
		'<font size=12><b>Hearing Right</b></font> ',"<font size=11>"+self.hearingRightTxtCtrl.GetValue()+"</font>"]])
		self.dataList.append([['<font size=12><b>Nose</b></font> ',"<font size=11>"+self.noseTxtCtrl.GetValue()+"</font>",
		'<font size=12><b>Throat</b></font> ',"<font size=11>"+self.throatTxtCtrl.GetValue()+"</font>",'<font size=12><b>Mouth</b></font> ',"<font size=11>"+self.mouthTxtCtrl.GetValue()+"</font>"]])
		self.dataList.append([['']])

		self.json_build_data["Ears".lower()]=self.earsTxtCtrl.GetValue().lower()
		self.json_build_data["Hearing Left".lower()]=self.hearingLeftTxtCtrl.GetValue().lower()
		self.json_build_data["Hearing Right".lower()]=self.hearingRightTxtCtrl.GetValue().lower()
		self.json_build_data["Nose".lower()]=self.noseTxtCtrl.GetValue().lower()
		self.json_build_data["Throat".lower()]=self.throatTxtCtrl.GetValue().lower()
		self.json_build_data["Mouth".lower()]=self.mouthTxtCtrl.GetValue().lower()
		


		self.dataList.append([['<font size=12><b>WITHOUT GLASSES</b></font>','<font size=12><b>WITH GLASSES</b></font>']])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Visual Acuity </b></font>','<font size=12><b>Dist (20 ft.)</b></font>','<font size=12><b>Near (14 in.)</b></font>','<font size=12><b>Dist (20 ft.)</b></font>','<font size=12><b>Near (14 in.)</b></font>']])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>RIGHT EYE</b></font></font>',"<font size=11>"+self.rightEyeDistanceWithOutGlassesTxtCtrl.GetValue()+"</font>","<font size=11>"+self.rightEyeNearWithOutGlassesTxtCtrl.GetValue()+"</font>",
			"<font size=11>"+self.rightEyeDistanceWithGlassesTxtCtrl.GetValue()+"</font>","<font size=11>"+self.rightEyeNearWithGlassesTxtCtrl.GetValue()+"</font>"]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>LEFT EYE</b></font>',"<font size=11>"+self.leftEyeDistanceWithOutGlassesTxtCtrl.GetValue()+"</font>","<font size=11>"+self.leftEyeNearWithOutGlassesTxtCtrl.GetValue()+"</font>"+"</font>",
			"<font size=11>"+self.leftEyeDistanceWithGlassesTxtCtrl.GetValue()+"</font>","<font size=11>"+self.leftEyeNearWithGlassesTxtCtrl.GetValue()+"</font>"]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Field of Vision</b></font>']])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Is there any limitation in the field of vision?</b></font> ','<font size=12><b>Right Eye:</b></font> ',"<font size=11>"+str(self.righteyeCheckBox.GetValue())+"</font>",
		'<font size=12><b>Left Eye:</b></font> ',"<font size=11>"+str(self.lefteyeCheckBox.GetValue())+"</font>"]])

		#self.dataList.append([['']]) 
		self.righteye_distance={"distance":{"with out glass":self.rightEyeDistanceWithOutGlassesTxtCtrl.GetValue().lower(),"with glass":self.rightEyeDistanceWithGlassesTxtCtrl.GetValue().lower()}}
		self.righteye_near={"near":{"with out glass":self.rightEyeNearWithOutGlassesTxtCtrl.GetValue().lower(),"with glass":self.rightEyeNearWithGlassesTxtCtrl.GetValue().lower()}}
                self.righteye=[self.righteye_distance,self.righteye_near]
                self.json_build_data["right".lower()]=self.righteye

                self.lefteye_distance={"distance":{"with out glass":self.leftEyeDistanceWithOutGlassesTxtCtrl.GetValue().lower(),"with glass":self.leftEyeDistanceWithGlassesTxtCtrl.GetValue().lower()}}
		self.lefteye_near={"near":{"with out glass":self.leftEyeNearWithOutGlassesTxtCtrl.GetValue().lower(),"with glass":self.leftEyeNearWithGlassesTxtCtrl.GetValue().lower()}}
                self.lefteye=[self.lefteye_distance,self.lefteye_near]
                self.json_build_data["left".lower()]=self.lefteye
                print self.righteyeCheckBox.GetValue()
                if self.righteyeCheckBox.GetValue()==True:self.righteye_fov="yes"
                else: self.righteye_fov="no"
                if self.lefteyeCheckBox.GetValue()==True:self.lefteye_fov="yes"
                else: self.lefteye_fov="no"

                self.fieldofvision={"righteye": self.righteye_fov,"lefteye":self.lefteye_fov}
                self.json_build_data["fieldofvision".lower()]=self.fieldofvision




		self.dataList.append([['<font size=12><b>Neck</b></font> ',"<font size=11>"+self.neckTxtCtrl.GetValue()+"</font>"]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Chest</b></font> ',"<font size=11>"+self.chestTxtCtrl.GetValue()+"</font>"]])
		#self.dataList.append([['']])
		self.json_build_data["neck".lower()]=self.neckTxtCtrl.GetValue().lower()
		self.json_build_data["Chest".lower()]=self.chestTxtCtrl.GetValue().lower()


		self.dataList.append([['<font size=12><b>Cardio Vascular System</b></font> ',"<font size=11>"+self.cardiovascularSystemTxtCtrl.GetValue()+"</font>"]])
		#self.dataList.append([['']])
   
		self.dataList.append([['<font size=12><b>Cardiac Status</b></font> ','<font size=12><b>Prognosis</b></font>']])
		#self.dataList.append([['']])
		self.Status=[]
		self.cardiac_status=""
		if self.uncompromisedCardiacStatusCheckBox.GetValue():
			self.Status.append('Uncompromised ')
			self.cardiac_status=self.cardiac_status+"Uncompromised ".lower()

		if self.slightlyCompromisedCardiacStatusCheckBox.GetValue():
			self.Status.append('Slightly Compromised')
			self.cardiac_status=self.cardiac_status+"Slightly Compromised ".lower()

		if self.moderatelyCompromisedCardiacStatusCardiacStatusCheckBox.GetValue():
			self.Status.append('Moderately Compromised ')
			self.cardiac_status=self.cardiac_status+"Moderately Compromised ".lower()

		if self.severelyCompromisedCardiacStatusCheckBox.GetValue():
			self.Status.append('Severely Compromised ')
			self.cardiac_status=self.cardiac_status+"Severely Compromised ".lower()

		else:
			self.Status.append(' ')
			self.cardiac_status=self.cardiac_status+" "

		self.json_build_data["cardiac status".lower()]=self.cardiac_status


		self.prognsis=""

		if self.goodPrognsisCheckBox.GetValue():
			self.Status.append('Good ')
			self.prognsis=self.prognsis+"Good ".lower()
		if self.goodWithTherapyPrognsisCheckBox.GetValue():
			self.Status.append('Good With Therapy ')
			self.prognsis=self.prognsis+"Good With Therapy ".lower()
		if self.fairWithTherapyPrognsisCheckBox.GetValue():
			self.Status.append('Fair With Therapy')
			self.prognsis=self.prognsis+"Fair With Therapy ".lower()
		if self.guardedDespiteTherapyCheckBox.GetValue():
			self.Status.append('Guarded Despite Therapy ')
			self.prognsis=self.prognsis+"Guarded Despite Therapy ".lower()
		else:
			self.Status.append(' ')
			self.prognsis=self.prognsis+" "

		self.json_build_data["prognsis".lower()]=self.prognsis

		
       
		self.dataList.append([self.Status])
		#self.dataList.append([['']])


		self.dataList.append([['<font size=12><b>Vascular System</b></font> ',"<font size=11>"+self.vascularSystemTxtCtrl.GetValue()+"</font>"]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Gastro Intestinal</b></font> ',"<font size=11>"+self.gastroIntestinalTxtCtrl.GetValue()+"</font>"]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Genitourinary</b></font> ',"<font size=11>"+self.genitourinaryTxtCtrl.GetValue()+"</font>"]])

		#self.dataList.append([['']])
		self.json_build_data["Vascular System".lower()]=self.vascularSystemTxtCtrl.GetValue().lower()
		self.json_build_data["Gastro Intestinal".lower()]=self.gastroIntestinalTxtCtrl.GetValue().lower()
		self.json_build_data["Genitourinary".lower()]=self.genitourinaryTxtCtrl.GetValue().lower()


		self.dataList.append([['<font size=12><b>Hernia</b></font> ',"<font size=11>"+self.herniaTxtCtrl.GetValue()+"</font>"]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Musculo Skeletal</b></font> ',"<font size=11>"+self.musculoskeletalTxtCtrl.GetValue()+"</font>"]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Neurological</b></font> ',"<font size=11>"+self.neurologicalTxtCtrl.GetValue()+"</font>"]])
		#self.dataList.append([['']])
		self.json_build_data["Hernia".lower()]=self.herniaTxtCtrl.GetValue().lower()
		self.json_build_data["Musculo Skeletal".lower()]=self.musculoskeletalTxtCtrl.GetValue().lower()
		self.json_build_data["Neurological".lower()]=self.neurologicalTxtCtrl.GetValue().lower()
		


		self.dataList.append([['<font size=12><b>Skin</b></font> ',"<font size=11>"+self.skinTxtCtrl.GetValue()+"</font>"]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Estimate of Mental Condition</b></font> ',"<font size=11>"+self.estimateofMentalConditionTxtCtrl.GetValue()+"</font>"]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Diagnosis</b></font> ',"<font size=11>"+self.diagnosisTxtCtrl.GetValue()+"</font>"]])

		#self.dataList.append([['']])
		self.json_build_data["Skin".lower()]=self.skinTxtCtrl.GetValue().lower()
		self.json_build_data["Mental Condition".lower()]=self.estimateofMentalConditionTxtCtrl.GetValue().lower()
		self.json_build_data["Diagnosis".lower()]=self.diagnosisTxtCtrl.GetValue().lower()
		

		self.dataList.append([['<font size=12><b>Prognosis</b></font> ',"<font size=11>"+self.prognosisTxtCtrl.GetValue()+"</font>"]])
		#self.dataList.append([['']])
		self.dataList.append([['<font size=12><b>Vacination</b></font> ',"<font size=11>"+self.vacinationTxtCtrl.GetValue()+"</font>"]])
		#self.dataList.append([['']])

		self.json_build_data["Prognosis".lower()]=self.prognosisTxtCtrl.GetValue().lower()
		self.json_build_data["Vacination".lower()]=self.vacinationTxtCtrl.GetValue().lower()
		self.json_data=json.dumps(self.json_build_data,indent=4)
		print self.json_data



		self.pdfBuilder=PdfBuilder(self.flash_directory, self.temp_directory,self.lastNameTxtCtrl.GetValue())
		self.pdfBuilder.getDataList(self.dataList)
		self.pdfBuilder.addMetadata(self.json_data)
		if self.pdfBuilder.check_file_exists():
			self.showMesssage("PDF Inserted")
			self.pdfBuilder.encrypt_decrypt_file_to_temp()
		else:
			self.showMesssage("PDF Not Inserted")
		print self.dataList
		event.Skip()

