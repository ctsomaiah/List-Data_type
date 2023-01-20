# Assignment - List Data Type
# 9. Why list data type methods do not require re-assignment
# 10. The difference between append, extend, and insert
# 11. The Difference between pop, and remove

#1
print("1. Create a list with certain values")
list = [9,5,6,8,7,2]
print("List :",list)
list.sort()
print(list)

#2
print("\n2. Append 10 to the created list")
print("Before :",list)
list.append(10)
print("After :",list)

#3
print("\n3. Delete the last value in the list")
print("Before :",list)
list.pop()
print("After :",list)

#4
print("\n4. Delete the 4th index in the list")
print("Before deleting :", list)
del list[4]
print("After deleting :",list)

#5
print("\n5. Add ['what', 'is', 'your', 'name'] to the list")
print("Before :",list)
list.extend(['what', 'is', 'your', 'name'])
print("After :",list)

#6
print("\n6. Access the 5th index in the list")
print("List :",list)
print("5th index element :",list[5])

#7
print("\n7. Access the last index in the list")
print("List :",list)
print(list[-1])

#8
print("\n8. Create a list with multiple values and reverse it using the REVERSE function")
print("Before :",list)
list.reverse()
print("After :",list)



