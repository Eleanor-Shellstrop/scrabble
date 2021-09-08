letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# We have provided you with two lists, letters and points. 
# We would like to combine these two into a dictionary 
# that would map a letter to its point value.
# Using a list comprehension and zip, 
# create a dictionary called letter_to_points 
# that has the elements of letters as the keys 
# and the elements of points as the values.

letter_to_points = {
    key: value
    for key, value
    in zip(letters, points)
}

print(letter_to_points)