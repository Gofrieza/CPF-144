def sumTriple(arr, num):
    for val in range(0, num - 2):
        for value in range(val + 1, num - 1):
            for numm in range(value + 1, num):
                if arr[val] + arr[value] + arr[numm] == 0:
                    print("arr[val]", arr[val], "arr[value]", arr[value], "arr[numm]", arr[numm])
    if arr[val] + arr[value] + arr[numm] != 0:
        print("No such triplet exist")


arr = [0, -1, 2, -3, 1]
num = len(arr)
sumTriple(arr, num)
