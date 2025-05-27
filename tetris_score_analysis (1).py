#Eva D.
#P1. 02/05/25
#Tetris Score Analysis


"""Rules
DO NOT use built-in functions like max(), min(), or sum().
ONLY use loops, variables, and if statements  to find the values."""

# List of Tetris scores (unsorted)
scores = [
    3600460, 1388900, 5435960, 4222920, 8063900, 1362703, 6529560, 2043580, 1390000, 1696224,
    1372600, 2535840, 2605320, 2275996, 11966100, 1472600, 1390780, 1768400, 1333731, 1317580,
    1777456, 4899280, 2790920, 1626880, 1476400, 29486164, 4570640, 1649100, 4890220, 6492500,
    1614120, 5157860, 1582980, 1357480, 2382340, 1532660, 2378832, 1316520, 2529080, 13793540,
    1386260, 1352620, 1442340, 1406260, 1705680, 12409180, 2281848, 3222400, 1349060, 2302480,
    1571120, 3067100, 3740500, 1606732, 2153480, 2011360, 1344740, 1371060, 1345420, 2373940,
    1702940, 2077552, 2108820, 1322485, 1404800, 2555620, 1405580, 4213540, 3835120, 6563440,
    1350742, 1537800, 1657560, 1333995, 1632505, 2743060, 1509751, 1554880, 1316540, 1323680,
    2433160, 1340460, 1659860, 1608500, 7220241, 1834120, 7081880, 1483360, 16700760, 1435280,
    1702640, 1371040, 1316900, 2114180, 1374100, 1412260, 1379220, 1319573, 1623160, 6787420
]

#functions

def highScore():
    global scores
    highestScore = 0
    for number in scores:
        if number > highestScore:
            highestScore = number
    print("\nHighest Score:", highestScore)
    return highScore

def lowestScore():
    lowestScore = scores[0]
    for score in scores:
        if score < lowestScore:
            lowestScore = score
    print("\nLowest Score:", lowestScore)
    return lowestScore

def averageScore():
    total = 0
    for score in scores:
        total += score
    avg = total / len(scores)
    print("\nAverage Score:", avg)


""" Create a function that allows the user to input a score.
If the score is greater than the lowest score on the tetris score list,
remove the lowest score and the new score will be added to the list.
Reject any scores that are not in the top 100 scores."""

def inputScore():
    new_score = int(input("Please enter a new Tetris score: "))  # Get the user's input
    lowest = lowestScore()  #current lowest score

    if new_score > lowest():
        scores.remove(lowest)  #Remove lowest score
        scores.append(new_score)  #Add new score
        print("\nNew score", new_score, "added, replacing", lowest,".")
    else:
        print("\nScore too low to enter the top 100.")


def tetrisMenu():
    while True:
        print("\nWelcome to Tetris Analyzer!")
        print("""\nMenu
              1. Check Highscore
              2. Check Lowest Score
              3. Check Average Score
              4. Input New Score
              5. Exit
        """)
        choice = input("Please select an option(1-5): ")
        if choice == '1':
            highScore()

        elif choice == '2':
            lowestScore()

        elif choice == '3':
            averageScore()

        elif choice == '4':
            inputScore()

        elif choice == '5':
            print("Exiting Tetris Analyzer. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a valid option between 1 and 5.")


#main
tetrisMenu()
