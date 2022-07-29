# PROBLEM STATEMENT
# Union of two arrays
# Given two arrays a[] and b[] of size n and m respectively. The task is to find union between these two arrays.
# Union of the two arrays can be defined as the set containing distinct elements from both the arrays.
# If there are repetitions, then only one occurrence of element should be printed in the union.

n=int(input("Enter the length of Array1 \n"))
n1=int(input("Enter the length of Array2 \n"))

test_arr1=[]
test_arr2=[]
print("Enter the elements of Array1")
for i in range(0,n):
    test_arr1.append(int(input()))

print("Enter the elements of Array2")
for i in range(0,n1):
    test_arr2.append(int(input()))

test_arr=test_arr1+test_arr2
print(set(test_arr))
