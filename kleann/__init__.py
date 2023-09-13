

class member():
    def __init__(self,moni =0):
        self.money = moni
    
    def get_money(self):
        return self.money
    
    def reduce_money(self,moni:int):
        if moni > self.money:
            return False
        else:
            self.money = self.money - moni
            return True

    def add_money(self,moni:int):
        self.money += moni
        