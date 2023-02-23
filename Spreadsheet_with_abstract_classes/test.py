from cell import Cell
from spreadsheet import Spreadsheet
import spreadsheet as sp
import cell
from color import Color
import datetime
 
my_cell = Cell()
my_sp = Spreadsheet(4, 5)
co = Color('Pink')
    
def testCellsetValue(val=5):
    my_cell.setValue(val) 
    if my_cell.value == str(val):
        return "test passed successfully"
    return "test failed successfully"
    
def testCellsetColor(col=co):
    my_cell.setColor(col)
    if my_cell.color == col:
        return "test passed successfully"
    return "test failed successfully"

def testCellgetValue(cell=my_cell):
    if my_cell.value == str(my_cell.value):
        return "test passed successfully"
    return "test failed successfully"

def testCellgetColor(col=co):
    if my_cell.color.name == col.name:
        return "test passed successfully"
    return "test failed successfully"
    
def testCelltoInt(cell=my_cell):
    cell.toInt()
    if cell.value == int(cell.value):
        return "test passed successfully"
    return "test failed successfully"

def testCelltoFloat(cell=my_cell):
    cell.toFloat()
    if cell.value == float(cell.value):
        return "test passed successfully"
    return "test failed successfully"

def testCelltoDate(cell=my_cell):
    if cell.toDate() == datetime.datetime.strptime(cell.value, form:='%Y-%m-%d'):
        return "test passed successfully"
    return "test failed successfully"

def testCellreset(cell=my_cell):
    if cell.value == "" and cell.color == "White":
        if cell.reset() != 'The cell is already reseted.':
            return "test failed successfully"
    cell.reset()
    if cell.value == "" and cell.color == "White":
        return "test passed successfully"
    return "test failed successfully"

def testSpsetSellAt(val1=2, val2=3, cell=my_cell):
    my_sp.setSellAt(val1, val2, cell)
    if my_sp.spreadsheet[val1][val2] == cell:
        return "test passed successfully"
    return "test failed successfully"

def testSpgetCellAt(val1=3, val2=4):
    if my_sp.getCellValue == my_sp.spreadsheet[val1][val2]:
        return "test passed successfully"
    return "test failed successfully"

def testSpaddRow(idx=2, cell=co):
    if my_sp.speadsheet[idx + 1] == cell:
        return "test passed successfully"
    return "test failed successfully"

def testSpremoveRow(idx=3):
    pass

def testSpaddColumn(idx=4):
    if my_sp.speadsheet[idx + 1] == cell:
        return "test passed successfully"
    return "test failed successfully"

col = Color('Black')
print(testCellgetColor(col))
