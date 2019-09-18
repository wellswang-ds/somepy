#Challenge: Use list comprehension to create the following list of lists
#'[[1, 2, 3], [4, 5, 6], [7, 8, 9]]'

a = [1,2,3]
b = [[i+3*(j-1) for i in a] for j in a]

print(b)


# a = [0,1,2]
# b = [[i+3*j+1 for i in a] for j in a]
# print(b)


jj = [[i+3*j+1 for i in range(3)] for j in range(3)]

a = 12
b = 3
k = [[x+i for i in range(b)] for x in range(1,a+1,b)]
kk= [x for x in range(1,10,3)]
print(jj)
print(k)
print(kk)

print(a)