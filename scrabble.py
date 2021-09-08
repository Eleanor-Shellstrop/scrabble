letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {
    key: value
    for key, value
    in zip(letters, points)
}

letter_to_points[" "] = 0

# We want to create a function that will 
# take in a word and return how many points 
# that word is worth. 
# Define a function called score_word that 
# takes in a parameter word. 
# Inside score_word, create a variable 
# called point_total and set it to 0.

def score_word(word):
    point_total = 0