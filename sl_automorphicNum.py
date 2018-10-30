#use remainder 


def checkNum(num):
	s=pow(num,2)
	x=(s-num)%(10*len(str(num)))
	if(x!=0):
		print("it's not a automorphic number.")
	else:
		print("it is a automorphic number.")
checkNum(int(input("please input number you want to check: ")))
