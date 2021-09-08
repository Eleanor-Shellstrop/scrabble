letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {
    key: value
    for key, value
    in zip(letters, points)
}

letter_to_points[" "] = 0


def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total   

# Let’s test this function! 
# Create a variable called brownie_points 
# and set it equal to the value 
# returned by the score_word() function 
# with an input of "BROWNIE"

brownie_points = score_word("BROWNIE")
print(brownie_points)   #Prints 15