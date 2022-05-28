class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__ (self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)



    def change_name(self, name: str):
        self.name = name
    
    def change_age(self, age: int):
        self.age = age
    
    def add_track(self, track):
        self.tracks.append(track)

    def get_score(self):
        return self.score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
    
# Expected methods
Bob.change_name("Sinke")
Bob.change_age(22)
Bob.add_track("Frontend")
Bob.get_score()
print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.score)