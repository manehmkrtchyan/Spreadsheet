from color import Color
from datetime import datetime
import abc

class Cell(abc.ABC):
    def __init__(self, value, color):
        self.color = color
        self.value = value
        
    def __repr__(self) -> str:
        return str(((self.value), self.color))
    
    @abc.abstractmethod
    def set_value(self):
        pass
    
    def get_value(self):
        return self.value 

    def setColor(self, color: 'Color'):
        self.color = color

    def getColor(self):
        return self.color.name
    
    def get_string_value(self):
        return str(self.value)

    def to_date(self):
        form = '%Y-%m-%d'
        dateObj = datetime.datetime.strptime(self.value, form)
        return dateObj
    
    @abc.abstractmethod
    def reset(self):
        pass
        
        
class IntCell(Cell):
    def __init__(self, value=0, color=Color('White')):
        if isinstance(value, int):
            super().__init__(value, color)
        else:
            raise TypeError('You are creating IntCell')
        
    def set_value(self, value):
        if isinstance(value, int):
            self.value = value
    
    def reset(self):
        if self.value == 0 and self.color.name == 'White':
            return 'The cell is already reseted.'
        answer = input('Are you sure you want to reset the cell? Press Y or N')
        if answer == 'Y':
            self.value = 0
            self.color.name = 'White'
        elif answer == 'N':
            return 'Nothing is changed'

class StrCell(Cell):
    def __init__(self, value=' ', color=Color('White')):
        if isinstance(value, str):
            super().__init__(value, color)
        else:
            raise TypeError('You are creating StrCell')
        
    def set_value(self,value):
        if isinstance(value,str):
            self.value = value
        else:
            raise TypeError('you are a bad girl')
    
    def reset(self):
        if self.value == ' ' and self.color.name == 'White':
            return 'The cell is already reseted.'
        answer = input('Are you sure you want to reset the cell? Press Y or N')
        if answer == 'Y':
            self.value = ' '
            self.color.name = 'White'
        elif answer == 'N':
            return 'Nothing is changed'
        
class FloatCell(Cell):
    def __init__(self, value=0.0, color=Color('White')):
        if isinstance(value, float):
            super().__init__(value, color)
        else:
            raise TypeError('You are creating FloatCell')
        
    def set_value(self,value):
        if isinstance(value, float):
            self.value = value
        else:
            raise TypeError('you are creating FloatCell')
    
    def reset(self):
        if self.value == 0.0 and self.color.name == 'White':
            return 'The cell is already reseted.'
        answer = input('Are you sure you want to reset the cell? Press Y or N')
        if answer == 'Y':
            self.value = 0.0
            self.color.name = 'White'
        elif answer == 'N':
            return 'Nothing is changed'
        
        
class DateCell(Cell):
    def __init__(self, value='00-00-00', color=Color('White')):
        try: 
            value = datetime.strptime(str(value), '%Y-%m-%d')
            super().__init__(value, color)
        except ValueError:
            raise TypeError('you are creating DateCell')
        
    def set_value(self,value):
        try: 
            value = datetime.strptime(value, '%Y-%m-%d')
            self.value = value
        except ValueError:
            raise TypeError('you are creating DateCell')
    
    def reset(self):
        if self.value == 00-00-00 and self.color.name == 'White':
            return 'The cell is already reseted.'
        answer = input('Are you sure you want to reset the cell? Press Y or N')
        if answer == 'Y':
            self.value = 00-00-00
            self.color.name = 'White'
        elif answer == 'N':
            return 'Nothing is changed'
        
        

