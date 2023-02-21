from color import Color
import datetime

class Cell:
    def __init__(self, value = " ", color = Color('White')):
        self.value = value
        self.color = color
        
    def __repr__(self) -> str:
        return str(((self.value), self.color))

    def setValue(self, value):
        self.value = value

    def setColor(self, color: 'Color'):
        self.color = color

    def getValue(self):
        return self.value 

    def getColor(self):
        return self.color.name 

    def toInt(self):
        self.value = int(self.value) 

    def toFloat(self):
        self.value = float(self.value)

    def toDate(self):
        form = '%Y-%m-%d'
        dateObj = datetime.datetime.strptime(self.value, form)
        return dateObj
    
    def reset(self):
        if self.value == '' and self.color.name == 'White':
            return 'The cell is already reseted.'
        answer = input('Are you sure you want to reset the cell? Press Y or N')
        if answer == 'Y':
            self.value = ''
            self.color.name = 'White'
        elif answer == 'N':
            return 
        else:
            return 'Nothing is changed'
        
