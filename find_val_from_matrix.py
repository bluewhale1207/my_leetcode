＃在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
＃请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


def func(arr, value):
    length = len(arr)
    i =0
    j = length - 1

    while True:
        if arr[i][j] == value:
            return True

        while j >= 0 and arr[i][j] > value:
            j -= 1

        while i <= length -1 and arr[i][j] < value:
            i += 1

        if j < 0 or i > length -1:
            return False
  

print func([[1,4,7,10,15], [2,5,8,12,19], [3,6,9,16,22], [10,13,14,17,24], [18,21, 23, 26, 30]], 6)
