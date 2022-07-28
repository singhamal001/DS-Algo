# This code is to reverse an array (original)
def RevArr(Arr):
    x=len(Arr)-1
    res_arr=[]
    while x>=0:
        res_arr.append(Arr[x])
        x-=1
    return res_arr

test_arr=[1,2,3,4,5]
print(test_arr)
print(RevArr(test_arr))

#(Another approach found online)(gog)
# Iterative python program to reverse an array
 
# Function to reverse A[] from start to end
def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
 
# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)
# This program is contributed by Pratik Chhajer
