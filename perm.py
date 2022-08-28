import math

def small(suf, sub):
	flag = True
	for i in range(len(sub) - 1):
		for j in range((i + 1), len(sub)):
			smal = int(sub[i])
			tiny = int(sub[j])
			if(smal < tiny):
				flag = False
				return flag
			elif(smal > suf or tiny > suf):
				flag = False
				return flag
	return flag
			
def longSuf(nums):
	#iterate thru all elements in nums
	for k in range(len(nums)):
	
		suf = int(nums[k])

		if(k == len(nums) - 1):
			return k

		if(k == len(nums) - 2):
			if(suf > int(nums[len(nums) - 1])):
				return k
			else:
				return(k + 1)

		#create a sublist			
		sub = nums[k + 1 : len(nums)]	
		flag = small(suf, sub)

		if(flag == True):
			return k
		
	
def pivSwap(nums, suf):
	piv = suf - 1
	smallSwap = 100
	ind = 0
	for k in range(suf, len(nums)):
		if(nums[piv] < nums[k]):
			if(int(nums[k]) <= smallSwap):
				ind = k
				smallSwap = int(nums[k]) 

	temp = nums[ind]
	nums[ind] = nums[piv]
	nums[piv] = temp

	return(nums)

def revSuf(nums, suf):
	prefix = nums[0:suf]
	revSuf = nums[suf:len(nums)]
	revSuf.reverse()
	perm = prefix + revSuf
	return(perm)

def nextPerm(nums):
	suf = longSuf(nums)
	print(suf)
	newNums = pivSwap(nums, suf)
	return(revSuf(newNums, suf))

def findPerms(nums):
#	print(''.join(nums))
	for i in range(999999):
		perm = nextPerm(nums)
		print(''.join(perm))
		nums = perm
#0125330
numbers = list("0123456789")
findPerms(numbers)
