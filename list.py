# Basic list
# names=['Tim','Roy','Wang']
# print(names)
# print(names[2])
# print(names[-2])
# print(names[:2])
# print(names[2:])
# names[1:2]=["Juan"]
# print(names)

#different ways to add value in a list
# names.insert(0,"Will")
# print(names)
# names.append("Joe")
# print(names)
# extendlist=("Tom","Jerry")
# names.extend(extendlist)
# print(names)

#different ways to remove value in a list
# names.remove("Tim")
# print(names)
# names.pop()
# print(names)
# names.pop(1)
# print(names)
# names.clear()
# print(names)
# del names

#loops
# for i in names:
# 	print(i)

# # list comprehension
# newname=[i for i in names if 'Tim' in i]
# print(newname)

#sorting

fruits=['mango','apple','grapes']
fruits.sort()
print(fruits)

numbers=[110,10000000,234,56]
numbers.sort(reverse=True)
print(numbers)

#copy a list
copy_number=numbers.copy()
print(copy_number)
new_fruits=list(fruits)
print(new_fruits)

#list joing
concat_list=copy_number+new_fruits
print(concat_list)

for y in fruits:
	numbers.append(y)

print(numbers)
numbers.extend(fruits)
print(numbers)
