def read():
    arr=[]
    with open("input.txt") as f:
       arr=f.readlines()
    return arr


def write(outputINFO):
    with open("output.txt", "w") as file:
        for i in outputINFO:
            print(i, file=file)

def format_string(str):
    RECORDING=False
    firt_part_rec=False
    second_part_rec=False
    firt_part_rec_finish=False
    second_part_rec_finish=False
    all=""
    variable=""
    variable_copy=""
    equal_of_var=False
    find_plus=False
    find_equal=False


    for i in range(len(str)):

        if str[i]=="1" and find_plus and equal_of_var and RECORDING:
            all+=str[i]
            variable+="++"
            str.replace(all,variable)
            RECORDING=False

        elif str[i]==" " and find_plus and RECORDING:
            all+=str[i]

        elif str[i]=="+"and second_part_rec_finish  and RECORDING:
            all+=str[i]
            find_plus=True


        elif str[i]==" " and second_part_rec_finish  and RECORDING:
            all+=str[i]

        elif str[i]==" "and second_part_rec:
            second_part_rec_finish=True
            all+=str[i]
            if variable==variable_copy:
                equal_of_var=True
            else:
                RECORDING=False 
                all=""
                variable=""
                variable_copy=""
                firt_part_rec=False
                second_part_rec=False
                firt_part_rec_finish=False
                second_part_rec_finish=False
                find_equal=False


        elif str[i].isalpha() and second_part_rec and RECORDING:
            all+=str[i]
            variable_copy+=str[i]

        elif str[i].isalpha() and second_part_rec==False and find_equal and RECORDING:
            second_part_rec=True
            all+=str[i]
            variable_copy+=str[i]

        elif str[i]=="="and firt_part_rec_finish and RECORDING:
            find_equal=True
            all+=str[i]

        elif str[i]==" "and firt_part_rec_finish and RECORDING:
            all+=str[i]

        elif str[i]==" "and firt_part_rec and RECORDING:
            firt_part_rec_finish=True
            all+=str[i]

        elif str[i].isalpha() and firt_part_rec and RECORDING:
            variable+=str[i]
            all+=str[i]

        elif str[i].isalpha() and firt_part_rec==False:
            RECORDING=True
            firt_part_rec=True
            variable+=str[i]
            all+=str[i]
    return str


def main():
    text=read()
    ssa=0
    result=[]
    for i in range(len(text)):
        result.append(format_string(text[i]))
    write(result)
    
main()
