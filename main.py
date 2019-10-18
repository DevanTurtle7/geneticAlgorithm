#Devan Kavalchek
#Genetic Algorithm
#2019

import matplotlib.pyplot as plt
import numpy as np
from random import randint
from random import shuffle
import math

class city:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class offspring:
    def __init__(self, genome):
        self.genome = genome
        self.fitness = 0

    def getDistance(self):
        distance = 0

        for i in range(0, len(self.genome)):
            if i is not 0:
                x1 = self.genome[i-1].x
                y1 = self.genome[i-1].y
                x2 = self.genome[i].x
                y2 = self.genome[i].y
            else:
                x1 = self.genome[len(self.genome)-1].x
                y1 = self.genome[len(self.genome)-1].y
                x2 = self.genome[i].x
                y2 = self.genome[i].y

            #pythag theorem
            distance += (((x2-x1) ** 2) + ((y2-y1) ** 2)) ** .5
        
        return distance

    def printGenome(self):
        printString = '['
        for i in range(0, len(self.genome)):
            if self.genome[i] is not None:
                printString += '(' + str(self.genome[i].x) + ', ' + str(self.genome[i].y) + ')' + ', '
            else:
                printString += 'None, '
        
        printString = printString + ']'

        print(printString)

class generation:
    def __init__(self, children):
        self.children = children
        self.children.sort(key = lambda x: x.getDistance())

    def getAverage(self):
        average = 0
        for i in range(0, len(self.children)):
             average += self.children[i].getDistance()

        return average / len(self.children)
    
    def newGeneration(self):
        parents = []
        nextGeneration = []
        for i in range(0, len(self.children)):
            self.children[i].fitness = 100-i #Backwards: round(100 * ((i+1)/len(self.children)))
            print(str(self.children[i].fitness) + ', ' + str(self.children[i].getDistance()))

        print('--------------------------------------------')

        percentTable = []
        for i in range(0, len(self.children)):
            weightedPercent =  abs(2500 * (self.children[i].fitness - 50))
            weightedPercent **= (1/3)
            if self.children[i].fitness < 50:
                weightedPercent = -weightedPercent
            weightedPercent += 50
            weightedPercent = round(weightedPercent)

            percentTable += [self.children[i]] * weightedPercent

        shuffle(percentTable)

        for i in range(0, math.floor(len(self.children)/2)):
            randNum = randint(0, len(percentTable)-1)
            parents.append(percentTable[randNum])
            percentTable = list(filter((percentTable[randNum]).__ne__, percentTable)) #removes all elements of chosen

        shuffle(parents)
        sub = len(parents) % 2

        
        for i in range(0, len(parents)):
            for i in range(0, 2):
                nextGeneration.append(breed(parents[i], parents[randint(0, len(parents)-1)]))

        return generation(nextGeneration)
        
def breed(p1,p2):
    startIndex = randint(0, len(p1.genome)-1)
    endIndex = startIndex + math.floor(len(p1.genome) / 2)
    cGenome = [None] * len(p1.genome)

    if endIndex > len(p1.genome):
        endIndex = math.floor(len(p1.genome) / 2) - (len(p1.genome) - startIndex)

    if endIndex < startIndex:
        #print('it overflows')
        i = startIndex
        satisfied = False
        while not satisfied:
            #print(i)
            cGenome[i] = p1.genome[i]

            i += 1
            
            if i == endIndex:
                satisfied = True

            if i >= len(p1.genome):
                i = 0
    else:
        for i in range(startIndex, endIndex):
            cGenome[i] = p1.genome[i]
            #print('placing ' + str(i))
        
    k = endIndex #index pointer in p2
    x = endIndex #index pointed in c

    satisfied = False
    while not satisfied:
        if x == len(p2.genome):
            x = 0
        
        if x == startIndex:
            satisfied = True
        else:
            if k < len(p2.genome) and p2.genome[k] not in cGenome:
                cGenome[x] = p2.genome[k]
                #print(str(cGenome[i].x) + ', ' + str(cGenome[i].y))

                if x-1 >= len(cGenome):
                    x = 0
                else:
                    x+=1
            else:
                validK = False
                while not validK:
                    #print(x)
                    k += 1
                    if k >= len(p2.genome):
                        k = 0
                    
                    if p2.genome[k] not in cGenome:
                        validK = True
    
    mutationChance = randint(0, 100)

    if mutationChance <= 1:
        pos1 = randint(0, len(cGenome)-1)
        pos2 = randint(0, len(cGenome)-1)

        tempVal1 = cGenome[pos1]
        tempVal2 = cGenome[pos2]

        cGenome[pos1] = tempVal2
        cGenome[pos2] = tempVal1

    #print('done')
    return offspring(cGenome)

maxData = []
avgData = []
minData = []
countData = []

def simulate(generation, step, maxStep):
    maxData.append(generation.children[0].getDistance())
    avgData.append(generation.getAverage())
    minData.append(generation.children[len(generation.children) - 1].getDistance())

    genomeCopies = []
    
    for i in range(0, len(generation.children)):
        if not genomeCopies.__contains__(generation.children[i].genome):
            genomeCopies.append(generation.children[i].genome)

    countData.append(len(genomeCopies))

    if step <= maxStep:
        simulate(generation.newGeneration(), step + 1, maxStep)
    
    return generation

#Initial Generation
generationList = []
referenceCities = []

circleX = []
circleY = []

for i in range(0, round(20 * math.pi)):
    referenceCities.append(city(math.cos(i), math.sin(i)))
    circleX.append(math.cos(i/10))
    circleY.append(math.sin(i/10))

#plt.scatter(circleX, circleY)
#plt.show()

for i in range(0, 100):
    satisfied = False
    while not satisfied:
        randGenome = referenceCities.copy()
        shuffle(randGenome)
        if randGenome not in generationList:
            satisfied = True

    generationList.append(offspring(randGenome))

myGeneration = generation(generationList)
myGeneration.newGeneration()

myGen = simulate(myGeneration, 1, 300)

plt.scatter(range(0, len(maxData)), maxData, color = 'blue', alpha = .5, label='Shortest Distance')
plt.scatter(range(0, len(avgData)), avgData, color = 'red', alpha = .5, label='Average Distance')
plt.scatter(range(0, len(minData)), minData, color = 'green', alpha = .5, label='Longest Distance')
plt.scatter(range(0, len(countData)), countData, color = 'orange', alpha = .5, label='Number of Unique Genomes')

#plt.plot(genXs, genYs)
plt.grid()
plt.xlabel('Generation')
plt.ylabel('Length')
plt.legend()
plt.show()

#xVals = []
#yVals = []
#for i in range(0, len(myGen.children[0].genome)):
    #xVals.append(myGen.children[0].genome[i].x)
    #yVals.append(myGen.children[0].genome[i].y)

#plt.plot(xVals, yVals)
#plt.show()
















# Prepare the data
#x = [0, 1, 2, 3, 4, 5, 6]
#y = [22, 10, 15, 16, 20, 26, 23]

#for i in range(50):
#    plt.scatter(x,y)
#    plt.pause(0.0001)
#    plt.grid()
#    plt.xlabel('Generation')
#    plt.ylabel('Length')
#    x.append(i)
#    y.append(1)
#    #print(i)
#    
#    plt.draw()
#    if i < 50-1:
#        plt.clf()
#plt.show()