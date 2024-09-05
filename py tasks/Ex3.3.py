score = input("Enter Score: ")
try:
    sc=float(score)       
except:
    print("plase insert a numerical value between 0.0 to 1.0")
    quit()
if(sc<0):
    print("plase insert a numerical value between 0.0 to 1.0")
    quit()
elif(sc>1):
    print("plase insert a numerical value between 0.0 to 1.0")
    quit()
if(sc>=0.9):
    grade="A"
elif(sc>=0.8):
    grade="B"
elif(sc>=0.):
    grade="C"
elif(sc>=0.6):
    grade="D"
else:
    grade="F"
print(grade)
    