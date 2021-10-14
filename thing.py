import math

def is_square(arr):
    # Your code here
    if arr == []:
        return None
    for i in arr:
        s = str(math.sqrt(i))
        if len(s) > 3:
            return False
    return True



a = is_square([1,5,9,16])
print(a)