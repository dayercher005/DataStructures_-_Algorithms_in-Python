def binary_search(a_list, n):           #binary_search function takes 2 arguments, a_list and n(target number)
    first = 0                           #first and last variables used to keep track of beginning and end of list we are searching.
    last = len(a_list) - 1              #We will be changing the value of the 2 variables as we divide a_list into smaller segments
    while last >= first:                #Algorithm's loop will continue as long as there is still items in list
        mid = (first + last) // 2       #Locate mid-point of a_list by averaging first and last.
        if a_list[mid] == n:
            return True                 #If element is at midpoint, return True
        else:
            if n < a_list[mid]:         #If item is no at midpoint and is less than midpoint value, set value of last to midpoint value minus 1, which cuts off the upper half of list from further processing
                last = mid - 1          
            else:                       #If target item is greater than midpoint value, set value of first to the midpoint value + 1, which cuts off lower half of the list from further processing
                first = mid + 1
    return False                        #When loop terminates, function returns False since we've made it to the end of the function and number is not in iterable


#Binary search takes O(log n) time. It is more efficient than linear search because we don't have to search the entire list. Only works with sorted data.