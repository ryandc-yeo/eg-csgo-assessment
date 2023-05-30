import pandas as pd

class ProcessGameState:
    def __init__(self, file_path, z_bounds, bounds):
        self.file_path = file_path
        self.boundary = bounds
        self.z_bounds = z_bounds
        self.__extract_data(file_path)
    

    def __extract_data(self, file_path):
        try:
            self.data = pd.read_pickle(file_path)
            x = [i[0] for i in self.boundary]
            y = [i[1] for i in self.boundary]
            self.x_bounds = (min(x), max(x))
            self.y_bounds = (min(y), max(y))
        except:
            self.data = None
            print(f"error: incorrect file path")

    def check_boundary(self):
        self.valid_rows = {}
        for index, row in self.data.iterrows():
            x, y, z = row['x'], row['y'], row['z']

            if self.x_bounds[0] <= x <= self.x_bounds[1] and self.y_bounds[0] <= y <= self.y_bounds[1] and self.z_bounds[0] <= z <= self.z_bounds[1]:
                self.valid_rows[index] = True
            else:
                self.valid_rows[index] = False
        return self.valid_rows
    
    def extract_weapons(self):
        self.weapons = {}
        for inv in self.data.inventory:
            if inv is not None:
                weapon_class = inv[0].get('weapon_class')
                weapon_name = inv[0].get('weapon_name')
                if self.weapons.get(weapon_class):
                    self.weapons[weapon_class].add(weapon_name)
                else:
                    self.weapons[weapon_class] = {weapon_name}
        return self.weapons




'''
# data = pd.read_pickle('game_state_frame_data.pickle')
# print(data.round_num)

# constants
Z_BOUNDS = [285, 421]
BOUNDS =  [[-1735, 250],[-2024, 398],[-2806, 742],[-2472, 1233], [-1565, 580]]

# example usage            
c = ProcessGameState('game_state_frame_data.pickle', Z_BOUNDS, BOUNDS)
c.extract_weapons()
'''