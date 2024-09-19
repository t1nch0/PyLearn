# 10.2 Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon. From stephen.marquard@uct.ac.za Sat Jan  5
# 09:14:16 2008 Once you have accumulated the counts for each hour, print out
# the counts, sorted by hour as shown below.
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count_hours=dict()
lst=list()
for line in handle:
    # print(line.strip())
    if 'From ' in line:
        # print(line.strip())
        words=line.split()
        hounrs=words[5].split(':')[0]
        # print(hounrs)
        # for word in hounrs:
        count_hours[hounrs]=count_hours.get(hounrs,0)+1
# print('daa',count_hours)
for key,val in count_hours.items():
    neword=(key,val)
    lst.append(neword)
    # print(key,val)
    lst.sort()
    # print(lst)
for n in lst:
    print(n[0],n[1])
# print('sorted',lst)
   