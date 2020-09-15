
# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#Count these lines and extract the floating point values from each of the lines and
#compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at
#http://www.py4e.com/code3/mbox-short.txt
#when you are testing below enter mbox-short.txt as the file name.7.1 Write a program that prompts for a file name,

# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)
count = 0
soma = 0

for line in fh:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:") :
        count = count + 1
        palavra = line[20:]
        palavra = float(palavra)
        soma = palavra + soma
        media = soma / count

print("Average spam confidence:", media)
