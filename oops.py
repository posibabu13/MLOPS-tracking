#initiating a class
class employee:
    #dunder/magic method/constructor/special method
    def __init__(self):
        self.id=123
        self.salary=60000
        self.designation="Data scientist"
    
    def travel(self,destination):
        print(f"This employee will be travelling to {destination}")    

# object calling
sam=employee()
print(sam.id)
print(sam.designation)

# method calling
sam.travel("Andhra pradesh")
    