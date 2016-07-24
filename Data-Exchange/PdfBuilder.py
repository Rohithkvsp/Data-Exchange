from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph,Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import datetime

class PdfBuilder():

	def __init__ (self,lastname):
		print lastname
		self.filename=lastname+"_"+datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
		self.doc = SimpleDocTemplate(str(self.filename+'.pdf'),pagesize = letter)
		self.story=[]
		self.styles = getSampleStyleSheet()
		self.styleN = self.styles['Normal']
		self.styles.leading = 40
		self.spacer=Spacer(0,0.2*inch)
		print "ok"

	def getDataList(self,data_list):
		for data in data_list:
			self.data_table = [[Paragraph(cell, self.styleN) for cell in row] for row in data]
			self.t=Table(self.data_table)
			self.story.append(self.t)
			self.story.append(self.spacer)
		self.doc.build(self.story)
		print data_list

if __name__ == "__main__":
	main()




