class Student:
    def  __init__(self,name,hometown,age,height,icecream):
          self.name=name
          self.hometown=hometown
          self.age=age
          self.height=height
          self.icecream=icecream


    def print_summary(self):
        print("my name is"+self.name)
        print("i live in"+self.hometown)
        
        print("my age is"+self.age)
        print("my height is"+self.height)
        print("my favorite icecream is"+self.icecream)

    def get_giraffe_gap(self):
        return 500-self.height
    
    
