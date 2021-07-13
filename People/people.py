
class Person():
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
        
    def judge_age(self):
        if self.age < 0:
            print('年龄错误')
        return "age input error"

    def judge_gender(self):
        if self.gender not in ['男','女']:
            print('性别错误')
        return "gender input error"
    








   

