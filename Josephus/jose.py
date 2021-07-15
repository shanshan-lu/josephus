class Josephus():
    def __init__(self,people,start_pos,step):
        self._people = people
        self.start_pos = start_pos
        self.step = step
        self.total_number = len(self._people)
        self.out_person = 0
        

    def add_person(self,person):
        self._people.append(person)
        return self._people
    
    
    def del_person(self,person):
        self._people.pop(self._people.index(person))
        return self._people
    
    def kill_people(self): 
        if len(self._people) > 1:
            out_location = (self.start_pos + self.step - 1 ) % len(self._people) 
            self.out_person = self._people[out_location]
            self._people.pop(out_location)
            self.start_pos = out_location
        yield self.out_person