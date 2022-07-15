from random import randint

m=2**68
n=2**69

x=randint(m,n)

print(f"0) Initial value ={x}")
n=1
while x!=1:
  if x%2!=0:
    x=3*x+1
    print(f"{n}) {x}")
  else:
    x=x/2
    print(f"{n}) {x}")
  n+=1  
else:
  print(f"x={x} reached at {n-1} iterations")  
  n=0  
  while n<16:
    if x%2!=0:
      x=3*x+1
      print(x)
    else:
      x=x/2
      print(x)
    n+=1
 

