class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

class Team:
    def __init__(self, team_members):
        self.team_members = team_members

    def __add__(self, other):
        # Adding Team objects creates a larger Team
        return Team(self.team_members + other.team_members)

class Employee:
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def __add__(self, other):
        # Use the + operator to create a Team with the name of each Employee
        return Team([self.name, other.name])

# Two teams
rookies = Team(["Casey", "Emmit"])
veterans = Team(["Mike", "Chuck"])
print(rookies.team_members)
print(veterans.team_members)

# Attempt to add these two Teams together
dream_team = rookies + veterans
print(dream_team.team_members)
print(type(dream_team.team_members))

# Create two Employee objects
anna = Employee('Ana', 'Technical Specialist')
jeff = Employee('Jeff', 'Musician')
audio_team = anna + jeff
print(audio_team.team_members)
print(type(audio_team))