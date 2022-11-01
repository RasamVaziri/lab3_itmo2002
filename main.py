import math


SurvivalTools = {'В': (3, 25),
             'П': (2, 15),
             'Б': (2, 15),
             "А": (2, 20),
             "И": (1, 5),
             "Н": (1, 15),
             "Т": (3, 20),
             "О": (1, 25),
             "Ф": (1, 15),
             "Д": (1, 10),
             "Е": (2, 20),
                 "Р": (2, 20)
                 }

backpack= [3 * 3, 10, 0]
taken = []
best = []
riri = [0]


for i in SurvivalTools:
    backpack[1] -= SurvivalTools[i][1]


def Select(index):
    taken.append(index)
    backpack[0] -= SurvivalTools[index][0]
    backpack[1] += 2 * SurvivalTools[index][1]


def Delete(index):
    taken.remove(index)
    backpack[0] += SurvivalTools[index][0]
    backpack[1] -= 2 * SurvivalTools[index][1]

def Count():
    if backpack[0] > 0:
        for index in SurvivalTools:
            if (index not in taken) and (backpack[0] - SurvivalTools[index][0] >= 0):
                Select(index)
                Count()
                Delete(index)
    else:
        riri[0] += 1
        if backpack[1] > backpack[2]:
            backpack[2] = backpack[1]
            del best[:]
            for i in taken:
                best.append(i)




Count()


print( 'Итоговые очки выживания:'+ str(backpack[2]) + '\n')


finalthings = [[0 for x in range(3)] for y in range(3)]
best1 = []

for a in best:
    for i in range(SurvivalTools[a][0]):
        best1.append(a)

for a in range(len(best1)):
    finalthings[math.floor(a / 3)][a - 3 * math.floor(a / 3)] = best1[a]

for y in range(len(finalthings)):
    for x in range(len(finalthings[y])):
        print(' [' + finalthings[y][x] + '] ', end='')
    print()
