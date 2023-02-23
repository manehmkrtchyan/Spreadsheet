class Color:
    def __init__(self, color_name) -> None:
        self.di = {
            'Violet': 'EE82EE',
            'LightBlue': 'ADD8E6',	
            'Blue': '0000FF',
            'Purple': '800080',
            'Grey': '808080',
            'Yellow': 'FFFF00',
            'Orange': 'FFA500',
            'White': 'FFFFFF',
            'Pink':	'FFC0CB',
            'Chocolate': 'D2691E',
            'Black': '000000'
        }
        self.name = self.di[color_name]
        
    def __repr__(self) -> str:
        return self.name
        
        