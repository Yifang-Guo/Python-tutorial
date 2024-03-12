from random import choice

capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the range"

def randomFunFact():
    funFacts = ["Kansas is considered flat", "A considerable portion of Kansas city", "Most Kansas are annoyed"]

    index = choice("012")

    print(funFacts[int(index)])

if __name__ == "__main__":
    randomFunFact()
