import textract
import codecs
# cad2021 cad2021_robotics_textbook.pdf
#text = textract.process("Padmanabhan2016_Book_ProgrammingWithPython.pdf")
text = textract.process("cad2021_robotics_textbook.pdf")
print(text)