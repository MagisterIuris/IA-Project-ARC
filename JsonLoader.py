import json
import matplotlib.pyplot as plt
from random import randrange

indexTab = []
index = open('data/indexTab2.txt','r').readlines()
for i in index:
    indexTab.append(i.replace('\n',''))

def openJsonFile():
    f = open('data/training/' + indexTab[randrange(len(indexTab))] + '.json','r')
    data = json.loads(f.read())

    grillestrain = []
    grillestest = []
    grillestest.append(data['test'][0]['input'])
    grillestest.append(data['test'][0]['output'])

    for i in range(0,len(data['train'][0])):
        grillestrain.append(data['train'][i])

    return (grillestrain,grillestest)

#grides est la grid de resultat du système
def draw(grillestrain,grillestest,gridres):
    grilleInput = []
    grilleOutput = []

    for i in range(0,len(grillestrain)):
        grilleInput.append(grillestrain[i]['input'])
        grilleOutput.append(grillestrain[i]['output'])
    
    row = len(grillestrain)
    col = 4
    fig = plt.figure(figsize=(6, 6))
    cpt = 1

    for i in range(0,row):
        fig.add_subplot(row, col, cpt)
        plt.title("Train Input "+str(i))
        plt.axis('off')
        plt.imshow(grilleInput[i])
        cpt = cpt + 1
        fig.add_subplot(row, col, cpt)
        plt.title("Train Output "+str(i))
        plt.axis('off')
        plt.imshow(grilleOutput[i])
        cpt = cpt + 1
    
    fig.add_subplot(2,2,3)
    plt.title("Test Input")
    plt.axis('off')
    plt.imshow(grillestest[0])
    fig.add_subplot(2,2,4)
    plt.title("Test Output")
    plt.axis('off')
    plt.imshow(grillestest[1])
    gridres.displayGrid()
    plt.show()

#gridres = 0
#grillestrain,grillestest = openJsonFile()
#draw(grillestrain,grillestest,gridres)
