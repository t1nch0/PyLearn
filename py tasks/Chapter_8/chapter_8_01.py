# 8.4 Open the file romeo.txt and read it line by line. For each line, 
# split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line 
# check to see if the word is already in the list and if not append it 
# to the list. When the program completes, sort and print the resulting 
# words in python sort() order as shown in the desired output.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
word =''
init=0
final=0
for line in fh:
    # print(line.rstrip())
    # print(len(line.rstrip()))
    line_len=len(line)
    aux=line.split()
    for word in aux:
        if word not in lst:
            lst.append(word)
    # spc_pos=aux.find(' ')
    # final=spc_pos+1
    # #print(line)
    # while ' ' in aux:
    #     # print(aux.rstrip())
    #     spc_pos=aux.find(' ')
    #     line_len=line_len-spc_pos
    #     final=spc_pos+1
    #     word=aux[:final].strip()
    #     # print(word)
    #     aux=aux[final:]
    #     # print(aux.rstrip())
    #     init=final
    #     if word not in lst:
    #         lst.append(word)

lst.sort()
print(lst)
    