
def lcm(n1,n2):
	if(n1>n2):
		n1,n2=n2,n1
	for i in range(1,n1+1):
		if((n2*i)%n1==0):
			return n2*i	
def hcf(n1,n2):
	if(n1>n2):
		n1,n2=n2,n1
	for i in reversed(range(1,n1+1)):
		if(n1%i==0 and n2%i==0):
			return i
a=int(input("input the first number: "))
b=int(input("input the second number: "))
print("the hcf is",hcf(a,b))
print("the lcm is",lcm(a,b))


