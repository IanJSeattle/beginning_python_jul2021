my_string = 'hello world'

# print out "hello"
print(my_string[:5])

# print out "world"
print(my_string[6:])

# print it backwards
print(my_string[::-1])

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
my_slice = my_list[2:7]
print(my_slice)

new_list = my_list
new_list[3] = 'z'
print(my_list)

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
new_list = my_list[:]
new_list[3] = 'z'
print(my_list)
print(new_list)
