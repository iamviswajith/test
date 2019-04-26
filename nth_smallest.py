def nthsmallest(arr, m):
    start = 0
    end = len(arr) - 2

    index = 0
    new_arr = [0]*(len(arr)-1)

    for i in range(1,len(arr)):
        if arr[i] < arr[index]:
            new_arr[start] = arr[i]
            start += 1
        else:
            new_arr[end] = arr[i]
            end -= 1
    print(new_arr)
    if m > start:
        return nthsmallest(new_arr[start+1:len(new_arr)], m-start+end-1)
    elif m < start:
        return nthsmallest(new_arr[0:start], m)
    else:
        return arr[start]


print(nthsmallest([10, 2, 5, 6, 11, 3, 15], 5))
