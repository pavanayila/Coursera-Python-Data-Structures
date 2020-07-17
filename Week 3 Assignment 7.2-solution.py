#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#    X-DSPAM-Confidence:    0.8475
#    Count these lines and extract the floating point values from each of the lines and
#    compute the average of those values and produce an output as shown below. Do
#    not use the sum() function or a variable named sum in your solution.
#    You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as     the file name.

#solution)

# Use the file name mbox-short.txt as the file name

total=0

count=0

fname = input("Enter file name: ")

fh = open(fname)

for line in fh:

    if not line.startswith("X-DSPAM-Confidence:") :

    	continue

    count=count+1


    pos=line.find(':')

    value=line[pos+1:]

    total=total+float(value)

    avg=total/count

print("Average spam confidence:",avg)
