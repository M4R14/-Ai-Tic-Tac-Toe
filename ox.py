import json
import numpy as np
from texttable import Texttable

class ox:
    board = { 1:'_', 2:'_', 3:'_',
              4:'_', 5:'_', 6:'_',
              7:'_', 8:'_', 9:'_'}

    backBoard = { 1:'_', 2:'_', 3:'_',
                  4:'_', 5:'_', 6:'_',
                  7:'_', 8:'_', 9:'_'}

    weight = { 1:3, 2:3, 3:3, 4:3, 5:4, 6:3, 7:3, 8:3, 9:3}

    score = [{'index':[1,2,3], 'line':[1,2,3], 'score':0},
             {'index':[4,5,6], 'line':[4,5,6], 'score':0},
             {'index':[7,8,9], 'line':[7,8,9], 'score':0},
             {'index':[1,4,7], 'line':[1,4,7], 'score':0},
             {'index':[2,5,8], 'line':[2,5,8], 'score':0},
             {'index':[3,6,9], 'line':[3,6,9], 'score':0},
             {'index':[1,5,9], 'line':[1,5,9], 'score':0},
             {'index':[7,5,3], 'line':[7,5,3], 'score':0}]

    def add(self, index, data):
        if self.board[index] == '_':
            self.board[index] = data

        if data == 'X':
            data = 1
        elif data == 'O':
            data = -1

        if self.backBoard[index] == '_':
            self.backBoard[index] = data

        self.printBoard()
        if self.updateScore():
            print(self.updateScore(), 'Win!!')
            exit()

    def printScore(self):
        self.updateScore()

        t = Texttable()
        rows = []
        rows.append(['line', 'index','score'])
        for score in self.score:
            rows.append([ score['line'], score['index'],score['score'] ])

        t.add_rows(rows)
        print(t.draw())

    def updateScore(self):
        for score in self.score:
            score['score'] = 0;
            for index in score['line']:
                if not self.backBoard[index] == '_':
                    for scoreIndex in score['index']:
                        if scoreIndex == index:
                            score['index'].remove(index)
                    score['score'] = score['score'] + self.backBoard[index]
                    if score['score'] == 3:
                        return 'X'
                    if score['score'] == -3:
                        return 'O'

    def updateWeigth(self):
        for wei in self.weight:
            self.weight[wei] = 0;

        for score in self.score:
            for index in score['index']:
                self.weight[index] = self.weight[index] + 1


    def printWeight(self):
        self.updateWeigth()

        t = Texttable()
        t.add_rows([['index',1, 2,3,4,5,6,7,8,9],
                    ['weight',self.weight[1],self.weight[2],self.weight[3],
                    self.weight[4],self.weight[5],self.weight[6],
                    self.weight[7],self.weight[8],self.weight[9]]
                    ])

        print(t.draw())

    def NextIndex(self):
        MaxScore = 0;
        lineMaxScore = [];
        NextIndex = 0;
        text = '';
        for score in self.score:
            for scoreIndex in score['index']:
                if abs(score['score'])*self.weight[scoreIndex] > MaxScore and score['score'] > -100:
                        MaxScore = abs(score['score'])*self.weight[scoreIndex]
                        lineMaxScore = score;
                        NextIndex = scoreIndex;
                        text = text + "\n scoreIndex = "+ str(scoreIndex) + ", score = " + str(score['score']) + ", weight=" + str(self.weight[scoreIndex]) + ", abs(score)*weight =" + str(abs(score['score'])*self.weight[scoreIndex]);
        return NextIndex, text

    def printBoard(self):
        t = Texttable()
        t.add_rows([['','1', '2', '3'],
                    ['0', self.board[1], self.board[2], self.board[3]],
                    ['3', self.board[4], self.board[5], self.board[6]],
                    ['6', self.board[7], self.board[8], self.board[9]]])

        print(t.draw())
        print('\n')

if __name__ == '__main__':
    # main()
    test = ox()
    test.printBoard()
    pos = 0;
    while not pos == 10:
         pos = int(input('O:'))
         if pos > 0 and pos < 10:
             test.add(pos,'O')
             test.printScore()
             test.printWeight()
             index, text = test.NextIndex();
             print(text)
             print('Next X: ',index)
             print('---------------------------------------------------------')
             if(test.NextIndex() == 0):
                 exit()
             test.add(index,'X')

    """
    test.add(2,'O')
    test.printScore()
    test.printWeight()

    test.add(test.NextIndex(),'X')
    test.printScore()
    test.printWeight()

    test.add(test.NextIndex(),'O')
    test.printScore()
    test.printWeight()

    test.add(test.NextIndex(),'X')
    test.printScore()
    test.printWeight()

    test.add(test.NextIndex(),'O')
    test.printScore()
    test.printWeight()

    test.add(test.NextIndex(),'X')
    test.printScore()
    test.printWeight()
    
    test.add(test.NextIndex(),'O')
    test.printScore()
    test.printWeight()
    
    test.add(test.NextIndex(),'X')
    test.printScore()
    test.printWeight()
    """
