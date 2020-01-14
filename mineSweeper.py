class MineSweeper():

    def __init__(self):
        self.field = []
        self.fieldToPrint = []
        self.stat = GameStatus.PLAYING

    def createField(self,rows,columns):
        for i in range(rows):
            row = []
            rowForFieldToPrint = []
            for j in range(columns):
                row.append('.')
                rowForFieldToPrint.append('.')
            self.fieldToPrint.append(rowForFieldToPrint)
            self.field.append(row)

    def layMine(self,row,col):
        self.field[row][col] = '*'

    def printField(self):
        toPrint=''
        for row in self.fieldToPrint:
            toPrint+='"'
            for col in row:
                toPrint+=col+' '
            toPrint= toPrint[:-1]+'"\n'
        toPrint= toPrint[:-1]
        print(toPrint)

    def minesAroundMe(self,location):
        if self.field[location[0]][location[1]] == '*':
            return '*'

        mines = 0
        for i in range(location[0]-1,location[0]+2):
            for j in range(location[1]-1,location[1]+2):
                try:
                    if self.inRange((i,j)):
                        if self.field[i][j] == '*':
                            mines +=1
                except:
                    pass
        if mines == 0 :
            return '+'
        return str(mines)

    def inRange(self,location):
        if location[0] >=0 and location[1] >= 0:
            if location[0] < len(self.field) and location[1] < len(self.field[0]):
                    return True

        return False

    def inRangeAndUntouched(self,location):
        if location[0] >=0 and location[1] >= 0:
            if location[0] < len(self.field) and location[1] < len(self.field[0]):
                if self.fieldToPrint[location[0]][location[1]] == '.':
                    return True

        return False


    def FloodFill (self ,row,col):
        location = (row,col)
        Q=[]
        Q.append(location)
        while len(Q)!= 0:
            current = Q.pop(0)
            minesAroundCurrent = self.minesAroundMe(current)
            self.fieldToPrint[current[0]][current[1]] = minesAroundCurrent
            if minesAroundCurrent != '+':
                continue

            west = (current[0],(current[1]-1))
            east = (current[0],(current[1]+1))
            north = ((current[0]+1),current[1])
            south = ((current[0]-1),current[1])

            if self.inRangeAndUntouched(west):
                Q.append(west)
            if self.inRangeAndUntouched(east):
                Q.append(east)
            if self.inRangeAndUntouched(north):
                Q.append(north)
            if self.inRangeAndUntouched(south):
                Q.append(south)
        return




    def checkWin(self):
        for i in range(0,len(self.field)):
            for j in range(0,len(self.field[0])):
                if self.fieldToPrint[i][j] == '.' and self.field[i][j] != '*':
                    return False
        for i in range(0, len(self.field)):
            for j in range(0, len(self.field[0])):
                if self.fieldToPrint[i][j] == '.':
                    self.fieldToPrint[i][j] = '*'

        return True

    def play(self,row,col):
        self.fieldToPrint[row][col] = self.field[row][col]
        if self.field[row][col] == '*':
            self.stat = GameStatus.LOST
            return
        self.FloodFill(row,col)
        if self.checkWin():
            self.stat = GameStatus.WIN


    def status(self):
        return self.stat




class GameStatus():
    LOST = "LOST"
    WIN = "WIN"
    PLAYING = "PLAYING"
