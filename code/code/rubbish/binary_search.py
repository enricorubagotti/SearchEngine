def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    print(str(arr[mid])+"=" + str(x))
    #It confuses between 0 and False
    if(str(arr[mid]) ==  str(x)):
        print(str(arr[mid]) == str(x))
        return mid
    else:
        print(str(arr[mid]) != str(x))
        return "not_found"
