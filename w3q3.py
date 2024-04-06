def powerset(A):
    if not A:
        return [[]]
    x = powerset(A[1:])
    return x + [[A[0]] + y for y in x]

print("Enter the number of elements you want in your array")
num_of_ele = int(input())
i=0
input_array=[]
while(i<num_of_ele):
    print(f"Enter the {i+1} element")
    input_arr = int(input("> "))
    input_array.append(input_arr)
    i+=1
A = set(input_array)

cardinality = len(A)
print("Set A:", A)
print("Cardinality of set A:", cardinality)

element = int(input("Enter Element: "))
if element in A:
    print(element, "is a member of set A")
else:
    print(element, "is not a member of set A")

power_set = powerset(list(A))
print("Power set of set A:", power_set)
