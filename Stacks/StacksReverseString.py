def reverse_string(a_string):   #Function reverse_string accepts string as parameter.
    stack = []
    string = " "
    for c in a_string:      #Use for loop to push each character onto your stack.
        stack.append(c)
    for c in a_string:      #Use another loop to iterate through stack and add each character to the a_string variable as your pop them off stack.
        string += stack.pop()
    return string           #Return reversed string.

print(reverse_string("Bieber"))

#"rebeiB"

