# Problem statement:
# Write a program to print the design attached in this mail. Here we can have 2 inputs: the number of rows and the number of columns.
# The first sample given is for rows value as 4 and the column as 7.
# In the second sample, it's 3 and 5 respectively.


def print_hexagonal_grid(rows, columns):
    for i in range((2*rows)+1):
        n_cols = (columns + 1) // 2 if i % 2 == 0 else (columns-1) // 2 
        for j in range(n_cols ):
            if i % 2 == 0 and i != 0 :
                print("\\___/   ", end="")
            if i% 2 == 0 and i == 0 :
                print(" ___    ", end="")
            
        for j in range(n_cols+1 ):
                
            if i % 2 != 0  and j != n_cols:

                print("/   \\___", end="")
            if i % 2 != 0  and j == n_cols:
                print("/   \\", end="")

            
        print()


print("Grid pattern with inputs(rows and columns) as: 4 and 7")
print_hexagonal_grid(4, 7)
print()
print("Grid with inputs(rows and columns) as: 3 and 5")
print_hexagonal_grid(3, 5)
