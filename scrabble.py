letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {
    key: value
    for key, value
    in zip(letters, points)
}

# Our letters list did not take into account blank tiles. 
# Add an element to the letter_to_points dictionary 
# that has a key of " " and a point value of 0.

letter_to_points[" "] = 0

print(letter_to_points)