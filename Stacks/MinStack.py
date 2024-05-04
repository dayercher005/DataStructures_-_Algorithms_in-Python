class MinStack:
    def __init__(self):
        self.main = []      #use main to keep track of main stack  
        self.min = []       #use min to keep track of smallest element

    def push(self, n):
        if len(self.main) == 0: #Check to see if self.main is empty since it will be smallest number in stack if its empty.
            self.min.append(n)  #Append n to min in self.main is empty.
        elif n<=self.min[-1]:   #If self.main isn't empty, check if n <= last item in self.min. Last item in self.min needs to be smallest number in stack.
            self.min.append(n)  #If n <=last item in self.min, append n to self.min
        else:
            self.min.append(self.min[-1])   #If n > self.min, append last item in self.min to self.min.
        self.main.append(n)

    def pop(self): 
        self.min.pop()
        return self.main.pop()
    
    def get_min(self):
        return self.min[-1]