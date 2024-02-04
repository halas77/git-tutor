# Revision for data structures and OOP

# list #
# -> Example: to send a wedding letter for many people


# print(invited_people)

# # out -  ['abebe', 'kebede', 'john', 'dawit', 'ali']

# # -> how to access data
# # -> how to perform tasks in the specific data

# # for and while 

for person in invited_people:
    print(f"Hello {person.capitalize()} , you are invited to the wedding")
#     # out ->  

# num_of_invited_people = len(invited_people)

# for i in range(num_of_invited_people):

#     person = invited_people[i]
#     print(f"Hello {person}, you are invited to the wedding")
    

# "Hello, {name} , you are invited to the wedding"


# Dictionary
# Example: to email passed job_seekers to the interview

# job_seekers = [
#     {
#         "name": "Nathan",
#         "score": 90
#     },
#     {
#         "name": "Biniam",
#         "score": 20
#     },{
#         "name": "Abigiya",
#         "score": 40
#     },{
#         "name": "Rakeb",
#         "score": 95
#     },
# ]


# passed studs

# for student in job_seekers:
#     if student["score"] > 80:
#         print(f"Congratulation  {student["name"]}, You are passed to the interview.")



# Highest score

# higher_score = 0
# higher_scorer = ''

# for student in job_seekers:
#     if student['score'] > higher_score:
#         higher_score = student['score']
#         higher_scorer = student['name']


# print(f'Congra {higher_scorer}, You are the highest scorer. Your score is {higher_score}')







# Class

# class Player():
#     def __init__(self, name, number, club) -> None:
#         self.name = name
#         self.number = number
#         self.club = club
#         self.speed = 0
#         legs = 2

#     def move(self, club):
#         self.club = club


# adane = Player('Adane Girma', 19, 'St. Jorge')
# saladin = Player('Seladin Sied', 7, 'Fasil Kenema') 

# print(adane.club)
# adane.move('Wolkite')
# print(adane.club)

# adane.number = 10

# print(adane.number)


        
        

invited_people = ['kebede','dawit', 'john','ali']

Working dir / unstaged

Staged

Commited


