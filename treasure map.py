line1= [" ", " ", " "]
line2= [" ", " ", " "]
line3= [" ", " ", " "]

grid= [line1, line2, line3]

print("mark your treasure with an X")

position = input( "input a letter a-c and a number 1-3: ")
letter = position[0].lower()
abc= ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
grid[number_index][letter_index] = "X"

print(line1, "\n", line2, "\n", line3)


