def check_parentheses(a_string):        #Function accepts string to check for balanced parentheses as parameter
    stack = []                          #Create stack using list.
    for c in a_string:                  #Use for loop to iterate through characters in a_string
        if c == "(":                    #If character is an opening parentheses , push it onto stack.
            stack.append(c)
        if c == ")":                    #If symbol is closing parentheses and stack is empty, return False since there's no matching opening parentheses on stack; string not balanced.
            if len(stack) == 0:         #If there're opening parentheses in stack, pop one off to match closing parentheses
                return False
            else:
                stack.pop()
    return len(stack) == 0              #Once for loop finishes, return whether or not length of stack is zero.
        
    