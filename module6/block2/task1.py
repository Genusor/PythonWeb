class NutritionInfo:
    def __init__(self, proteins, carbs, fats):
        self.proteins = proteins
        self.carbs = carbs
        self.fats = fats
        self.energy()           
    def energy(self):
        return int(self.fats * 9 + (self.carbs + self.proteins) * 4.2)
    
    def __add__(self, other):
        s = NutritionInfo(0,0,0)
        s.proteins = self.proteins + other.proteins
        s.carbs = self.carbs + other.carbs
        s.fats = self.fats + other.fats
        return s
 
tvorog_9 = NutritionInfo(18, 3, 9)
apple = NutritionInfo(0, 25, 0)

breakfast = apple + tvorog_9

print(breakfast.energy())