found=0
def binary_search(start,end,x):
	if end>=start:
		mid =start+(end-start)//2
		if arr[mid]==x:
			return mid
                        found=1
		if x>arr[mid]:
			return binary_search(mid+1,end,x)
		if x<arr[mid]:
			return binary_search(start,mid-1,x)
    		else:
			print("Element not found")
 			found=0
arr=[]
n=int(input("Enter the length of the list"))
for i in range(0,n):
	x=str(input("Enter a name"))
	arr.append(x)

x=str(input("Enter the value to be found"))
linear=arr.copy()

#Bubble sort:
swap=True

while swap:
	swap=False
	for i in range(0,len(arr)):
		for j in range(i+1,len(arr)):
			if arr[i]>arr[j]:
				arr[i],arr[j]=arr[j],arr[i]
				swap=True
print(arr,"is the sorted list")

start=0
end=len(arr)
binary=binary_search(start,end,x)
print(binary,"is the index of the name in the sorted list")

for i in range(0,end):
	if linear[i]==x:
		print(i,"is the index of the name")
  		found+=1
if found==0:
	print("The name is not found in the list")

