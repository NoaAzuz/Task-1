def exponent(x):
    aassembly=1
    denominator=1
    numerator=1
    number=1
    ssum=1
    while number<170:
            numerator=x*numerator
            denominator=(aassembly)*denominator
            aassembly=aassembly+1
            ssum=ssum+(numerator/denominator)
            number=number+1
    return ssum

def Ln(x):
   if x<=0.0:
       return 0.0
   n= 0.0
   yn1=0.0
   while n<1000:
       yn1=yn1+2*((x-exponent(yn1))/((x+exponent(yn1))))
       n=n+1.0 
   return yn1

def XtimesY(x,y):
    if x<=0.0:
        return 0.0
    outcome= exponent(y*Ln(x))
    return outcome

def sqrt(x,y):
    if x==0.0 or y<=0.0:
        return 0.0
    outCome= XtimesY(y, 1/x)
    return outCome

def calculate(x):
    if x<0.0:
        return 0.0
    calculation=(exponent(x))*(XtimesY(7,x))*(XtimesY(x,-1))*(sqrt(x,x))
    return calculation
   
 

   

 


      

            