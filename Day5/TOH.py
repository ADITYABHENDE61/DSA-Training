import time
class Tower:
    def __init__(self):
        print("Tower of Hanoi")
        print()
        print("Given problem   A=[3,2,1]")
        print()
        print("Excepted output   A=[]")
        self.A = []
        self.B = []
        self.C = []
        
    def tower(self, item):
        self.A.append(item)
        time.sleep(1)
        print("A = ", self.A)
        print("Items in tower A/n")
    
    def pass1(self):
        self.temp = self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(1)
        print("A =", self.A, "B=",self.B, "C=",self.C)
        print("Pass one is complete___________________")
    
    def pass2(self):
        self.temp = self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(1)
        print("A = ", self.A, "B=",self.B, "C =",self.C)
        print("Pass two is complete___________________")

    def pass3(self):
        self.temp = self.A.pop(0)
        self.B.append(self.temp)
        time.sleep(1)
        print("A = ", self.A, "B=",self.B, "C =",self.C)
        print("Pass three is complete___________________")
        
    def pass4(self):
        self.temp = self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(1)
        print("A = ", self.A, "B=",self.B, "C =",self.C)
        print("Pass four is complete___________________")

    def pass5(self):
        self.temp = self.B.pop(1)
        self.A.append(self.temp)
        time.sleep(1)
        print("A = ", self.A, "B=",self.B, "C =",self.C)
        print("Pass five is complete___________________")
        
    def pass6(self):
        self.temp = self.B.pop(0)
        self.A.append(self.temp)
        time.sleep(1)
        print("A = ", self.A, "B=",self.B, "C =",self.C)
        print("Pass six is complete___________________")

    def pass7(self):
        self.temp = self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(1)
        print("A = ", self.A, "B=",self.B, "C =",self.C)
        print("Pass seven is complete___________________")
        


obj= Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()

