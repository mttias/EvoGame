import random

class Character:
    # initialize values (assign them to a byte/activate them)
    def __init__(self):
        self.id = random.randint(1,100000)
        self.value = random.randint(10,20)
        self.attributes = []
        self.newAttribute()
    def getId(self):
        return self.id
    def getValue(self):
        return self.value
    def getAttributes(self):
        for x in range(len(self.attributes)):
            return str(self.attributes[x])
    # adds an attribute
    def newAttribute(self):
        with open("words_alpha.txt", "r") as myfile:
            # read the line
            lines = myfile.readlines() 

            # pick a random variable
            rand = random.randint(0,len(lines))

            # add the attribute from lines[random-index]
            self.attributes.append(lines[rand])

# how many new characters to animate
charAmount = 30

# init characters
x = [Character() for _ in range(charAmount)]

# characters
with open("charactersgen1.txt", "a") as myfile:
    for a in range(charAmount):
        myfile.write("ID: " + str(x[a].getId()) + "\n")
        myfile.write("Strength: " + str(x[a].getValue()) + "\n")
        myfile.write("Name: " + x[a].getAttributes())
        myfile.write("\n" + "\n")


# evolutionary algorithm
# generations: two characters can interbreed and create a third character
# each generation: totalCharacters / 2 get created
# totalCharacters / 3 get culled each generation
#   (following a probabilistic distribution driving certain traits. ie "strength")

