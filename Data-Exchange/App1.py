# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from PdfBuilder import PdfBuilder

###########################################################################
## Class Frame
###########################################################################

class Frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Report of Physical or Mental Examination", pos = wx.DefaultPosition, size = wx.Size( 800,900 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizerScrolled = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.patientName = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Patient Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.patientName.Wrap( -1 )
		self.patientName.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer2.Add( self.patientName, 0, wx.ALL, 5 )
		
		self.patientNameTextCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.patientNameTextCtrl, 0, wx.ALL, 5 )
		
		self.dataOfBirth = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Date of Birth", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dataOfBirth.Wrap( -1 )
		self.dataOfBirth.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer2.Add( self.dataOfBirth, 0, wx.ALL, 5 )
		
		self.dataOfBirthTextCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.dataOfBirthTextCtrl, 0, wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer2, 0, 0, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.address = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Address", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.address.Wrap( -1 )
		self.address.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer3.Add( self.address, 0, wx.ALL, 5 )
		
		self.addressTextCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		bSizer3.Add( self.addressTextCtrl, 0, wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer3, 0, 0, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.caseName = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Case Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.caseName.Wrap( -1 )
		self.caseName.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer4.Add( self.caseName, 0, wx.ALL, 5 )
		
		self.caseNametxtCrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.caseNametxtCrl, 0, wx.ALL, 5 )
		
		self.caseNumber = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Case No", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.caseNumber.Wrap( -1 )
		self.caseNumber.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer4.Add( self.caseNumber, 0, wx.ALL, 5 )
		
		self.caseNumberTxtctrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.caseNumberTxtctrl, 0, wx.ALL, 5 )
		
		self.category = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Category", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.category.Wrap( -1 )
		self.category.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer4.Add( self.category, 0, wx.ALL, 5 )
		
		self.categoryTextCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.categoryTextCtrl, 0, wx.ALL, 5 )
		
		self.appNo = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"App. No.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.appNo.Wrap( -1 )
		self.appNo.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer4.Add( self.appNo, 0, wx.ALL, 5 )
		
		self.appNoTxtctrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.appNoTxtctrl, 0, wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer4, 0, 0, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.eligibilitySpecialist  = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Eligibility Specialist ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.eligibilitySpecialist .Wrap( -1 )
		self.eligibilitySpecialist .SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer5.Add( self.eligibilitySpecialist , 0, wx.ALL, 5 )
		
		self.eligibiltySpecialistTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.eligibiltySpecialistTxtCtrl, 0, wx.ALL, 5 )
		
		self.bJN = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"BJN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bJN.Wrap( -1 )
		self.bJN.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer5.Add( self.bJN, 0, wx.ALL, 5 )
		
		self.bJNtxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.bJNtxtCtrl, 0, wx.ALL, 5 )
		
		self.mailCode = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Mail Code", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mailCode.Wrap( -1 )
		self.mailCode.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer5.Add( self.mailCode, 0, wx.ALL, 5 )
		
		self.mailCodeTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.mailCodeTxtCtrl, 0, wx.ALL, 5 )
		
		self.medicalAuthDate = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Medical Authorization Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.medicalAuthDate.Wrap( -1 )
		self.medicalAuthDate.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer5.Add( self.medicalAuthDate, 0, wx.ALL, 5 )
		
		self.medicalAuthDateTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.medicalAuthDateTxtCtrl, 0, wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer5, 1, wx.BOTTOM, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.tobecompletedbyphysician = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"TO BE COMPLETED BY EXAMINING PHYSICIAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tobecompletedbyphysician.Wrap( -1 )
		self.tobecompletedbyphysician.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer6.Add( self.tobecompletedbyphysician, 0, wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer6, 0, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.medicalhistory = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Medical History", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.medicalhistory.Wrap( -1 )
		self.medicalhistory.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer7.Add( self.medicalhistory, 0, wx.ALL, 5 )
		
		self.medicalHistoryTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer7.Add( self.medicalHistoryTxtCtrl, 1, wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.height = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Height", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.height.Wrap( -1 )
		self.height.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer8.Add( self.height, 0, wx.ALL, 5 )
		
		self.heightTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.heightTxtCtrl, 0, wx.ALL, 5 )
		
		self.weight = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Weight", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.weight.Wrap( -1 )
		self.weight.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer8.Add( self.weight, 0, wx.ALL, 5 )
		
		self.weightTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.weightTxtCtrl, 0, wx.ALL, 5 )
		
		self.bloodpressure = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Blood Pressure", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bloodpressure.Wrap( -1 )
		self.bloodpressure.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer8.Add( self.bloodpressure, 0, wx.ALL, 5 )
		
		self.bloodPressureTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.bloodPressureTxtCtrl, 0, wx.ALL, 5 )
		
		self.pulse  = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Pulse", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pulse .Wrap( -1 )
		self.pulse .SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer8.Add( self.pulse , 0, wx.ALL, 5 )
		
		self.pulseTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.pulseTxtCtrl, 0, wx.ALL, 5 )
		
		self.generalappearance = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"General Appearance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.generalappearance.Wrap( -1 )
		self.generalappearance.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer8.Add( self.generalappearance, 0, wx.ALL, 5 )
		
		self.generalAppearanceTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.generalAppearanceTxtCtrl, 0, wx.ALL, 5 )
		
		self.headscalp = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Head, Scalp", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.headscalp.Wrap( -1 )
		self.headscalp.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer8.Add( self.headscalp, 0, wx.ALL, 5 )
		
		self.headScalpTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.headScalpTxtCtrl, 0, wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer8, 0, 0, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ears = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Ears", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ears.Wrap( -1 )
		self.ears.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( self.ears, 0, wx.ALL, 5 )
		
		self.earsTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.earsTxtCtrl, 0, wx.ALL, 5 )
		
		self.hearingleft = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Hearing Left", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hearingleft.Wrap( -1 )
		self.hearingleft.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( self.hearingleft, 0, wx.ALL, 5 )
		
		self.hearingLeftTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.hearingLeftTxtCtrl, 0, wx.ALL, 5 )
		
		self.hearingright = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Hearing Right", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hearingright.Wrap( -1 )
		self.hearingright.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( self.hearingright, 0, wx.ALL, 5 )
		
		self.hearingRightTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.hearingRightTxtCtrl, 0, wx.ALL, 5 )
		
		self.nose = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Nose", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nose.Wrap( -1 )
		self.nose.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( self.nose, 0, wx.ALL, 5 )
		
		self.noseTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.noseTxtCtrl, 0, wx.ALL, 5 )
		
		self.throat = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Throat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.throat.Wrap( -1 )
		self.throat.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( self.throat, 0, wx.ALL, 5 )
		
		self.throatTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.throatTxtCtrl, 0, wx.ALL, 5 )
		
		self.mouth = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Mouth", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mouth.Wrap( -1 )
		self.mouth.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( self.mouth, 0, wx.ALL, 5 )
		
		self.mouthTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.mouthTxtCtrl, 0, wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer9, 1, 0, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer10_1 = wx.BoxSizer( wx.VERTICAL )
		
		self.visualacuity = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Visual Acuity ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.visualacuity.Wrap( -1 )
		self.visualacuity.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_1.Add( self.visualacuity, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 25 )
		
		self.righteye1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"RIGHT EYE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.righteye1.Wrap( -1 )
		self.righteye1.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_1.Add( self.righteye1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.lefteye1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"LEFT EYE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lefteye1.Wrap( -1 )
		self.lefteye1.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_1.Add( self.lefteye1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer10.Add( bSizer10_1, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer10_2 = wx.BoxSizer( wx.VERTICAL )
		
		self.withoutglasses = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"WITHOUT GLASSES", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.withoutglasses.Wrap( -1 )
		self.withoutglasses.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_2.Add( self.withoutglasses, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer10_2_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer10_2_1_1 = wx.BoxSizer( wx.VERTICAL )
		
		self.distancewithoutglases = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Distance (20 ft.) ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.distancewithoutglases.Wrap( -1 )
		self.distancewithoutglases.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_2_1_1.Add( self.distancewithoutglases, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.rightEyeDistanceWithOutGlassesTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10_2_1_1.Add( self.rightEyeDistanceWithOutGlassesTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.leftEyeDistanceWithOutGlassesTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10_2_1_1.Add( self.leftEyeDistanceWithOutGlassesTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer10_2_1.Add( bSizer10_2_1_1, 1, wx.EXPAND, 5 )
		
		bSizer10_2_1_2 = wx.BoxSizer( wx.VERTICAL )
		
		self.nearwithoutglases = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Near (14 in.)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nearwithoutglases.Wrap( -1 )
		self.nearwithoutglases.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_2_1_2.Add( self.nearwithoutglases, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
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
		
		bSizer10_3.Add( self.withglasess, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		bSizer10_3_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer10_3_1_1 = wx.BoxSizer( wx.VERTICAL )
		
		self.distancewithglases = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Distance (20 ft.) ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.distancewithglases.Wrap( -1 )
		self.distancewithglases.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_3_1_1.Add( self.distancewithglases, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.rightEyeDistanceWithGlassesTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10_3_1_1.Add( self.rightEyeDistanceWithGlassesTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.leftEyeDistanceWithGlassesTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10_3_1_1.Add( self.leftEyeDistanceWithGlassesTxtCtrl, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer10_3_1.Add( bSizer10_3_1_1, 1, wx.EXPAND, 5 )
		
		bSizer10_3_1_2 = wx.BoxSizer( wx.VERTICAL )
		
		self.neardwithglases = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Near (14 in.)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.neardwithglases.Wrap( -1 )
		self.neardwithglases.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer10_3_1_2.Add( self.neardwithglases, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
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
		self.fieldofvision.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer11_1.Add( self.fieldofvision, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer11.Add( bSizer11_1, 1, wx.EXPAND, 5 )
		
		bSizer11_2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.limitationfieldofvision = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Is there any limitation in the field of vision?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.limitationfieldofvision.Wrap( -1 )
		self.limitationfieldofvision.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer11_2.Add( self.limitationfieldofvision, 0, wx.ALL, 5 )
		
		self.righteye = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Right Eye:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.righteye.Wrap( -1 )
		self.righteye.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer11_2.Add( self.righteye, 0, wx.ALL, 5 )
		
		self.righteyeCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Yes/No", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.righteyeCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer11_2.Add( self.righteyeCheckBox, 0, wx.ALL, 5 )
		
		self.lefteye = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Left Eye:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lefteye.Wrap( -1 )
		self.lefteye.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer11_2.Add( self.lefteye, 0, wx.ALL, 5 )
		
		self.lefteyeCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Yes/No", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lefteyeCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer11_2.Add( self.lefteyeCheckBox, 0, wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer11_2, 1, wx.EXPAND, 5 )
		
		
		bSizerScrolled.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer12_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.neck = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Neck", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.neck.Wrap( -1 )
		self.neck.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer12_1.Add( self.neck, 0, wx.ALL, 5 )
		
		self.neckTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12_1.Add( self.neckTxtCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer12.Add( bSizer12_1, 0, wx.EXPAND, 5 )
		
		bSizer12_2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.chest = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Chest", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.chest.Wrap( -1 )
		self.chest.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer12_2.Add( self.chest, 0, wx.ALL, 5 )
		
		self.chestTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12_2.Add( self.chestTxtCtrl, 1, wx.ALL, 5 )
		
		
		bSizer12.Add( bSizer12_2, 0, wx.EXPAND, 5 )
		
		
		bSizerScrolled.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer13_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cardiovascularsystem = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Cardiovascular System", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cardiovascularsystem.Wrap( -1 )
		self.cardiovascularsystem.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_1.Add( self.cardiovascularsystem, 0, wx.ALL, 5 )
		
		self.cardiovascularSystemTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13_1.Add( self.cardiovascularSystemTxtCtrl, 1, wx.ALL, 5 )
		
		
		bSizer13.Add( bSizer13_1, 0, wx.EXPAND, 5 )
		
		bSizer13_2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer13_2_1 = wx.BoxSizer( wx.VERTICAL )
		
		self.cardiacstatus = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Cardiac Status", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cardiacstatus.Wrap( -1 )
		self.cardiacstatus.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_1.Add( self.cardiacstatus, 0, wx.ALL, 5 )
		
		bSizer13_2_1_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.uncompromisedCardiacStatusCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Uncompromised", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.uncompromisedCardiacStatusCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_1_1.Add( self.uncompromisedCardiacStatusCheckBox, 0, wx.ALL, 5 )
		
		self.slightlyCompromisedCardiacStatusCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Slightly Compromised", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.slightlyCompromisedCardiacStatusCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_1_1.Add( self.slightlyCompromisedCardiacStatusCheckBox, 0, wx.ALL, 5 )
		
		self.moderatelyCompromisedCardiacStatusCardiacStatusCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Moderately Compromised", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.moderatelyCompromisedCardiacStatusCardiacStatusCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_1_1.Add( self.moderatelyCompromisedCardiacStatusCardiacStatusCheckBox, 0, wx.ALL, 5 )
		
		self.severelyCompromisedCardiacStatusCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Severely Compromised", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.severelyCompromisedCardiacStatusCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_1_1.Add( self.severelyCompromisedCardiacStatusCheckBox, 0, wx.ALL, 5 )
		
		
		bSizer13_2_1.Add( bSizer13_2_1_1, 1, wx.EXPAND, 5 )
		
		
		bSizer13_2.Add( bSizer13_2_1, 1, wx.EXPAND, 5 )
		
		bSizer13_2_2 = wx.BoxSizer( wx.VERTICAL )
		
		self.prognosis1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Prognosis", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.prognosis1.Wrap( -1 )
		self.prognosis1.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_2.Add( self.prognosis1, 0, wx.ALL, 5 )
		
		bSizer13_2_2_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.goodPrognsisCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Good", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.goodPrognsisCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_2_1.Add( self.goodPrognsisCheckBox, 0, wx.ALL, 5 )
		
		self.goodWithTherapyPrognsisCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Good With Therapy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.goodWithTherapyPrognsisCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_2_1.Add( self.goodWithTherapyPrognsisCheckBox, 0, wx.ALL, 5 )
		
		self.fairWithTherapyPrognsisCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Fair With Therapy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fairWithTherapyPrognsisCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_2_1.Add( self.fairWithTherapyPrognsisCheckBox, 0, wx.ALL, 5 )
		
		self.guardedDespiteTherapyCheckBox = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"Guarded Despite Therapy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.guardedDespiteTherapyCheckBox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer13_2_2_1.Add( self.guardedDespiteTherapyCheckBox, 0, wx.ALL, 5 )
		
		
		bSizer13_2_2.Add( bSizer13_2_2_1, 1, wx.EXPAND, 5 )
		
		
		bSizer13_2.Add( bSizer13_2_2, 1, wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer13_2, 1, wx.EXPAND, 5 )
		
		
		bSizerScrolled.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.vascularsystem = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Vascular System", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.vascularsystem.Wrap( -1 )
		self.vascularsystem.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer14.Add( self.vascularsystem, 0, wx.ALL, 5 )
		
		self.vascularSystemTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer14.Add( self.vascularSystemTxtCtrl, 1, wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer14, 0, wx.EXPAND, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.gastrointestinal = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Gastro Intestinal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gastrointestinal.Wrap( -1 )
		self.gastrointestinal.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer15.Add( self.gastrointestinal, 0, wx.ALL, 5 )
		
		self.gastroIntestinalTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer15.Add( self.gastroIntestinalTxtCtrl, 1, wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer15, 0, wx.EXPAND, 5 )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.genitourinary = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Genitourinary", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.genitourinary.Wrap( -1 )
		self.genitourinary.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer16.Add( self.genitourinary, 0, wx.ALL, 5 )
		
		self.genitourinaryTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer16.Add( self.genitourinaryTxtCtrl, 1, wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer16, 0, wx.EXPAND, 5 )
		
		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.hernia = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Hernia", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hernia.Wrap( -1 )
		self.hernia.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer17.Add( self.hernia, 0, wx.ALL, 5 )
		
		self.herniaTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer17.Add( self.herniaTxtCtrl, 1, wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer17, 0, wx.EXPAND, 5 )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.musculoskeletal = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Musculoskeletal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.musculoskeletal.Wrap( -1 )
		self.musculoskeletal.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer18.Add( self.musculoskeletal, 0, wx.ALL, 5 )
		
		self.musculoskeletalTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer18.Add( self.musculoskeletalTxtCtrl, 1, wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer18, 0, wx.EXPAND, 5 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.neurological = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Neurological", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.neurological.Wrap( -1 )
		self.neurological.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer19.Add( self.neurological, 0, wx.ALL, 5 )
		
		self.neurologicalTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer19.Add( self.neurologicalTxtCtrl, 1, wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer19, 0, wx.EXPAND, 5 )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.skin = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Skin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.skin.Wrap( -1 )
		self.skin.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer20.Add( self.skin, 0, wx.ALL, 5 )
		
		self.skinTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer20.Add( self.skinTxtCtrl, 1, wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer20, 0, wx.EXPAND, 5 )
		
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.estimateofmentalcondition = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Estimate of Mental Condition", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.estimateofmentalcondition.Wrap( -1 )
		self.estimateofmentalcondition.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer21.Add( self.estimateofmentalcondition, 0, wx.ALL, 5 )
		
		self.estimateofMentalConditionTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer21.Add( self.estimateofMentalConditionTxtCtrl, 1, wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer21, 0, wx.EXPAND, 5 )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.diagnosis = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"DIAGNOSIS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.diagnosis.Wrap( -1 )
		self.diagnosis.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer22.Add( self.diagnosis, 0, wx.ALL, 5 )
		
		self.diagnosisTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer22.Add( self.diagnosisTxtCtrl, 1, wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer22, 0, wx.EXPAND, 5 )
		
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.prognosis = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"PROGNOSIS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.prognosis.Wrap( -1 )
		self.prognosis.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer23.Add( self.prognosis, 0, wx.ALL, 5 )
		
		self.prognosisTxtCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer23.Add( self.prognosisTxtCtrl, 1, wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer23, 0, wx.EXPAND, 5 )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.submit = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Submit Form", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.submit.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer24.Add( self.submit, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizerScrolled.Add( bSizer24, 0, wx.EXPAND, 5 )
		
		
		self.m_scrolledWindow1.SetSizer( bSizerScrolled )
		self.m_scrolledWindow1.Layout()
		bSizerScrolled.Fit( self.m_scrolledWindow1 )
		bSizer1.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.submit.Bind( wx.EVT_BUTTON, self.Submitted )

		self.dataList=[]
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Submitted( self, event ):
		self.dataList.append([['<b>Patient Name</b> '+self.patientNameTextCtrl.GetValue(),'<b>Date of Birth</b> '+self.dataOfBirthTextCtrl.GetValue()]])
		self.dataList.append([['']])
		self.dataList.append([['<b>Address</b> '+self.addressTextCtrl.GetValue()]])
		self.dataList.append([['']])
		self.dataList.append([['<b>Case Name</b> '+self.caseNametxtCrl.GetValue(),'<b>Case No</b> '+self.caseNumberTxtctrl.GetValue(),
		'<b>Category</b> '+self.categoryTextCtrl.GetValue(),'<b>App No</b> '+self.appNoTxtctrl.GetValue()]])
		self.dataList.append([['']])
		self.dataList.append([['<b>Eligibilty Specialist</b> '+self.eligibiltySpecialistTxtCtrl.GetValue(),'<b>BJN</b> '+self.bJNtxtCtrl.GetValue(),
		'<b>Mail Code</b> '+self.mailCodeTxtCtrl.GetValue(),'<b>Medical Auth Date</b> '+self.medicalAuthDateTxtCtrl.GetValue()]])
		self.dataList.append([['']])

		self.dataList.append([['<b>TO BE COMPLETED BY EXAMINING PHYSICIAN</b>']])
		self.dataList.append([['']])
		self.dataList.append([['<b>Medical History</b> '+self.medicalHistoryTxtCtrl.GetValue()]])
		self.dataList.append([['']])

		self.dataList.append([['<b>Height</b> '+self.heightTxtCtrl.GetValue(),'<b>weight</b> '+self.weightTxtCtrl.GetValue(),
		'<b>Blood Pressure</b> '+self.bloodPressureTxtCtrl.GetValue(),'<b>Pulse</b> '+self.pulseTxtCtrl.GetValue(),
		'<b>General Appearance</b> '+self.generalAppearanceTxtCtrl.GetValue(),'<b>Head,Scalp </b> '+self.headScalpTxtCtrl.GetValue()]])
		self.dataList.append([['']])
		self.dataList.append([['<b>Ears</b> '+self.earsTxtCtrl.GetValue(),'<b>Hearing Left</b> '+self.hearingLeftTxtCtrl.GetValue(),
		'<b>Hearing Right</b> '+self.hearingRightTxtCtrl.GetValue(),'<b>Nose</b> '+self.noseTxtCtrl.GetValue(),
		'<b>Throat</b> '+self.throatTxtCtrl.GetValue(),'<b>Mouth</b> '+self.mouthTxtCtrl.GetValue()]])
		self.dataList.append([['']])

		self.dataList.append([['<b>WITHOUT GLASSES</b>','<b>WITH GLASSES</b>']])
		self.dataList.append([['']])
		self.dataList.append([['<b>Visual Acuity </b>','<b>Distance (20 ft.)</b>','<b>Near (14 in.)</b>','<b>Distance (20 ft.)</b>','<b>Near (14 in.)</b>']])
		self.dataList.append([['']])
		self.dataList.append([['<b>RIGHT EYE</b>',self.rightEyeDistanceWithOutGlassesTxtCtrl.GetValue(),self.rightEyeNearWithOutGlassesTxtCtrl.GetValue(),
			self.rightEyeDistanceWithGlassesTxtCtrl.GetValue(),self.rightEyeNearWithGlassesTxtCtrl.GetValue()]])
		self.dataList.append([['']])
		self.dataList.append([['<b>LEFT EYE</b>',self.leftEyeDistanceWithOutGlassesTxtCtrl.GetValue(),self.leftEyeNearWithOutGlassesTxtCtrl.GetValue(),
			self.leftEyeDistanceWithGlassesTxtCtrl.GetValue(),self.leftEyeNearWithGlassesTxtCtrl.GetValue()]])
		self.dataList.append([['']])
		self.dataList.append([['<b>Field of Vision</b>']])
		self.dataList.append([['']])
		self.dataList.append([['<b>Is there any limitation in the field of vision?</b> ','<b>Right Eye:</b> '+str(self.righteyeCheckBox.GetValue()),
		'<b>Left Eye:</b> '+str(self.lefteyeCheckBox.GetValue())]])
		self.dataList.append([['']])

		self.dataList.append([['<b>Neck</b> '+self.neckTxtCtrl.GetValue()]])
		self.dataList.append([['']])
		self.dataList.append([['<b>Chest</b> '+self.chestTxtCtrl.GetValue()]])
		self.dataList.append([['']])
		self.dataList.append([['<b>Cardio Vascular System</b> '+self.cardiovascularSystemTxtCtrl.GetValue()]])
		self.dataList.append([['']])

		self.dataList.append([['<b>Cardiac Status</b> ','<b>Prognosis</b>']])
		self.dataList.append([['']])
		self.Status=[]
		if self.uncompromisedCardiacStatusCheckBox.GetValue():
			self.Status.append('Uncompromised ')
		if self.slightlyCompromisedCardiacStatusCheckBox.GetValue():
			self.Status.append('Slightly Compromised ')
		if self.moderatelyCompromisedCardiacStatusCardiacStatusCheckBox.GetValue():
			self.Status.append('Moderately Compromised ')
		if self.severelyCompromisedCardiacStatusCheckBox.GetValue():
			self.Status.append('Severely Compromised</b> ')

		if self.goodPrognsisCheckBox.GetValue():
			self.Status.append('Good ')
		if self.goodWithTherapyPrognsisCheckBox.GetValue():
			self.Status.append('Good With Therapy ')
		if self.fairWithTherapyPrognsisCheckBox.GetValue():
			self.Status.append('Fair With Therapy')
		if self.guardedDespiteTherapyCheckBox.GetValue():
			self.Status.append('Guarded Despite Therapy ')
       
		self.dataList.append([self.Status])
		self.dataList.append([['']])


		self.dataList.append([['<b>Vascular System</b> '+self.vascularSystemTxtCtrl.GetValue()]])
		self.dataList.append([['']])
		self.dataList.append([['<b>Gastro Intestinal</b> '+self.gastroIntestinalTxtCtrl.GetValue()]])
		self.dataList.append([['']])
		self.dataList.append([['<b>Genitourinary</b> '+self.genitourinaryTxtCtrl.GetValue()]])
		self.dataList.append([['']])

		self.dataList.append([['<b>Hernia</b> '+self.herniaTxtCtrl.GetValue()]])
		self.dataList.append([['']])
		self.dataList.append([['<b>Musculo Skeletal</b> '+self.musculoskeletalTxtCtrl.GetValue()]])
		self.dataList.append([['']])
		self.dataList.append([['<b>Neurological</b> '+self.neurologicalTxtCtrl.GetValue()]])
		self.dataList.append([['']])

		self.dataList.append([['<b>Skin</b> '+self.skinTxtCtrl.GetValue()]])
		self.dataList.append([['']])
		self.dataList.append([['<b>Estimate of Mental Condition</b> '+self.estimateofMentalConditionTxtCtrl.GetValue()]])
		self.dataList.append([['']])
		self.dataList.append([['<b>Diagnosis</b> '+self.diagnosisTxtCtrl.GetValue()]])
		self.dataList.append([['']])

		self.dataList.append([['<b>Prognosis</b> '+self.prognosisTxtCtrl.GetValue()]])
		self.dataList.append([['']])


		self.pdfBuilder=PdfBuilder()
		self.pdfBuilder.getDataList(self.dataList)
		print self.dataList
		event.Skip()


app=wx.App()
frame=Frame(None)
frame.Show()
frame.Maximize(True)
app.MainLoop()
	

