def EvenOddSum(a, n):
    list1 = [11, 5, 17, 18, 23,5]


    total = sum(list1)


    print("Sum of all elements in given list: ", total)

    if (total % 2) == 0:
        print("{0} is Even".format(total))
    else:
        print("{0} is Odd".format(total))


arr = [11, 5, 17, 18, 23,5]
n = len(arr)

EvenOddSum(arr, n)