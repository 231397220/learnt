'''


'''



class Role (object):
    def __init__(self,name,role,weapon,life_value):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.lift_value = life_value
    def buy_weapon(self,weapon):
        print("%s 正在买%s枪" %(self.name,weapon) )
        self.weapon = weapon







p1 = Role('sam','p','b11',100)
p1.buy_weapon('b42')


print(p1.weapon)