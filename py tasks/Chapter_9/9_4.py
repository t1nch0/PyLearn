# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number
#  of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the
#  person who sent the mail. The program creates a Python dictionary that maps the sender's mail address 
# to a count of the number of times they appear in the file. After the dictionary is produced, the program 
# reads through the dictionary using a maximum loop to find the most prolific committer.
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
counts=dict()

handle = open(name)
for line in handle:
    if 'From ' in line:
        # print(line)
        byWord=line.split()
        # print(byWord)

        counts[byWord[1]]=counts.get(byWord[1],0)+1
# print(counts)
maxemail=max(counts, key = counts.get)
print(maxemail,counts[maxemail])
# for email in counts:
#     number=counts.get(email)
#     print(counts.get(email))
#     if number>counts.get(email):
#         number=counts.get(email)
#         print('este es',number)