
# 7.1 Write a program that prompts for a file name,
# then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt
# text = "X-DSPAM-Confidence:    0.8475";

var = text.find('0')
vor = text.find('5')

host = text[var+1:vor+1]

host = float(host)
print(host)
