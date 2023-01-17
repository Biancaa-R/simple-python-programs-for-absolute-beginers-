def binary_search(start,end,x):
	if end>=start:
		mid =start+(end-start)//2
		if arr[mid]==x:
			return mid
		if x>arr[mid]:
			return binary_search(mid+1,end,x)
		if x<arr[mid]:
			return binary_search(start,mid-1,x)
    		else:
			print("Element not found")
arr=[]
n=int(input("Enter the length of the list"))
for i in range(0,n):
	x=int(input("Enter a number"))
	arr.append(x)

x=int(input("Enter the value to be found"))

#Bubble sort:
swap=True

while swap:
	swap=False
	for i in range(0,len(arr)):
		for j in range(i+1,len(arr)):
			if arr[i]>arr[j]:
				arr[i],arr[j]=arr[j],arr[i]
				swap=True
print(arr)

start=0
end=len(arr)
x=binary_search(start,end,x)
print(x)
