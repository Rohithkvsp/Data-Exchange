from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import datetime

class PdfBuilder():

	def __init__ (self):
		self.filename=datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
		self.doc = SimpleDocTemplate(str(self.filename+'.pdf'),pagesize = letter)
		self.story=[]
		self.styles = getSampleStyleSheet()
		self.styleN = self.styles['Normal']
		print "ok"

	def getDataList(self,data_list):
		for data in data_list:
			self.data_table = [[Paragraph(cell, self.styleN) for cell in row] for row in data]
			self.t=Table(self.data_table)
			self.story.append(self.t)
		self.doc.build(self.story)
		print data_list

if __name__ == "__main__":
	main()




