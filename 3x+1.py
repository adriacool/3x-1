from random import randint

x=randint(1,2000)
print(x)

print(f"0) Initial value ={x}")
n=1
while x!=4 and x!=2 and x!=1:
  if x%2!=0:
    x=3*x+1
    print(f"{n}) {x}")
  else:
    x=x/2
    print(f"{n}) {x}")
  n+=1  
else:
  print(f"Loop reached at {n-1} iterations(@x={x})")  
  n=0  
  while n<16:
    if x%2!=0:
      x=3*x+1
      print(x)
    else:
      x=x/2
      print(x)
    n+=1
 



