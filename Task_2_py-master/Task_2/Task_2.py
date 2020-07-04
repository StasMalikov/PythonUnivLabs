arr=[]
with open("input.txt") as f:
    for line in f:
        arr.append([int(x) for x in line.split()])

for i in range(len(arr)):
    print(arr[i])

new_arr= arr
i=0

for i in range(len(new_arr)):
    for j in range(len(new_arr[i])):
        if(i+j>=len(new_arr)):
            continue
        else:
            new_arr[i][i+j],new_arr[i+j][i]=new_arr[i+j][i],new_arr[i][i+j]

with open("output.txt", "w") as file:
	for i in range(len(new_arr)):
		print(new_arr[i], file=file)