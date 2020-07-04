import find_name_m

def read():
    arr=[]
    with open("input.txt") as f:
       arr=f.readlines()
    result=[]
    for i in range(len(arr)):
        result.append(arr[i].split())
    return result

def write(outputINFO):
    with open("output.txt", "w") as file:
        for i in range(len(outputINFO)):
            print(outputINFO[i], file=file)

def main():
    write(find_name_m.find_name.find_names(read()))

main()