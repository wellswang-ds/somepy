#Challenge: Use list comprehension to create the following list of lists
#'[[1, 2, 3], [4, 5, 6], [7, 8, 9]]'

a = [1,2,3]
b = [[i+3*(j-1) for i in a] for j in a]

print(b)


# a = [0,1,2]
# b = [[i+3*j+1 for i in a] for j in a]
# print(b)


jj = [[i+3*j+1 for i in range(3)] for j in range(3)]
[[x+i for i in range(3)] for x in range(1,8,3)]
print(jj)


print(a)