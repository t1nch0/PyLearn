hrs = input("Enter Hours:")
h = float(hrs)
rate= input("Enter Rate:")
r=float(rate)
def computepay(h, r):
    if h>=40:
        h2=h-40
        GP=h2*r*1.5+r*40    
    else:
        GP=h*r    
    return(GP)   
p = computepay(h, r)
print("Pay", p)

