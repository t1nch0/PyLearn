#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce
#  an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

fname = input("Enter file name: ")
fh = open(fname)
new_val=0
total=0
added_values=0
for line in fh:
    line2=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    total=total+1
    #print(line2)
    spc_pos=line2.find(' ')   
    cut_text=spc_pos    
    #print(float(line2[cut_text:]))
    added_values=added_values+float(line2[cut_text:])
    #print(total, added_values)
total=added_values/total
print('Average spam confidence:',total)
