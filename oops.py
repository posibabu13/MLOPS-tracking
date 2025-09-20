#initiating a class
class employee:
    #dunder/magic method/constructor/special method
    def __init__(self):
        self.id=123
        self.salary=60000
        self.designation="Data scientist"
    
    def travel(self,destination):
        print(f"This employee will be travelling to {destination}")    

sam=employee()
print(sam.id)
print(sam.designation)
sam.travel("Andhra pradesh")
    