class MapLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.map_data = []
        self.pacman_pos = None
        self.food = set()
        self.magic_pies = set()
        self.width = None
        self.height = None

    def load(self):
        with open(self.file_path, 'r') as f:
            lines = f.readlines()
        for y, line in enumerate(lines):
            row = []
            for x, ch in enumerate(line.strip('\n')):
                row.append(ch)
                if ch == 'P':
                    self.pacman_pos = (x, y)
                elif ch == '.':
                    self.food.add((x, y))
                elif ch == 'O':
                    self.magic_pies.add((x, y))
            self.map_data.append(row)
        return self

    def getWidth(self):
        self.width = len(self.map_data[0])
        return self.width
    
    def getHeight(self):
        self.height = len(self.map_data)
        return self.height