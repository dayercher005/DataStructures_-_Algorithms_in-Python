def linear_search(a_list, n):       #Calls linear_search function and passes in a list and the number to search for, n.
    for i in a_list:        
        if n == True:
            return True
    return False

a_list = [1, 8, 32, 91, 5, 15, 9, 100, 3] 
print(linear_search(a_list, 91))        #If there is a match, you return True. If you make it through the list and there is no match, you return False.
                                        # Will return True

# Linear search's time complexity is O(n). Should consider using linear search if data is not sorted.