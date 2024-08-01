# Tower of Hanoi Puzzle

# Step 1

# In this project, you will solve the mathematical puzzle known as the Tower of Hanoi. 
# The puzzle consists of three rods and a number of disks of different diameters.

# The goal of this puzzle is moving the disks from the first rod to the third rod, following specific 
# rules that restrict placing a larger disk on top of a smaller one.

# Start by creating an empty dictionary named rods to represent the rods.

rods = {}

# Step 2

# The rods dictionary will represent the three rods with their disks. 
# Give it the strings 'A', 'B', and 'C' as keys and set each of them to an empty list.

rods = {'A': [], 'B': [], 'C': []}

# Step 3

# The puzzle starts with the disks piled up on the first rod, in decreasing size. 
# You need to populate your first list with numbers representing the various disk sizes.

# Instead of adding the items manually to the first list, generate a sequence of numbers from 3 to 1 
# by using the range() function and assign it to rods['A'].

# The syntax is range(x, y, h), where x is the starting integer (inclusive), y is the last integer (not inclusive), 
# and h is the difference between a number and the next one in the sequence.

rods = {
    'A': range(3,0,-1),
    'B': [],
    'C': []
}

# Step 4

# Now check the data type of your 'A' key by passing it to the type() function and print the result on the terminal.

print(type(rods['A']))





