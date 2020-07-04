class find_name:
    def __init__(self):
        pass

    def find_names(arr):
        result=[]
        tmp=""
        key=0
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if key==3:
                    result.append(tmp)
                    key=0
                    tmp=""
                if arr[i][j][0].isupper():
                    key+=1
                    tmp=tmp+" "+arr[i][j]
                else:
                    key=0
                    tmp=""
        return result