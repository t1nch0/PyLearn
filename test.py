data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])
data=data.upper()
print(data)
stuff = dict()
print(stuff.get('candy',-1))