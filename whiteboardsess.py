# Write a function that doubles every second integer in a list starting from the left.
# -> [1, 4, 3, 8]

list1 = [1,2,3,4]

def double_every_other():
    list2 = list1[1::2]
    return list2
        
    
        

print(double_every_other())

