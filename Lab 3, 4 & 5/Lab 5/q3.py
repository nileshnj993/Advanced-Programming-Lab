class subsets:
    def __init__(self, unique):
        self.subsets = [[]] # initial empty subset list
        self.unique = unique

    def subsetCreate(self): 
         for i in range(len(self.unique)): 
            initial = self.subsets[:] # all subsets before current
            new = self.unique[i] 
            for j in range(len(self.subsets)): 
                self.subsets[j] = self.subsets[j] + [new] # adding all elements possible in a subset
            self.subsets = initial + self.subsets # appending possible subsets to list

print("Enter list of unique numbers:")
unique = list(map(int, input().split())) 

subset = subsets(unique)
subset.subsetCreate()
print("Subsets are : ", subset.subsets)