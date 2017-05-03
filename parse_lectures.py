#print "document1.pdf has %s pages." % input1.getNumPages())
from pyPdf import PdfFileWriter, PdfFileReader


input1 = PdfFileReader(file("QuantumNotes.pdf", "rb"))

lec_first_page = [4,6,10,14,18,23,28,32,37,40,45,49,53,58,64,68,72]

zero_indexed = [l-1 for l in lec_first_page]


for lec_num in range(0,len(zero_indexed)):
	output = PdfFileWriter()
	for i in range(zero_indexed[lec_num],zero_indexed[lec_num+1]):
		output.addPage(input1.getPage(i))
		outputStream = file("IndividualLectures/Lecture_" + str(lec_num+1) + ".pdf", "wb")
		output.write(outputStream)
