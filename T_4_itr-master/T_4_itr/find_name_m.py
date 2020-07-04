import MyItr

class find_name:
    def __init__(self):
        pass

    def find_names(arr):
        result=set()
        tmp=""
        key=0
        my_iter = MyItr.MyIterator(0, len(arr), 1)

        for i in my_iter:
            my_iter_tmp = MyItr.MyIterator(0, len(arr[i]), 1)
            for j in my_iter_tmp:
                if key==3:
                    result.add(tmp)
                    key=0
                    tmp=""
                if arr[i][j][0].isupper():
                    key+=1
                    if key==1:
                        tmp=arr[i][j]
                    else:
                        tmp=tmp+" "+arr[i][j]
                else:
                    key=0
                    tmp=""
        return result