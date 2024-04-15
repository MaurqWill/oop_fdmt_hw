class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner updated to {new_owner}")

    def new_owner_info(self):
        info = input("Enter your info: ")
        self.info = info
        print(info)

vehicle = Vehicle("GBOS7414", "Car", "Big Homie")
vehicle.update_owner("Lil Homie")
vehicle.new_owner_info()


class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0 

    def add_participant(self):  
        self.participant_count += 1  

    def get_participant_count(self):  
        return self.participant_count  
    


my_event = Event("Job Interview", "2024-04-01")

my_event.add_participant()  
my_event.add_participant()  

print("Participant count:", my_event.get_participant_count()) 