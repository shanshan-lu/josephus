import sys
sys.path.append('../JosephusProblem')
from achieve.achieve import Achieve


if __name__ == '__main__':
    obj = Achieve()
    file_name = '../Josephusproblem/data/txt.txt'
    obj.select_reader(file_name)
    obj.create_people()
    obj.set_start(2)
    obj.set_step(1)
    result = obj.set_josephus_sample()
    
    for out_person in result:
        print(out_person)
        
          

    
    


