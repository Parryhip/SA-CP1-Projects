#Samuel Andelin, Counting Characters
grid = [
['A', 'B', 'C', 'A', 'D'],
['C', 'A', 'B', 'D', 'E'],
['A', 'D', 'C', 'E', 'A'],
['B', 'A', 'C', 'A', 'D'],
['D', 'C', 'B', 'E', 'A'] ]
a_count = 0
b_count = 0
c_count = 0
d_count = 0
e_count = 0
for list in grid:
    for i in list:
        if i == "A":
            a_count += 1
        elif i == "B":
            b_count += 1
        elif i == "C":
            c_count += 1
        elif i == "D":
            d_count += 1
        elif i == "E":
            e_count += 1
print("The number of 'A's in the grid is "+str(a_count))
print("The number of 'B's in the grid is "+str(b_count))
print("The number of 'C's in the grid is "+str(c_count))
print("The number of 'D's in the grid is "+str(d_count))
print("The number of 'E's in the grid is "+str(e_count))
