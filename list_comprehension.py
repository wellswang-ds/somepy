#Challenge: Use list comprehension to create the following list of lists
#'[[1, 2, 3], [4, 5, 6], [7, 8, 9]]'

a = [1,2,3]
b = [[i+3*j for i in a] for j in range(3)]

print(b)
