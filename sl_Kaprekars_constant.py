#easy
def ka_sub(num):
	digit=[]
	for i in num:
		digit.append(i)

	digit_0=sorted(digit,reverse=0)  #升序排序
	digit_1=sorted(digit,reverse=1) #降序排列

	num_min=int(''.join(digit_0))
	num_max=int(''.join(digit_1))
	sub=num_max-num_min
	print(num_max,num_min,sub)
	return sub

def search_ka(ori):
	temp=0
	temp_0=ka_sub(ori)
	while(temp_0!=temp):
		print(ori,temp,temp_0)
		temp=temp_0
		temp_0=ka_sub(str(temp_0))
	return temp

print(search_ka(input("please input a number: ")))


#medium



#hard
