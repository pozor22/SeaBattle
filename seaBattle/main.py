import random
import time

class map():
    # 0 - пустое поле 1 - стоит корабль(виден только на своей карте) 2 - выстрелел, но не попал 3 - выстрелел и пострелил корабль

    LibraryLetter = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "К"]
    LibraryNumber = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    def __init__(self, mapInput1, mapInput2):
        self.mapWe = mapInput1
        self.mapHidden = mapInput2

    def PutShipOnYourMap(self):
        ship = 10
        while ship != 0:
            PutShip = str(input("Куда поставить корабль: "))
            if len(PutShip) == 2:
                flagLetter = False
                flagNumber = False
                for i in map.LibraryLetter:
                    if PutShip[0].upper() == i:
                        flagLetter = True
                        break
                for i in map.LibraryNumber:
                    if PutShip[1] == i:
                        flagNumber = True
                        break
                if flagLetter == True and flagNumber == True:
                    for i in self.mapWe:
                        if PutShip[0].upper() == i[0]:
                            if PutShip[1] == "0":
                                i[10] = "1"
                            else:
                                i[int(PutShip[1])] = "1"
                    ship -= 1
                    for i in self.mapWe:
                        print(i)
                else:
                    print("введите правильные координаты!")
            else:
                print("введите правильные координаты!")
        print("Корабли расставлены!")

    def PutShipOnEnemyMap(self):
        ship = 10
        while ship != 0:
            PutShip = random.choice(map.LibraryLetter) + random.choice(map.LibraryNumber)
            for i in self.mapWe:
                if PutShip[0].upper() == i[0]:
                    if PutShip[1] == "0":
                        i[10] = "1"
                    else:
                        i[int(PutShip[1])] = "1"
            ship -= 1
        print("Корабли противника расставлены!")
        for i in self.mapHidden:
            print(i)
        print("-----------------------------------------")
        for i in self.mapWe:
            print(i)

    def YourRound(self, mapenemy):
        TrueStepLetter = 0
        TrueStepNumber = 0
        while TrueStepLetter != 1 and TrueStepNumber != 1:
            step = str(input("Куда будем стрелять: "))
            if len(step) == 2:
                for i in map.LibraryLetter:
                    if step[0].upper() == i:
                        TrueStepLetter = 1
                        break
                for i in map.LibraryNumber:
                    if step[1] == i:
                        TrueStepNumber = 1
                        break
            if TrueStepLetter == 1 and TrueStepNumber == 1:
                for i in mapenemy:
                    if step[0].upper() == i[0]:
                        for j in self.mapHidden:
                            if step[0].upper() == j[0]:
                                if step[1] == "0":
                                    if i[10] == "0":
                                        i[10] = "2"
                                        j[10] = "2"
                                    elif i[10] == "1":
                                        i[10] = "3"
                                        j[10] = "3"
                                    elif i[10] == "2":
                                        i[10] = "2"
                                        j[10] = "2"
                                    elif i[10] == "3":
                                        i[10] = "3"
                                        j[10] = "3"
                                else:
                                    if i[int(step[1])] == "0":
                                        i[int(step[1])] = "2"
                                        j[int(step[1])] = "2"
                                    elif i[int(step[1])] == "1":
                                        i[int(step[1])] = "3"
                                        j[int(step[1])] = "3"
                                    elif i[int(step[1])] == "2":
                                        i[int(step[1])] = "2"
                                        j[int(step[1])] = "2"
                                    elif i[int(step[1])] == "3":
                                        i[int(step[1])] = "3"
                                        j[int(step[1])] = "3"
                for i in self.mapHidden:
                    print(i)
            else:
                if TrueStepLetter == 1 and TrueStepNumber == 0:
                    TrueStepLetter = 0
                elif TrueStepLetter == 0 and TrueStepNumber == 1:
                    TrueStepNumber = 0

    def EnemyRound(self, mapyour):
        print("Противник делает ход!")
        enemyStep = random.choice(map.LibraryLetter) + random.choice(map.LibraryNumber)
        for i in mapyour:
            if enemyStep[0].upper() == i[0]:
                if enemyStep[1] == "0":
                    if i[10] == "0":
                        i[10] = "2"
                    elif i[10] == "1":
                        i[10] = "3"
                    elif i[10] == "2":
                        i[10] = "2"
                    elif i[10] == "3":
                        i[10] = "3"
                else:
                    if i[int(enemyStep[1])] == "0":
                        i[int(enemyStep[1])] = "2"
                    elif i[int(enemyStep[1])] == "1":
                        i[int(enemyStep[1])] = "3"
                    elif i[int(enemyStep[1])] == "2":
                        i[int(enemyStep[1])] = "2"
                    elif [int(enemyStep[1])] == "3":
                        i[int(enemyStep[1])] = "3"
        for i in mapyour:
            print(i)

    def lose(self):
        flag = 0
        for i in self.mapWe:
            flag += i.count("1")
        if flag == 1:
            return True
        else:
            return False


class game():
    def Game(self):
        mapYour = map([["-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
            ["А", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["Б", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["В", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["Г", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["Д", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["Е", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["Ж", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["З", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["И", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["К", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]], [["-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
            ["А", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["Б", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["В", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["Г", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["Д", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["Е", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["Ж", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["З", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["И", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["К", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]])
        mapEnemy = map([["-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
            ["А", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["Б", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["В", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["Г", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["Д", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["Е", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["Ж", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["З", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["И", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["К", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]], [["-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
            ["А", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["Б", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["В", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["Г", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["Д", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["Е", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["Ж", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["З", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["И", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["К", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]])
        mapYour.PutShipOnYourMap()
        time.sleep(2)
        mapEnemy.PutShipOnEnemyMap()
        while True:
            time.sleep(2)
            mapYour.YourRound(mapEnemy.mapWe)
            time.sleep(2)
            if mapYour.lose() == True:
                print("Ты проиграл!!!")
                break
            elif mapEnemy.lose() == True:
                print("Ты выиграл!!!!!!!!!")
                break
            mapEnemy.EnemyRound(mapYour.mapWe)
            if mapYour.lose() == True:
                print("Ты проиграл!!!")
                break
            elif mapEnemy.lose() == True:
                print("Ты выиграл!!!!!!!!!")
                break


def main():
    game1 = game()
    game1.Game()


if __name__ == "__main__":
    main()
