from numpy import full
from cell import Cell
import numpy as np
import copy

class Spreadsheet:
    def __init__(self, row, col):
        #'''Better way'''
        #self.spreadsheet = [[Cell() for y in range(col)] for x in range(row)]
        self.spreadsheet = full((row, col), Cell())

    def setCellAt(self, row, col, cell):
        self.spreadsheet[row][col] = cell

    def getCellAt(self, row, col):
        return self.spreadsheet[row][col]
    
    def addRow(self, idx):
        a = np.array([Cell() for i in self.spreadsheet[0]])
        self.spreadsheet = np.insert(self.spreadsheet,idx , a, axis=0)
        
    def removeRow(self, idx):
        self.spreadsheet = np.delete(self.spreadsheet, idx, axis=0)
        
    def addColumn(self, idx):
        a = np.array([Cell() for i in self.spreadsheet])
        self.spreadsheet = np.insert(self.spreadsheet,idx , a, axis=1)
        
    def removeColumn(self, idx):
        self.spreadsheet = np.delete(self.spreadsheet, idx, axis=1)
    
    def swapRows(self, idx1, idx2):
        self.spreadsheet[idx1], self.spreadsheet[idx2] = copy.deepcopy(self.spreadsheet[idx2]), copy.deepcopy(self.spreadsheet[idx1])

    def swapColumn(self, idx1, idx2):
        for row in self.spreadsheet:
            row[idx1], row[idx2] = row[idx2], row[idx1]
            
cell = Cell('Hello')
sp = Spreadsheet(3, 4)
sp.setCellAt(2, 1, cell)
sp.swapRows(0, 2)
sp.swapColumn(1, 2)
print(sp.spreadsheet)