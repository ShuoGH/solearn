#use the dictionary

def che_pandi(num):
	dic = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'0':0}
	n_str=str(num)
	for i in n_str:
		dic[i]+=1
	for idic,idic_num in dic.items():
		if(idic_num==0):
			print("sorry, it's not a Pandigital number.")
			return 0
	print("the number you put is a Pandigital number.")
	print("digit:times")
	for d,dt in dic.items():
		print("  "+d+" : ",dt)
	return 0

num=int(input("please input the number you want to check: "))
che_pandi(num)


'''
str convert int to str
str is a list 
use the function of list to check 

dictionary 
'''