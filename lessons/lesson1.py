class Hero:

    def __init__(self, name, lvl, hp):
        self.hero_name = name
        self.hero_lvl = lvl
        self.hero_hp = hp

    def action(self):
        print(self.hero_name," attacks" )


    def show(self):
        print(self.hero_name,self.hero_lvl,self.hero_hp)

kirito = Hero("Kirito", 100,1000)

kirito.show()
