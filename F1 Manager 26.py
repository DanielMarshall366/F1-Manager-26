import random, os, sqlite3, json, winsound, contextlib, wave
import tkinter as tk
from tkinter import simpledialog

class Game:
    def __init__(self):
        self.music=1
        self.sound=1
        self.forenames=["James","Michael","Robert","John","David","William","Richard","Joseph","Thomas","Christopher","Daniel","Charles","Matthew","Anthony","Mark","Donald","Steven",
        "Paul","Kevin","Joshua","Brian","Timothy","Ronald","Jeffrey","Nicholas","Gary","Eric","Steven","Larry","Nathan","Douglas","Keith","Carl","Gerald","Boris","Frank","Florence","Gurtrude",
        "Emily","Elisabeth","Matilda","Penelope","Esther","Jessica","Delilah","Doris","Olivia","Amelia","Bethany"]
        self.surnames=["Smith","Jones","Williams","Brown","Senna","Mansell","Marshall","Thomas","Johnson","White","Wright","Edwards","Green","Clarke","Morris","King","Allen","Phillips",
                       "Young","Griffiths","Collins","Murphy","Miller","Simpson","Russell","Knight","Jordan","Toleman","Beaumont","Williamson","Parsons"]
        self.countries=["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina",
                         "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados",
                         "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina",
                         "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia",
                         "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia",
                         "Comoros", "Congo", "Costa Rica", "Cote D’Ivoire", "Croatia", "Cuba", "Cyprus", "Czechia",
                         "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", "Dominican Republic",
                         "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini",
                         "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana",
                         "Greece", "Grenada", "Guatemala", "Guinea", "Guinea Bissau", "Guyana", "Haiti", "Honduras",
                         "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy",
                         "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos",
                         "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg",
                         "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
                         "Mauritania", "Mauritius", "Mexico", "Micronesia", "Monaco", "Mongolia", "Montenegro", "Morocco",
                         "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua",
                         "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau",
                         "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar",
                         "Moldova", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
                         "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe",
                         "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia",
                         "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain",
                         "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syrian Arab Republic", "Tajikistan",
                         "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey",
                         "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
                         "Tanzania", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City",
                         "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]
        self.name=""
        self.team=""
        self.country=""
        self.newTeam=0
        self.engine=""
        self.sponsor=""
        self.totalIncome=0
        self.money=0
        self.car1=""
        self.car2=""
        self.position=11
        self.ranking=11
        self.season=2026
        self.race=-1
        self.races=22
        self.drivers=[]
        self.teams=[]
        self.cars=[]
        self.engineDurability=[]
        self.car1ID=-1
        self.car2ID=-1
        self.driver1=""
        self.driver2=""
        self.confidence=[]
        self.positions=[]
        self.tyrePace=[]
        self.tyre=[]
        self.tyreRemaining=[]
        self.engineReliability=[]
        self.lap=[]
        self.lap_=[]
        self.time=[]
        self.distance=[]
        self.currentLapTime=[]
        self.tyreCompoundsUsed=[]
        self.damage=[]
        self.overtaking=[]
        self.defending=[]
        self.control=[]
        self.experience=[]
        self.reaction=[]
        self.DRS=[]
        self.tyreAggression=[]
        self.fuelAggression=[]
        self.car1Instructions=[]
        self.car2Instructions=[]
        self.fuel=[]
        self.engineTemperature=[]
        self.ERSdeployment=[]
        self.ERS=[]
        self.racePace=[]
        self.drs=0
        self.ers=0
        self.length=0
        self.wearConstant=0
        self.tyreWear=[]
        self.grip=[]
        self.overtakeability=0
        self.risk=0
        self.frontWings=[]
        self.repairBill=[]
        self.penalties=[]
        self.street=0
        self.safety=0
        self.safetyLaps=0
        self.maxRain=0
        self.maxWater=0
        self.rain=0
        self.water=0
        self.wet=0
        self.rainStarts=0
        self.rainStops=0
        self.drying=0
        self.leader=""
        self.expectedTyreLife=[]
        self.raceFinished=0
        self.pitLap=[]
        self.pitTyre=[]
        self.lapPittedTo=[]
        self.pitting=[]
        self.bestPitStop=[-1,100]
        self.skippingLaps=0
        self.thingHappened=0
        self.tyrePreservation=[]
        self.startLap=1
        self.injured=[]
        self.dead=[]
        self.cycles=0
        self.expectations=[]
        self.faults=[]
        self.laps=0
        self.stops=[]
        self.screen="Title Screen"
        self.newGame=0
        self.driversChosen=[]
        self.legends=0
        self.newTeams=[]
        self.track=""
        self.rawPace=[]
        self.qualifying=0
        self.rainChaince=0
        self.temperature=0
        self.weatherMessage=[]
        self.ta=0
        self.fa=0
        self.ed=0
        self.gridPenalties=[]
        self.penaltyPlace=[]
        self.log=[]
        self.playing=0
        self.pause=0
        self.pittingDriver=0
        self.news=[]
        self.pointsScored=[]
        self.raceCountry=""
        self.displayedImage=0
        self.action=0
        self.maximumUpgradePoints=0
        self.upgradePoints=[]
        self.remainingUpgradePoints=0
        self.attributes=["Drag Reduction","Low Speed Cornering","Medium Speed Cornering","High Speed Cornering","Cooling","Tyre Preservation","Driveability"]
        self.scouting=0
        self.options=[]
        self.displayedName=0
        self.role=0
        self.salary=0
        self.contractLength=0
        self.scoutingAge=0
        self.cooling=[]
        self.buyout=0
        self.displayed=0
        self.actions=3
        self.swappable=0
        self.replacing=0
        self.done=0
        self.vote=0
        self.proposed=0
        self.crashMessage=[]
        self.gender=""
        self.oldTeam=0
        self.legendAvailable=0
        self.strategy=[]
        self.suits=[]
        self.fired=0
        self.expected=[]
        self.replay=0
        self.rainStopped=0
        self.SCPitTyre=[]
        self.aggressions=[]
        self.promoting=0
        self.roles=[]
        self.carConfidence=0
        self.offer=""
        self.roleOptions=[]
        self.teamOrders=1
        self.pit=0
        self.events=0
        self.driver=1
        self.database="F1 Manager 26 Save Data 1.db"
        self.loaded=0
        self.battery=[]
        self.fastest=[-1,0,10]

    def FillDatabase(self):
        F1=sqlite3.connect(GAME.database)
        c=F1.cursor()
        #Teams
        c.execute('''INSERT into Teams (Name, Appearance, OriginalName, Position, Points, Money, Income, TeamPrincipal, Country, Reputation, Sponsor, PreviousPosition, PressConferences) VALUES ("McLaren", "McLaren", "McLaren", 1, 0, 50000000, 1500000, "Andrea Stella", "United Kingdom", 80, "Mastercard", 1, 0)''')
        c.execute('''INSERT into Teams (Name, Appearance, OriginalName, Position, Points, Money, Income, TeamPrincipal, Country, Reputation, Sponsor, PreviousPosition, PressConferences) VALUES ("Ferrari", "Ferrari", "Ferrari", 2, 0, 55000000, 2000000, "Fred Vasseur", "Italy", 90, "HP", 4, 0)''')
        c.execute('''INSERT into Teams (Name, Appearance, OriginalName, Position, Points, Money, Income, TeamPrincipal, Country, Reputation, Sponsor, PreviousPosition, PressConferences) VALUES ("Red Bull", "Red Bull", "Red Bull", 3, 0, 40000000, 1400000, "Laurent Mekies", "Austria", 65, "Oracle", 3, 0)''')
        c.execute('''INSERT into Teams (Name, Appearance, OriginalName, Position, Points, Money, Income, TeamPrincipal, Country, Reputation, Sponsor, PreviousPosition, PressConferences) VALUES ("Mercedes", "Mercedes", "Mercedes", 4, 0, 45000000, 1500000, "Toto Wolff", "Germany", 70, "Petronas", 2, 0)''')
        c.execute('''INSERT into Teams (Name, Appearance, OriginalName, Position, Points, Money, Income, TeamPrincipal, Country, Reputation, Sponsor, PreviousPosition, PressConferences) VALUES ("Aston Martin", "Aston Martin", "Aston Martin", 5, 0, 70000000, 2200000, "Adrian Newey", "United Kingdom", 70, "Aramco", 7, 0)''')
        c.execute('''INSERT into Teams (Name, Appearance, OriginalName, Position, Points, Money, Income, TeamPrincipal, Country, Reputation, Sponsor, PreviousPosition, PressConferences) VALUES ("Alpine", "Alpine", "Alpine", 6, 0, 18000000, 1100000, "Flavio Briatore", "France", 50, "BWT", 10, 0)''')
        c.execute('''INSERT into Teams (Name, Appearance, OriginalName, Position, Points, Money, Income, TeamPrincipal, Country, Reputation, Sponsor, PreviousPosition, PressConferences) VALUES ("Haas", "Haas", "Haas", 7, 0, 15000000, 1000000, "Ayao Komatsu", "United States of America", 55, "Gazoo Racing", 8, 0)''')
        c.execute('''INSERT into Teams (Name, Appearance, OriginalName, Position, Points, Money, Income, TeamPrincipal, Country, Reputation, Sponsor, PreviousPosition, PressConferences) VALUES ("Racing Bulls", "Racing Bulls", "Racing Bulls", 8, 0, 15000000, 1000000, "Alan Permane", "Austria", 35, "Visa & Cash App", 6, 0)''')
        c.execute('''INSERT into Teams (Name, Appearance, OriginalName, Position, Points, Money, Income, TeamPrincipal, Country, Reputation, Sponsor, PreviousPosition, PressConferences) VALUES ("Williams", "Williams", "Williams", 9, 0, 15000000, 1000000, "James Vowles", "United Kingdom", 85, "Atlassian", 5, 0)''')
        c.execute('''INSERT into Teams (Name, Appearance, OriginalName, Position, Points, Money, Income, TeamPrincipal, Country, Reputation, Sponsor, PreviousPosition, PressConferences) VALUES ("Audi", "Audi", "Audi", 10, 0, 50000000, 2000000, "Jonathan Wheatley", "Germany", 75, "Revolut", 9, 0)''')
        c.execute('''INSERT into Teams (Name, Appearance, OriginalName, Position, Points, Money, Income, TeamPrincipal, Country, Reputation, Sponsor, PreviousPosition, PressConferences) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Cadillac", "Cadillac", "Cadillac", 11, 0, 32000000, 1400000, "Graeme Lowdon", "United States of America", 40, 0, 0, 0,))

        #Drivers
        path = "F1 Manager 26 Driver Data.json"
        with open(path, "r") as file:
            jsonData = json.load(file)
        data = jsonData["Drivers"]["Standard"]
        for driver in data:
            c.execute("""
                INSERT INTO Drivers (Name, Appearance, Team, Role, Country, Position, Points, Salary, Condition, Rating, Overtaking, Defending, Pace, Experience, Control, Reaction, Calmness, Age, Marketability, DevelopmentRate, ContractEnd, NewTeam, NewSalary, NewRole, Championships, Wins, Legend) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                driver['Name'],
                0,
                driver['Team'],
                driver['Role'],
                driver['Country'],
                0,
                0,
                driver['Salary'],
                'Well',
                driver['Rating'],
                driver['Overtaking'],
                driver['Defending'],
                driver['Pace'],
                driver['Experience'],
                driver['Control'],
                driver['Reaction'],
                driver['Calmness'],
                driver['Age'],
                driver['Marketability'],
                driver['DevelopmentRate'],
                driver['ContractEnd'],
                0,
                0,
                0,
                driver['Championships'],
                driver['Wins'],
                0
            ))
        if GAME.legends==1:
            data = jsonData["Drivers"]["Legends"]
            for driver in data:
                c.execute("""
                INSERT INTO Drivers (Name, Appearance, Team, Role, Country, Position, Points, Salary, Condition, Rating, Overtaking, Defending, Pace, Experience, Control, Reaction, Calmness, Age, Marketability, DevelopmentRate, ContractEnd, NewTeam, NewSalary, NewRole, Championships, Wins, Legend) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                driver['Name'],
                0,
                'Legend',
                'Legend',
                driver['Country'],
                0,
                0,
                0,
                'Legend',
                driver['Rating'],
                driver['Overtaking'],
                driver['Defending'],
                driver['Pace'],
                driver['Experience'],
                driver['Control'],
                driver['Reaction'],
                driver['Calmness'],
                driver['Age'],
                driver['Marketability'],
                0,
                0,
                0,
                0,
                0,
                driver['Championships'],
                driver['Wins'],
                driver['Tier']
            ))

        if GAME.team!="Mercedes":
            c.execute("UPDATE Drivers SET ContractEnd=2027 WHERE Name='George Russell'")

        #Staff
        
        #Technical Directors
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Peter Prodromou", "McLaren", "Technical Director", 90, 5000000, 95, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Loic Serra", "Ferrari", "Technical Director", 90, 5000000, 90, "France", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Pierre Wache", "Red Bull", "Technical Director", 92, 5000000, 65, "France", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("James Allison", "Mercedes", "Technical Director", 91, 5000000, 70, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Enrico Cardile", "Aston Martin", "Technical Director", 92, 5000000, 88, "Italy", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("David Sanchez", "Alpine", "Technical Director", 85, 3000000, 70, "France", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Andrea de Zordo", "Haas", "Technical Director", 87, 3000000, 85, "Italy", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Dan Fallows", "Racing Bulls", "Technical Director", 85, 2000000, 70, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Matt Harman", "Williams", "Technical Director", 85, 2500000, 85, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("James Key", "Audi", "Technical Director", 88, 3000000, 80, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Pat Symonds", "Cadillac", "Technical Director", 92, 3000000, 80, "United Kingdom", 0, 0, 0))

        #Sporting Directors
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Will Courtenay", "McLaren", "Sporting Director", 90, 4000000, 95, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Diego Ioverno", "Ferrari", "Sporting Director", 95, 4000000, 85, "Italy", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Steve Knowles", "Red Bull", "Sporting Director", 87, 4000000, 66, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Ron Meadows", "Mercedes", "Sporting Director", 90, 4000000, 70, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Andy Stevenson", "Aston Martin", "Sporting Director", 89, 4000000, 85, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Steve Nielsen", "Alpine", "Sporting Director", 82, 2500000, 70, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Mark Lowe", "Haas", "Sporting Director", 80, 2000000, 85, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Marco Perrone", "Racing Bulls", "Sporting Director", 78, 1500000, 70, "Italy", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Sven Smeets", "Williams", "Sporting Director", 79, 1500000, 80, "Belgium", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Inaki Rueda", "Audi", "Sporting Director", 85, 2000000, 80, "Spain", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Rob White", "Cadillac", "Sporting Director", 85, 2000000, 80, "United Kingdom", 0, 0, 0))

        #Race Engineers
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("William Joseph", "McLaren", "Race Engineer 2", 86, 2000000, 95, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Tom Stallard", "McLaren", "Race Engineer 1", 85, 2000000, 95, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Bryan Bozzi", "Ferrari", "Race Engineer 1", 85, 2000000, 90, "Italy", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Cédric Grosjean", "Ferrari", "Race Engineer 2", 95, 2000000, 90, "France", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Gianpiero Lambiase", "Red Bull", "Race Engineer 1", 91, 2000000, 75, "Italy", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Richard Wood", "Red Bull", "Race Engineer 2", 85, 2000000, 70, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Marcus Dudley", "Mercedes", "Race Engineer 1", 90, 1800000, 70, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Peter Bonnington", "Mercedes", "Race Engineer 2", 92, 2000000, 70, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Andrew Vizard", "Aston Martin", "Race Engineer 2", 85, 1500000, 85, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Gary Gannon", "Aston Martin", "Race Engineer 1", 85, 1500000, 65, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Josh Peckett", "Alpine", "Race Engineer 1", 84, 1500000, 70, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Stuart Barlow", "Alpine", "Race Engineer 2", 84, 1500000, 70, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Laura Mueller", "Haas", "Race Engineer 1", 85, 1500000, 85, "Germany", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Ronan OHare", "Haas", "Race Engineer 2", 85, 1500000, 84, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Alexandre Iliopoulos", "Racing Bulls", "Race Engineer 1", 84, 1500000, 70, "Italy", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Pierre Hamelin", "Racing Bulls", "Race Engineer 2", 83, 1500000, 70, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("James Urwin", "Williams", "Race Engineer 1", 78, 1000000, 80, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Gaetan Jego", "Williams", "Race Engineer 2", 76, 1000000, 85, "France", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Steven Petrik", "Audi", "Race Engineer 1", 80, 1000000, 85, "Switzerland", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Jose Manuel Lopez", "Audi", "Race Engineer 2", 80, 1000000, 85, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("John Howard", "Cadillac", "Race Engineer 1", 84, 1500000, 70, "United Kingdom", 0, 0, 0))
        c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',("Carlo Pasetti", "Cadillac", "Race Engineer 2", 84, 1500000, 70, "Italy", 0, 0, 0))
        
        #Regulations
        c.execute('''INSERT into Regulations (Regulation, True) VALUES ("Double Points On Last Race", 0)''')
        c.execute('''INSERT into Regulations (Regulation, True) VALUES ("Team Orders", 1)''')
        c.execute('''INSERT into Regulations (Regulation, True) VALUES ("Reduced Winner Windtunnel Time", 0)''')
        c.execute('''INSERT into Regulations (Regulation, True) VALUES ("Old Points System", 0)''')
        c.execute('''INSERT into Regulations (Regulation, True) VALUES ("ERS", 1)''')
        c.execute('''INSERT into Regulations (Regulation, True) VALUES ("Fastest Lap Point", 0)''')

        #Engines
        c.execute('''INSERT into Engines (Name, Manufacturer, Power, Reliability, Battery, Research) VALUES ("Mercedes", "Mercedes", 9, 8, 7, 1)''')
        c.execute('''INSERT into Engines (Name, Manufacturer, Power, Reliability, Battery, Research) VALUES ("Ferrari", "Ferrari", 8, 10, 6, 1)''')
        c.execute('''INSERT into Engines (Name, Manufacturer, Power, Reliability, Battery, Research) VALUES ("Red Bull", "Red Bull", 7, 8, 7, 1)''')
        c.execute('''INSERT into Engines (Name, Manufacturer, Power, Reliability, Battery, Research) VALUES ("Audi", "Audi", 7, 8, 5, 1)''')
        c.execute('''INSERT into Engines (Name, Manufacturer, Power, Reliability, Battery, Research) VALUES ("Honda", "Aston Martin", 4, 1, 3, 1)''')

        #Cars
        c.execute('''INSERT into Cars (Team, Engine, DragReduction, LowSpeed, MediumSpeed, HighSpeed, Cooling, TyrePreservation, car1Engine, car1EngineDurability, car2Engine, car2EngineDurability, Research, Ranking, Driveability) VALUES ("McLaren", "Mercedes", 60, 60, 60, 60, 45, 60, 1, 100, 1, 100, 1, 4, 11)''')
        c.execute('''INSERT into Cars (Team, Engine, DragReduction, LowSpeed, MediumSpeed, HighSpeed, Cooling, TyrePreservation, car1Engine, car1EngineDurability, car2Engine, car2EngineDurability, Research, Ranking, Driveability) VALUES ("Ferrari", "Ferrari", 70, 80, 80, 80, 60, 62, 1, 100, 1, 100, 1, 2, 15)''')
        c.execute('''INSERT into Cars (Team, Engine, DragReduction, LowSpeed, MediumSpeed, HighSpeed, Cooling, TyrePreservation, car1Engine, car1EngineDurability, car2Engine, car2EngineDurability, Research, Ranking, Driveability) VALUES ("Red Bull", "Red Bull", 62, 58, 58, 58, 35, 62, 1, 100, 1, 100, 1, 3, 15)''')
        c.execute('''INSERT into Cars (Team, Engine, DragReduction, LowSpeed, MediumSpeed, HighSpeed, Cooling, TyrePreservation, car1Engine, car1EngineDurability, car2Engine, car2EngineDurability, Research, Ranking, Driveability) VALUES ("Mercedes", "Mercedes", 85, 80, 80, 80, 60, 55, 1, 100, 1, 100, 1, 1, 15)''')
        c.execute('''INSERT into Cars (Team, Engine, DragReduction, LowSpeed, MediumSpeed, HighSpeed, Cooling, TyrePreservation, car1Engine, car1EngineDurability, car2Engine, car2EngineDurability, Research, Ranking, Driveability) VALUES ("Aston Martin", "Honda", 30, 30, 30, 30, 25, 34, 1, 100, 1, 100, 1, 7, 14)''')
        c.execute('''INSERT into Cars (Team, Engine, DragReduction, LowSpeed, MediumSpeed, HighSpeed, Cooling, TyrePreservation, car1Engine, car1EngineDurability, car2Engine, car2EngineDurability, Research, Ranking, Driveability) VALUES ("Alpine", "Mercedes", 47, 47, 47, 47, 33, 38, 1, 100, 1, 100, 1, 6, 12)''')
        c.execute('''INSERT into Cars (Team, Engine, DragReduction, LowSpeed, MediumSpeed, HighSpeed, Cooling, TyrePreservation, car1Engine, car1EngineDurability, car2Engine, car2EngineDurability, Research, Ranking, Driveability) VALUES ("Haas", "Ferrari", 47, 47, 47, 47, 35, 40, 1, 100, 1, 100, 1, 5, 15)''')
        c.execute('''INSERT into Cars (Team, Engine, DragReduction, LowSpeed, MediumSpeed, HighSpeed, Cooling, TyrePreservation, car1Engine, car1EngineDurability, car2Engine, car2EngineDurability, Research, Ranking, Driveability) VALUES ("Racing Bulls", "Red Bull", 50, 45, 45, 45, 40, 45, 1, 100, 1, 100, 1, 7, 20)''')
        c.execute('''INSERT into Cars (Team, Engine, DragReduction, LowSpeed, MediumSpeed, HighSpeed, Cooling, TyrePreservation, car1Engine, car1EngineDurability, car2Engine, car2EngineDurability, Research, Ranking, Driveability) VALUES ("Williams", "Mercedes", 40, 40, 40, 40, 30, 35, 1, 100, 1, 100, 1, 8, 12)''')
        c.execute('''INSERT into Cars (Team, Engine, DragReduction, LowSpeed, MediumSpeed, HighSpeed, Cooling, TyrePreservation, car1Engine, car1EngineDurability, car2Engine, car2EngineDurability, Research, Ranking, Driveability) VALUES ("Audi", "Audi", 48, 48, 48, 48, 33, 40, 1, 100, 1, 100, 1, 9, 15)''')
        c.execute('''INSERT into Cars (Team, Engine, DragReduction, LowSpeed, MediumSpeed, HighSpeed, Cooling, TyrePreservation, car1Engine, car1EngineDurability, car2Engine, car2EngineDurability, Research, Ranking, Driveability) VALUES ("Cadillac", "Ferrari", 30, 30, 30, 30, 30, 30, 1, 100, 1, 100, 1, 10, 15)''')
        if GAME.newTeam==1:
            c.execute('''INSERT into Cars (Team, Engine, DragReduction, LowSpeed, MediumSpeed, HighSpeed, Cooling, TyrePreservation, car1Engine, car1EngineDurability, car2Engine, car2EngineDurability, Research, Ranking, Driveability) VALUES (?, ?, 30, 30, 30, 30, 30, 30, 1, 100, 1, 100, 0, 12, 12)''',(GAME.team, GAME.engine))

        #Sponsors
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("HP", "Ferrari", 70000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Oracle", "Red Bull", 50000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Petronas", "Mercedes", 70000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Aramco", "Aston Martin", 58000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("BWT", "Alpine", 40000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Gazoo Racing", "Haas", 40000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Visa & Cash App", "Racing Bulls", 42500)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Atlassian", "Williams", 40000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Apple", "None", 45000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Adidas", "None", 40000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Microsoft", "None", 50000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Tesco", "None", 37500)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("EA", "None", 50000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Games Workshop", "None", 37500)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Disney", "None", 75000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Opera GX", "None", 37500)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Coca Cola", "None", 70000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("NVIDIA", "None", 65000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Google", "None", 65000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Netflix", "None", 60000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("IBM", "None", 60000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("McDonald", "None", 65000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Uber", "None", 50000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Virgin", "None", 65000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Vodafone", "None", 72000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Mastercard", "McLaren", 70000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Revolut", "Audi", 65000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("Malboro", "None", 80000)''')
        c.execute('''INSERT into Sponsors (Name, Team, Pay) VALUES ("West", "None", 68000)''')
        c.execute("DELETE FROM Sponsors WHERE Name=?",(GAME.team,))
        sponsor=0
        if GAME.team=="Malboro Ferrari":
            sponsor="Malboro"
        elif GAME.team=="Vodafone McLaren":
            sponsor="Vodafone"
        elif GAME.team=="West McLaren":
            sponsor="West"
        if sponsor!=0:
            c.execute("UPDATE Teams SET Sponsor=? WHERE Name=?",(sponsor,GAME.team,))
            c.execute("UPDATE Sponsors SET Team=? WHERE Name=?",(GAME.team,sponsor,))

        #Tracks
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Albert Park", "Australia", 5.278, 58, 50, 25, 30, "High", 40, 0, 0, 3)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Shanghai", "China", 5.451, 56, 35, 1, 25, "Medium", 50, 1, 0, 2)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Suzuka", "Japan", 5.807, 53, 75, 15, 20, "High", 55, 0, 0, 1)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Sakhir", "Bahrain", 5.412, 57, 40, 0, 25, "Medium", 50, 1, 0, 4)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Jeddah", "Saudi Arabia", 6.174, 50, 60, 0, 35, "Medium", 65, 0, 1, 3)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Miami", "United States of America", 5.412, 57, 50, 5, 25, "Low", 50, 1, 0, 3)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Imola", "Italy", 4.909, 63, 70, 5, 20, "Medium", 30, 0, 0, 2)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Monte Carlo", "Monaco", 3.337, 78, 88, 25, 15, "Low", 5, 0, 0, 1)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Catalunya", "Spain", 4.657, 66, 40, 5, 25, "Medium", 65, 0, 0, 3)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Montreal", "Canada", 4.361, 70, 40, 10, -15, "Low", 48, 0, 0, 3)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Red Bull Ring", "Austria", 4.318, 71, 65, 5, 15, "High", 75, 0, 0, 4)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Silverstone", "United Kingdom", 5.891, 52, 50, 65, 18, "High", 65, 0, 0, 4)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Spa", "Belgium", 7.004, 44, 70, 30, 10, "High", 75, 1, 0, 3)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Hungaroring", "Hungary", 4.381, 70, 50, 5, 11, "Medium", 58, 0, 0, 2)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Zandvoort", "Netherlands", 4.259, 72, 55, 10, 17, "High", 35, 0, 0, 2)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Monza", "Italy", 5.793, 53, 68, 5, 20, "High", 100, 0, 0, 3)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Baku", "Azerbaijan", 6.003, 51, 85, 1, 15, "Low", 80, 0, 1, 2)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Marina Bay", "Singapore", 4.940, 62, 83, 5, 32, "Medium", 35, 0, 1, 2)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Austin", "United States of America", 5.513, 56, 60, 0, 30, "Medium", 58, 0, 1, 4)''')        
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Mexico City", "Mexico", 4.304, 71, 50, 5, 21, "Medium", 50, 1, 0, 3)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Interlagos", "Brazil", 4.309, 71, 50, 75, 30, "Low", 50, 0, 1, 5)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Las Vegas", "United States of America", 6.201, 50, 65, 5, 10, "Low", 70, 0, 1, 3)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Qatar", "Qatar", 5.419, 57, 60, 0, 22, "High", 38, 1, 0, 2)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Abu Dhabi", "Abu Dhabi", 5.281, 58, 50, 0, 20, "Medium", 65, 0, 0, 3)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Madrid", "Spain", 5.474, 57, 50, 5, 25, "Medium", 45, 0, 1, 3)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Istanbul Park", "Turkey", 5.338, 58, 55, 20, 25, "Medium", 40, 0, 0, 3)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Nürburgring", "Germany", 5.148, 60, 95, 23, 20, "High", 45, 0, 0, 3)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Hockenheim", "Germany", 4.574, 67, 68, 23, 20, "Medium", 65, 0, 0, 4)''')
        c.execute('''INSERT into Tracks (Name, Country, Length, Laps, Risk, RainChance, Temperature, Corners, Straights, Sprint, Street, Overtakeability) VALUES ("Portimão", "Portugal", 4.653, 66, 60, 40, 18, "High", 50, 0, 0, 3)''')
        
        #Player
        c.execute('''INSERT into Player (Name, Country, Team, newTeam, Season, Race, RegulationChange, Points, Wins, Championships, NextYearEngine, Actions, Financial, Management, Warnings, TyreWear, MovingTo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(GAME.name, GAME.country, GAME.team, GAME.newTeam, 2026, -1, 2029, 0, 0, 0, 0, 3, 5, 3, 0, 0, 0))
        
        #History
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2001, "Michael Schumacher", "Ferrari")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2002, "Michael Schumacher", "Ferrari")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2003, "Michael Schumacher", "Ferrari")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2004, "Michael Schumacher", "Ferrari")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2005, "Fernando Alonso", "Renault")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2006, "Fernando Alonso", "Renault")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2007, "Kimi Raikkonen", "Ferrari")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2008, "Lewis Hamilton", "Ferrari")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2009, "Jenson Button", "Brawn")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2010, "Sebastian Vettel", "Red Bull")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2011, "Sebastian Vettel", "Red Bull")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2012, "Sebastian Vettel", "Red Bull")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2013, "Sebastian Vettel", "Red Bull")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2014, "Lewis Hamilton", "Mercedes")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2015, "Lewis Hamilton", "Mercedes")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2016, "Nico Rosberg", "Mercedes")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2017, "Lewis Hamilton", "Mercedes")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2018, "Lewis Hamilton", "Mercedes")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2019, "Lewis Hamilton", "Mercedes")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2020, "Lewis Hamilton", "Mercedes")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2021, "Max Verstappen", "Mercedes")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2022, "Max Verstappen", "Red Bull")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2023, "Max Verstappen", "Red Bull")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2024, "Max Verstappen", "McLaren")''')
        c.execute('''INSERT into History (Year, Driver, Constructor) VALUES (2025, "Lando Norris", "McLaren")''')

        #Buyers
        c.execute('''INSERT into Buyers(Name, Country) VALUES("BMW", "Germany")''')
        c.execute('''INSERT into Buyers(Name, Country) VALUES("Lotus", "United Kingdom")''')
        c.execute('''INSERT into Buyers(Name, Country) VALUES("Amazon", "United States of America")''')
        c.execute('''INSERT into Buyers(Name, Country) VALUES("Force India", "India")''')
        c.execute('''INSERT into Buyers(Name, Country) VALUES("Ford", "United States of America")''')
        c.execute('''INSERT into Buyers(Name, Country) VALUES("Tesla", "United States of America")''')
        c.execute('''INSERT into Buyers(Name, Country) VALUES("Benneton", "Italy")''')
        c.execute('''INSERT into Buyers(Name, Country) VALUES("Honda", "Japan")''')
        c.execute('''INSERT into Buyers(Name, Country) VALUES("Alfa Romeo", "Italy")''')
        c.execute('''INSERT into Buyers(Name, Country) VALUES("Renault", "France")''')
        c.execute('''INSERT into Buyers(Name, Country) VALUES("Porsche", "Germany")''')
        c.execute('''INSERT into Buyers(Name, Country) VALUES("Kia", "South Korea")''')
        c.execute('''INSERT into Buyers(Name, Country) VALUES("Mazda", "Japan")''')
        c.execute('''INSERT into Buyers(Name, Country) VALUES("Lamborghini", "Italy")''')
        c.execute('''INSERT into Buyers(Name, Country) VALUES("Volkswagen", "Germany")''')
        c.execute('''INSERT into Buyers(Name, Country) VALUES("Volvo", "Sweden")''')
        c.execute('''INSERT into Buyers(Name, Country) VALUES("JLR", "United Kingdom")''')
        c.execute("DELETE FROM Buyers WHERE Name=?",(GAME.team,))

        #Team Principals
        c.execute('''INSERT into TeamPrincipals(Name, Team) VALUES("Andrea Stella", "McLaren")''')
        c.execute('''INSERT into TeamPrincipals(Name, Team) VALUES("Fred Vasseur", "Ferrari")''')
        c.execute('''INSERT into TeamPrincipals(Name, Team) VALUES("Laurent Mekies", "Red Bull")''')
        c.execute('''INSERT into TeamPrincipals(Name, Team) VALUES("Toto Wolff", "Mercedes")''')
        c.execute('''INSERT into TeamPrincipals(Name, Team) VALUES("Adrian Newey", "Aston Martin")''')
        c.execute('''INSERT into TeamPrincipals(Name, Team) VALUES("Flavio Briatore", "Alpine")''')
        c.execute('''INSERT into TeamPrincipals(Name, Team) VALUES("Ayao Komatsu", "Haas")''')
        c.execute('''INSERT into TeamPrincipals(Name, Team) VALUES("Alan Permane", "Racing Bulls")''')
        c.execute('''INSERT into TeamPrincipals(Name, Team) VALUES("James Vowles", "Williams")''')
        c.execute('''INSERT into TeamPrincipals(Name, Team) VALUES("Jonathan Wheatley", "Audi")''')
        c.execute('''INSERT into TeamPrincipals(Name, Team) VALUES("Graeme Lowdon", "Cadillac")''')
        c.execute('''INSERT into TeamPrincipals(Name, Team) VALUES("Christian Horner", "None")''')
        c.execute("UPDATE TeamPrincipals SET Team='None' WHERE Team=?",(GAME.team,))
        F1.commit()
        F1.close()

    def StopMusic(self):
        winsound.PlaySound(None, winsound.SND_PURGE)
    def GenerateName(self):
        F1=sqlite3.connect(GAME.database)
        c=F1.cursor()
        forename=random.choice(GAME.forenames)
        name=forename+" "+random.choice(GAME.surnames)
        c.execute('''SELECT Name FROM Drivers WHERE Name=?''',(name,))
        f=c.fetchall()
        c.execute('''SELECT Name FROM Staff WHERE Name=?''',(name,))
        F=c.fetchall()
        if len(f)>=1 or len(F)>=1:
            while len(f)>=1 or len(F)>=1:
                forename=random.choice(GAME.forenames)
                name=forename+" "+random.choice(GAME.surnames)
                c.execute('''SELECT Name FROM Drivers WHERE Name=?''',(name,))
                f=c.fetchall()
                c.execute('''SELECT Name FROM Staff WHERE Name=?''',(name,))
                F=c.fetchall()
        if GAME.forenames.index(forename)<=35:
            GAME.gender="Male"
        else:
            GAME.gender="Female"
        F1.commit()
        F1.close()
        return(name)
    def GeneratePeople(self,role):
        Name=GAME.GenerateName()
        with sqlite3.connect(GAME.database) as c:
            if role=="Driver":
                if GAME.gender=="Male":
                    appearance="Man "+str(random.randint(1,3))
                else:
                    appearance="Woman "+str(random.randint(1,2))
                Overtaking=random.randint(20,85)
                Defending=random.randint(20,85)
                Pace=random.randint(20,85)
                Experience=random.randint(0,60)
                Control=random.randint(20,85)
                Reaction=random.randint(20,85)
                Rating=round((Overtaking+Defending+Pace+Experience+Control+Reaction)/6)
                c.execute('''INSERT into Drivers (Name, Appearance,Team, Role, Country, Position, Points, Salary, Condition, Rating, Overtaking, Defending, Pace, Experience, Control, Reaction, Calmness, Age, Marketability, DevelopmentRate, ContractEnd, NewTeam, NewSalary, NewRole, Championships, Wins, Legend) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(Name, appearance, "Free Agent", "Free Agent", random.choice(GAME.countries), 0, 0, 0, "Well", Rating, Overtaking, Defending, Pace, Experience, Control, Reaction, random.randint(0,100), random.randint(12,25), random.randint(50,95), random.randint(70,180), 0, 0, 0, 0, 0, 0, 0))
            else:
                if role=="Race Engineer 1" or role=="Race Engineer 2":
                    role="Race Engineer"
                rating=random.randint(20,100)
                num=random.randint(20,100)
                if num<rating:
                    rating=num
                c.execute('''INSERT into Staff (Name, Team, Role, Rating, Salary, Morale, Country, NewTeam, NewSalary, NewRole) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(Name, "Free Agent", role, rating, 0, 50, random.choice(GAME.countries), 0, 0, 0))
    def Sanitise(self, item):
        newItem=""
        item=str(item)
        for x in range(len(item)):
            if item[x]!='"' and item[x]!="(" and item[x]!=")" and item[x]!="," and item[x]!="'" and item[x]!="[" and item[x]!="]":
                newItem=newItem+item[x]
        return newItem
    def Validate(self, item):
        item=str(item)
        if item=="None":
            return(0)
        if len(item)==0 or len(item)>20:
            return(0)
        valid=0
        for x in range(len(item)):
            if item[x]!=" ":
                valid=1
        return valid
    def CalculateIncome(self, team):
        F1=sqlite3.connect(GAME.database)
        c=F1.cursor()
        c.execute('''SELECT Income FROM Teams WHERE Name=?''',(team,))
        baseIncome=int(GAME.Sanitise(c.fetchall()[0]))
        c.execute('''SELECT Name FROM Drivers WHERE Team=? AND Role="1"''',(team,))
        car1=GAME.Sanitise(c.fetchall()[0])
        c.execute('''SELECT Name FROM Drivers WHERE Team=? AND Role="2"''',(team,))
        car2=GAME.Sanitise(c.fetchall()[0])
        c.execute('''SELECT Marketability FROM Drivers WHERE Name=?''',(car1,))
        marketability=int(GAME.Sanitise(c.fetchall()[0]))
        c.execute('''SELECT Marketability FROM Drivers WHERE Name=?''',(car2,))
        marketability+=int(GAME.Sanitise(c.fetchall()[0]))
        c.execute('''SELECT Reputation FROM Teams WHERE Name=?''',(team,))
        marketability+=int(GAME.Sanitise(c.fetchall()[0]))
        c.execute('''SELECT Pay FROM Sponsors WHERE Team=?''',(team,))
        f=c.fetchall()
        if len(f)==1:
            sponsorPay=int(GAME.Sanitise(f[0]))
            sponsorPay=sponsorPay*marketability
            totalIncome=baseIncome+sponsorPay
        else:
            totalIncome=baseIncome+(marketability*20000)
        c.execute('''SELECT Salary FROM Drivers WHERE Team=?''',(team,))
        salaries=c.fetchall()
        salary=0
        for x in range(len(salaries)):
            salary+=int(GAME.Sanitise(salaries[x]))
        c.execute('''SELECT Salary FROM Staff WHERE Team=?''',(team,))
        salaries=c.fetchall()
        for x in range(len(salaries)):
            salary+=int(GAME.Sanitise(salaries[x]))
        salary=round(salary/12)
        totalIncome=totalIncome-salary
        engine=GAME.Sanitise(c.execute("SELECT Engine FROM Cars WHERE Team=?",(team,)).fetchall()[0])
        if team!="Racing Bulls" or engine!="Red Bull":
            manufacturer=len(c.execute("SELECT Name FROM Engines WHERE Name=? AND Manufacturer=?",(engine,team,)).fetchall())
            if manufacturer>0:
                customers=len(c.execute("SELECT Team FROM Cars WHERE Engine=? AND Team!='Racing Bulls' AND Team!=?",(engine,team,)).fetchall())
                totalIncome+=1000000*customers
            else:
                totalIncome-=1000000
        c.execute('''SELECT PreviousPosition FROM Teams WHERE Name=?''',(team,))
        previousPosition=int(GAME.Sanitise(c.fetchall()[0]))
        if previousPosition==1:
            totalIncome+=5416667
        elif previousPosition==2:
            totalIncome+=5125000
        elif previousPosition==3:
            totalIncome+=4750000
        elif previousPosition==4:
            totalIncome+=4416667
        elif previousPosition==5:
            totalIncome+=4083333
        elif previousPosition==6:
            totalIncome+=3791667
        elif previousPosition==7:
            totalIncome+=3500000
        elif previousPosition==8:
            totalIncome+=3125000
        elif previousPosition==9:
            totalIncome+=2791667
        elif previousPosition==10:
            totalIncome+=2458333
        elif previousPosition==11:
            totalIncome+=2166667
        F1.commit()
        F1.close()
        return totalIncome
    def TeamAcquired(self, oldTeam, newTeam):
        F1=sqlite3.connect(GAME.database)
        c=F1.cursor()
        money=int(GAME.Sanitise(c.execute("SELECT Money FROM Teams WHERE Name=?",(oldTeam,)).fetchall()[0]))
        if GAME.team!=oldTeam:
            money+=random.randint(1,8)*1000000
        income=int(GAME.Sanitise(c.execute("SELECT Income FROM Teams WHERE Name=?",(oldTeam,)).fetchall()[0]))
        income+=random.randint(100000,round(income/1.5))
        reputation=int(GAME.Sanitise(c.execute("SELECT Reputation FROM Teams WHERE Name=?",(oldTeam,)).fetchall()[0]))
        reputation=random.randint(round(reputation*0.8),round(reputation*1.8))
        c.execute('''UPDATE Teams SET Name=?, Money=?, Reputation=?, Income=? WHERE Name=?''',(newTeam, money, reputation, income, oldTeam))
        c.execute('''UPDATE Drivers SET Team=? WHERE Team=?''',(newTeam, oldTeam))
        c.execute('''UPDATE Drivers SET NewTeam=? WHERE NewTeam=?''',(newTeam, oldTeam))
        c.execute('''UPDATE Staff SET Team=? WHERE Team=?''',(newTeam, oldTeam))
        c.execute('''UPDATE Staff SET NewTeam=? WHERE NewTeam=?''',(newTeam, oldTeam))
        c.execute('''UPDATE Cars SET Team=? WHERE Team=?''',(newTeam, oldTeam))
        c.execute('''UPDATE Sponsors SET Team=? WHERE Team=?''',(newTeam, oldTeam))
        c.execute('''UPDATE Player SET Team=? WHERE Team=?''',(newTeam, oldTeam))
        c.execute('''UPDATE TeamPrincipals SET Team=? WHERE Team=?''',(newTeam, oldTeam))
        c.execute('''UPDATE Engines SET Manufacturer=? WHERE Manufacturer=?''',(newTeam, oldTeam))
        if GAME.season>2026:
            c.execute("UPDATE Engines SET Manufacturer='None' WHERE Manufacturer=? AND Name='Audi'",(newTeam,))
        if len(c.execute("SELECT Name FROM Engines WHERE Name=? AND Manufacturer=?",(oldTeam,oldTeam,)).fetchall())>0:
            c.execute("UPDATE Engines SET Name=? WHERE Manufacturer=? AND Name=?",(newTeam, newTeam, oldTeam,))
            c.execute("UPDATE Engines SET Manufacturer='None' WHERE Name='Red Bull' AND Manufacturer!='Red Bull'")
            if oldTeam!="Audi":
                c.execute("UPDATE Cars SET Engine=? WHERE Engine=?",(newTeam,oldTeam,))
        if GAME.team==oldTeam:
            GAME.team=newTeam
        F1.commit()
        F1.close()
    def Income(self):
        F1=sqlite3.connect(GAME.database)
        c=F1.cursor()
        c.execute('''SELECT Name FROM Teams''')
        f=c.fetchall()
        for x in range(len(f)):
            team=GAME.Sanitise(f[x])
            income=GAME.CalculateIncome(team)
            c.execute('''SELECT Money FROM Teams WHERE Name=?''',(team,))
            money=int(GAME.Sanitise(c.fetchall()[0]))
            money+=income
            if money>100000000:
                money=100000000
            if team==GAME.team:
                GAME.money=money
            c.execute('''UPDATE Teams SET Money=? WHERE Name=?''',(money, team,))
        c.execute("UPDATE Teams SET Money=100000000 WHERE Money>100000000")
        F1.commit()
        F1.close()
    def Upgrade(self, team):
        F1=sqlite3.connect(GAME.database)
        c=F1.cursor()
        rating=int(GAME.Sanitise(c.execute('''SELECT Rating FROM Staff WHERE Team=? AND Role="Technical Director"''',(team,)).fetchall()[0]))
        money=int(GAME.Sanitise(c.execute('''SELECT Money FROM Teams WHERE Name=?''',(team,)).fetchall()[0]))
        if 5000000>money/3:
            maximum=(round(money/3))//500000
        else:
            maximum=10
        if maximum==10:
            if GAME.races<20:
                maximum=12
            elif GAME.races<23:
                maximum=11
            reduced=0
            if len(c.execute("SELECT Name FROM Teams WHERE Name=? AND PreviousPosition=1",(team,)).fetchall())>0:
                if len(c.execute("SELECT Regulation FROM Regulations WHERE Regulation='Reduced Winner Windtunnel Time' AND True=1").fetchall())>0:
                    reduced=1
                    maximum-=2
                    if maximum<1:
                        maximum=1
            if money>=55000000:
                extra=(money-50000000)//5000000
                if reduced==1:
                    extra=round(extra/1.5)
                maximum+=extra
            if rating>90:
                extra=rating-90
                if reduced==1:
                    extra=round(extra/1.5)
                maximum+=extra
        if maximum>(round(money/3))//500000:
            maximum=(round(money/3))//500000
        if money>25000000 or maximum<7:
            actionPoints=maximum
        else:
            actionPoints=random.randint(6,maximum)
        dragReduction=0
        lowSpeed=0
        mediumSpeed=0
        highSpeed=0
        cooling=0
        tyrePreservation=0
        driveability=0
        Driveability=0
        for x in range(actionPoints):
            num=random.randint(1,7)
            if num<5 or num==8:
                Driveability+=round(random.randint(-250,100)/1000)
            if num==1:
                dragReduction+=1
            elif num==2:
                lowSpeed+=1
            elif num==3:
                mediumSpeed+=1
            elif num==4:
                highSpeed+=1
            elif num==5:
                cooling+=1
            elif num==6:
                tyrePreservation+=1
            elif num==7:
                driveability+=1
        if dragReduction>0:
            dragReduction=round(random.randint(-1,round((rating**2)*dragReduction/4000))/3)
        if lowSpeed>0:
            lowSpeed=round(random.randint(-1,round((rating**2)*lowSpeed/4000))/3)
        if mediumSpeed>0:
            mediumSpeed=round(random.randint(-1,round((rating**2)*mediumSpeed/4000))/3)
        if highSpeed>0:
            highSpeed=round(random.randint(-1,round((rating**2)*highSpeed/4000))/3)
        if cooling>0:
            cooling=round(random.randint(-1,round((rating**2)*cooling/4000))/3)
        if tyrePreservation>0:
            tyrePreservation=round(random.randint(-1,round((rating**2)*tyrePreservation/4000))/3)
        if driveability>0:
            driveability=round(random.randint(-5,5*driveability)/8)
        driveability+=Driveability
        c.execute('''SELECT DragReduction FROM Cars WHERE Team=?''',(team,))
        dragReduction+=int(GAME.Sanitise(c.fetchall()[0]))
        c.execute('''SELECT LowSpeed FROM Cars WHERE Team=?''',(team,))
        lowSpeed+=int(GAME.Sanitise(c.fetchall()[0]))
        c.execute('''SELECT MediumSpeed FROM Cars WHERE Team=?''',(team,))
        mediumSpeed+=int(GAME.Sanitise(c.fetchall()[0]))
        c.execute('''SELECT HighSpeed FROM Cars WHERE Team=?''',(team,))
        highSpeed+=int(GAME.Sanitise(c.fetchall()[0]))
        c.execute('''SELECT Cooling FROM Cars WHERE Team=?''',(team,))
        cooling+=int(GAME.Sanitise(c.fetchall()[0]))
        c.execute('''SELECT TyrePreservation FROM Cars WHERE Team=?''',(team,))
        tyrePreservation+=int(GAME.Sanitise(c.fetchall()[0]))
        c.execute('''SELECT Driveability FROM Cars WHERE Team=?''',(team,))
        driveability+=int(GAME.Sanitise(c.fetchall()[0]))
        if driveability>20:
            driveability=20
        money-=actionPoints*500000
        F1=sqlite3.connect(GAME.database)
        c=F1.cursor()
        c.execute('''UPDATE Cars SET DragReduction=?, LowSpeed=?, MediumSpeed=?, HighSpeed=?, Cooling=?, TyrePreservation=?, Driveability=? WHERE Team=?''',(dragReduction, lowSpeed, mediumSpeed, highSpeed, cooling, tyrePreservation, driveability, team,))
        c.execute('''UPDATE Teams SET Money=? WHERE Name=?''',(money, team,))
        F1.commit()
        F1.close()
    def Research(self, team):
        F1=sqlite3.connect(GAME.database)
        c=F1.cursor()
        c.execute('''SELECT Money FROM Teams WHERE Name=?''',(team,))
        money=int(GAME.Sanitise(c.fetchall()[0]))
        if GAME.race==GAME.races:
            research=random.randint(round(money/2.5),money)
        elif money>60000000:
            research=random.randint(10000000,round(money/2.5))
        elif money>1400000:
            research=random.randint(200000,round(money/7))
        elif money>=100000:
            research=100000
        else:
            research=0
        money-=research
        c.execute('''SELECT Rating FROM Staff WHERE Team=? AND Role="Technical Director"''',(team,))
        rating=int(GAME.Sanitise(c.fetchall()[0]))
        research=research*(rating**3)*random.randint(2,3)
        if len(c.execute("SELECT Name FROM Engines WHERE Manufacturer=?",(team,)).fetchall())>0:
            research=round(research*1.5)
        c.execute('''SELECT Research FROM Cars WHERE Team=?''',(team,))
        research+=int(GAME.Sanitise(c.fetchall()[0]))
        c.execute('''UPDATE Cars SET Research=? WHERE Team=?''',(research, team,))
        c.execute('''UPDATE Teams SET Money=? WHERE Name=?''',(money, team,))
        F1.commit()
        F1.close()
    def EngineResearch(self, engine, team):
        F1=sqlite3.connect(GAME.database)
        c=F1.cursor()
        money=int(GAME.Sanitise(c.execute('''SELECT Money FROM Teams WHERE Name=?''',(team,)).fetchall()[0]))
        if money>=1000008:
            if GAME.race==GAME.races:
                research=random.randint(money//2,money)
            elif money>=150000000/GAME.races:
                research=money//4
            else:
                research=random.randint(money//8,money//4)
            money-=research
            rating=int(GAME.Sanitise(c.execute('''SELECT Rating FROM Staff WHERE Team=? AND Role="Technical Director"''',(team,)).fetchall()[0]))
            research=research*(rating**3)*random.randint(2,3)
            if engine=="Honda":
                research=round(research*1.5)
            research+=int(GAME.Sanitise(c.execute("SELECT Research FROM Engines WHERE Name=?",(engine,)).fetchall()[0]))
            c.execute('''UPDATE Engines SET Research=? WHERE Name=?''',(research, engine,))
            c.execute('''UPDATE Teams SET Money=? WHERE Name=?''',(money, team,))
        F1.commit()
        F1.close()
    def DriverSuitability(self, Team):
        F1=sqlite3.connect(GAME.database)
        c=F1.cursor()
        c.execute('''SELECT Name FROM Drivers WHERE Condition="Well" AND Team!=? AND NewTeam="0"''',(Team,))
        f=c.fetchall()
        c.execute('''SELECT Ranking FROM Cars WHERE Team=?''',(Team,))
        Ranking=int(GAME.Sanitise(c.fetchall()[0]))
        c.execute('''SELECT Position FROM Teams WHERE Name=?''',(Team,))
        Position=int(GAME.Sanitise(c.fetchall()[0]))
        drivers=[]
        for x in range(len(f)):
            driver=GAME.Sanitise(f[x])
            team=GAME.Sanitise(c.execute('''SELECT Team FROM Drivers WHERE Name=?''',(driver,)).fetchall()[0])
            if team!=Team:
                age=1
                if GAME.scouting=="Junior Driver":
                    if len(c.execute("SELECT Name FROM Drivers WHERE Name=? AND Age<18",(driver,)).fetchall())==0:
                        age=0
                if age==1:
                    c.execute('''SELECT Role FROM Drivers WHERE Name=?''',(driver,))
                    role=GAME.Sanitise(c.fetchall()[0])
                    if role=="Reserve" or role=="Junior" or role=="Free Agent":
                        drivers.append(driver)
                    elif GAME.race>=7:
                        c.execute('''SELECT ContractEnd FROM Drivers WHERE Name=?''',(driver,))
                        contractEnd=int(GAME.Sanitise(c.fetchall()[0]))
                        if Team==GAME.team and Team=="Racing Bulls" and team=="Red Bull" and contractEnd==GAME.season and GAME.race>=GAME.races-6:
                            drivers.append(driver)
                        else:
                            c.execute('''SELECT Ranking FROM Cars WHERE Team=?''',(team,))
                            ranking=int(GAME.Sanitise(c.fetchall()[0]))
                            c.execute('''SELECT Position FROM Teams WHERE Name=?''',(team,))
                            position=int(GAME.Sanitise(c.fetchall()[0]))
                            if contractEnd==GAME.season:
                                if Ranking<=ranking+1 or Position<=position+1 or GAME.race>=20:
                                    drivers.append(driver)
                            elif Ranking<ranking or Position<position:
                                drivers.append(driver)
        F1.commit()
        F1.close()
        return drivers
    def StaffSuitability(self, Team, role):
        F1=sqlite3.connect(GAME.database)
        c=F1.cursor()
        if role=="Race Engineer":
            c.execute('''SELECT Name FROM Staff WHERE Role="Race Engineer" OR Role="Race Engineer 1" OR Role="Race Engineer 2"''')
            f=c.fetchall()
        else:
            c.execute('''SELECT Name FROM Staff WHERE Role=?''',(role,))
            f=c.fetchall()
        c.execute('''SELECT Ranking FROM Cars WHERE Team=?''',(Team,))
        Ranking=int(GAME.Sanitise(c.fetchall()[0]))
        c.execute('''SELECT Position FROM Teams WHERE Name=?''',(Team,))
        Position=int(GAME.Sanitise(c.fetchall()[0]))
        staff=[]
        for x in range(len(f)):
            name=GAME.Sanitise(f[x])
            c.execute('''SELECT Team FROM staff WHERE Name=?''',(name,))
            team=GAME.Sanitise(c.fetchall()[0])
            if (team=="Free Agent" or GAME.race>=7) and team!=Team:
                c.execute('''SELECT NewTeam FROM Staff WHERE Name=?''',(name,))
                newTeam=GAME.Sanitise(c.fetchall()[0])
                if newTeam=="0":
                    if team=="Free Agent":
                        staff.append(name)
                    else:
                        c.execute('''SELECT Ranking FROM Cars WHERE Team=?''',(team,))
                        ranking=int(GAME.Sanitise(c.fetchall()[0]))
                        c.execute('''SELECT Position FROM Teams WHERE Name=?''',(team,))
                        position=int(GAME.Sanitise(c.fetchall()[0]))
                        if Ranking<=ranking+1 or Position<=position+1 or GAME.race>=20:
                            staff.append(name)
        F1.commit()
        F1.close()
        return staff
    def Resign(self, driver):
        resigned=0
        F1=sqlite3.connect(GAME.database)
        c=F1.cursor()
        c.execute('''SELECT Role FROM Drivers WHERE Name=?''',(driver,))
        role=GAME.Sanitise(c.fetchall()[0])
        c.execute('''SELECT Team FROM Drivers WHERE Name=?''',(driver,))
        team=GAME.Sanitise(c.fetchall()[0])
        age=int(GAME.Sanitise(c.execute("SELECT Age FROM Drivers WHERE Name=?",(driver,)).fetchall()[0]))
        if role=="Junior" or role=="Reserve":
            drivers=[]
            c.execute('''SELECT Name FROM Drivers WHERE Team=? AND Role="1"''',(team,))
            drivers.append(GAME.Sanitise(c.fetchall()[0]))
            c.execute('''SELECT Name FROM Drivers WHERE Team=? AND Role="2"''',(team,))
            drivers.append(GAME.Sanitise(c.fetchall()[0]))
            replacing=[]
            resigned=0
            for x in range(2):
                if resigned==0:
                    c.execute('''SELECT NewTeam FROM Drivers WHERE Name=?''',(drivers[x],))
                    if GAME.Sanitise(c.fetchall()[0])!="0":
                        replacing.append(drivers[x])
                    else:
                        c.execute('''SELECT ContractEnd FROM Drivers WHERE Name=?''',(drivers[x],))
                        contractEnd=int(GAME.Sanitise(c.fetchall()[0]))
                        if contractEnd==GAME.season:
                            c.execute('''SELECT Role FROM Drivers WHERE Name=?''',(drivers[x],))
                            role=GAME.Sanitise(c.fetchall()[0])
                            c.execute('''SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole=?''',(team, role,))
                            f=c.fetchall()
                            if len(f)==1:
                                replacing.append(drivers[x])
                            else:
                                if random.randint(1,5)==5 and drivers[x]!="Lance Stroll":
                                    length=random.randint(1,2)
                                    GAME.news.append("BREAKING NEWS! "+team+" has extended their contract with")
                                    if length==1:
                                        GAME.news.append(f"{drivers[x]} for another season.")
                                    else:
                                        GAME.news.append(f"{drivers[x]} for another {length} seasons.")
                                    c.execute('''UPDATE Drivers SET ContractEnd=?, NewTeam=? WHERE Name=?''',(GAME.season+length, team, drivers[x],))
                                elif random.randint(1,10)==10 and age>16:
                                    length=random.randint(1,3)
                                    GAME.news.append("BREAKING NEWS! "+team+" is promoting "+driver+" to replace "+drivers[x]+" with a "+str(length)+" season contract.")
                                    c.execute('''SELECT Rating FROM Drivers WHERE Name=?''',(driver,))
                                    rating=int(GAME.Sanitise(c.fetchall()[0]))
                                    salary=random.randint(rating*37500,rating*250000)
                                    c.execute('''UPDATE Drivers SET ContractEnd=?, NewTeam=?, NewRole=?, NewSalary=? WHERE Name=?''',(GAME.season+length, team, x+1, salary, driver))
                                    resigned=1
            if resigned==0:
                if len(replacing)>=1 and age>16:
                    length=random.randint(1,4)
                    replace=replacing[len(replacing)-1]
                    c.execute('''SELECT Role FROM Drivers WHERE Name=?''',(replace,))
                    seat=GAME.Sanitise(c.fetchall()[0])
                    GAME.news.append("BREAKING NEWS! "+team+" is promoting "+driver+" to replace "+replace+" with a "+str(length)+" year contract.")
                    c.execute('''SELECT Rating FROM Drivers WHERE Name=?''',(driver,))
                    rating=int(GAME.Sanitise(c.fetchall()[0]))
                    salary=random.randint(rating*37500,rating*250000)
                    c.execute('''UPDATE Drivers SET ContractEnd=?, NewTeam=?, NewRole=?, NewSalary=? WHERE Name=?''',(GAME.season+length, team, seat, salary, driver,))
                    resigned=1
                elif (role=="Junior" and random.randint(1,10)!=10) or (role=="Reserve" and random.randint(1,4)==4):
                    length=random.randint(1,4)
                    GAME.news.append("BREAKING NEWS! "+team+" has extended their contract with")
                    if length==1:
                        GAME.news.append(f"{driver} as a {role} driver for another season.")
                    else:
                        GAME.news.append(f"{driver} as a {role} driver for another {length} seasons.")
                    resigned=1
                    c.execute('''UPDATE Drivers SET ContractEnd=?, NewTeam=? WHERE Name=?''',(GAME.season+length, team, driver,))
        else:
            c.execute('''SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole=?''',(team, role,))
            if len(c.fetchall())==1:
                resigned=0
            else:
                if random.randint(1,5)==5 and driver!="Lance Stroll":
                    resigned=1
                    length=random.randint(1,4)
                    GAME.news.append("BREAKING NEWS! "+team+" has extended their contract with")
                    if length==1:
                        GAME.news.append(f"{driver} for another season.")
                    else:
                        GAME.news.append(f"{driver} for another {length} seasons.")
                    c.execute('''UPDATE Drivers SET ContractEnd=?, NewTeam=? WHERE Name=?''',(GAME.season+length, team, driver,))
        F1.commit()
        F1.close()
        return resigned
    def Replace(self, name):
        F1=sqlite3.connect(GAME.database)
        c=F1.cursor()
        c.execute('''SELECT Team FROM Drivers WHERE Name=?''',(name,))
        f=c.fetchall()
        if len(f)==1:
            team=GAME.Sanitise(f[0])
            c.execute('''SELECT Role FROM Drivers WHERE Name=?''',(name,))
            role=GAME.Sanitise(c.fetchall()[0])
            if GAME.race<=25:
                c.execute('''SELECT Name FROM Drivers WHERE NewTeam="0" AND (Team="Free Agent" OR (Team=? AND (Role="Junior" OR Role="Reserve")))''',(team,))
                F=c.fetchall()
            else:
                c.execute('''SELECT Name FROM Drivers WHERE NewTeam="0" AND (Team!=? AND ContractEnd=?) OR (Team=? AND (Role="Junior" OR Role="Reserve")))''',(team, GAME.season, team,))
                F=c.fetchall()
            best=0
            bestIndex=0
            if random.randint(1,7)<=5:
                for x in range(len(F)):
                    c.execute('''SELECT Rating FROM Drivers WHERE Name=?''',(GAME.Sanitise(F[x]),))
                    rating=int(GAME.Sanitise(c.fetchall()[0]))
                    if rating>best:
                        best=rating
                        bestIndex=x
            else:
                for x in range(len(F)):
                    c.execute('''SELECT DevelopmentRate FROM Drivers WHERE Name=?''',(GAME.Sanitise(F[x]),))
                    developmentRate=int(GAME.Sanitise(c.fetchall()[0]))
                    if developmentRate>best:
                        best=developmentRate
                        bestIndex=x
            hired=GAME.Sanitise(F[bestIndex])
            message="BREAKING NEWS! "+team+" has hired "+hired+" to replace "+name+" as a driver."
            c.execute('''SELECT ContractEnd FROM Drivers WHERE Name=?''',(hired,))
            contractEnd=int(GAME.Sanitise(c.fetchall()[0]))
            if contractEnd==GAME.season or contractEnd==0:
                length=random.randint(1,3)
            elif contractEnd-GAME.season<3:
                length=random.randint(contractEnd-GAME.season,3)
            else:
                length=contractEnd-GAME.season
            c.execute('''SELECT Rating FROM Drivers WHERE Name=?''',(hired,))
            rating=int(GAME.Sanitise(c.fetchall()[0]))
            c.execute('''SELECT Salary FROM Drivers WHERE Name=?''',(hired,))
            currentSalary=int(GAME.Sanitise(c.fetchall()[0]))
            salary=random.randint(rating*37500,rating*250000)
            if salary<currentSalary:
                salary=currentSalary
            c.execute('''UPDATE Drivers SET Role=?, Team=?, Salary=?, ContractEnd=? WHERE Name=?''',(role, team, salary, GAME.season+length, hired,))
        else:
            c.execute('''SELECT Team FROM Staff WHERE Name=?''',(name,))
            team=GAME.Sanitise(c.fetchall()[0])
            c.execute('''SELECT Role FROM Staff WHERE Name=?''',(name,))
            role=GAME.Sanitise(c.fetchall()[0])
        F1.commit()
        F1.close()
    def PressConference(self,objective):
            GAME.ChangeScreen("Press Conference")
            F1=sqlite3.connect(GAME.database)
            c=F1.cursor()
            c.execute("UPDATE Player SET Actions=1")
            message=[]
            retirement=0
            if objective=="Upgrade":
                team=GAME.Sanitise(c.execute("SELECT Name FROM Teams WHERE Position=?",(random.randint(2,3),)).fetchall()[0])
            else:
                if GAME.race>GAME.races-3:
                    f=c.execute("SELECT Team FROM Drivers WHERE Age>35 AND NewTeam='0' AND ContractEnd=? AND Team!=? AND Team!='Dead' AND Team!='Free Agent' AND Legend=0",(GAME.season,GAME.team,)).fetchall()
                    if len(f)>0:
                        retirement=1
                        team=GAME.Sanitise(random.choice(f))
                        pressConferenceNumber=int(GAME.Sanitise(c.execute("SELECT PressConferences FROM Teams WHERE Name=?",(team,)).fetchall()[0]))+1
                if retirement==0:
                    teams=c.execute('''SELECT Name FROM Teams WHERE PressConferences=0''').fetchall()
                    if len(teams)>0:
                        pressConferenceNumber=1
                    else:
                        pressConferenceNumber=2
                        c.execute('''SELECT Name FROM Teams WHERE PressConferences=1''')
                        teams=c.fetchall()
                        if len(teams)==0:
                            c.execute('''SELECT Name FROM Teams WHERE PressConferences=2''')
                            teams=c.fetchall()
                    team=GAME.Sanitise(random.choice(teams))
            if team!=GAME.team:
                    message.append(team+" has held a press conference.")
                    swap=0
                    if team=="Red Bull" and objective==0:
                        #Swapping Red Bull Drivers
                        c.execute('''SELECT Name FROM Teams WHERE Name="Racing Bulls"''')
                        if len(c.fetchall())==1:
                            redBullPos=[]
                            c.execute('''SELECT Ranking FROM Cars WHERE Team="Red Bull"''')
                            ranking=int(GAME.Sanitise(c.fetchall()[0]))
                            c.execute('''SELECT Position FROM Drivers WHERE Team="Red Bull" and Role="1"''')
                            redBullPos.append(int(GAME.Sanitise(c.fetchall()[0])))
                            c.execute('''SELECT Position FROM Drivers WHERE Team="Red Bull" and Role="2"''')
                            redBullPos.append(int(GAME.Sanitise(c.fetchall()[0])))
                            c.execute('''SELECT Position FROM Drivers WHERE Team="Racing Bulls" and Role="1"''')
                            redBullPos.append(int(GAME.Sanitise(c.fetchall()[0])))
                            c.execute('''SELECT Position FROM Drivers WHERE Team="Racing Bulls" and Role="2"''')
                            redBullPos.append(int(GAME.Sanitise(c.fetchall()[0])))
                            moved=[]
                            c.execute('''SELECT NewTeam FROM Drivers WHERE Team="Red Bull" AND Role="1"''')
                            moved.append(GAME.Sanitise(c.fetchall()[0]))
                            c.execute('''SELECT NewTeam FROM Drivers WHERE Team="Red Bull" AND Role="2"''')
                            moved.append(GAME.Sanitise(c.fetchall()[0]))
                            if ((redBullPos[0]<=redBullPos[2] or redBullPos[0]<=redBullPos[3]) and moved[0]!="Red Bull") or ((redBullPos[1]<=redBullPos[2] or redBullPos[1]<=redBullPos[3]) and moved[1]!="Red Bull"):
                                if redBullPos[0]>redBullPos[1] and moved[0]!="Red Bull":
                                    swap=1
                                    c.execute('''SELECT Name FROM Drivers WHERE Team="Red Bull" AND Role="1"''')
                                    redBullDriver=GAME.Sanitise(c.fetchall()[0])
                                    redBullSeat=1
                                    if redBullPos[2]<=redBullPos[3]:
                                        #swap RB1 with 1
                                        c.execute('''SELECT Name FROM Drivers WHERE Team="Racing Bulls" AND Role="1"''')
                                        racingBullsDriver=GAME.Sanitise(c.fetchall()[0])
                                        racingBullsSeat=1
                                    else:
                                        #swap RB1 with 2
                                        c.execute('''SELECT Name FROM Drivers WHERE Team="Racing Bulls" AND Role="2"''')
                                        racingBullsDriver=GAME.Sanitise(c.fetchall()[0])
                                        racingBullsSeat=2
                                elif moved[1]!="Red Bull":
                                    swap=1
                                    c.execute('''SELECT Name FROM Drivers WHERE Team="Red Bull" AND Role="2"''')
                                    redBullDriver=GAME.Sanitise(c.fetchall()[0])
                                    redBullSeat=2
                                    if redBullPos[2]<=redBullPos[3]:
                                        #swap RB2 with 1
                                        c.execute('''SELECT Name FROM Drivers WHERE Team="Racing Bulls" AND Role="1"''')
                                        racingBullsDriver=GAME.Sanitise(c.fetchall()[0])
                                        racingBullsSeat=1
                                    else:
                                        #swap RB2 with 2
                                        c.execute('''SELECT Name FROM Drivers WHERE Team="Racing Bulls" AND Role="2"''')
                                        racingBullsDriver=GAME.Sanitise(c.fetchall()[0])
                                        racingBullsSeat=2
                            elif (redBullPos[0]<(ranking*2)-1 and moved[0]!="Red Bull") or (redBullPos[1]<(ranking*2)-1 and moved[1]!="Red Bull"):
                                if redBullPos[0]>redBullPos[1] and moved[0]!="Red Bull":
                                    swap=1
                                    c.execute('''SELECT Name FROM Drivers WHERE Team="Red Bull" AND Role="1"''')
                                    redBullDriver=GAME.Sanitise(c.fetchall()[0])
                                    redBullSeat=1
                                    if redBullPos[2]<=redBullPos[3]:
                                        #swap RB1 with 1
                                        c.execute('''SELECT Name FROM Drivers WHERE Team="Racing Bulls" AND Role="1"''')
                                        racingBullsDriver=GAME.Sanitise(c.fetchall()[0])
                                        oldSeat=1
                                    else:
                                        #swap RB1 with 2
                                        c.execute('''SELECT Name FROM Drivers WHERE Team="Racing Bulls" AND Role="2"''')
                                        racingBullsDriver=GAME.Sanitise(c.fetchall()[0])
                                        oldSeat=2
                                elif moved[1]!="Red Bull":
                                    swap=1
                                    c.execute('''SELECT Name FROM Drivers WHERE Team="Red Bull" AND Role="2"''')
                                    redBullDriver=GAME.Sanitise(c.fetchall()[0])
                                    redBullSeat=2
                                if redBullPos[2]<=redBullPos[3]:
                                        #swap RB2 with 1
                                        c.execute('''SELECT Name FROM Drivers WHERE Team="Racing Bulls" AND Role="1"''')
                                        racingBullsDriver=GAME.Sanitise(c.fetchall()[0])
                                        racingBullsSeat=1
                                else:
                                    #swap RB2 with 2
                                    c.execute('''SELECT Name FROM Drivers WHERE Team="Racing Bulls" AND Role="2"''')
                                    racingBullsDriver=GAME.Sanitise(c.fetchall()[0])
                                    racingBullsSeat=2
                    if swap==1:
                        topics=["Swap","Controversy"]
                    else:
                        topics=["Expectations","Expectations","Controversy"]
                    c.execute('''SELECT Name FROM Drivers WHERE Age>34 AND Team=? AND NewTeam="0" AND ContractEnd=? AND Legend=0''',(team,GAME.season,))
                    oldDrivers=c.fetchall()
                    if len(oldDrivers)>0:
                        oldest=0
                        oldestName=""
                        for x in range(len(oldDrivers)):
                            name=GAME.Sanitise(oldDrivers[x])
                            c.execute('''SELECT Age FROM Drivers WHERE Name=?''',(name,))
                            age=int(GAME.Sanitise(c.fetchall()[0]))
                            if age>oldest:
                                oldest=age
                                oldestName=name
                        if oldest<40:
                            if random.randint(1,20)==20:
                                topics.append("Retirement")
                        elif oldest<43:
                            if random.randint(1,10)==10:
                                topics.append("Retirement")
                        elif oldest<46:
                            if random.randint(1,5)==5:
                                topics.append("Retirement")
                        else:
                            topics.append("Retirement")
                    if objective=="Upgrade":
                        topic="Upgrade"
                    elif "Retirement" in topics and GAME.race>=GAME.races-5:
                        topic="Retirement"
                    else:
                        topic=random.choice(topics)
                    c.execute('''SELECT TeamPrincipal FROM Teams WHERE Name=?''',(team,))
                    teamPrincipal=GAME.Sanitise(c.fetchall()[0])
                    if topic=="Retirement":
                        message.append("They have come to announce that "+oldestName+" has decided to retire at the end of the "+str(GAME.season)+" season.")
                        c.execute('''UPDATE Drivers SET NewTeam="Retired" WHERE Name=?''',(oldestName,))
                        GAME.DisplayDriver(oldestName,520,500)
                        root.after(7500, lambda: GAME.Menu())
                    elif topic=="Swap":
                        message.append("They have decided to promote "+racingBullsDriver+" to the Red Bull team to replace "+redBullDriver+".") 
                        c.execute('''UPDATE Drivers SET Team="Racing Bulls", Role=? WHERE Name=?''',(racingBullsSeat, redBullDriver,))
                        c.execute('''UPDATE Drivers SET Team="Red Bull", Role=?, NewTeam="Red Bull" WHERE Name=?''',(redBullSeat, racingBullsDriver,))
                        c.execute('''SELECT ContractEnd FROM Drivers WHERE Name=?''',(racingBullsDriver,))
                        if int(GAME.Sanitise(c.fetchall()[0]))==GAME.season:
                            c.execute('''UPDATE Drivers SET ContractEnd=? WHERE Name=?''',(GAME.season+1, racingBullsDriver,))
                        c.execute("UPDATE Drivers SET NewTeam='Red Bull' WHERE Name=? AND NewTeam='Racing Bulls'",(racingBullsDriver,))
                        c.execute("UPDATE Drivers SET NewTeam='Racing Bulls' WHERE Name=? AND NewTeam='Red Bull'",(redBullDriver,))
                        F1.commit()
                        F1.close()
                        GAME.DisplayDriver(redBullDriver,120,500)
                        GAME.DisplayDriver(racingBullsDriver,850,500)
                        F1=sqlite3.connect(GAME.database)
                        c=F1.cursor()
                        if GAME.team=="Racing Bulls":
                            if racingBullsSeat==1:
                                GAME.car1=redBullDriver
                            else:
                                GAME.car2=redBullDriver
                        root.after(7500, lambda: GAME.Menu())
                    else:
                        if topic=="Expectations":
                            GAME.expectations=[team]
                            c.execute('''SELECT Ranking FROM Cars WHERE Team=?''',(team,))
                            ranking=int(GAME.Sanitise(c.fetchall()[0]))
                            if ranking<=2 and random.randint(1,3)>=2:
                                GAME.expectations.append("Podium")
                            elif ranking<=4 and random.randint(1,2)==2:
                                GAME.expectations.append("Top 5")
                            elif ranking<=5 and random.randint(1,3)>=2:
                                GAME.expectations.append("Double Points")
                            elif ranking<=7:
                                GAME.expectations.append("Points")
                            else:
                                GAME.expectations.append("Top 15")
                            GAME.expected=GAME.expectations.copy()
                            race=GAME.Sanitise(c.execute("SELECT Track FROM Calendar WHERE ID=?",(GAME.race,)).fetchall()[0])
                            message.append(f"{GAME.GenerateName()}: So what can we expect from {team} for {race}?")
                            message.append("")
                            if GAME.expectations[1]=="Podium":
                                message.append('"We are confident in what our team can do, we are expecting a podium and hoping for a win."')
                            else:
                                message.append(f'"We are looking at what our team can do and are expecting a {GAME.expectations[1]} finish."')
                            message.append(f"  - {teamPrincipal}")
                            for x in range(2):
                                message.append("")
                            pos=int(GAME.Sanitise(c.execute("SELECT Position FROM Teams WHERE Name=?",(team,)).fetchall()[0]))
                            previousPos=int(GAME.Sanitise(c.execute("SELECT PreviousPosition FROM Teams WHERE Name=?",(team,)).fetchall()[0]))
                            driverPos=0
                            while True:
                                if driverPos>25:
                                    break
                                else:
                                    driverPos+=1
                                    try:
                                        driver=GAME.Sanitise(c.execute("SELECT Name FROM Drivers WHERE Team=? AND Position=?",(team,driverPos,)).fetchall()[0])
                                        break
                                    except:
                                        pass
                            if previousPos!=0:
                                if previousPos-pos>0 or pos==1:
                                    message.append(f"{team} is having a great season, they are currently in P{pos} in the Championship,")
                                    message.append(f"having finished P{previousPos} last season.")
                                    message.append("")
                                    message.append(f"And {driver} is currently P{driverPos} in the Drivers' Championship.")
                                elif previousPos-pos>-2 and pos<9:
                                    message.append(f"{team} is having a decent season, they are currently in P{pos} in the Championship,")
                                    message.append("")
                                    message.append(f"And {driver} is currently P{driverPos} in the Drivers' Championship.")
                                elif previousPos-pos>-3:
                                    message.append(f"{team} isn't having a good season, they are currently in P{pos} in the Championship,")
                                    message.append("")
                                    message.append(f"And {driver} is currently P{driverPos} in the Drivers' Championship.")
                                else:
                                    message.append(f"{team} is having a terrible season, they are currently in P{pos} in the Championship,")
                                    message.append("")
                                    message.append(f"And {driver} is currently P{driverPos} in the Drivers' Championship.")
                        elif topic=="Controversy":
                            message.append(f"{GAME.GenerateName()}: What do you have to say about the allegations against you, {teamPrincipal}?")
                            message.append("")
                            if GAME.season==2026:
                                num=random.randint(1,4)
                            else:
                                num=random.randint(1,5)
                            reputation=int(GAME.Sanitise(c.execute('''SELECT Reputation FROM Teams WHERE Name=?''',(team,)).fetchall()[0]))
                            if num<=3:
                                message.append(teamPrincipal+" was able to bring clarity and resolve the situation.")
                                reputation+=random.randint(10,30)
                            elif num==5:
                                message.append(teamPrincipal+": **** ******** ************ ******** ****")
                                newTeamPrincipal=GAME.Sanitise(random.choice(c.execute("SELECT Name FROM TeamPrincipals WHERE Team='None'").fetchall()))
                                message.append(f"{team} has announced that after that, they are firing {teamPrincipal} and replacing them with")
                                message.append(f"{newTeamPrincipal} but the damage might already be done.")
                                reputation=round(reputation/3)
                                c.execute('''UPDATE Teams SET TeamPrincipal=? WHERE Name=?''',(newTeamPrincipal,team,))
                                c.execute("UPDATE TeamPrincipals SET Team='None' WHERE Team=?",(team,))
                                c.execute("UPDATE TeamPrincipals SET Team=? WHERE Name=?",(team,newTeamPrincipal,))
                            else:
                                message.append(teamPrincipal+" refused to comment.")
                                reputation-=5
                            for x in range(2):
                                message.append("")
                            pos=int(GAME.Sanitise(c.execute("SELECT Position FROM Teams WHERE Name=?",(team,)).fetchall()[0]))
                            previousPos=int(GAME.Sanitise(c.execute("SELECT PreviousPosition FROM Teams WHERE Name=?",(team,)).fetchall()[0]))
                            if previousPos!=0:
                                if num==5:
                                    if pos<previousPos:
                                        message.append(f"{teamPrincipal} was very successful in this season with {team}.")
                                        message.append(f"In the last season, they improved from P{previousPos} to P{pos} in the Championship.")
                                    elif pos==1:
                                        message.append(f"{teamPrincipal} was very successful in this season with {team}.")
                                        message.append(f"{team} are currently leading the Constructors Championship.")
                                    else:
                                        message.append(f"{teamPrincipal} wasn't very successful in this season with {team}.")
                                        message.append("It isn't a surprise that their time as Team Principal is over.")
                                else:
                                    if pos<previousPos:
                                        message.append(f"{teamPrincipal} has been very successful in this season with {team}.")
                                        message.append(f"In the last season, they have improved from P{previousPos} to P{pos} in the Championship.")
                                    elif pos==1:
                                        message.append(f"{teamPrincipal} has been very successful in this season with {team}.")
                                        message.append(f"{team} are currently leading the Constructors Championship.")
                                    else:
                                        message.append(f"{teamPrincipal} hasn't been very successful in this season with {team}.")
                                        message.append("There are questions about whether or not they should be Team Principal.")
                            if reputation>100:
                                reputation=100
                            elif reputation<1:
                                reputation=1
                            c.execute('''UPDATE Teams SET Reputation=? WHERE Name=?''',(reputation,team,))
                        elif topic=="Upgrade":
                            message.append(f"{GAME.GenerateName()}: What can we expect from {team} after the summer break?")
                            message.append("")
                            message.append(f'"We are bringing some big upgrades and hope to challenge {GAME.team}." - {teamPrincipal}')
                            for x in range(2):
                                message.append("")
                            message.append("This title battle will be one to watch.")
                            for y in range(6):
                                if y==0:
                                    stat=int(GAME.Sanitise(c.execute("SELECT DragReduction FROM Cars WHERE Team=?",(team,)).fetchall()[0]))
                                elif y==1:
                                    stat=int(GAME.Sanitise(c.execute("SELECT LowSpeed FROM Cars WHERE Team=?",(team,)).fetchall()[0]))
                                elif y==2:
                                    stat=int(GAME.Sanitise(c.execute("SELECT MediumSpeed FROM Cars WHERE Team=?",(team,)).fetchall()[0]))
                                elif y==3:
                                    stat=int(GAME.Sanitise(c.execute("SELECT HighSpeed FROM Cars WHERE Team=?",(team,)).fetchall()[0]))
                                elif y==4:
                                    stat=int(GAME.Sanitise(c.execute("SELECT Cooling FROM Cars WHERE Team=?",(team,)).fetchall()[0]))
                                else:
                                    stat=int(GAME.Sanitise(c.execute("SELECT TyrePreservation FROM Cars WHERE Team=?",(team,)).fetchall()[0]))
                                stat+=10
                                if y==0:
                                    c.execute("UPDATE Cars SET DragReduction=? WHERE Team=?",(stat,team,))
                                elif y==1:
                                    c.execute("UPDATE Cars SET LowSpeed=? WHERE Team=?",(stat,team,))
                                elif y==2:
                                    c.execute("UPDATE Cars SET MediumSpeed=? WHERE Team=?",(stat,team,))
                                elif y==3:
                                    c.execute("UPDATE Cars SET HighSpeed=? WHERE Team=?",(stat,team,))
                                elif y==4:
                                    c.execute("UPDATE Cars SET Cooling=? WHERE Team=?",(stat,team,))
                                else:
                                    c.execute("UPDATE Cars SET TyrePreservation=? WHERE Team=?",(stat,team,))
                            engine=GAME.Sanitise(c.execute("SELECT Engine FROM Cars WHERE Team=?",(team,)).fetchall()[0])
                            if engine!=GAME.engine:
                                for x in range(2):
                                    if x==0:
                                        stat=int(GAME.Sanitise(c.execute("SELECT Power FROM Engines WHERE Name=?",(engine,)).fetchall()[0]))
                                    else:
                                        stat=int(GAME.Sanitise(c.execute("SELECT Reliability FROM Engines WHERE Name=?",(engine,)).fetchall()[0]))
                                    if stat<10:
                                        stat+=1
                                        if x==0:
                                            c.execute("UPDATE Engines SET Power=? WHERE Name=?",(stat,engine,))
                                        else:
                                            c.execute("UPDATE Engines SET Reliability=? WHERE Name=?",(stat,engine,))
                        root.after(10000, lambda: GAME.Menu())
                    if team in steam:
                        appearance=team
                    else:
                        appearance=GAME.Sanitise(c.execute("SELECT Appearance FROM Teams WHERE Name=?",(team,)).fetchall()[0])
                    if appearance!="0":
                        if appearance in steam:
                            logo=logos[steam.index(appearance)-1]
                        else:
                            try:
                                logo=sponsorLogos[sponsors.index(appearance)]
                            except:
                                logo=0
                        if logo!=0:
                            canvas.image=logo
                            canvas.create_image(1250, 685, anchor=tk.NW, image=logo)
                    if topic!="Upgrade":
                        c.execute('''UPDATE Teams SET PressConferences=? WHERE Name=?''',(pressConferenceNumber,team,))
                    F1.commit()
                    F1.close()
            else:
                engine=0
                c.execute('''SELECT RegulationChange FROM Player''')
                if int(GAME.Sanitise(c.fetchall()[0]))==GAME.season+1:
                    regulationChange=1
                else:
                    regulationChange=0
                if GAME.engine not in GAME.team and not(GAME.team=="Cadillac" and GAME.season==2028):
                    if team!="Racing Bulls" or len(c.execute("SELECT Name FROM Teams WHERE Name='Red Bull'").fetchall())==0:
                        engine=1
                if GAME.Sanitise(c.execute("SELECT NextYearEngine FROM Player").fetchall()[0])!="0" or GAME.team=="Cadillac":
                    engine=0
                if engine==1:
                    message.append("PRESS CONFERENCE! You are holding a press conference as Team Principal of "+GAME.team)
                    message.append("It's time to announce to the world what engine")
                    message.append(f"{GAME.team} will be using in the {GAME.season+1} season.")
                    GAME.options=["No Change"]
                    if len(c.execute("SELECT Name FROM Engines WHERE Manufacturer=?",(GAME.team,)).fetchall())==0 and regulationChange==1:
                        GAME.options.append(GAME.team)
                    c.execute('''SELECT Name FROM Engines WHERE ((Name!="Red Bull" AND Name!=? AND Name!='Honda' AND Manufacturer!=?) OR Manufacturer="None") AND Power>0''',(GAME.engine,GAME.team))
                    engines=c.fetchall()
                    for x in range(len(engines)):
                        engine=GAME.Sanitise(engines[x])
                        GAME.options.append(engine)
                    if len(c.execute("SELECT Name FROM Engines WHERE Name='Honda' AND Manufacturer='None'").fetchall())>0:
                        GAME.options.append("Honda")
                    GAME.displayed=0
                    GAME.NextEngine()
                else:
                    offer=0
                    Position=int(GAME.Sanitise(c.execute("SELECT Position FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0]))
                    if Position<len(teams)-2 and pressConferenceNumber==2:
                        if regulationChange==1 and random.randint(1,5)>2:
                            offer=1
                        elif regulationChange==0 and random.randint(1,3)==3:
                            offer=1
                    if offer==1:
                        position=random.randint(Position+2,len(teams))
                        GAME.offer=GAME.Sanitise(c.execute("SELECT Name FROM Teams WHERE Position=?",(position,)).fetchall()[0])
                        message.append(f"{GAME.offer} would like you to be their team principal for {GAME.season+1}.")
                        if regulationChange==1:
                            message.append("They are confident in their design for next year's car.")
                        else:
                            message.append("They have decided it's time to invest more in their team.")
                            message.append(f"They think {GAME.offer} and {GAME.name} would make a good partnership.")
                        message.append("Will you accept their offer?")
                        GAME.Button("Decline",350,550)
                        GAME.Button("Accept",890,550)
                        GAME.screen="Team Offer"
                        if GAME.offer in steam:
                            appearance=GAME.offer
                        else:
                            appearance=GAME.Sanitise(c.execute("SELECT Appearance FROM Teams WHERE Name=?",(GAME.offer,)).fetchall()[0])
                        if appearance!="0":
                            if appearance in steam:
                                logo=logos[steam.index(appearance)-1]
                            else:
                                try:
                                    logo=sponsorLogos[sponsors.index(appearance)]
                                except:
                                    logo=0
                            if logo!=0:
                                canvas.image=logo
                                canvas.create_image(675, 480, anchor=tk.NW, image=logo)
                    else:
                        message.append("PRESS CONFERENCE! You are holding a press conference as Team Principal of "+GAME.team)
                        c.execute('''SELECT Track FROM Calendar WHERE ID=?''',(GAME.race,))
                        track=GAME.Sanitise(c.fetchall()[0])
                        message.append(GAME.GenerateName()+": what are your expectations for "+track+"?")
                        message.append("A higher prediction means more reputation if you're correct")
                        message.append("but you lose reputation if you're incorrect.")
                        GAME.options=["Double Podium","Podium","Top 5","Double Points","Points","Top 15"]
                        GAME.displayed=0
                        GAME.Expectations()
                c.execute('''UPDATE Teams SET PressConferences=? WHERE Name=?''',(pressConferenceNumber,GAME.team,))
                if GAME.team in steam:
                    appearance=GAME.team
                else:
                    appearance=GAME.Sanitise(c.execute("SELECT Appearance FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0])
                    if appearance!="0":
                        if appearance in steam:
                            logo=logos[steam.index(appearance)-1]
                        else:
                            try:
                                logo=sponsorLogos[sponsors.index(appearance)]
                            except:
                                logo=0
                        if logo!=0:
                            canvas.image=logo
                            canvas.create_image(1400, 730, anchor=tk.NW, image=logo)
                F1.commit()
                F1.close()
            for x in range(len(message)):
                canvas.create_text(80, 240+(x*30), text=message[x], fill="black", font=("Arial", 20), anchor="nw")
    def NextEngine(self):
        GAME.screen="Next Engine"
        GAME.Button("Name Selector",150,450)
        GAME.Button("Choose Engine",1100,520)
        engine=GAME.options[GAME.displayed]
        if engine=="No Change":
            engine=GAME.engine
            engine=f"Continue Using {engine}"
        elif engine==GAME.team:
            engine=f"New {GAME.team} Engines"
        canvas.create_text(300, 520, text=engine, fill="black", font=("Arial", 30), anchor="nw")
    def Expectations(self):
        GAME.screen="Expectations"
        GAME.Button("Name Selector",150,450)
        GAME.Button("Choose",1100,520)
        canvas.create_text(300, 520, text=GAME.options[GAME.displayed], fill="black", font=("Arial", 40), anchor="nw")
    def SponsorReview(self):
        GAME.ChangeScreen("Sponsor Review")
        if GAME.team=="McLaren" or GAME.team=="Mercedes" or GAME.team=="Red Bull" or GAME.team=="Ferrari" or GAME.team=="Williams" or GAME.team=="Racing Bulls" or GAME.team=="Aston Martin" or GAME.team=="Haas" or GAME.team=="Audi" or GAME.team=="Alpine":
            fired=-1
        else:
            fired=0
        with sqlite3.connect(GAME.database) as c:
            sponsorPay=int(GAME.Sanitise(c.execute("SELECT Pay FROM Sponsors WHERE Team=?",(GAME.team,)).fetchall()[0]))
            if sponsorPay>=70000:
                tier=3
            elif sponsorPay>50000:
                tier=2
            else:
                tier=1
            position=int(GAME.Sanitise(c.execute("SELECT Position FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0]))
            previousPosition=int(GAME.Sanitise(c.execute("SELECT PreviousPosition FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0]))
            improvement=previousPosition-position
            if position==len(c.execute("SELECT Name FROM Teams").fetchall()):
                approval=1
            elif position==1 or improvement>1 or (tier<3 and improvement>0):
                approval=4
            elif improvement==1 or (tier<3 and improvement==0):
                approval=3
            elif improvement==0 or (tier==2 and improvement==-1) or (tier==1 and improvement>-3) or position==2:
                approval=2
            else:
                approval=1

            financial=int(GAME.Sanitise(c.execute("SELECT Financial FROM Player").fetchall()[0]))
            management=int(GAME.Sanitise(c.execute("SELECT Management FROM Player").fetchall()[0]))
            if approval<3:
                if approval==2:
                    financial-=1
                    if financial<1:
                        financial=1
                else:
                    management-=1
                    if management<1:
                        management=1
                if management==1 or financial==1:
                    if fired==0:
                        fired=1
            approvals=["Happy","Satisfied","Unhappy","Disappointed"]
            consequences=["Increased Sponsor Revenue","No Change","Decreased Sponsor Revenue"]
            if fired==1:
                consequence=["End of partnership with",f"{GAME.sponsor}."]
            elif approval==1:
                consequence=["Worsened Relations with",f"{GAME.sponsor}."]
            else:
                consequence=[consequences[4-approval]]
            approval=approvals[4-approval]
            canvas.create_text(60, 230, text=f"Sponsor: {GAME.sponsor}", fill="#D4D4D4", font=("Arial", 30), anchor="nw")
            canvas.create_text(60, 420, text=f"Approval: {approval}", fill="#D4D4D4", font=("Arial", 30), anchor="nw")
            canvas.create_text(60, 470, text="Consequences:", fill="#D4D4D4", font=("Arial", 30), anchor="nw")
            for x in range(len(consequence)):
                canvas.create_text(60, 520+(50*x), text=consequence[x], fill="#D4D4D4", font=("Arial", 30), anchor="nw")
            if GAME.team in steam:
                appearance=GAME.team
            else:
                appearance=GAME.Sanitise(c.execute("SELECT Appearance FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0])
            if appearance!="0":
                if appearance in steam:
                    logo=logos[steam.index(appearance)-1]
                else:
                    try:
                        logo=sponsorLogos[sponsors.index(appearance)]
                    except:
                        logo=0
                if logo!=0:
                    canvas.image=logo
                    canvas.create_image(950, 400, anchor=tk.NW, image=logo)
            logo=sponsorLogos[sponsors.index(GAME.sponsor)]
            canvas.image=logo
            canvas.create_image(1150, 400, anchor=tk.NW, image=logo)

            reputation=int(GAME.Sanitise(c.execute("SELECT Reputation FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0]))
            income=int(GAME.Sanitise(c.execute("SELECT Income FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0]))
            if approval=="Happy":
                reputation+=20
                income+=400000
            elif approval=="Satisfied":
                reputation+=5
                income+=100000
            elif approval=="Unhappy":
                reputation-=10
            elif fired==1:
                reputation-=20
                GAME.sponsor="0"
                c.execute("UPDATE Sponsors SET Team='None' WHERE Team=?",(GAME.team,))
                c.execute("UPDATE Teams SET Sponsor='0' WHERE Name=?",(GAME.team,))
            else:
                reputation-=30
                income-=500000
            if reputation>100:
                reputation=100
            elif reputation<1:
                reputation=1
            if income<1:
                income=1
            c.execute("UPDATE Teams SET Reputation=?, Income=? WHERE Name=?",(reputation,income,GAME.team,))
            c.execute("UPDATE Player SET Financial=?, Management=?",(financial,management,))
        root.after(10000, lambda: GAME.Menu())
    def Menu(self):
        if os.path.isfile(GAME.database):
            GAME.swappable=0
            if GAME.actions==0:
                GAME.action=1
            GAME.ChangeScreen("Board Room")
            GAME.Button("Standings",400,510)
            GAME.Button("Data",950,650)
            with sqlite3.connect(GAME.database) as c:
                if int(GAME.Sanitise(c.execute("SELECT RegulationChange FROM Player").fetchall()[0]))==GAME.season+1:
                    nextEngine=GAME.Sanitise(c.execute("SELECT NextYearEngine FROM Player").fetchall()[0])
                    manufacturedEngine=c.execute("SELECT Name FROM Engines WHERE Manufacturer=?",(GAME.team,)).fetchall()
                    if len(manufacturedEngine)==0:
                        manufacturedEngine=0
                    else:
                        manufacturedEngine=GAME.Sanitise(manufacturedEngine[0])
                    if (manufacturedEngine!=0 and(nextEngine=="0" or nextEngine==manufacturedEngine)) or nextEngine=="Honda" or GAME.action==0:
                        GAME.Button("Research",870,580)
                if GAME.team=="Red Bull":
                    if len(c.execute("SELECT Name FROM Teams WHERE Name='Racing Bulls'").fetchall())==1 or len(c.execute("SELECT Name FROM Drivers WHERE Role='Reserve' AND Team='Red Bull'").fetchall())>0:
                        GAME.swappable=1
                elif GAME.team=="Racing Bulls":
                    if len(c.execute("SELECT Name FROM Drivers WHERE Role='Reserve' AND (Team='Red Bull' OR Team='Racing Bulls')").fetchall())>0:
                        GAME.swappable=1
                elif GAME.team=="Alpine":
                    if len(c.execute("SELECT Name FROM Drivers WHERE Role='Reserve' AND Team='Alpine'").fetchall())>0:
                        GAME.swappable=1
                if GAME.action==0:
                    if GAME.money>0:
                        GAME.Button("Upgrade Car",820,510)
                    GAME.Button("Scouting",350,580)
                    GAME.actions=1
                    c.execute("UPDATE Player SET Actions=1")
                else:
                    GAME.Button("View Contracts",350,580)
                    unableToRace=len(c.execute("SELECT Name FROM Drivers WHERE Team=? AND Condition!='Well'",(GAME.team,)).fetchall())
                    if unableToRace>0 and len(c.execute("SELECT Name FROM Drivers WHERE Team=? AND Role='Reserve'",(GAME.team,)).fetchall())<unableToRace:
                        GAME.Button("Hire Reserve",300,650)
                        if GAME.swappable==1:
                            GAME.swappable=0
                    GAME.actions=0
                    c.execute("UPDATE Player SET Actions=0")
                if GAME.swappable==1:
                    GAME.Button("Swap Drivers",300,650)
                #Board Finances
                if GAME.money<2000000:
                    financial=int(GAME.Sanitise(c.execute("SELECT Financial FROM Player").fetchall()[0]))
                    if GAME.money<=0:
                        financial=1
                    else:
                        if financial>2:
                            financial=3
                    c.execute("UPDATE Player SET Financial=?",(financial,))
            GAME.Button("Next Race",620,412)
            GAME.Button("Quit",5,730)
            GAME.DisplayMoney()
            GAME.BoardRoomLogo()
        else:
            GAME.ChangeScreen("Missing Required Files")
    def DisplayMoney(self):
        if GAME.money<0:
            negative=1
            money=-GAME.money
        else:
            negative=0
            money=GAME.money
        money="{:,}".format(money)
        if negative==1:
            text=f"-${money}"
        else:
            text=f"${money}"
        canvas.create_text(1190, 700, text=text, fill="#DADADA", font=("Arial", 30), anchor="nw")
    def BoardRoomLogo(self):
        if GAME.team in steam:
            appearance=GAME.team
        else:
            with sqlite3.connect(GAME.database) as c:
                appearance=GAME.Sanitise(c.execute("SELECT Appearance FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0])
        if appearance!="0":
            if appearance in steam:
                logo=logos[steam.index(appearance)-1]
            else:
                try:
                    logo=sponsorLogos[sponsors.index(appearance)]
                except:
                    logo=0
            if logo!=0:
                canvas.image=logo
                canvas.create_image(1090, 220, anchor=tk.NW, image=logo)
                canvas.create_image(240, 220, anchor=tk.NW, image=logo)
    def Hire(self,team):
        F1=sqlite3.connect(GAME.database)
        c=F1.cursor()
        gap=0
        redBull=0
        if team=="Racing Bulls":
            c.execute('''SELECT Name FROM Teams WHERE Name="Red Bull"''')
            redBull=len(c.fetchall())
        elif team=="Red Bull":
            c.execute('''SELECT Name FROM Teams WHERE Name="Racing Bulls"''')
            if len(c.fetchall())==1:
                redBull=2
        #Drivers
        #Car 1
        if random.randint(1,2)==2 or GAME.race>=GAME.races-4:
            c.execute('''SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole="1"''',(team,))
            if len(c.fetchall())==0:
                c.execute('''SELECT Name FROM Drivers WHERE Team=? AND Role="1"''',(team,))
                driver=GAME.Sanitise(c.fetchall()[0])
                c.execute('''SELECT NewTeam FROM Drivers WHERE Name=?''',(driver,))
                newTeam=GAME.Sanitise(c.fetchall()[0])
                if newTeam!="0" and newTeam!=team:
                    gap="1"
                elif newTeam=="0":
                    c.execute('''SELECT ContractEnd FROM Drivers WHERE Name=?''',(driver,))
                    contractEnd=int(GAME.Sanitise(c.fetchall()[0]))
                    if random.randint(1,3)==3 and contractEnd==GAME.season:
                        #Rehired
                        c.execute('''SELECT Salary FROM Drivers WHERE Name=?''',(driver,))
                        currentSalary=int(GAME.Sanitise(c.fetchall()[0]))
                        c.execute('''SELECT Rating FROM Drivers WHERE Name=?''',(driver,))
                        rating=int(GAME.Sanitise(c.fetchall()[0]))
                        minimumSalary=rating*37500
                        if minimumSalary<currentSalary:
                            minimumSalary=currentSalary
                        newSalary=random.randint(minimumSalary,round(minimumSalary*1.1))
                        length=random.randint(1,2)
                        GAME.news.append("BREAKING NEWS! "+team+" has extended their contract with")
                        if length==1:
                            GAME.news.append(f"{driver} for another season.")
                        else:
                            GAME.news.append(f"{driver} for another {length} seasons.")
                        c.execute('''UPDATE Drivers SET ContractEnd=?, NewSalary=?, NewTeam=?, NewRole=1 WHERE Name=?''',(GAME.season+length,newSalary,team,driver,))
                    elif contractEnd==GAME.season:
                        gap="1"

        if gap==0 and (random.randint(1,2)==2 or GAME.race>=GAME.races-4):
            #Car 2
            c.execute('''SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole="2"''',(team,))
            if len(c.fetchall())==0:
                c.execute('''SELECT Name FROM Drivers WHERE Team=? AND Role="2"''',(team,))
                driver=GAME.Sanitise(c.fetchall()[0])
                c.execute('''SELECT NewTeam FROM Drivers WHERE Name=?''',(driver,))
                newTeam=GAME.Sanitise(c.fetchall()[0])
                if newTeam!="0" and newTeam!=team:
                    gap="2"
                elif newTeam=="0":
                    c.execute('''SELECT ContractEnd FROM Drivers WHERE Name=?''',(driver,))
                    contractEnd=int(GAME.Sanitise(c.fetchall()[0]))
                    if random.randint(1,3)==3 and contractEnd==GAME.season:
                        #Rehired
                        c.execute('''SELECT Salary FROM Drivers WHERE Name=?''',(driver,))
                        currentSalary=int(GAME.Sanitise(c.fetchall()[0]))
                        c.execute('''SELECT Rating FROM Drivers WHERE Name=?''',(driver,))
                        rating=int(GAME.Sanitise(c.fetchall()[0]))
                        minimumSalary=rating*37500
                        if minimumSalary<currentSalary:
                            minimumSalary=currentSalary
                        newSalary=random.randint(minimumSalary,round(minimumSalary*1.1))
                        length=random.randint(1,2)
                        GAME.news.append("BREAKING NEWS! "+team+" has extended their contract with")
                        if length==1:
                            GAME.news.append(f"{driver} for another season.")
                        else:
                            GAME.news.append(f"{driver} for another {length} seasons.")
                        c.execute('''UPDATE Drivers SET ContractEnd=?, NewSalary=?, NewTeam=?, NewRole=2 WHERE Name=?''',(GAME.season+length,newSalary,team,driver,))
                        gap="Rehired"
                    elif contractEnd==GAME.season:
                        gap="2"
        
        if gap==0 and redBull!=1 and GAME.race<=16:
            #Reserve drivers
            c.execute('''SELECT Name FROM Drivers WHERE (Team=? AND Role="Reserve") OR (NewRole="Reserve" AND NewTeam=?)''',(team,team,))
            f=c.fetchall()
            if len(f)<3:
                gap="Reserve"
            elif len(c.execute("SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole='Reserve'",(team,)).fetchall())<3:
                f=c.execute('''SELECT Name FROM Drivers WHERE Team=? AND Role="Reserve"''',(team,)).fetchall()
                driver=GAME.Sanitise(random.choice(f))
                c.execute('''SELECT NewTeam FROM Drivers WHERE Name=?''',(driver,))
                newTeam=GAME.Sanitise(c.fetchall()[0])
                if newTeam=="0":
                    contractEnd=int(GAME.Sanitise(c.execute('''SELECT ContractEnd FROM Drivers WHERE Name=?''',(driver,)).fetchall()[0]))
                    if random.randint(1,2)==2 and contractEnd==GAME.season:
                        #Rehired
                        c.execute('''SELECT Salary FROM Drivers WHERE Name=?''',(driver,))
                        currentSalary=int(GAME.Sanitise(c.fetchall()[0]))
                        c.execute('''SELECT Rating FROM Drivers WHERE Name=?''',(driver,))
                        rating=int(GAME.Sanitise(c.fetchall()[0]))
                        minimumSalary=rating*30000
                        if minimumSalary<currentSalary:
                            minimumSalary=currentSalary
                        newSalary=random.randint(minimumSalary,round(minimumSalary*1.1))
                        length=random.randint(1,3)
                        GAME.news.append(f"BREAKING NEWS! {team} has extended their contract with")
                        if length==1:
                            GAME.news.append(f"{driver} as a Reserve driver for another season.")
                        else:
                            GAME.news.append(f"{driver} as a Reserve driver for another "+str(length)+" seasons.")
                        c.execute('''UPDATE Drivers SET ContractEnd=?, NewSalary=?, NewTeam=?, NewRole="Reserve" WHERE Name=?''',(GAME.season+length,newSalary,team,driver,))
                        gap="Rehired"

        if gap==0 and redBull!=1 and GAME.race<=11:
            #Junior drivers
            c.execute('''SELECT Name FROM Drivers WHERE (Team=? AND Role="Junior") OR (NewRole="Junior" AND NewTeam=?)''',(team,team,))
            f=c.fetchall()
            if len(f)<3:
                gap="Junior"
            elif len(c.execute("SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole='Junior'",(team,)).fetchall())<3:
                f=c.execute('''SELECT Name FROM Drivers WHERE Team=? AND Role="Junior" AND NewTeam="0"''',(team,)).fetchall()
                driver=GAME.Sanitise(random.choice(f))
                c.execute('''SELECT NewTeam FROM Drivers WHERE Name=?''',(driver,))
                contractEnd=int(GAME.Sanitise(c.execute('''SELECT ContractEnd FROM Drivers WHERE Name=?''',(driver,)).fetchall()[0]))
                if random.randint(1,2)==2 and contractEnd==GAME.season:
                    #Rehired
                    c.execute('''SELECT Salary FROM Drivers WHERE Name=?''',(driver,))
                    currentSalary=int(GAME.Sanitise(c.fetchall()[0]))
                    c.execute('''SELECT Rating FROM Drivers WHERE Name=?''',(driver,))
                    rating=int(GAME.Sanitise(c.fetchall()[0]))
                    minimumSalary=rating*25000
                    if minimumSalary<currentSalary:
                        minimumSalary=currentSalary
                    newSalary=random.randint(minimumSalary,round(minimumSalary*1.1))
                    length=random.randint(1,3)
                    GAME.news.append(f"BREAKING NEWS! {team} has extended their contract with")
                    if length==1:
                        GAME.news.append(f"{driver} as a Junior driver for another season.")
                    else:
                        GAME.news.append(f"{driver} as a Junior driver for another "+str(length)+" seasons.")
                    c.execute('''UPDATE Drivers SET ContractEnd=?, NewSalary=?, NewTeam=?, NewRole="Junior" WHERE Name=?''',(GAME.season+length,newSalary,team,driver,))
                    gap="Rehired"

        if gap==0:
            #Technical Director
            c.execute('''SELECT Name FROM Staff WHERE NewTeam=? AND NewRole="Technical Director"''',(team,))
            if len(c.fetchall())==0:
                c.execute('''SELECT Name FROM Staff WHERE Team=? AND Role="Technical Director"''',(team,))
                name=GAME.Sanitise(c.fetchall()[0])
                c.execute('''SELECT NewTeam FROM Staff WHERE Name=?''',(name,))
                newTeam=GAME.Sanitise(c.fetchall()[0])
                if newTeam!="0" and newTeam!=team:
                    gap="Technical Director"
                elif newTeam=="0" and random.randint(1,3)>1:
                    #Rehired
                    GAME.news.append(f"BREAKING NEWS! {team} has extended their contract with")
                    GAME.news.append(f"{name} as their Technical Director.")
                    c.execute('''SELECT Salary FROM Staff WHERE Name=?''',(name,))
                    currentSalary=int(GAME.Sanitise(c.fetchall()[0]))
                    c.execute('''SELECT Rating FROM Staff WHERE Name=?''',(name,))
                    rating=int(GAME.Sanitise(c.fetchall()[0]))
                    minimumSalary=rating*25000
                    if minimumSalary<currentSalary:
                        minimumSalary=currentSalary
                    newSalary=random.randint(minimumSalary,round(minimumSalary*1.1))
                    c.execute('''UPDATE Staff SET NewSalary=?, NewTeam=?, NewRole="Technical Director" WHERE Name=?''',(newSalary,team,name,))
                    gap="Rehired"
                elif newTeam=="0":
                    gap="Technical Director"

        if gap==0:
            #Sporting Director
            c.execute('''SELECT Name FROM Staff WHERE NewTeam=? AND NewRole="Sporting Director"''',(team,))
            if len(c.fetchall())==0:
                c.execute('''SELECT Name FROM Staff WHERE Team=? AND Role="Sporting Director"''',(team,))
                name=GAME.Sanitise(c.fetchall()[0])
                c.execute('''SELECT NewTeam FROM Staff WHERE Name=?''',(name,))
                newTeam=GAME.Sanitise(c.fetchall()[0])
                if newTeam!="0" and newTeam!=team:
                    gap="Sporting Director"
                elif newTeam=="0" and random.randint(1,3)>1:
                    #Rehired
                    GAME.news.append(f"BREAKING NEWS! {team} has extended their contract with")
                    GAME.news.append(f"{name} as their Sporting Director.")
                    c.execute('''SELECT Salary FROM Staff WHERE Name=?''',(name,))
                    currentSalary=int(GAME.Sanitise(c.fetchall()[0]))
                    c.execute('''SELECT Rating FROM Staff WHERE Name=?''',(name,))
                    rating=int(GAME.Sanitise(c.fetchall()[0]))
                    minimumSalary=rating*12500
                    if minimumSalary<currentSalary:
                        minimumSalary=currentSalary
                    newSalary=random.randint(minimumSalary,round(minimumSalary*1.1))
                    c.execute('''UPDATE Staff SET NewSalary=?, NewTeam=?, NewRole="Sporting Director" WHERE Name=?''',(newSalary,team,name,))
                    gap="Rehired"
                elif newTeam=="0":
                    gap="Sporting Director"

        if gap==0:
            #Race Engineer 1
            c.execute('''SELECT Name FROM Staff WHERE NewTeam=? AND NewRole="Race Engineer 1"''',(team,))
            if len(c.fetchall())==0:
                c.execute('''SELECT Name FROM Staff WHERE Team=? AND Role="Race Engineer 1"''',(team,))
                name=GAME.Sanitise(c.fetchall()[0])
                c.execute('''SELECT NewTeam FROM Staff WHERE Name=?''',(name,))
                newTeam=GAME.Sanitise(c.fetchall()[0])
                if newTeam!="0" and newTeam!=team:
                    gap="Race Engineer 1"
                elif newTeam=="0" and random.randint(1,3)>1:
                    #Rehired
                    GAME.news.append(f"BREAKING NEWS! {team} has extended their contract with")
                    GAME.news.append(f"{name} as a Race Engineer.")
                    c.execute('''SELECT Salary FROM Staff WHERE Name=?''',(name,))
                    currentSalary=int(GAME.Sanitise(c.fetchall()[0]))
                    c.execute('''SELECT Rating FROM Staff WHERE Name=?''',(name,))
                    rating=int(GAME.Sanitise(c.fetchall()[0]))
                    minimumSalary=rating*12500
                    if minimumSalary<currentSalary:
                        minimumSalary=currentSalary
                    newSalary=random.randint(minimumSalary,round(minimumSalary*1.1))
                    c.execute('''UPDATE Staff SET NewSalary=?, NewTeam=?, NewRole="Race Engineer 1" WHERE Name=?''',(newSalary,team,name,))
                    gap="Rehired"
                elif newTeam=="0":
                    gap="Race Engineer 1"

        if gap==0:
            #Race Engineer 2
            c.execute('''SELECT Name FROM Staff WHERE NewTeam=? AND NewRole="Race Engineer 2"''',(team,))
            if len(c.fetchall())==0:
                c.execute('''SELECT Name FROM Staff WHERE Team=? AND Role="Race Engineer 2"''',(team,))
                name=GAME.Sanitise(c.fetchall()[0])
                c.execute('''SELECT NewTeam FROM Staff WHERE Name=?''',(name,))
                newTeam=GAME.Sanitise(c.fetchall()[0])
                if newTeam!="0" and newTeam!=team:
                    gap="Race Engineer 2"
                elif newTeam=="0" and random.randint(1,3)>1:
                    #Rehired
                    GAME.news.append(f"BREAKING NEWS! {team} has extended their contract with")
                    GAME.news.append(f"{name} as a Race Engineer.")
                    c.execute('''SELECT Salary FROM Staff WHERE Name=?''',(name,))
                    currentSalary=int(GAME.Sanitise(c.fetchall()[0]))
                    c.execute('''SELECT Rating FROM Staff WHERE Name=?''',(name,))
                    rating=int(GAME.Sanitise(c.fetchall()[0]))
                    minimumSalary=rating*12500
                    if minimumSalary<currentSalary:
                        minimumSalary=currentSalary
                    newSalary=random.randint(minimumSalary,round(minimumSalary*1.1))
                    c.execute('''UPDATE Staff SET NewSalary=?, NewTeam=?, NewRole="Race Engineer 2" WHERE Name=?''',(newSalary,team,name,))
                    gap="Rehired"
                elif newTeam=="0":
                    gap="Race Engineer 2"

        if gap==0:
            F1.commit()
            F1.close()
            GAME.Upgrade(team)
            F1=sqlite3.connect(GAME.database)
            c=F1.cursor()
        elif len(c.execute("SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole=?",(team,gap,)).fetchall())==0 and len(c.execute("SELECT Name FROM Staff WHERE NewTeam=? AND NewRole=?",(team,gap,)).fetchall())==0:
            if gap=="1" or gap=="2":
                promoted=0
                if redBull==0:
                    if team=="Ferrari" and len(c.execute("SELECT Team FROM Cars WHERE Team='Haas' AND Engine='Ferrari'").fetchall())>0:
                        c.execute('''SELECT Name FROM Drivers WHERE ((Team=? AND (Role="Junior" OR Role="Reserve")) OR (Team="Haas" AND (Role="1" OR Role="2"))) AND Age>16''',(team,))
                    else:
                        c.execute('''SELECT Name FROM Drivers WHERE Team=? AND (Role="Junior" OR Role="Reserve") AND Age>16''',(team,))
                elif redBull==2:
                    c.execute('''SELECT Name FROM Drivers WHERE (Team="Red Bull" AND (Role="Junior" OR Role="Reserve")) OR Team="Racing Bulls" AND Age>16''')
                else:
                    c.execute('''SELECT Name FROM Drivers WHERE Team="Red Bull" AND (Role="Junior" OR Role="Reserve") AND Age>16''')
                juniors=c.fetchall()
                if len(juniors)>0 and random.randint(1,4)==4:
                    promoted=1
                    if len(juniors)==1:
                        hiredDriver=GAME.Sanitise(juniors[0])
                        c.execute('''SELECT Rating FROM Drivers WHERE Name=?''',(hiredDriver,))
                        highest=int(GAME.Sanitise(c.fetchall()[0]))
                    else:
                        highest=0
                        hiredDriver=0
                        for x in range(len(juniors)):
                            name=GAME.Sanitise(juniors[x])
                            c.execute('''SELECT Rating FROM Drivers WHERE Name=?''',(name,))
                            rating=int(GAME.Sanitise(c.fetchall()[0]))
                            if rating>highest:
                                highest=rating
                                hiredDriver=name
                    c.execute('''SELECT NewTeam FROM Drivers WHERE Name=?''',(hiredDriver,))
                    if GAME.Sanitise(c.fetchall()[0])!="0":
                        promoted=0
                if promoted==0:
                    promoted=0
                    drivers=GAME.DriverSuitability(team)
                    removed=0
                    for x in range(len(drivers)):
                        c.execute('''SELECT Name FROM Drivers WHERE Name=? AND NewTeam="0" AND Age>16 AND (ContractEnd=? OR Team="Free Agent")''',(drivers[x-removed],GAME.season,))
                        if len(c.fetchall())==0:
                            drivers.pop(x-removed)
                            removed+=1
                    driverPool=[]
                    for x in range(15):
                        if len(drivers)>0:
                            driver=random.choice(drivers)
                            drivers.remove(driver)
                            driverPool.append(driver)
                    ratings=[]
                    for x in range(len(driverPool)):
                        c.execute('''SELECT Rating FROM Drivers WHERE Name=?''',(driverPool[x],))
                        ratings.append(int(GAME.Sanitise(c.fetchall()[0])))
                    highest=0
                    highestIndex=0
                    for x in range(len(driverPool)):
                        if ratings[x]>highest:
                            highest=ratings[x]
                            highestIndex=x
                    if len(driverPool)==0:
                        for x in range(10):
                            GAME.GeneratePeople("Driver")
                        c.execute('''SELECT Name FROM Drivers WHERE NewTeam="0" AND (Team="Free Agent" OR ContractEnd=?) AND Age>16''',(GAME.season,))
                        driverPool.append(GAME.Sanitise(c.fetchall()[0]))
                    hiredDriver=driverPool[highestIndex]
                minimumSalary=highest*40000
                c.execute('''SELECT Salary FROM Drivers WHERE Name=?''',(hiredDriver,))
                currentSalary=int(GAME.Sanitise(c.fetchall()[0]))
                if minimumSalary<currentSalary:
                    minimumSalary=currentSalary
                salary=random.randint(minimumSalary,round(minimumSalary*1.1))
                length=random.randint(1,3)
                c.execute('''SELECT Name FROM Drivers WHERE Team=? AND Role=?''',(team,gap,))
                f=c.fetchall()
                if promoted==1:
                    message="promoted "
                else:
                    message="hired "
                GAME.news.append("BREAKING NEWS! "+team+" has "+message+hiredDriver)
                if len(f)>0:
                    replacing=GAME.Sanitise(f[0])
                    if length==1:
                        GAME.news.append("to replace "+replacing+" for the "+str(GAME.season+1)+" season.")
                    else:
                        GAME.news.append("to replace "+replacing+" for the next "+str(length)+" seasons.")
                else:
                    replacing=0
                    if length==1:
                        GAME.news.append("for the "+str(GAME.season+1)+" season.")
                    else:
                        GAME.news.append("for the next "+str(length)+" seasons.")
                c.execute('''UPDATE Drivers SET NewTeam=?, NewSalary=?, NewRole=?, ContractEnd=? WHERE Name=?''',(team,salary,gap,GAME.season+length,hiredDriver,))
                if GAME.Sanitise(c.execute("SELECT Team FROM Drivers WHERE Name=?",(hiredDriver,)).fetchall()[0])==GAME.team:
                    oldRole=GAME.Sanitise(c.execute("SELECT Role FROM Drivers WHERE Name=?",(hiredDriver,)).fetchall()[0])
                    if len(c.execute("SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole=?",(GAME.team,oldRole,)).fetchall())==0:
                        management=int(GAME.Sanitise(c.execute("SELECT Management FROM Player").fetchall()[0]))-1
                        if management<1:
                            management=1
                        c.execute("UPDATE Player SET Management=?",(management,))
            elif gap=="Junior" or gap=="Reserve":
                promoted=0
                if gap=="Reserve":
                    c.execute('''SELECT Name FROM Drivers WHERE Team=? AND Role="Junior" AND Age>16''',(team,))
                    f=c.fetchall()
                    if len(f)>0:
                        drivers=[]
                        ratings=[]
                        for x in range(len(f)):
                            driver=GAME.Sanitise(f[x])
                            drivers.append(driver)
                            c.execute('''SELECT Rating FROM Drivers WHERE Name=?''',(driver,))
                            ratings.append(int(GAME.Sanitise(c.fetchall()[0])))
                        highest=0
                        highestIndex=0
                        for x in range(len(drivers)):
                            if ratings[x]>highest:
                                highest=ratings[x]
                                highestIndex=x
                        hiredDriver=drivers[highestIndex]
                        rating=highest
                        promoted=1
                if promoted==0:
                    c.execute('''SELECT Name FROM Drivers WHERE (Team=? AND Role="Junior") OR (NewTeam=? AND NewRole="Junior")''',(team,team,))
                    if len(c.fetchall())<3:
                        gap="Junior"
                        GAME.scouting="Junior Driver"
                        drivers=GAME.DriverSuitability(team)
                        GAME.scouting=0
                        removed=0
                        for x in range(len(drivers)):
                            c.execute('''SELECT Name FROM Drivers WHERE Name=? AND Team!=? AND NewTeam="0" AND Age<17 AND Role="Free Agent" AND ContractEnd=?''',(drivers[x-removed],team,GAME.season,))
                            if len(c.fetchall())==0:
                                drivers.pop(x-removed)
                                removed+=1
                        driverPool=[]
                        for x in range(15):
                            if len(drivers)>0:
                                driver=random.choice(drivers)
                                drivers.remove(driver)
                                driverPool.append(driver)
                        ratings=[]
                        if random.randint(1,2)==1 or gap=="Reserve":
                            for x in range(len(driverPool)):
                                c.execute('''SELECT Rating FROM Drivers WHERE Name=?''',(driverPool[x],))
                                ratings.append(int(GAME.Sanitise(c.fetchall()[0])))
                        else:
                            for x in range(len(driverPool)):
                                c.execute('''SELECT DevelopmentRate FROM Drivers WHERE Name=?''',(driverPool[x],))
                                ratings.append(int(GAME.Sanitise(c.fetchall()[0])))
                        highest=0
                        highestIndex=0
                        for x in range(len(driverPool)):
                            if ratings[x]>highest:
                                highest=ratings[x]
                                highestIndex=x
                        if len(driverPool)==0:
                            F1.commit()
                            F1.close()
                            for x in range(10):
                                GAME.GeneratePeople("Driver")
                            F1=sqlite3.connect(GAME.database)
                            c=F1.cursor()
                            c.execute('''SELECT Name FROM Drivers WHERE NewTeam="0" AND Team="Free Agent" AND Age<21 AND Condition="Well"''')
                            driverPool.append(GAME.Sanitise(c.fetchall()[0]))
                        hiredDriver=driverPool[highestIndex]
                        c.execute('''SELECT Rating FROM Drivers WHERE Name=?''',(hiredDriver,))
                        rating=int(GAME.Sanitise(c.fetchall()[0]))
                    else:
                        gap=0
                        F1.commit()
                        F1.close()
                        GAME.Upgrade(team)
                        F1=sqlite3.connect(GAME.database)
                        c=F1.cursor()
                if gap!=0:
                    minimumSalary=rating*3500
                    c.execute('''SELECT Salary FROM Drivers WHERE Name=?''',(hiredDriver,))
                    currentSalary=int(GAME.Sanitise(c.fetchall()[0]))
                    if minimumSalary<currentSalary:
                        minimumSalary=currentSalary
                    length=random.randint(1,4)
                    salary=random.randint(minimumSalary,round(minimumSalary*1.1))
                    if length==1:
                        GAME.news.append(f"BREAKING NEWS! {team} has hired {hiredDriver}")
                        GAME.news.append(f"as a {gap} Driver for the {GAME.season+1} season.")
                    else:
                        GAME.news.append(f"BREAKING NEWS! {team} has hired {hiredDriver}")
                        GAME.news.append(f"as a {gap} Driver for the next {length} seasons.")
                    c.execute('''UPDATE Drivers SET NewTeam=?, NewSalary=?, NewRole=?, ContractEnd=? WHERE Name=?''',(team,salary,gap,GAME.season+length,hiredDriver,))
                    if GAME.Sanitise(c.execute("SELECT Team FROM Drivers WHERE Name=?",(hiredDriver,)).fetchall()[0])==GAME.team:
                        oldRole=GAME.Sanitise(c.execute("SELECT Role FROM Drivers WHERE Name=?",(hiredDriver,)).fetchall()[0])
                        if len(c.execute("SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole=?",(GAME.team,oldRole,)).fetchall())==0:
                            management=int(GAME.Sanitise(c.execute("SELECT Management FROM Player").fetchall()[0]))-1
                            if management<1:
                                management=1
                            c.execute("UPDATE Player SET Management=?",(management,))
            elif gap!="Rehired":
                if gap=="Race Engineer 1" or gap=="Race Engineer 2":
                    role="Race Engineer"
                else:
                    role=gap
                staff=GAME.StaffSuitability(team,role)
                pool=[]
                for x in range(8):
                    if len(staff)>0:
                        S=random.choice(staff)
                        staff.remove(S)
                        c.execute('''SELECT Name FROM Staff WHERE Name=? AND NewTeam="0"''',(S,))
                        if len(c.fetchall())>0:
                            pool.append(S)
                ratings=[]
                for x in range(len(pool)):
                    c.execute('''SELECT Rating FROM Staff WHERE Name=?''',(pool[x],))
                    ratings.append(int(GAME.Sanitise(c.fetchall()[0])))
                highest=-1000000
                highestIndex=0
                for x in range(len(pool)):
                    if ratings[x]>highest:
                        highest=ratings[x]
                        highestIndex=x
                if len(pool)==0:
                    for x in range(10):
                        GAME.GeneratePeople(role)
                else:
                    hired=pool[highestIndex]
                    GAME.news.append(f"BREAKING NEWS! {team} has hired {hired} as a")
                    GAME.news.append(f"{role} for the {GAME.season+1} season.")
                    c.execute('''UPDATE Staff SET NewTeam=?, NewRole=? WHERE Name=?''',(team,gap,hired))
                    if GAME.Sanitise(c.execute("SELECT Team FROM Staff WHERE Name=?",(hired,)).fetchall()[0])==GAME.team:
                        oldRole=GAME.Sanitise(c.execute("SELECT Role FROM Staff WHERE Name=?",(hired,)).fetchall()[0])
                        if len(c.execute("SELECT Name FROM Staff WHERE NewTeam=? AND NewRole=?",(GAME.team,oldRole,)).fetchall())==0:
                            management=int(GAME.Sanitise(c.execute("SELECT Management FROM Player").fetchall()[0]))-1
                            if management<1:
                                management=1
                            c.execute("UPDATE Player SET Management=?",(management,))
        F1.commit()
        F1.close()
    def Poach(self,team):
        with sqlite3.connect(GAME.database) as c:
            options=[]
            rating1=int(GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Team=? AND Role='1'",(team,)).fetchall()[0]))
            rating2=int(GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Team=? AND Role='2'",(team,)).fetchall()[0]))
            if len(c.execute("SELECT Name FROM Drivers WHERE (Team=? AND Role='1' AND (ContractEnd=? OR (NewTeam!='0' AND NewTeam!=?))) OR (NewTeam=? AND NewRole='1')",(team,GAME.season,team,team,)).fetchall())==0:
                driver1=0
            else:
                driver1=1
            if len(c.execute("SELECT Name FROM Drivers WHERE (Team=? AND Role='2' AND (ContractEnd=? OR (NewTeam!='0' AND NewTeam!=?))) OR (NewTeam=? AND NewRole='2')",(team,GAME.season,team,team,)).fetchall())==0:
                driver2=0
            else:
                driver2=1
        if driver1!=0 or driver2!=0:
            with sqlite3.connect(GAME.database) as c:
                if driver1==0:
                    rating=rating2
                    role="2"
                elif driver2==0:
                    rating=rating1
                    role="1"
                elif rating2>rating1:
                    rating=rating1
                    role="1"
                else:
                    rating=rating2
                    role="2"
                f=c.execute("SELECT Name FROM Drivers WHERE Team='Free Agent' AND Condition='Well' AND Rating>? AND NewTeam='0' AND Age>16",(rating,)).fetchall()
                if len(f)>0:
                    for x in range(len(f)):
                        options.append(GAME.Sanitise(f[x]))
                f=c.execute("SELECT Name FROM Drivers WHERE Team=? AND ContractEnd=? AND Condition='Well' AND Rating>? AND Age>16",(GAME.team,GAME.season,rating,)).fetchall()#
                if len(f)>0:
                    position=int(GAME.Sanitise(c.execute("SELECT Position FROM Teams WHERE Name=?",(team,)).fetchall()[0]))
                    Position=int(GAME.Sanitise(c.execute("SELECT Position FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0]))
                    if position<Position+3:
                        for x in range(len(f)):
                            options.append(GAME.Sanitise(f[x]))
                name="Max Verstappen"
                highestRating=0
                for x in range(len(options)):
                    rating=int(GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Name=?",(options[x],)).fetchall()[0]))
                    if rating>highestRating:
                        name=options[x]
                        highestRating=rating
                minimumSalary=highestRating*40000
                currentSalary=int(GAME.Sanitise(c.execute('''SELECT Salary FROM Drivers WHERE Name=?''',(name,)).fetchall()[0]))
                if minimumSalary<currentSalary:
                    minimumSalary=currentSalary
                salary=random.randint(minimumSalary,round(minimumSalary*1.1))
                length=random.randint(1,3)
                GAME.news.append("BREAKING NEWS! "+team+" has hired "+name)
                replacing=GAME.Sanitise(c.execute("SELECT Name FROM Drivers WHERE Team=? AND Role=?",(team,role,)).fetchall()[0])
                if length==1:
                    GAME.news.append("to replace "+replacing+" for the "+str(GAME.season+1)+" season.")
                else:
                    GAME.news.append("to replace "+replacing+" for the next "+str(length)+" seasons.")
                c.execute('''UPDATE Drivers SET NewTeam=?, NewSalary=?, NewRole=?, ContractEnd=? WHERE Name=?''',(team,salary,role,GAME.season+length,name,))
                if GAME.Sanitise(c.execute("SELECT Team FROM Drivers WHERE Name=?",(name,)).fetchall()[0])==GAME.team:
                    oldRole=GAME.Sanitise(c.execute("SELECT Role FROM Drivers WHERE Name=?",(name,)).fetchall()[0])
                    if len(c.execute("SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole=?",(GAME.team,oldRole,)).fetchall())==0:
                        management=int(GAME.Sanitise(c.execute("SELECT Management FROM Player").fetchall()[0]))-1
                        if management<1:
                            management=1
                        c.execute("UPDATE Player SET Management=?",(management,))
        else:
            GAME.Upgrade(team)
    def ActionRound(self):
        GAME.CarRanking()
        GAME.news=[]
        GAME.scouting=0
        if GAME.actions==3:
            if GAME.races==27 or GAME.races==28:
                if GAME.race%2==1 and GAME.race!=9 and GAME.race!=19:
                    GAME.Income()
            elif GAME.races==25 or GAME.races==26:
                if GAME.race%2==1 and GAME.race!=13:
                    GAME.Income()
            elif GAME.races==23 or GAME.races==24:
                if GAME.race%2==1:
                    GAME.Income()
            elif GAME.races==21 or GAME.races==22:
                if GAME.race%2==1 or GAME.race==10:
                    GAME.Income()
            elif GAME.races==19 or GAME.races==20:
                if GAME.race%2==1 or GAME.race==6 or GAME.race==14:
                    GAME.Income()
            elif GAME.races==17 or GAME.races==18:
                if GAME.race%2==1 or GAME.race%4==0:
                    GAME.Income()
            with sqlite3.connect(GAME.database) as c:
                if len(c.execute("SELECT Name FROM Teams WHERE Name='Red Bull'").fetchall())>0:
                    c.execute("UPDATE Drivers SET NewTeam='Red Bull' WHERE NewTeam='Racing Bulls' AND (NewRole='Junior' OR NewRole='Reserve')")
                    c.execute("UPDATE Drivers SET Team='Red Bull' WHERE Team='Racing Bulls' AND (Role='Junior' OR Role='Reserve')")
                f=c.execute('''SELECT Name FROM Teams''').fetchall()
                regulationChange=int(GAME.Sanitise(c.execute('''SELECT RegulationChange FROM Player''').fetchall()[0]))
                GAME.car1=GAME.Sanitise(c.execute('''SELECT Name FROM Drivers WHERE Team=? AND Role="1"''',(GAME.team,)).fetchall()[0])
                GAME.car2=GAME.Sanitise(c.execute('''SELECT Name FROM Drivers WHERE Team=? AND Role="2"''',(GAME.team,)).fetchall()[0])
                #Events

                #Illness
                driver=0
                dead=[]
                deadTeam=[]
                if random.randint(1,40)==40:
                    driver=GAME.Sanitise(random.choice(c.execute('''SELECT Name FROM Drivers WHERE Condition="Well" AND (Role="1" OR Role="2")''').fetchall()))
                    GAME.news.append("BREAKING NEWS! "+driver+" is ill and will be unable to race in the next Grand Prix.")
                    c.execute('''UPDATE Drivers SET Condition="Ill" WHERE Name=?''',(driver,))
                else:
                    fetch=c.execute('''SELECT Name FROM Drivers WHERE Condition="Ill" or Condition="Injured"''').fetchall()
                    for y in range(len(fetch)):
                        name=GAME.Sanitise(fetch[y])
                        if random.randint(1,3)==3:
                            GAME.news.append("BREAKING NEWS! "+name+" has recovered and will be able to race again.")
                            c.execute('''UPDATE Drivers SET Condition="Well" WHERE Name=?''',(name,))
                        elif random.randint(1,80)==80 and GAME.season>2026:
                            condition=GAME.Sanitise(c.execute('''SELECT Condition FROM Drivers WHERE Name=?''',(name,)).fetchall()[0])
                            if condition=="Ill":
                                causeOfDeath="illness"
                            else:
                                causeOfDeath="injuries"
                            message="BREAKING NEWS! It is a sad day because "+name+" has died from their "+causeOfDeath+", they will be missed."
                            GAME.news.append(message)
                            dead.append(name)
                            deadTeam.append(GAME.Sanitise(c.execute('''SELECT Team FROM Drivers WHERE Name=?''',(name,)).fetchall()[0]))
            if len(dead)>0:
                for x in range(len(dead)):
                    if deadTeam[x]==GAME.team:
                        GAME.YourDriverDied(dead[x])
                    else:
                        GAME.Replace(dead[x])
                    with sqlite3.connect(GAME.database) as c:
                        c.execute('''UPDATE Drivers SET Condition="Dead", Team="Dead", Role="Dead", NewTeam="Dead" WHERE Name=?''',(dead[x],))
            #Legends
            if GAME.legends==1:
                hired=0
                if len(c.execute("SELECT Name FROM Drivers WHERE Legend=?",(GAME.season,)).fetchall())<3 and random.randint(1,8)<3:
                    tier=random.randint(1,4)
                    legends=c.execute("SELECT Name FROM Drivers WHERE Condition='Legend' AND Legend<=?",(tier,)).fetchall()
                    if len(legends)==0 and tier<3:
                        legends=c.execute("SELECT Name FROM Drivers WHERE Condition='Legend' AND Legend<=3").fetchall()
                    if tier>2:
                        primes=c.execute("SELECT Name FROM Drivers WHERE (Name='Lewis Hamilton' OR Name='Fernando Alonso') AND Legend=0").fetchall()
                    else:
                        primes=[]
                    if len(legends)>0:
                        num=random.randint(0,len(legends)+len(primes)-1)
                        if num<len(legends):
                            legend=GAME.Sanitise(legends[num])
                            position=random.randint(1,6-tier)
                            with sqlite3.connect(GAME.database) as c:
                                team=GAME.Sanitise(c.execute("SELECT Name FROM Teams WHERE Position=?",(position,)).fetchall()[0])
                                if team!=GAME.team:
                                    seats=[]
                                    for x in range(2):
                                        if len(c.execute("SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole=?",(team,str(x+1),)).fetchall())==0:
                                            seats.append(str(x+1))
                                    if len(seats)>0:
                                        if len(seats)==1:
                                            seat=seats[0]
                                        else:
                                            position1=int(GAME.Sanitise(c.execute("SELECT Position FROM Drivers WHERE Team=? AND Role='1'",(team,)).fetchall()[0]))
                                            position2=int(GAME.Sanitise(c.execute("SELECT Position FROM Drivers WHERE Team=? AND Role='2'",(team,)).fetchall()[0]))
                                            if position1<position2:
                                                seat="2"
                                            else:
                                                seat="1"
                                        rating=int(GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Team=? AND Role=?",(team,seat,)).fetchall()[0]))
                                        legendRating=int(GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Name=?",(legend,)).fetchall()[0]))
                                        if legendRating>rating:
                                            hired=1
                                            replacing=GAME.Sanitise(c.execute("SELECT Name FROM Drivers WHERE Team=? AND Role=?",(team,seat,)).fetchall()[0])
                                            c.execute("UPDATE Drivers SET ContractEnd=? WHERE Team=? AND Role=? AND NewTeam='0'",(GAME.season,team,seat,))
                                            tier=int(GAME.Sanitise(c.execute("SELECT Legend FROM Drivers WHERE Name=?",(legend,)).fetchall()[0]))
                                            salary=((legendRating*tier*random.randint(150000,250000))//100000)*100000
                                            c.execute("UPDATE Drivers SET NewTeam=?, NewRole=?, NewSalary=?, ContractEnd=?, Legend=?, Condition='Well' WHERE Name=?",(team,seat,salary,GAME.season+1,GAME.season,legend))
                                            GAME.news.append("BREAKING NEWS! "+team+" has hired "+legend)
                                            GAME.news.append("to replace "+replacing+" for the "+str(GAME.season+1)+" season.")
                        else:
                            with sqlite3.connect(GAME.database) as c:
                                legend=GAME.Sanitise(primes[num-len(legends)])
                                if legend=="Lewis Hamilton":
                                    rating=round((554+int(GAME.Sanitise(c.execute("SELECT Experience FROM Drivers WHERE Name='Lewis Hamilton'").fetchall()[0])))/6)
                                    c.execute("UPDATE Drivers SET Rating=?, Overtaking=110, Defending=100, Pace=150, Control=100 WHERE Name='Lewis Hamilton'",(rating,))
                                else:
                                    rating=round((624+int(GAME.Sanitise(c.execute("SELECT Experience FROM Drivers WHERE Name='Fernando Alonso'").fetchall()[0])))/6)
                                    c.execute("UPDATE Drivers SET Rating=?, Overtaking=100, Defending=200, Pace=130, Control=100 WHERE Name='Fernando Alonso'",(rating,))
                                c.execute("UPDATE Drivers SET Legend=? WHERE Name=?",(GAME.season,legend,))
                                Team=GAME.Sanitise(c.execute("SELECT Team FROM Drivers WHERE Name=?",(legend,)).fetchall()[0])
                                if Team=="Retired" or Team=="Free Agent" and len(c.execute("SELECT Name FROM Drivers WHERE Name=? AND (NewTeam=0 OR NewTeam=?)",(legend,Team,)).fetchall())>0:
                                    position=random.randint(1,3)
                                    team=GAME.Sanitise(c.execute("SELECT Name FROM Teams WHERE Position=?",(position,)).fetchall()[0])
                                    if team!=GAME.team:
                                        seats=[]
                                        for x in range(2):
                                            if len(c.execute("SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole=?",(team,str(x+1),)).fetchall())==0:
                                                seats.append(str(x+1))
                                        if len(seats)>0:
                                            if len(seats)==1:
                                                seat=seats[0]
                                            else:
                                                position1=int(GAME.Sanitise(c.execute("SELECT Position FROM Drivers WHERE Team=? AND Role='1'",(team,)).fetchall()[0]))
                                                position2=int(GAME.Sanitise(c.execute("SELECT Position FROM Drivers WHERE Team=? AND Role='2'",(team,)).fetchall()[0]))
                                                if position1<position2:
                                                    seat="2"
                                                else:
                                                    seat="1"
                                            rating=int(GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Team=? AND Role=?",(team,seat,)).fetchall()[0]))
                                            legendRating=int(GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Name=?",(legend,)).fetchall()[0]))
                                            if legendRating>rating:
                                                hired=1
                                                replacing=GAME.Sanitise(c.execute("SELECT Name FROM Drivers WHERE Team=? AND Role=?",(team,seat,)).fetchall()[0])
                                                c.execute("UPDATE Drivers SET ContractEnd=? WHERE Team=? AND Role=? AND NewTeam='0'",(GAME.season,team,seat,))
                                                tier=int(GAME.Sanitise(c.execute("SELECT Legend FROM Drivers WHERE Name=?",(legend,)).fetchall()[0]))
                                                salary=((legendRating*tier*random.randint(150000,250000))//100000)*100000
                                                c.execute("UPDATE Drivers SET NewTeam=?, NewRole=?, NewSalary=?, ContractEnd=?, Legend=?, Condition='Well' WHERE Name=?",(team,seat,salary,GAME.season+1,GAME.season,legend))
                                                GAME.news.append(f"BREAKING NEWS! {legend} has returned to his prime and has signed a contract with {team}")
                                                GAME.news.append("to replace "+replacing+" for the "+str(GAME.season+1)+" season.")
                                    if hired==0:
                                        if Team=="Retired":
                                            GAME.news.append(f"BREAKING NEWS! {legend} has returned to his prime and ended his retirement.")
                                        else:
                                            GAME.news.append(f"BREAKING NEWS! {legend} has returned to his prime and is open to a Formula 1 seat.")
                                else:
                                    GAME.news.append(f"BREAKING NEWS! {legend} has returned to his prime.")
                            
            #Contract Clauses
            if GAME.race==13:
                with sqlite3.connect(GAME.database) as c:
                    if GAME.season<2028:
                        c.execute("UPDATE Drivers SET ContractEnd=? WHERE Name='Max Verstappen' AND Team='Red Bull' AND Role='1' AND Position>? AND NewTeam='0'",(GAME.season,2028-GAME.season,))
                    if GAME.season==2026:
                        ferrariPos=int(GAME.Sanitise(c.execute("SELECT Position FROM Teams WHERE Name='Ferrari'").fetchall()[0]))
                        if ferrariPos>3 or (ferrariPos==3 and random.randint(1,5)<3):
                            c.execute("UPDATE Drivers SET ContractEnd=2026 WHERE Name='Charles Leclerc' AND Position>3 AND NewTeam='0'")
                        landoPos=int(GAME.Sanitise(c.execute("SELECT Position FROM Drivers WHERE Name='Lando Norris'").fetchall()[0]))
                        c.execute("UPDATE Drivers SET COntractEnd=2026 WHERE Name='Oscar Piastri' AND Position>? AND Position>3",(landoPos+2,))
                        if GAME.team!="Mercedes":
                            kimiPos=int(GAME.Sanitise(c.execute("SELECT Position FROM Drivers WHERE Name='Kimi Antonelli'").fetchall()[0]))
                            c.execute("UPDATE Drivers SET ContractEnd=2026 WHERE Name='George Russell' AND NewTeam='0' AND Position>?",(kimiPos,))
                    if GAME.team!="Aston Martin" and len(c.execute("SELECT Name FROM Drivers WHERE NewTeam='Aston Martin' AND NewRole='1'").fetchall())==0:
                        c.execute("UPDATE Drivers SET ContractEnd=?, NewTeam='Aston Martin', NewRole='1' WHERE Name='Lance Stroll' AND NewTeam='0' AND Team='Aston Martin' AND Role='1'",(GAME.season+1,))
                    
            #Actions
            if GAME.race>=8:
                poacher=0
            else:
                poacher=GAME.Sanitise(random.choice(f))
                if poacher==GAME.team:
                    while poacher==GAME.team:
                        poacher=GAME.Sanitise(random.choice(f))
            for x in range(len(f)):
                team=GAME.Sanitise(f[x])
                research=0
                if team!=GAME.team:
                    actions=[]
                    with sqlite3.connect(GAME.database) as c:
                        money=int(GAME.Sanitise(c.execute('''SELECT Money FROM Teams WHERE Name=?''',(team,)).fetchall()[0]))
                        if money<0:
                            money=0
                            c.execute('''UPDATE Teams SET Money=0 WHERE Name=?''',(team,))
                        if money>=2000000:
                            if regulationChange!=GAME.season+1 or GAME.race<GAME.races-4:
                                for y in range(5):
                                    actions.append("Upgrade")
                            if regulationChange==GAME.season+1:
                                for y in range(4):
                                    actions.append("Research")
                                engine=c.execute("SELECT Name FROM Engines WHERE Manufacturer=?",(team,)).fetchall()
                                if len(engine)>0:
                                    engine=GAME.Sanitise(engine[0])
                                    GAME.EngineResearch(engine,team)
                    if GAME.race>=8:
                        for y in range(2):
                            actions.append("Hire")
                    elif poacher==team:
                        #Poaching
                        rating1=int(GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Team=? AND Role='1'",(team,)).fetchall()[0]))
                        rating2=int(GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Team=? AND Role='2'",(team,)).fetchall()[0]))
                        if len(c.execute("SELECT Name FROM Drivers WHERE Team=? AND Role='1' AND (ContractEnd=? OR (NewTeam!='0' AND NewTeam!=?))",(team,GAME.season,team,)).fetchall())==0:
                            driver1=0
                        else:
                            driver1=1
                        if len(c.execute("SELECT Name FROM Drivers WHERE Team=? AND Role='2' AND (ContractEnd=? OR (NewTeam!='0' AND NewTeam!=?))",(team,GAME.season,team,)).fetchall())==0:
                            driver2=0
                        else:
                            driver2=1
                        if driver1==1 or driver2==1:
                            if driver1==0:
                                rating=rating2
                            elif driver2==0:
                                rating=rating1
                            elif rating2>rating1:
                                rating=rating1
                            else:
                                rating=rating2
                            if len(c.execute("SELECT Name FROM Drivers WHERE Team='Free Agent' AND Condition='Well' AND Rating>? AND NewTeam='0'",(rating,)).fetchall())>0:
                                actions.append("Poach")
                            else:
                                position=int(GAME.Sanitise(c.execute("SELECT Position FROM Teams WHERE Name=?",(team,)).fetchall()[0]))
                                Position=int(GAME.Sanitise(c.execute("SELECT Position FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0]))
                                if position<Position+3 and len(c.execute("SELECT Name FROM Drivers WHERE Team=? AND ContractEnd=? AND Condition='Well' AND Rating>?",(GAME.team,GAME.season,rating,)).fetchall())>0:
                                    actions.append("Poach")
                    if len(actions)!=0:
                        for y in range(2):
                            if y==0 and "Poach" in actions:
                                GAME.Poach(team)
                            else:
                                action=random.choice(actions)
                                if action=="Upgrade":
                                    GAME.Upgrade(team)
                                elif action=="Research":
                                    GAME.Research(team)
                                elif action=="Hire":
                                    GAME.Hire(team)
            GAME.actions=2
            with sqlite3.connect(GAME.database) as c:
                c.execute("UPDATE Player SET Actions=2")
        if len(GAME.news)>0:
            GAME.ChangeScreen("Breaking News")
            for x in range(len(GAME.news)):
                if x<20:
                    canvas.create_text(150, 180+(x*30), text=GAME.news[x], fill="white", font=("Arial", 20), anchor="nw")
            GAME.news=[]
            root.after(10000, lambda: GAME.PressConferences())
        else:
            GAME.PressConferences()
    def PressConferences(self):
        GAME.action=0
        if GAME.actions==2:
            if GAME.race==round((GAME.races/2)+0.55) and GAME.sponsor!="0":
                GAME.SponsorReview()
            else:
                with sqlite3.connect(GAME.database) as c:
                    position=int(GAME.Sanitise(c.execute("SELECT Position FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0]))
                    pressConferences=len(c.execute('''SELECT Name FROM Teams''').fetchall())*2
                if position==1 and GAME.race==round(GAME.races/2)+2:
                    GAME.PressConference("Upgrade")
                elif pressConferences>GAME.races:
                    GAME.PressConference(0)
                elif GAME.race>round((GAME.races-pressConferences)/2) and GAME.race<GAME.races-round((23-pressConferences)/2):
                    GAME.PressConference(0)
                else:
                    GAME.Menu()
        else:
            GAME.Menu()
    def CalculateTime(self):
        lead_driver = GAME.positions[0]
        GAME.time[lead_driver] = 0.0
        for x in range(1, len(GAME.positions)):
            current = GAME.positions[x]
            ahead = GAME.positions[x - 1]
            if GAME.lap[current] > GAME.lap[ahead] or (
               GAME.lap[current] == GAME.lap[ahead] and GAME.distance[current] > GAME.distance[ahead]):
                GAME.lap[current] = GAME.lap[ahead]
                GAME.distance[current] = max(0, GAME.distance[ahead] - random.uniform(0.5, 1.5))
            lead_total = GAME.lap[ahead] * GAME.length + GAME.distance[ahead]
            current_total = GAME.lap[current] * GAME.length + GAME.distance[current]
            distance_gap = lead_total - current_total
            time_gap = round(distance_gap / 41.67, 3)
            GAME.time[current] = max(0, time_gap)
    def Raining(self):
        if GAME.rainStopped==0 and GAME.replay!=5:
            if GAME.rainStops<=GAME.lap[GAME.positions[0]] and GAME.rainStops!=0 and GAME.water>0 and GAME.replay==0:
                #Drying
                if GAME.rainStops==GAME.lap[GAME.positions[0]]:
                    GAME.AddToLog("The rain has stopped.")
                GAME.drying=random.randint(int(round(GAME.drying*100)),120)/100
                GAME.water-=GAME.drying
                if GAME.water<=0:
                    GAME.water=0
                    GAME.rainStopped=1
            elif GAME.rainStarts<=GAME.lap[GAME.positions[0]] and GAME.water<GAME.maxWater:
                #Raining
                if GAME.rainStarts==GAME.lap[GAME.positions[0]]:
                    GAME.AddToLog("It has started raining.")
                if GAME.rain<GAME.maxRain:
                    GAME.rain=random.randint(int(GAME.rain*100),int(GAME.maxRain*100))/100
                GAME.water+=GAME.rain
                if GAME.water>GAME.maxWater:
                    GAME.water=GAME.maxWater
    def Move(self):
        if GAME.replay==2 and GAME.lap[GAME.positions[0]]>54:
            GAME.pause=3
            GAME.replay=7
            GAME.displayed=1
        elif GAME.replay==7 and GAME.lap[GAME.positions[0]]>60 and ((GAME.positions[0]==3 or GAME.positions[0]==20) and (GAME.positions[1]==3 or GAME.positions[1]==20)):
            GAME.pause=3
            GAME.displayed=2
        elif GAME.replay==1 and GAME.lap[GAME.positions[0]]>52:
            GAME.pause=3
        else:
            if GAME.replay==2:
                if GAME.positions.index(20)<4:
                    GAME.racePace.pop(20)
                    GAME.racePace.insert(20,200)
                elif GAME.racePace[20]==200:
                    GAME.racePace.pop(20)
                    GAME.racePace.insert(20,1000)
                if GAME.positions.index(21)<4:
                    GAME.racePace.pop(21)
                    GAME.racePace.insert(21,200)
                elif GAME.racePace[21]==200:
                    GAME.racePace.pop(21)
                    GAME.racePace.insert(21,1000)
                if GAME.lap[GAME.positions[0]]>=30:
                    if GAME.positions.index(3)>0:
                        GAME.overtaking.pop(3)
                        GAME.overtaking.insert(3,15)
                        GAME.racePace.pop(3)
                        if GAME.lap[GAME.positions[0]]>=50:
                            GAME.racePace.insert(3,1500)
                        else:
                            GAME.racePace.insert(3,500)
                    elif GAME.racePace[3]>=500:
                        GAME.racePace.pop(3)
                        GAME.racePace.insert(3,230)
                    if GAME.positions.index(4)>0 and GAME.positions.index(21)<GAME.positions.index(4):
                        GAME.overtaking.pop(4)
                        GAME.overtaking.insert(4,10)
                        GAME.racePace.pop(4)
                        GAME.racePace.insert(4,300)
                    else:
                        GAME.overtaking.pop(4)
                        GAME.overtaking.insert(4,5)
                        GAME.racePace.pop(4)
                        GAME.racePace.insert(4,215)
            elif GAME.replay==1:
                for x in range(2):
                    if GAME.positions[0]!=x and GAME.teams[x]!=GAME.team:
                        if (GAME.stops[1-x]>0 and GAME.time[x]>5) or GAME.positions.index(x)>5:
                            GAME.racePace[x]=320
                            GAME.overtaking[x]=30
                        elif GAME.stops[1-x]>0 and GAME.time[x]>1:
                            GAME.racePace[x]=280
                            GAME.overtaking[x]=5
                        else:
                            GAME.racePace[x]=250
                            GAME.overtaking[x]=5
            elif GAME.replay==9:
                for x in range(2):
                    GAME.racePace[x]==250
                    GAME.overtaking[x]=5
            elif GAME.replay==3:
                if GAME.lap[4]==5 and GAME.events==0:
                    GAME.AddToLog("Lewis Hamilton crashed into Mark Webber.")
                    GAME.positions.remove(4)
                    GAME.positions.insert(6,4)
                    GAME.positions.remove(3)
                    GAME.positions.insert(11,3)
                    GAME.events=1
                    GAME.racePace[4]=250
                    GAME.overtaking[4]=20
                elif GAME.events==1 and GAME.lap[6]>13:
                    GAME.AddToLog("Jenson Button served his Drive Through Penalty.")
                    GAME.distance[6]-=833
                    position=GAME.positions.index(6)
                    while True:
                        if position==21:
                            break
                        elif GAME.distance[6]<GAME.distance[GAME.positions[position]]:
                            position+=1
                        else:
                            break
                    GAME.positions.remove(6)
                    GAME.positions.insert(position,6)
                    GAME.events=2
                if GAME.lap[0]>10 and GAME.lap[0]<19:
                    GAME.water=6.5-(GAME.lap[0]/5)
                    GAME.rainStarts=19
                elif GAME.lap[0]==19:
                    GAME.maxWater=4.2
                    GAME.rain=0.6
                elif GAME.lap[0]==20:
                    GAME.safety=2
                elif GAME.lap[0]>33 and GAME.lap[0]<40:
                    GAME.rainStops=33
                    GAME.water=9.9-(GAME.lap[0]/5)
                    GAME.maxWater=GAME.water
                elif GAME.lap[0]>45 and GAME.lap[0]<55:
                    GAME.water=11.3-(GAME.lap[0]/5)
                    GAME.maxWater=GAME.water
                if GAME.lap[0]>36 and 1 in GAME.positions:
                    if GAME.positions.index(1)<GAME.positions.index(6):
                        GAME.racePace[1]=10
                        GAME.defending[1]=1
                    else:
                        GAME.racePace[1]=500
                        GAME.overtaking[1]=100
                    if GAME.lap[0]>40 and 1 in GAME.positions:
                        GAME.AddToLog("Fernando Alonso crashed.")
                        GAME.positions.remove(1)
                        GAME.safety=2
                if GAME.lap[0]>55 and GAME.events==2:
                    GAME.AddToLog("Nick Heidfeld ran over his front wing.")
                    GAME.positions.remove(8)
                    GAME.safety=2
                    GAME.water=0.5
                    GAME.maxWater=0.5
                    GAME.racePace[0]=200
                    GAME.racePace[6]=280
                    GAME.overtaking[0]=5
                    GAME.overtaking[6]=15
                    GAME.events=3
                if GAME.lap[18]==28 and 18 in GAME.positions:
                    GAME.AddToLog("Heikki Kovalainen has an engine failure, he is out of the race.")
                    GAME.positions.remove(18)
            elif GAME.replay==4:
                if GAME.lap[0]>8 and GAME.lap[0]<12:
                    GAME.water=9.4-(GAME.lap[0]*0.8)
                elif GAME.lap[0]>11 and GAME.lap[0]<20:
                    GAME.water=0
                elif GAME.lap[0]>40 and GAME.lap[0]<51:
                    if GAME.water==0:
                        GAME.AddToLog("It has started raining.")
                    GAME.water=(GAME.lap[0]-40)*0.3
                if 3 in GAME.positions and GAME.lap[0]>49:
                    if GAME.team=="Ferrari":
                        if GAME.positions.index(3)>11:
                            GAME.racePace[3]=1000
                        elif GAME.positions.index(3)>7:
                            GAME.racePace[3]=300
                    elif GAME.positions.index(3)<6:
                        GAME.racePace[3]=75
                        GAME.defending[3]=1
                    elif GAME.positions.index(3)==6:
                        GAME.racePace[3]=120
            elif GAME.replay==5:
                if GAME.lap[0]<8:
                    GAME.water=3.5-(GAME.lap[0]/2)
                    GAME.maxWater=GAME.water
                if GAME.lap[0]>35:
                    try:
                        if GAME.team=="Ferrari":
                            if GAME.positions.index(0)>GAME.positions.index(3) and GAME.time[0]>1:
                                GAME.racePace[0]=300
                                GAME.overtaking[0]=20
                            else:
                                GAME.racePace[0]=230
                                GAME.overtaking[0]=8
                        else:
                            if GAME.positions.index(3)>GAME.positions.index(0) and GAME.time[3]>1:
                                GAME.racePace[3]=300
                                GAME.overtaking[3]=20
                            else:
                                GAME.racePace[3]=240
                                GAME.overtaking[3]=15
                    except:
                        pass
            elif GAME.replay==6:
                if 11 in GAME.positions:
                    if GAME.positions.index(11)>8:
                        GAME.overtakeability=3
                    else:
                        GAME.overtakeability=2
            GAME.RefreshScreen()
            GAME.cycles+=1
            if GAME.cycles>40:
                for x in range(len(GAME.positions)):
                    index=GAME.positions[x]
                    lap=GAME.lap[index]+1
                    GAME.lap.pop(index)
                    GAME.lap.insert(index,lap)
                    GAME.cycles=0
            driversUsed=[]
            overtakes=0
            if GAME.wet==1:
                grip=10-(GAME.water*5)
                if grip<0:
                    grip=0
                GAME.grip.append(grip)
                grip=10-(GAME.water*1.25)
                if grip<0:
                    grip=0
                GAME.grip.append(grip)
                grip=10-(GAME.water*0.5)
                if grip<0:
                    grip=0
                GAME.grip.append(grip)
            else:
                GAME.grip=[10,10,10]
            driversRemoved=0
            runOutOfFuel=[]
            GAME.pitting=[]
            for x in range(len(GAME.positions)):
                index=GAME.positions[x]
                if GAME.ERSdeployment[index]==4 and (GAME.time[index]>=1 or x==0 or GAME.ERS[index]<1 or GAME.water>=1):
                    GAME.ERSdeployment[index]=3
                tyreRemaining=GAME.tyreRemaining[index]
                distance=GAME.distance[index]
                if GAME.safety==0:
                    if tyreRemaining>10:
                        if GAME.tyre[index]=="Soft":
                            tyrePace=GAME.tyrePace[0]*GAME.grip[0]/10
                        elif GAME.tyre[index]=="Medium":
                            tyrePace=GAME.tyrePace[1]*GAME.grip[0]/10
                        elif GAME.tyre[index]=="Hard":
                            tyrePace=GAME.tyrePace[2]*GAME.grip[0]/10
                        elif GAME.tyre[index]=="Intermediate" or GAME.replay==5:
                            tyrePace=0.6*GAME.grip[1]
                        else:
                            tyrePace=0.5*GAME.grip[2]
                        if tyreRemaining>75:
                            T=round(tyreRemaining/5)
                        elif tyreRemaining>50:
                            T=round(tyreRemaining/10)
                        elif tyreRemaining>30:
                            T=round(tyreRemaining/15)
                        else:
                            T=random.randint(1,2)/2
                    else:
                        tyrePace=0.1
                        T=0.5
                    speed=GAME.racePace[index]
                    speed+=T+tyrePace
                    speed=speed*(100-GAME.damage[index])/100
                    speed+=(GAME.tyreAggression[index]*10)
                    if GAME.tyreAggression[index]==2:
                        speed=round(speed/1.2)
                    elif GAME.tyreAggression[index]==1:
                        speed=round(speed/1.5)
                    speed+=(GAME.fuelAggression[index]*15)
                    if GAME.drs==1 and GAME.water<1 and x!=0 and GAME.lap[index]>GAME.startLap:
                        if GAME.time[index]<1:
                            speed+=random.randint(round(GAME.DRS[index]/2),GAME.DRS[index])
                    if GAME.ers>0:
                        if GAME.ERS[index]>0:
                            speed+=(GAME.ERSdeployment[index]*20)
                    if GAME.water>=1:
                        speed=(speed+GAME.water*GAME.experience[index])/2
                    speed-=round(GAME.fuel[index]/1.5)
                    if GAME.teams[index]==GAME.team and ((GAME.cars[index]==1 and "Drive in Clean Air" in GAME.car1Instructions) or (GAME.cars[index]==2 and "Drive in Clean Air" in GAME.car2Instructions)) and x!=0 and GAME.time[index]<=2:
                        speed-=25
                    speed+=1
                    if tyreRemaining==0:
                        speed=round(speed/4)
                    if GAME.replay==4 and GAME.tyre[index]!="Wet" and GAME.tyre[index]!="Intermediate" and GAME.water>=1:
                        speed=round(speed/2)

                    #Fastest Lap
                    if speed>GAME.fastest[1] and (x==0 or GAME.time[index]>=0.9) and GAME.water<=GAME.fastest[2]:
                        GAME.fastest=[index,speed,GAME.water]
                        GAME.AddToLog(f"{GAME.drivers[index]} has set the fastest lap of the race so far.")
                    
                    if GAME.time[index]>20 and GAME.teams[index]!=GAME.team:
                        speed=round(speed*1.6)
                    distance+=speed
                if GAME.fuel[index]<=0:
                    #Run out of fuel
                    GAME.AddToLog(GAME.drivers[index]+" has run out of fuel.")
                    GAME.crashMessage.append(GAME.drivers[index]+" has run out of fuel.")
                    GAME.safety=3
                    runOutOfFuel.append(index)
                    if index in GAME.pitting:
                        GAME.pitting.remove(index)
                else:
                    if distance>=GAME.length:
                        distance-=GAME.length
                        lap=GAME.lap[index]+1
                        if distance>=GAME.distance[index-1] and GAME.lap[index]==GAME.lap[index-1] and GAME.safety!=0:
                            distance=GAME.distance[index-1]-(random.randint(100,300)/300)
                        GAME.lap.pop(index)
                        GAME.lap.insert(index, lap)
                    #Tyre and Fuel management
                    if GAME.teams[index]!=GAME.team:
                        if GAME.lap[index]==2:
                            GAME.fuelAggression.pop(index)
                            GAME.fuelAggression.insert(index, 2)
                            GAME.tyreAggression.pop(index)
                            GAME.tyreAggression.insert(index, 2)
                        else:
                            #Fuel management
                            if GAME.lap[GAME.positions[0]]==GAME.laps:
                                if GAME.fuel[index]>6:
                                    if GAME.fuelAggression[index]!=3:
                                        GAME.fuelAggression.pop(index)
                                        GAME.fuelAggression.insert(index, 3)
                                elif GAME.fuel[index]<4:
                                    if GAME.fuelAggression[index]!=1:
                                        GAME.fuelAggression.pop(index)
                                        GAME.fuelAggression.insert(index, 1)
                                elif GAME.fuelAggression[index]!=2:
                                    GAME.fuelAggression.pop(index)
                                    GAME.fuelAggression.insert(index, 2)
                            elif GAME.fuel[index]<(92/(GAME.laps*(GAME.laps-GAME.lap[GAME.positions[0]]))) or GAME.engineTemperature[index]>=120:
                                GAME.fuelAggression.pop(index)
                                GAME.fuelAggression.insert(index, 1)
                            elif GAME.fuel[index]<(95/(GAME.laps*(GAME.laps-GAME.lap[GAME.positions[0]]))) and GAME.fuelAggression[index]==3:
                                GAME.fuelAggression.pop(index)
                                GAME.fuelAggression.insert(index, 2)
                            elif GAME.lap[GAME.positions[0]]>=GAME.laps-5 and GAME.fuel[index]>=(95/(GAME.laps*(GAME.laps-GAME.lap[GAME.positions[0]]))):
                                GAME.fuelAggression.pop(index)
                                GAME.fuelAggression.insert(index, 3)
                        #Tyre Management
                        tyreAge=GAME.lap[index]-GAME.lapPittedTo[index]
                        if GAME.lap[index]==GAME.pitLap[index] or GAME.lap[GAME.positions[0]]==GAME.laps:
                            GAME.tyreAggression.pop(index)
                            GAME.tyreAggression.insert(index, 5)
                        elif GAME.tyre[index]!="Intermediate" and GAME.tyre[index]!="Wet":
                            if GAME.strategy[index]!=0:
                                if tyreAge==0:
                                    if GAME.tyreAggression[index]!=3:
                                        GAME.tyreAggression.pop(index)
                                        GAME.tyreAggression.insert(index,3)
                                else:
                                    stops=GAME.stops[index]
                                    if GAME.tyre[index]=="Soft":
                                        wear=GAME.tyreWear[0]
                                    elif GAME.tyre[index]=="Medium":
                                        wear=GAME.tyreWear[1]
                                    else:
                                        wear=GAME.tyreWear[2]
                                    pitWindowLength=GAME.pitLap[index]-GAME.lapPittedTo[index]
                                    if pitWindowLength<=0:
                                        pitWindowLength=GAME.laps-GAME.lapPittedTo[index]
                                    if pitWindowLength<=0:
                                        expectedWear=1000
                                    else:
                                        expectedWear=round(75-(wear*tyreAge/pitWindowLength))
                                    if GAME.tyreRemaining[index]>expectedWear+25:
                                        aggression=5
                                    elif GAME.tyreRemaining[index]>expectedWear+10:
                                        aggression=4
                                    elif GAME.tyreRemaining[index]>expectedWear-10:
                                        aggression=3
                                    elif GAME.tyreRemaining[index]>expectedWear-25:
                                        aggression=2
                                    else:
                                        aggression=1
                                    if GAME.tyreAggression[index]!=aggression:
                                        GAME.tyreAggression.pop(index)
                                        GAME.tyreAggression.insert(index,aggression)
                            else:
                                if GAME.tyre[index]=="Soft":
                                    wear=GAME.tyreWear[0]
                                elif GAME.tyre[index]=="Medium":
                                    wear=GAME.tyreWear[1]
                                else:
                                    wear=GAME.tyreWear[2]
                                if GAME.wet==0:
                                    if GAME.pitLap[index]==0:
                                        lapsLeft=GAME.laps-GAME.lap[GAME.positions[0]]
                                    else:
                                        lapsLeft=GAME.pitLap[index]-GAME.lap[index]
                                elif GAME.rainStops<GAME.lap[GAME.positions[0]]:
                                    if GAME.pitLap[index]==0:
                                        lapsLeft=GAME.laps-GAME.lap[GAME.positions[0]]
                                    else:
                                        lapsLeft=GAME.pitLap[index]-GAME.lap[index]
                                else:
                                    lapsLeft=-1
                                if lapsLeft==-1:
                                    if GAME.tyreRemaining[index]<38:
                                        if GAME.rainStarts-GAME.lap[GAME.positions[0]]<=5:
                                            GAME.tyreAggression.pop(index)
                                            GAME.tyreAggression.insert(index, 1)
                                        elif GAME.pitLap[index]==0:
                                            lapsLeft=GAME.rainStarts-GAME.lap[GAME.positions[0]]
                                            GAME.pitLap.pop(index)
                                            GAME.pitLap.insert(index, GAME.lap[index])
                                            GAME.pitTyre.pop(index)
                                            if lapsLeft<GAME.expectedTyreLife[0]:
                                                GAME.pitTyre.insert(index,"Soft")
                                            elif lapsLeft<GAME.expectedTyreLife[1]:
                                                GAME.pitTyre.insert(index,"Medium")
                                            else:
                                                GAME.pitTyre.insert(index,"Hard")
                                    elif GAME.tyreAggression[index]!=3:
                                        GAME.tyreAggression.pop(index)
                                        GAME.tyreAggression.insert(index, 3)
                                elif GAME.tyreRemaining[index]-30>wear*lapsLeft:
                                    if GAME.tyreRemaining[index]-30>wear*lapsLeft*1.5:
                                        if GAME.tyreAggression!=5:
                                            GAME.tyreAggression.pop(index)
                                            GAME.tyreAggression.insert(index,5)
                                    elif GAME.tyreRemaining[index]-30>wear*lapsLeft*1.2:
                                        if GAME.tyreAggression!=4:
                                            GAME.tyreAggression.pop(index)
                                            GAME.tyreAggression.insert(index,4)
                                    elif GAME.tyreAggression!=3:
                                        GAME.tyreAggression.pop(index)
                                        GAME.tyreAggression.insert(index,3)
                                else:
                                    if GAME.tyreRemaining[index]-30>wear*lapsLeft/1.5:
                                        if lapsLeft<=15 and GAME.tyreRemaining[index]<=45 and GAME.pitLap[index]==0:
                                            if GAME.tyreAggression[index]!=5:
                                                GAME.tyreAggression.pop(index)
                                                GAME.tyreAggression.insert(index, 5)
                                            GAME.pitLap.pop(index)
                                            GAME.pitLap.insert(index, GAME.lap[index])
                                            GAME.pitTyre.pop(index)
                                            GAME.pitTyre.insert(index, "Soft")
                                        elif GAME.tyreAggression[index]!=1:
                                            GAME.tyreAggression.pop(index)
                                            GAME.tyreAggression.insert(index, 1)
                                    elif GAME.tyreRemaining[index]-30>wear*lapsLeft/1.2:
                                        if GAME.tyreAggression[index]!=2:
                                            GAME.tyreAggression.pop(index)
                                            GAME.tyreAggression.insert(index, 2)
                                    elif GAME.tyreAggression[index]!=3:
                                        GAME.tyreAggression.pop(index)
                                        GAME.tyreAggression.insert(index, 3)
                    GAME.distance.pop(index)
                    GAME.distance.insert(index,distance)
                if GAME.lap_[index]!=GAME.lap[index]:
                    if x==0:
                        GAME.cycles=0
                        if GAME.wet==1:
                            GAME.Raining()
                        if GAME.lap[index]>5:
                            GAME.displayedImage=random.randint(1,2)
                    GAME.lap_.pop(index)
                    GAME.lap_.insert(index,GAME.lap[index])
                    #Tyre, Fuel and ERS Usage

                    #Tyre Usage
                    if GAME.safety==0:
                        if GAME.tyre[index]=="Soft":
                            tyreWear=GAME.tyreWear[0]*GAME.tyreAggression[index]/3
                        elif GAME.tyre[index]=="Medium":
                            tyreWear=GAME.tyreWear[1]*GAME.tyreAggression[index]/3
                        elif GAME.tyre[index]=="Hard":
                            tyreWear=GAME.tyreWear[2]*GAME.tyreAggression[index]/3
                        elif GAME.tyre[index]=="Intermediate":
                            if GAME.water>=1:
                                tyreWear=GAME.tyreWear[3]*GAME.tyreAggression[index]/3
                            elif GAME.water>=0.8:
                                tyreWear=GAME.tyreWear[3]*GAME.tyreAggression[index]/2.5
                            elif GAME.water>=0.5:
                                tyreWear=GAME.tyreWear[3]*GAME.tyreAggression[index]
                            else:
                                tyreWear=GAME.tyreWear[3]*GAME.tyreAggression[index]*3
                        else:
                            if GAME.water>=4:
                                tyreWear=GAME.tyreWear[3]*GAME.tyreAggression[index]/3
                            elif GAME.water>=2.5:
                                tyreWear=GAME.tyreWear[3]*GAME.tyreAggression[index]/2.5
                            elif GAME.water>=2:
                                tyreWear=GAME.tyreWear[3]*GAME.tyreAggression[index]
                            elif GAME.water>=1.5:
                                tyreWear=GAME.tyreWear[3]*GAME.tyreAggression[index]*2
                            else:
                                tyreWear=GAME.tyreWear[3]*GAME.tyreAggression[index]*5
                        try:
                            t=random.randint(GAME.tyrePreservation[index],200)
                        except:
                            t=200
                        tyreWear=tyreWear*((210-t)/100)
                        if GAME.replay==7:
                            tyreWear=round(tyreWear/3)
                        elif GAME.replay==8:
                            tyreWear=0

                        #Fuel Usage
                        fuelUsage=45*GAME.fuelAggression[index]/int(GAME.laps)
                        if GAME.replay==7:
                            fuelUsage=fuelUsage/3
                        elif GAME.replay==8:
                            fuelUsage=0
                        
                        #Engine Temperature
                        temperature=GAME.engineTemperature[index]
                        if x==0:
                            dirtyAir=0
                        elif GAME.time[index]<=1:
                            dirtyAir=2
                        elif GAME.time[index]<=2:
                            dirtyAir=1
                        else:
                            dirtyAir=0
                        change=0
                        climate=GAME.temperature-(GAME.water*1.2)
                        if climate<=22:
                            change+=random.randint(-2,0)
                        elif climate<30:
                            change+=random.randint(-1,1)
                        else:
                            change+=random.randint(0,2)
                        if GAME.fuelAggression[index]==1:
                            change+=random.randint(-4,-1)
                        elif GAME.fuelAggression[index]==3:
                            change+=random.randint(1,3)
                        else:
                            change+=random.randint(-1,0)
                        if GAME.teams[index]==GAME.team and ((GAME.cars[index]==1 and "Drive in Clean Air" in GAME.car1Instructions) or (GAME.cars[index]==2 and "Drive in Clean Air" in GAME.car2Instructions)):
                            dirtyAir=0
                        if dirtyAir==1:
                            change+=random.randint(0,2)
                        elif dirtyAir==2:
                            change+=random.randint(1,3)
                        for x in range(3):
                            if random.randint(1,100)<=GAME.cooling[index]:
                                change-=1
                        if temperature+change<100:
                            if change<0:
                                for y in range(-change):
                                    if random.randint(1,3)==3:
                                        temperature-=1
                            else:
                                for y in range(change):
                                    if random.randint(1,2)==2:
                                        temperature+=1
                                temperature+=change
                        else:
                            temperature+=change
                        if temperature<85:
                            temperature=85
                        GAME.engineTemperature.pop(index)
                        GAME.engineTemperature.insert(index,temperature)
                        #Engine Failures
                        if GAME.replay==0 or GAME.teams[index]==GAME.team:
                            durability=GAME.engineDurability[index]
                            reliability=GAME.engineReliability[index]
                            fault=0
                            if temperature>120:
                                try:
                                    if random.randint(1,temperature)+durability-40>115 and random.randint(1,reliability)==1:
                                        #Fault
                                        fault=1
                                    elif GAME.faults[index]!=0 and random.randint(1,reliability*10)==1:
                                        #Fault
                                        fault=1
                                except:
                                    if random.randint(1,temperature)+durability-40>115:
                                        #Fault
                                        fault=1
                            elif durability<=40:
                                try:
                                    if random.randint(1,round(durability*reliability*100/random.randint(100,250)))==1:
                                        #Fault
                                        fault=1
                                except:
                                    fault=1
                            if fault==1:
                                currentState=GAME.faults[index]
                                F=0
                                if currentState!="Major":
                                    for y in range(10):
                                        if reliability<=y and random.randint(1,5)==5:
                                            F+=1
                                if F==0:
                                    if currentState==0:
                                        fault="Minor"
                                    elif currentState=="Minor":
                                        fault="Major"
                                    else:
                                        fault="Failure"
                                elif F==1:
                                    if currentState==0:
                                        fault="Major"
                                    else:
                                        fault="Failure"
                                else:
                                    fault="Failure"
                                GAME.thingHappened=1
                                GAME.faults.pop(index)
                                GAME.faults.insert(index,fault)
                                if fault=="Failure":
                                    GAME.AddToLog(GAME.drivers[index]+" has an engine failure, they are out of the race.")
                                    if GAME.playing==0 and GAME.sound==1:
                                        GAME.Voice(GAME.drivers[index],"Out")
                                else:
                                    GAME.AddToLog(GAME.drivers[index]+" has a "+fault+" fault with their engine.")

                        #ERS Usage
                        if GAME.ers>0:
                            if GAME.replay==7 or GAME.replay==8:
                                if GAME.ERSdeployment[index]==1:
                                    ERS=GAME.ERS[index]+random.randint(7,10)
                                    if ERS>100:
                                        ERS=100
                                    if ERS>90 and GAME.teams[index]!=GAME.team:
                                        GAME.ERSdeployment.pop(index)
                                        GAME.ERSdeployment.insert(index, 3)
                                elif GAME.ERSdeployment[index]==2:
                                    ERS=GAME.ERS[index]+random.randint(0,1)
                                    if ERS>100:
                                        ERS=100
                                        if GAME.teams[index]!=GAME.team:
                                            GAME.ERSdeployment.pop(index)
                                            GAME.ERSdeployment.insert(index, 3)
                                else:
                                    ERS=GAME.ERS[index]-random.randint(3,10)
                                    if ERS<0:
                                        ERS=0
                                    if ERS<50 and GAME.teams[index]!=GAME.team:
                                        GAME.ERSdeployment.pop(index)
                                        GAME.ERSdeployment.insert(index, random.randint(1,2))
                            elif GAME.ers==2:
                                if GAME.ERSdeployment[index]==1:
                                    ERS=GAME.ERS[index]+random.randint(20,30)
                                    if ERS>100:
                                        ERS=100
                                    if ERS>90 and GAME.teams[index]!=GAME.team:
                                        GAME.ERSdeployment.pop(index)
                                        GAME.ERSdeployment.insert(index, 3)
                                elif GAME.ERSdeployment[index]==2:
                                    ERS=GAME.ERS[index]+random.randint(0,2)
                                    if ERS>100:
                                        ERS=100
                                        if GAME.teams[index]!=GAME.team:
                                            GAME.ERSdeployment.pop(index)
                                            GAME.ERSdeployment.insert(index, 3)
                                else:
                                    ERS=GAME.ERS[index]-random.randint(10,30)
                                    if ERS<0:
                                        ERS=0
                                    if ERS<50 and GAME.teams[index]!=GAME.team:
                                        GAME.ERSdeployment.pop(index)
                                        GAME.ERSdeployment.insert(index, random.randint(1,2))
                            else:
                                if GAME.teams[index]!=GAME.team and GAME.lap[index]>GAME.startLap and GAME.time[index]<0.5 and x>0 and GAME.ERS[index]>=60 and random.randint(1,2)==2 and GAME.water<1:
                                    GAME.ERSdeployment[index]=4
                                if GAME.ERSdeployment[index]==1:
                                    ERS=GAME.ERS[index]+random.randint(6,15)+(4*GAME.battery[index])
                                    if ERS>100:
                                        ERS=100
                                    if GAME.teams[index]!=GAME.team:
                                        if ERS>90:
                                            GAME.ERSdeployment[index]=3
                                        elif ERS>60:
                                            GAME.ERSdeployment[index]=2
                                elif GAME.ERSdeployment[index]==2:
                                    ERS=GAME.ERS[index]+random.randint(-4,0)+(GAME.battery[index]//3)
                                    if ERS>100:
                                        ERS=100
                                    elif ERS<0:
                                        ERS=0
                                        if GAME.teams[index]!=GAME.team:
                                            GAME.ERSdeployment.pop(index)
                                            GAME.ERSdeployment.insert(index, 1)
                                elif GAME.ERSdeployment[index]==3:
                                    ERS=GAME.ERS[index]-random.randint(15,35)+GAME.battery[index]
                                    if ERS<0:
                                        ERS=0
                                    if ERS<50 and GAME.teams[index]!=GAME.team:
                                        GAME.ERSdeployment.pop(index)
                                        GAME.ERSdeployment.insert(index, round(random.randint(1,5)/2))
                                elif GAME.ERS[index]<50:
                                    if GAME.teams[index]!=GAME.team:
                                        GAME.ERSdeployment[index]=1
                                    else:
                                        GAME.ERSdeployment[index]=3
                            try:
                                GAME.ERS[index]=ERS
                            except:
                                pass
                    elif GAME.safety==1:
                        tyreWear=1
                        fuelUsage=40/GAME.laps
                        ERS=GAME.ERS[index]+random.randint(15,30)
                        if ERS>100:
                            ERS=100
                    else:
                        tyreWear=2
                        fuelUsage=30/GAME.laps
                        ERS=GAME.ERS[index]+random.randint(25,50)
                        if ERS>100:
                            ERS=100
                    tyreRemaining-=tyreWear
                    if tyreRemaining>=1:
                        if tyreRemaining<=30 and random.randint(1,round(tyreRemaining))==1:
                            #Puncture
                            GAME.AddToLog(GAME.drivers[index]+" has a puncture.")
                            GAME.thingHappened=1
                            tyreRemaining=0
                    elif tyreRemaining<1 and tyreRemaining>0:
                        #Puncture
                        GAME.AddToLog(GAME.drivers[index]+" has a puncture.")
                        GAME.thingHappened=1
                        tyreRemaining=0
                    fuel=GAME.fuel[index]-fuelUsage
                    if tyreRemaining<0:
                        tyreRemaining=0
                    if fuel<=0:
                        fuel=0
                    GAME.tyreRemaining.pop(index)
                    GAME.tyreRemaining.insert(index, tyreRemaining)
                    GAME.fuel.pop(index)
                    GAME.fuel.insert(index, fuel)
                    if GAME.lap[index]>GAME.laps and GAME.replay!=7 and GAME.replay!=8:
                        GAME.raceFinished=1
                    elif (GAME.replay==7 or GAME.replay==8) and GAME.lap[index]>66:
                        GAME.raceFinished=1
                    else:
                        pitting=0
                        if GAME.lap[index]>GAME.pitLap[index] and GAME.pitLap[index]!=0:
                            pitting=1
                        elif GAME.teams[index]!=GAME.team and not (GAME.drivers[index]=="Timo Glock" and GAME.lap[0]>40):
                            #Pit now
                            if GAME.tyreRemaining[index]==0 or GAME.strategy[index]==0 and (GAME.tyreRemaining[index]<10 or (GAME.tyreRemaining[index]<=25 and (GAME.lap[GAME.positions[0]]<GAME.laps-5 or GAME.lap[index]<GAME.pitLap[index]-5)) or (GAME.tyreRemaining[index]<=20 and (GAME.lap[GAME.positions[0]]<GAME.laps-3 or GAME.lap[index]<GAME.pitLap[index]-5))):
                                pitting=1
                                GAME.pitTyre.pop(index)
                                if GAME.wet==0:
                                    tyre="Slick"
                                    lapsLeft=GAME.laps-GAME.lap[GAME.positions[0]]
                                elif GAME.water==0 and GAME.rainStarts-GAME.lap[GAME.positions[0]]<=6:
                                    tyre="Slick"
                                    lapsLeft=GAME.rainStarts-GAME.lap[GAME.positions[0]]
                                elif GAME.water>0 and GAME.water<=1 and GAME.rain==0:
                                    tyre="Slick"
                                    lapsLeft=GAME.laps-GAME.lap[GAME.positions[0]]
                                elif GAME.water<2.5 or GAME.maxWater<4:
                                    tyre="Intermediate"
                                else:
                                    tyre="Wet"
                                if tyre=="Slick":
                                    if lapsLeft<=GAME.expectedTyreLife[0]*0.8 and (GAME.tyreCompoundsUsed[index]>1 or GAME.tyre[index]!="Soft"):
                                        GAME.pitTyre.insert(index,"Soft")
                                    elif lapsLeft<=GAME.expectedTyreLife[1]*0.8 and (GAME.tyreCompoundsUsed[index]>1 or GAME.tyre[index]!="Medium"):
                                        GAME.pitTyre.insert(index,"Medium")
                                    elif GAME.tyreCompoundsUsed[index]>1 or GAME.tyre[index]!="Hard":
                                        GAME.pitTyre.insert(index,"Hard")
                                    else:
                                        GAME.pitTyre.insert(index,"Medium")
                                else:
                                    GAME.pitTyre.insert(index,tyre)
                            elif GAME.wet==1 and GAME.replay!=5:
                                if GAME.water>=0.65 and GAME.water<2.5 and (GAME.tyre[index]=="Soft" or GAME.tyre[index]=="Medium" or GAME.tyre[index]=="Hard") and GAME.teams[index]!="Ferrari":
                                    if GAME.water>=1:
                                        pitting=1
                                        GAME.pitTyre.pop(index)
                                        GAME.pitTyre.insert(index,"Intermediate")
                                    elif random.randint(round(GAME.water*100),100)>90:
                                        pitting=1
                                        GAME.pitTyre.pop(index)
                                        GAME.pitTyre.insert(index,"Intermediate")
                                elif GAME.teams[index]=="Ferrari" and GAME.water>=0.5 and (GAME.tyre[index]=="Soft" or GAME.tyre[index]=="Medium" or GAME.tyre[index]=="Hard"):
                                    if GAME.water>=1.5:
                                        num=random.randint(1,7)
                                        if num==7:
                                            GAME.pitTyre.pop(index)
                                            GAME.pitTyre.insert(index,"Wet")
                                        elif num>=3:
                                            GAME.pitTyre.pop(index)
                                            GAME.pitTyre.insert(index,"Intermediate")
                                    elif random.randint(round(GAME.water*100),150)>=120:
                                        pitting=1
                                        GAME.pitTyre.pop(index)
                                        if random.randint(1,100)==100:
                                            GAME.pitTyre.insert(index,"Wet")
                                        else:
                                            GAME.pitTyre.insert(index,"Intermediate")
                                elif GAME.water>=2.5 and GAME.tyre[index]!="Wet" and GAME.maxWater>=4 and (GAME.rain>0 or GAME.water>4) and GAME.rainStops-GAME.lap[GAME.positions[0]]>=5:
                                    if GAME.water>=3.5:
                                        pitting=1
                                        GAME.pitTyre.pop(index)
                                        GAME.pitTyre.insert(index,"Wet")
                                    elif random.randint(round(GAME.water*100),350)>=315:
                                        pitting=1
                                        GAME.pitTyre.pop(index)
                                        GAME.pitTyre.insert(index,"Wet")
                                elif GAME.water<=1 and GAME.rain==0 and (GAME.tyre[index]=="Intermediate" or GAME.tyre[index]=="Wet"):
                                    if GAME.teams[index]=="Ferrari" and random.randint(1,1000)==1000:
                                        pitting=1
                                        GAME.pitTyre.pop(index)
                                        GAME.pitTyre.insert(index,"Wet")
                                    elif GAME.tyre=="Wet" or random.randint(round(GAME.water*100),150)<=100:
                                        pitting=1
                                        GAME.pitTyre.pop(index)
                                        lapsLeft=GAME.laps-GAME.lap[GAME.positions[0]]
                                        if lapsLeft<=GAME.expectedTyreLife[0]:
                                            if random.randint(1,5)==5:
                                                GAME.pitTyre.insert(index,"Medium")
                                            else:
                                                GAME.pitTyre.insert(index,"Soft")
                                        elif lapsLeft<=GAME.expectedTyreLife[1]:
                                            num=random.randint(1,10)
                                            if num==1:
                                                GAME.pitTyre.insert(index,"Soft")
                                            elif num<=7:
                                                GAME.pitTyre.insert(index,"Medium")
                                            else:
                                                GAME.pitTyre.insert(index,"Hard")
                                        elif lapsLeft<=GAME.expectedTyreLife[2]:
                                            if random.randint(1,8)==8:
                                                GAME.pitTyre.insert(index,"Medium")
                                            else:
                                                GAME.pitTyre.insert(index,"Hard")
                                        else:
                                            num=random.randint(1,4)
                                            if num==1:
                                                GAME.pitTyre.insert(index,"Soft")
                                            elif num<=3:
                                                GAME.pitTyre.insert(index,"Medium")
                                            else:
                                                GAME.pitTyre.insert(index,"Hard")
                                elif GAME.water<2.5 and GAME.tyre[index]=="Wet" and GAME.rain==0:
                                    if GAME.teams[index]!="Ferrari" or random.randint(1,8)!=8:
                                        pitting=1
                                        GAME.pitTyre.pop(index)
                                        GAME.pitTyre.insert(index,"Intermediate")
                                if pitting==1:
                                    GAME.pitLap.pop(index)
                                    GAME.pitLap.insert(index,0)
                        if pitting==1:
                            GAME.AddToLog(GAME.drivers[index]+" is pitting.")
                            GAME.pitting.append(index)
                            GAME.pitLap.pop(index)
                            GAME.pitLap.insert(index,0)
                            GAME.lapPittedTo.pop(index)
                            GAME.lapPittedTo.insert(index,GAME.lap[index])
            if len(runOutOfFuel)>=1:
                for x in range(len(runOutOfFuel)):
                    GAME.positions.remove(runOutOfFuel[x])
            #Pit stops
            if len(GAME.pitting) >= 1:
                baseTimeLost = {0: 20, 1: 15, 2: 10, 3: 0}[GAME.safety]
                for driverIndex in GAME.pitting:
                    GAME.CalculateTime()
                    pos=GAME.positions.index(driverIndex)
                    team=GAME.teams[driverIndex]
                    if GAME.replay==0:
                        with sqlite3.connect(GAME.database) as c:
                            pitStopRating = int(GAME.Sanitise(c.execute('''SELECT Rating FROM Staff WHERE Role="Sporting Director" AND Team=?''', (team,)).fetchone()[0]))
                            role = "Race Engineer 1" if GAME.cars[driverIndex] == 1 else "Race Engineer 2"
                            result = c.execute('''SELECT Rating FROM Staff WHERE Role=? AND Team=?''', (role, team)).fetchone()
                        engineerRating = int(GAME.Sanitise(result[0])) if result else 50
                        pitStopRating += round(engineerRating / 2)
                    else:
                        pitStopRating=100
                    pitStopScore = random.randint(1, pitStopRating)
                    if pitStopScore <= 20:
                        pitStopTime = random.uniform(4.0, 10.0)  # Terrible
                    elif pitStopScore <= 50:
                        pitStopTime = random.uniform(3.5, 5.0)   # Bad
                    elif pitStopScore <= 80:
                        pitStopTime = random.uniform(2.5, 3.5)   # Average
                    elif pitStopScore <= 100:
                        pitStopTime = random.uniform(2.2, 2.9)   # Good
                    else:
                        pitStopTime = random.uniform(1.8, 2.3)   # Amazing
                    if pitStopTime < GAME.bestPitStop[1]:
                        GAME.AddToLog(f"{GAME.drivers[driverIndex]} has just completed a {pitStopTime:.3f} second pit stop, the fastest of the race so far.")
                        GAME.bestPitStop = [GAME.drivers[driverIndex], pitStopTime]
                    if GAME.penalties[driverIndex]>0:
                        penalty=GAME.penalties[driverIndex]
                        GAME.penalties.pop(driverIndex)
                        GAME.penalties.insert(driverIndex,0)
                    else:
                        penalty=0
                    totalTimeLost = baseTimeLost + pitStopTime + penalty
                    distanceLost = round(totalTimeLost*41.67,3)
                    distance=GAME.distance[driverIndex]-distanceLost
                    GAME.distance.pop(driverIndex)
                    GAME.distance.insert(driverIndex,distance)
                    if pos<len(GAME.positions)-1:
                        newPos=pos
                        while True:
                            if distance<GAME.distance[GAME.positions[newPos+1]]:
                                newPos+=1
                                if newPos==len(GAME.positions)-1:
                                    break
                            else:
                                break
                        GAME.positions.remove(driverIndex)
                        GAME.positions.insert(newPos,driverIndex)
                    if GAME.replay==5:
                        if GAME.pitTyre[driverIndex]=="Medium":
                            if GAME.tyre[driverIndex]=="Hard":
                                GAME.pitTyre[driverIndex]="Soft"
                            else:
                                GAME.pitTyre[driverIndex]="Hard"
                        elif GAME.pitTyre[driverIndex]=="Intermediate":
                            GAME.pitTyre[driverIndex]="Hard"
                    if GAME.tyre[driverIndex]!=GAME.pitTyre[driverIndex]:
                        GAME.tyre[driverIndex] = GAME.pitTyre[driverIndex]
                        GAME.tyreCompoundsUsed[driverIndex]+=1
                    GAME.tyreRemaining[driverIndex] = 100
                    GAME.stops[driverIndex] += 1
                    lapsLeft=GAME.laps-GAME.lap[GAME.positions[0]]
                    if GAME.strategy[driverIndex]>GAME.stops[driverIndex]:
                        if lapsLeft<GAME.expectedTyreLife[0]:
                            pitTyre="Soft"
                        elif lapsLeft<GAME.expectedTyreLife[1] and random.randint(1,3)>1:
                            pitTyre="Medium"
                        else:
                            pitTyre="Hard"
                        if pitTyre=="Wet":
                            tyreLife=GAME.expectedTyreLife[3]
                        else:
                            tyreLife=GAME.expectedTyreLife[Tyres.index(pitTyre)]
                        if pitTyre=="Hard":
                            length=tyreLife+GAME.expectedTyreLife[1]
                        else:
                            length=tyreLife+GAME.expectedTyreLife[2]
                        pitLap=GAME.lap[driverIndex]+(lapsLeft*tyreLife/length)+random.randint(-3,3)
                        GAME.pitLap.pop(driverIndex)
                        GAME.pitLap.insert(driverIndex,pitLap)
                        GAME.pitTyre.pop(driverIndex)
                        GAME.pitTyre.insert(driverIndex,pitTyre)
                GAME.CalculateTime()
            removed=0
            for x in range(len(GAME.positions)):
                index=GAME.positions[x-removed]
                if GAME.faults[index]=="Failure":
                    GAME.positions.pop(x-removed)
                    removed+=1
            #Overtaking
            for x in range(len(GAME.positions)):
                driverID=GAME.positions[x-driversRemoved]
                driver=GAME.drivers[driverID]
                if GAME.replay==2:
                    replay=1
                    if x-driversRemoved>0:
                        if GAME.lap[GAME.positions[0]]>=50 and GAME.positions[x-driversRemoved-1]==3:
                            replay=1
                        elif GAME.positions[x-driversRemoved-1]==21 and driverID==20:
                            replay=-1
                        elif driverID==3 and x-driversRemoved>0 and GAME.lap[GAME.positions[0]]>=50:
                            replay=-1
                        elif driverID>19:
                            if GAME.positions[x-driversRemoved-1]!=20:
                                replay=0
                        elif GAME.overtaking[driverID]>5:
                            replay=0
                        elif GAME.positions[x-driversRemoved-1]>19 and x-driversRemoved==1:
                            replay=0
                elif GAME.replay==7:
                    replay=0
                    if x-driversRemoved>0:
                        if GAME.positions[x-driversRemoved-1]==20 and driverID==21:
                            replay=1
                        elif GAME.positions[x-driversRemoved-1]==3 and driverID!=20:
                            replay=1
                        elif GAME.positions[x-driversRemoved-1]==21 and driverID==20:
                            replay=-1
                elif GAME.replay==9:
                    if GAME.tyre[GAME.positions[x-1]]=="Soft" and GAME.lapPittedTo[x-1]<54:
                        replay=1
                    else:
                        replay=0
                elif GAME.replay==3:
                    if driver=="Lewis Hamilton" and GAME.positions[x-1-driversRemoved]==6:
                        replay=1
                        if GAME.lap[4]>7:
                            GAME.AddToLog("Jenson Button and Lewis Hamilton have crashed.")
                            GAME.positions.remove(4)
                            GAME.tyreRemaining[6]=0
                            GAME.safety=2
                            driversRemoved+=1
                    elif GAME.lap[6]>36 and driver=="Jenson Button" and GAME.positions[x-1-driversRemoved]==1:
                        replay=1
                        GAME.AddToLog("Jenson Button crashed into Fernando Alonso")
                        GAME.positions.remove(1)
                        GAME.tyreRemaining[6]=0
                        GAME.safety=2
                        driversRemoved+=1
                    elif GAME.positions[x-1-driversRemoved]==0 and not (driver=="Jenson Button" and GAME.lap[6]>60):
                        replay=1
                    elif GAME.positions[x-1-driversRemoved]==4:
                        replay=1
                    elif GAME.events==0 and driver=="Jenson Button":
                        replay=1
                    else:
                        replay=0
                else:
                    replay=0
                if driver not in driversUsed and x!=0 and overtakes<20 and replay<=0:
                    driversUsed.append(driver)
                    if GAME.safety==0:
                        teamOrders=0
                        faster=0
                        if (GAME.replay==1 or GAME.replay==9) and (driver=="Lewis Hamilton" or driver=="Max Verstappen") and driver!=GAME.car1 and GAME.teams[GAME.positions[x-1]]==GAME.teams[driverID]:
                            teamOrders=2
                        if GAME.teams[driverID]==GAME.team:
                            if (GAME.cars[driverID]==1 and "Maintain Position" in GAME.car1Instructions) or (GAME.cars[driverID]==2 and "Maintain Position" in GAME.car2Instructions):
                                teamOrders=1
                            if GAME.teams[GAME.positions[x-1-driversRemoved]]==GAME.team:
                                if ((GAME.cars[driverID]==1 and "Team Orders" in GAME.car1Instructions) or (GAME.cars[driverID]==2 and "Team Orders" in GAME.car2Instructions)) and GAME.tyreRemaining[driverID]>0:
                                    teamOrders=1
                                elif ((GAME.cars[driverID]==1 and "Team Orders" in GAME.car2Instructions) or (GAME.cars[driverID]==1 and "Team Orders" in GAME.car1Instructions)) and GAME.tyreRemaining[GAME.positions[x-1-driversRemoved]]>0:
                                    teamOrders=2    
                        if GAME.time[driverID]<0.1 and teamOrders!=-1:
                            if teamOrders==0:
                                outgripped=0
                                if GAME.wet==1:
                                    if GAME.tyre[driverID]=="Soft" or GAME.tyre[driverID]=="Medium" or GAME.tyre[driverID]=="Hard":
                                        Grip=GAME.grip[0]
                                    elif GAME.tyre[driverID]=="Intermediate":
                                        Grip=GAME.grip[1]
                                    else:
                                        Grip=GAME.grip[2]
                                    if GAME.tyre[GAME.positions[x-1-driversRemoved]]=="Soft" or GAME.tyre[GAME.positions[x-1-driversRemoved]]=="Medium" or GAME.tyre[GAME.positions[x-1-driversRemoved]]=="Hard":
                                        grip=GAME.grip[0]
                                    elif GAME.tyre[GAME.positions[x-1-driversRemoved]]=="Intermediate":
                                        grip=GAME.grip[1]
                                    else:
                                        grip=GAME.grip[2]
                                    if Grip>grip:
                                        outgripped=1
                                        faster=2
                                if outgripped==0:
                                    if replay==-1:
                                        faster=3
                                    elif (GAME.tyreRemaining[GAME.positions[x-1-driversRemoved]]==0 or GAME.lap[driverID]>GAME.lap[GAME.positions[x-1-driversRemoved]]) and GAME.tyreRemaining[driverID]>0:
                                        faster=3
                                    elif GAME.teams[GAME.positions[x-1-driversRemoved]]==GAME.team and (GAME.cars[GAME.positions[x-1-driversRemoved]]==1 and "Drive in Clean Air" in GAME.car1Instructions) or (GAME.cars[GAME.positions[x-1-driversRemoved]]==2 and "Drive in Clean Air" in GAME.car2Instructions):
                                        faster=3
                                    elif (GAME.tyreRemaining[GAME.positions[x-1-driversRemoved]]+20<=GAME.tyreRemaining[driverID] or GAME.tyreAggression[GAME.positions[x-1-driversRemoved]]+2<=GAME.tyreAggression[driverID] or GAME.fuelAggression[GAME.positions[x-1-driversRemoved]]+1<=GAME.fuelAggression[driverID] or GAME.ERS[GAME.positions[x-1-driversRemoved]]==0 or GAME.ERSdeployment[GAME.positions[x-1-driversRemoved]]+1<=GAME.ERSdeployment[driverID]) and GAME.tyreRemaining[driverID]>0 and GAME.ERS[driverID]>0:
                                        faster=2
                                    elif (GAME.tyreAggression[GAME.positions[x-1-driversRemoved]]<GAME.tyreAggression[driverID] and GAME.tyreRemaining[driverID]>=30) or GAME.tyreRemaining[GAME.positions[x-1-driversRemoved]]+10<=GAME.tyreRemaining[driverID]:
                                        faster=1
                                if GAME.ERSdeployment[driverID]==4 and GAME.ERSdeployment[x-1-driversRemoved]<4:
                                    faster+=1
                            aheadID=GAME.positions[x-1-driversRemoved]
                            ahead=GAME.drivers[aheadID]
                            difference=GAME.overtaking[driverID]-GAME.defending[aheadID]
                            if GAME.replay==9:
                                faster=3
                            if difference>=20 or faster==3 or teamOrders==2:
                                probability=14
                            elif difference>=15:
                                probability=15
                            elif difference>=10:
                                probability=17
                            elif difference>=5:
                                probability=19
                            elif difference>=0:
                                probability=21
                            elif difference>=-5:
                                probability=23
                            elif difference>=-10:
                                probability=26
                            elif difference>=-15:
                                probability=31
                            else:
                                probability=41
                            if faster==2:
                                probability-=5
                            elif faster==1:
                                probability-=3
                            probability-=GAME.overtakeability*2
                            try:
                                O=random.randint(1,probability)
                            except:
                                O=1
                            if O<=2 or faster>2 or teamOrders==2:
                                #Successful overtake
                                if x==1:
                                    message=(driver+" overtook "+ahead+" for the lead!")
                                elif x==2:
                                    message=(driver+" overtook "+ahead+" for 2nd place.")
                                elif x==3:
                                    message=(driver+" overtook "+ahead+" for 3rd place.")
                                elif x==21:
                                    message=(driver+" overtook "+ahead+" for 21st place.")
                                elif x==22:
                                    message=(driver+" overtook "+ahead+" for 22nd place.")
                                elif x==23:
                                    message=(driver+" overtook "+ahead+" for 23rd place.")
                                else:
                                    message=(driver+" overtook "+ahead+" for "+str(x)+"th place.")
                                GAME.AddToLog(message)
                                GAME.positions.pop(x-driversRemoved)
                                GAME.positions.insert(x-1-driversRemoved,driverID)
                                overtake=1
                                if GAME.playing==0 and GAME.sound==1:
                                    if x-driversRemoved==1:
                                        GAME.Voice(driver,"Lead")
                                    else:
                                        GAME.Voice(driver,"Overtake")
                                distance=GAME.distance[GAME.positions[x-driversRemoved]]+(random.randint(100,200)/100)
                                GAME.distance.pop(GAME.positions[x-1-driversRemoved])
                                GAME.distance.insert(GAME.positions[x-1-driversRemoved],distance)
                                if GAME.lap[GAME.positions[x-1-driversRemoved]]!=GAME.lap[GAME.positions[x-driversRemoved]]:
                                    lap=GAME.lap[GAME.positions[x-driversRemoved]]
                                    GAME.lap.pop(GAME.positions[x-1-driversRemoved])
                                    GAME.lap.insert(GAME.positions[x-1-driversRemoved], lap)
                            else:
                                overtake=0
                                distance=GAME.distance[GAME.positions[x-1-driversRemoved]]-(random.randint(2000,4000)/100)
                                GAME.distance.pop(GAME.positions[x-driversRemoved])
                                GAME.distance.insert(GAME.positions[x-driversRemoved],distance)
                                if GAME.lap[GAME.positions[x-1-driversRemoved]]!=GAME.lap[GAME.positions[x-driversRemoved]]:
                                    lap=GAME.lap[GAME.positions[x-1-driversRemoved]]
                                    GAME.lap.pop(GAME.positions[x-driversRemoved])
                                    GAME.lap.insert(GAME.positions[x-driversRemoved], lap)
                            if teamOrders==0 and GAME.replay>0:
                                control=GAME.control[driverID]+GAME.control[aheadID]
                                if control<=GAME.risk:
                                    control=GAME.risk+1
                                if random.randint(1,(2*control)-GAME.risk)==1:
                                    if overtake==1:
                                        crasher=ahead
                                        crashedInto=driver
                                    else:
                                        crasher=driver
                                        crashedInto=ahead
                                    severity=random.randint(GAME.risk,150)
                                    if severity>=135:
                                        #Severe
                                        if GAME.playing==0 and GAME.sound==1:
                                            if crasher=="Isack Hadjar":
                                                GAME.Voice(0,"Destroyed The Car")
                                            elif random.randint(1,2)==1:
                                                GAME.Voice(0,"Crash")
                                            else:
                                                GAME.Voice(crasher,"Out")
                                        driversOut=random.randint(1,2)
                                        drivers=[crasher,crashedInto]
                                        GAME.AddToLog(crasher+" crashed into "+crashedInto+", it was a severe crash.")
                                        GAME.crashMessage.append(crasher+" crashed into "+crashedInto+", it was a severe crash.")
                                        for y in range(driversOut):
                                            driverOut=random.choice(drivers)
                                            drivers.remove(driverOut)
                                            num=random.randint(1,100+GAME.risk)
                                            if num>=150:
                                                #Injured or dead
                                                if random.randint(1,5)==5 and GAME.season>2026:
                                                    #Dead
                                                    GAME.AddToLog(driverOut+" has died.")
                                                    GAME.safety=3
                                                    GAME.dead.append(driverOut)
                                                else:
                                                    #Injured
                                                    GAME.AddToLog(driverOut+" is injured and out of the race.")
                                                    GAME.crashMessage.append(driverOut+" is injured and out of the race.")
                                                    GAME.safety=3
                                                    GAME.injured.append(driverOut)
                                            elif num>=130:
                                                #Injured
                                                GAME.AddToLog(driverOut+" is injured and out of the race.")
                                                GAME.crashMessage.append(driverOut+" is injured and out of the race.")
                                                GAME.injured.append(driverOut)
                                                if random.randint(1,5)==5 and GAME.street==0 and GAME.safety<2:
                                                    GAME.safety=2
                                                else:
                                                    GAME.safety=3
                                            elif GAME.street==1:
                                                GAME.AddToLog(driverOut+" is out of the race.")
                                                GAME.crashMessage.append(driverOut+" is out of the race.")
                                                GAME.safety=3
                                            else:
                                                if GAME.safety<2:
                                                    GAME.safety=2
                                                else:
                                                    GAME.safety=3
                                                GAME.AddToLog(driverOut+" is out of the race.")
                                                GAME.crashMessage.append(driverOut+" is out of the race.")
                                            GAME.engineDurability.pop(GAME.drivers.index(driverOut))
                                            GAME.engineDurability.insert(GAME.drivers.index(driverOut), 0)
                                            repairBill=GAME.repairBill[GAME.drivers.index(driverOut)]+random.randint(2000000,5000000)
                                            GAME.repairBill.pop(GAME.drivers.index(driverOut))
                                            GAME.repairBill.insert(GAME.drivers.index(driverOut), repairBill)
                                            GAME.positions.remove(GAME.drivers.index(driverOut))
                                            driversRemoved+=1
                                            if driverOut==driver:
                                                out=1
                                        if driversOut==1:
                                            if driverOut==crasher:
                                                driver=crashedInto
                                            else:
                                                driver=crasher
                                            index=GAME.drivers.index(driver)
                                            if GAME.frontWings[index]==1:
                                                GAME.AddToLog(driver+" has major front wing and chassis damage.")
                                                GAME.frontWings.pop(index)
                                                GAME.frontWings.insert(index, 0)
                                            else:
                                                GAME.AddToLog(driver+" has major damage to their car.")
                                            damage=random.randint(40,70)
                                            repairBill=GAME.repairBill[index]+(damage*random.randint(10000,100000))
                                            GAME.repairBill.pop(index)
                                            GAME.repairBill.insert(index, repairBill)
                                            damage+=GAME.damage[index]
                                            GAME.damage.pop(index)
                                            GAME.damage.insert(index, damage)
                                            engineDurability=round(GAME.engineDurability[index]/2)
                                            GAME.engineDurability.pop(index)
                                            GAME.engineDurability.insert(index, engineDurability)
                                            if damage>=100:
                                                GAME.AddToLog("They are out of the race.")
                                                driversRemoved+=1
                                                if drivers[0]==driver:
                                                    out=1
                                                GAME.positions.remove(index)
                                                if GAME.safety<=1 and random.randint(1,2)==2:
                                                    GAME.safety=2
                                                else:
                                                    GAME.safety=3
                                            elif driver==crasher:
                                                #Penalty
                                                penalty=GAME.penalties[index]+10
                                                GAME.penalties.pop(index)
                                                GAME.penalties.insert(index, penalty)
                                                GAME.AddToLog(crasher+" has a 10 second penalty.")
                                                GAME.crashMessage.append(crasher+" has a 10 second penalty.")
                                            GAME.damage.insert(index, damage)
                                    elif severity>=100:
                                        if GAME.playing==0 and GAME.sound==1:
                                            if crasher=="Isack Hadjar":
                                                GAME.Voice(0,"Destroyed The Car")
                                            else:
                                                GAME.Voice(0,"Crash")
                                        #Damaging
                                        GAME.AddToLog(crasher+" crashed into "+crashedInto+", it was a bad crash.")
                                        GAME.crashMessage.append(crasher+" crashed into "+crashedInto+", it was a bad crash.")
                                        #Crasher
                                        index=GAME.drivers.index(crasher)
                                        if GAME.frontWings[index]==1:
                                            GAME.AddToLog(crasher+" has front wing and chassis damage.")
                                            GAME.frontWings.pop(index)
                                            GAME.frontWings.insert(index, 0)
                                        else:
                                            GAME.AddToLog(crasher+" has damage to their car.")
                                        damage=random.randint(20,60)
                                        repairBill=GAME.repairBill[index]+(damage*random.randint(10000,100000))
                                        GAME.repairBill.pop(index)
                                        GAME.repairBill.insert(index, repairBill)
                                        damage+=GAME.damage[index]
                                        GAME.damage.pop(index)
                                        GAME.damage.insert(index, damage)
                                        engineDurability=round(GAME.engineDurability[index]/2)
                                        GAME.engineDurability.pop(index)
                                        GAME.engineDurability.insert(index, engineDurability)
                                        if damage>=100:
                                            GAME.AddToLog("They are out of the race.")
                                            driversRemoved+=1
                                            if crasher==driver:
                                                out=1
                                            GAME.positions.remove(index)
                                            if GAME.safety<=1 and random.randint(1,2)==2:
                                                GAME.safety=2
                                            else:
                                                GAME.safety=3
                                        else:
                                            #Penalty
                                            penalty=GAME.penalties[index]+5
                                            GAME.penalties.pop(index)
                                            GAME.penalties.insert(index, penalty)
                                            GAME.AddToLog(crasher+" has a 5 second penalty.")
                                            GAME.crashMessage.append(crasher+" has a 5 second penalty.")
                                        GAME.damage.insert(index, damage)
                                        #Crashed Into
                                        index=GAME.drivers.index(crashedInto)
                                        if GAME.frontWings[index]==1:
                                            GAME.AddToLog(crashedInto+" has front wing and chassis damage.")
                                            GAME.frontWings.pop(index)
                                            GAME.frontWings.insert(index, 0)
                                        else:
                                            GAME.AddToLog(crashedInto+" has damage to their car.")
                                        damage=random.randint(20,60)
                                        repairBill=GAME.repairBill[index]+(damage*random.randint(10000,100000))
                                        GAME.repairBill.pop(index)
                                        GAME.repairBill.insert(index, repairBill)
                                        damage+=GAME.damage[index]
                                        GAME.damage.pop(index)
                                        GAME.damage.insert(index, damage)
                                        engineDurability=round(GAME.engineDurability[index]/2)
                                        GAME.engineDurability.pop(index)
                                        GAME.engineDurability.insert(index, engineDurability)
                                        if damage>=100:
                                            GAME.AddToLog("They are out of the race.")
                                            driversRemoved+=1
                                            if crashedInto==driver:
                                                out=1
                                            GAME.positions.remove(index)
                                            if GAME.safety<=1 and random.randint(1,2)==2:
                                                GAME.safety=2
                                            else:
                                                GAME.safety=3
                                        GAME.damage.insert(index, damage)
                                    else:
                                        if GAME.playing==0 and GAME.sound==1:
                                            if crasher=="Isack Hadjar":
                                                GAME.Voice(0,"Destroyed The Car")
                                            else:
                                                GAME.Voice(0,"Crash")
                                        #Minor
                                        GAME.AddToLog(crasher+" crashed into "+crashedInto+".")
                                        GAME.crashMessage.append(crasher+" crashed into "+crashedInto+".")
                                        #Crasher
                                        index=GAME.drivers.index(crasher)
                                        damage=random.randint(10,30)
                                        repairBill=GAME.repairBill[index]+(damage*random.randint(10000,100000))
                                        GAME.repairBill.pop(index)
                                        GAME.repairBill.insert(index, repairBill)
                                        if GAME.frontWings[index]==1:
                                            if damage>=20:
                                                GAME.AddToLog(crasher+" has front wing damage.")
                                            else:
                                                GAME.AddToLog(crasher+" has minor front wing damage.")
                                            GAME.frontWings.pop(index)
                                            GAME.frontWings.insert(index, 0)
                                        else:
                                            GAME.AddToLog(crasher+" has minor damage to their car.")
                                        damage+=GAME.damage[index]
                                        GAME.damage.pop(index)
                                        GAME.damage.insert(index, damage)
                                        engineDurability=round(GAME.engineDurability[index]/2)
                                        GAME.engineDurability.pop(index)
                                        GAME.engineDurability.insert(index, engineDurability)
                                        if damage>=100:
                                            GAME.AddToLog("They are out of the race.")
                                            driversRemoved+=1
                                            if crasher==driver:
                                                out=1
                                            GAME.positions.remove(index)
                                            if GAME.safety<=1 and random.randint(1,2)==2:
                                                GAME.safety=2
                                            else:
                                                GAME.safety=3
                                        GAME.damage.insert(index, damage)
                                        #CrashedInto
                                        index=GAME.drivers.index(crashedInto)
                                        damage=random.randint(10,30)
                                        repairBill=GAME.repairBill[index]+(damage*random.randint(10000,100000))
                                        GAME.repairBill.pop(index)
                                        GAME.repairBill.insert(index, repairBill)
                                        if GAME.frontWings[index]==1:
                                            if damage>=20:
                                                GAME.AddToLog(crashedInto+" has front wing damage.")
                                            else:
                                                GAME.AddToLog(crashedInto+" has minor front wing damage.")
                                            GAME.frontWings.pop(index)
                                            GAME.frontWings.insert(index, 0)
                                        else:
                                            GAME.AddToLog(crashedInto+" has minor damage to their car.")
                                        damage+=GAME.damage[index]
                                        GAME.damage.pop(index)
                                        GAME.damage.insert(index, damage)
                                        engineDurability=round(GAME.engineDurability[index]/2)
                                        GAME.engineDurability.pop(index)
                                        GAME.engineDurability.insert(index, engineDurability)
                                        if damage>=100:
                                            GAME.AddToLog("They are out of the race.")
                                            driversRemoved+=1
                                            if crasher==driver:
                                                out=1
                                            GAME.positions.remove(index)
                                            if GAME.safety<=1 and random.randint(1,2)==2:
                                                GAME.safety=2
                                            else:
                                                GAME.safety=3
                                        GAME.damage.insert(index, damage)
                            #Overtake Mode
                            if GAME.ers==1 and GAME.ERSdeployment[driverID]==4:
                                ERS=GAME.ERS[driverID]+random.randint(-5,5)-(10*(13-GAME.battery[driverID]))
                                if ERS<0:
                                    ERS=0
                                GAME.ERS[driverID]=ERS
                    else:
                        if GAME.distance[x-driversRemoved]>=GAME.distance[GAME.positions[x-1-driversRemoved]]:
                            distance=GAME.distance[GAME.positions[x-1-driversRemoved]]-(random.randint(100,200)/100)
                            GAME.distance.pop(x-driversRemoved)
                            GAME.distance.insert(x-driversRemoved, distance)

            #Mistakes
            if (GAME.replay==0 or GAME.replay==3 or GAME.replay==6) and GAME.safety==0:
                mistake=0
                GAME.CalculateTime()
                for x in range(len(GAME.positions)):
                    if mistake==0 and not (GAME.replay==6 and GAME.positions[x]==11):
                        try:
                            if (GAME.tyre[driverID]=="Soft" or GAME.tyre[driverID]=="Medium" or GAME.tyre[driverID]=="Hard") and GAME.water>=1.4 and random.randint(1,20)==20:
                                mistake=1
                            elif GAME.tyre[driverID]!="Wet" and GAME.water>=4.3 and random.randint(1,20)==20:
                                mistake=1
                            elif GAME.water>=5 and random.randint(1,50)==50:
                                mistake=1
                            driverID=GAME.positions[x]
                            driver=GAME.drivers[driverID]
                            confidence=GAME.confidence[driverID]
                            if confidence<15:
                                confidence=15
                            if GAME.water==0:
                                risk=GAME.risk-10
                            else:
                                if GAME.tyre[driverID]=="Soft" or GAME.tyre[driverID]=="Medium" or GAME.tyre[driverID]=="Hard":
                                    grip=GAME.grip[0]
                                elif GAME.tyre[driverID]=="Intermediate":
                                    grip=GAME.grip[1]
                                else:
                                    grip=GAME.grip[2]
                                risk=GAME.risk-grip
                            if GAME.tyreRemaining[driverID]<30:
                                risk+=30-GAME.tyreRemaining[driverID]
                                if GAME.tyreRemaining[driverID]==0:
                                    risk=random.randint(risk*2,risk*3)
                            if GAME.replay==6:
                                risk=risk*3
                            elif GAME.replay==3 and GAME.tyre[driverID]!="Intermediate" and GAME.tyre[driverID]!="Wet":
                                risk=risk*2
                            if random.randint(1,confidence*1500)<=risk or random.randint(1,GAME.control[driverID]*1500)<=risk or mistake>0:
                                #Mistake
                                if GAME.replay==3 and GAME.tyre[driverID]!="Intermediate" and GAME.tyre[driverID]!="Wet":
                                    mistake=random.randint(2,5)
                                elif GAME.street==1:
                                    mistake=random.randint(0,9)
                                else:
                                    mistake=random.randint(1,9)
                                if GAME.tyreRemaining[driverID]==0:
                                    if mistake>2:
                                        mistake-=2
                                if mistake<=1 and not ((driver=="Ayrton Senna" or driver=="Alain Prost" or driver=="Nigel Mansell" or driver=="Niki Lauda") and GAME.replay==6):
                                    #Crashed into wall
                                    if GAME.playing==0 and GAME.sound==1:
                                        if crasher=="Isack Hadjar":
                                            GAME.Voice(0,"Destroyed The Car")
                                        elif random.randint(1,2)==1:
                                            GAME.Voice(0,"Crash")
                                        else:
                                            GAME.Voice(crasher,"Out")
                                    GAME.AddToLog(f"{driver} crashed into the wall and is out of the race.")
                                    GAME.repairBill[driverID]+=random.randint(2000000,5000000)
                                    if GAME.replay==0:
                                        if GAME.street==1 or random.randint(1,4)==4:
                                            GAME.safety=3
                                            if random.randint(1,200)==200 and GAME.season>2026:
                                                    #Dead
                                                    GAME.AddToLog(f"{driver} has died.")
                                                    GAME.dead.append(driver)
                                            elif random.randint(1,6)==6:
                                                GAME.AddToLog(f"{driver} is injured.")
                                                GAME.injured.append(driver)
                                        else:
                                            GAME.safety=2
                                    GAME.positions.pop(x)
                                    engineDurability=GAME.engineDurability[driverID]-random.randint(20,60)
                                    GAME.engineDurability.pop(driverID)
                                    GAME.engineDurability.insert(driverID,engineDurability)
                                else:
                                    if mistake>5:
                                        #Lock up
                                        GAME.AddToLog(f"{driver} locked up.")
                                        tyreRemaining=GAME.tyreRemaining[driverID]
                                        tyreRemaining-=random.randint(10,20)
                                        if tyreRemaining<5:
                                            tyreRemaining=5
                                        GAME.tyreRemaining.pop(driverID)
                                        GAME.tyreRemaining.insert(driverID,tyreRemaining)
                                        timeLost=random.randint(5,40)/10
                                        timeAccum = 0
                                        pos=x
                                        i = 1
                                        while pos + i < len(GAME.positions):
                                            next_driver = GAME.positions[pos + i]
                                            timeAccum += GAME.time[next_driver]
                                            if timeAccum > timeLost:
                                                break
                                            i += 1
                                        newPos = min(pos + i - 1, len(GAME.positions) - 1)
                                        distanceLost = round(timeLost/41.67,3)
                                        GAME.positions.remove(driverID)
                                        GAME.positions.insert(newPos, driverID)
                                        GAME.distance[driverID] -= distanceLost
                                    else:
                                        #Spun
                                        GAME.AddToLog(f"{driver} has spun.")
                                        tyreRemaining=GAME.tyreRemaining[driverID]
                                        tyreRemaining-=random.randint(10,20)
                                        if tyreRemaining<5:
                                            tyreRemaining=5
                                        GAME.tyreRemaining.pop(driverID)
                                        GAME.tyreRemaining.insert(driverID,tyreRemaining)
                                        timeLost=random.randint(20,100)/10
                                        distanceLost = round(timeLost/41.67,3)
                                        GAME.distance[driverID] -= distanceLost
                                        if random.randint(1,2)==2:
                                            timeAccum = 0
                                            pos=x
                                            i = 1
                                            while pos + i < len(GAME.positions):
                                                next_driver = GAME.positions[pos + i]
                                                timeAccum += GAME.time[next_driver]
                                                if timeAccum > timeLost:
                                                    break
                                                i += 1
                                            newPos = min(pos + i - 1, len(GAME.positions) - 1)
                                            GAME.positions.remove(driverID)
                                            GAME.positions.insert(newPos, driverID)
                                    confidence=round(GAME.confidence[driverID]*random.randint(4,8)/10)
                                    GAME.confidence.pop(driverID)
                                    GAME.confidence.insert(driverID,confidence)
                        except:
                            mistake=1
        if GAME.raceFinished==0:
            root.after(1250, lambda: GAME.NextMove())
        elif GAME.raceFinished==1:
            if GAME.replay==0:
                root.after(3000, lambda: GAME.EndOfRace())
            else:
                GAME.EndReplay()
    def NextMove(self):
        if GAME.pause==3:
            if GAME.replay==1:
                GAME.AddToLog("Nicholas Latifi crashed into the wall.")
                GAME.safetyLaps=0
                GAME.positions.remove(15)
                GAME.pause=4
                GAME.ChangeScreen("Latifi Crash")
                root.after(4000, lambda: GAME.SC())
            elif GAME.replay<9:
                if GAME.displayed==1:
                    if GAME.sound==1:
                        sound_path = os.path.join(os.path.dirname(__file__), "Voicelines", "F1 Movie Audio 1.wav")
                        if os.path.isfile(sound_path):
                            winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
                    root.after(500, lambda: GAME.ChangeScreen("F1 Movie 1"))
                    root.after(14100, lambda: GAME.ChangeScreen("F1 Movie 2"))
                    root.after(22100, lambda: GAME.ChangeScreen("F1 Movie 3"))
                    root.after(40700, lambda: GAME.MovieFinale())
                elif GAME.displayed==2:
                    if GAME.sound==1:
                        sound_path = os.path.join(os.path.dirname(__file__), "Voicelines", "F1 Movie Audio 2.wav")
                        if os.path.isfile(sound_path):
                            winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
                    root.after(500, lambda: GAME.ChangeScreen("F1 Movie 4"))
                    root.after(10100, lambda: GAME.ChangeScreen("F1 Movie 5"))
                    if GAME.sound==1:
                        sound_path = os.path.join(os.path.dirname(__file__), "Voicelines", "F1 Movie Audio 3.wav")
                        if os.path.isfile(sound_path):
                            root.after(16800, lambda: winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC))
                    root.after(16650, lambda: GAME.ChangeScreen("F1 Movie 6"))
                    root.after(28150, lambda: GAME.MovieFinalLap())
                GAME.displayed=0
        if GAME.safety==2:
            if GAME.replay==3:
                if GAME.lap[0]==20:
                    GAME.safetyLaps=14
                else:
                    GAME.safetyLaps=random.randint(3,4)
            else:
                GAME.safetyLaps=random.randint(3,6)
            GAME.thingHappened=1
            GAME.SC()
        elif GAME.safety==3:
            GAME.RedFlag()
        elif GAME.pause==0:
            GAME.Move()
        elif GAME.pause==2:
            GAME.Instructions()
        else:
            root.after(250, lambda: GAME.NextMove())
    def MovieFinale(self):
        GAME.tyre=[]
        GAME.tyreRemaining=[]
        GAME.ERS=[]
        GAME.lap=[]
        GAME.lap_=[]
        GAME.time=[]
        GAME.distance=[]
        GAME.lapPittedTo=[]
        for x in range(20):
            GAME.tyre.append("Soft")
            GAME.tyreRemaining.append(88)
            GAME.ERS.append(100)
            GAME.ERSdeployment.pop(x)
            GAME.ERSdeployment.insert(x,3)
            GAME.lap.append(56)
            GAME.lap_.append(56)
            GAME.time.append(0)
            GAME.distance.append(0)
            GAME.tyreAggression.pop(x)
            GAME.tyreAggression.insert(x,5)
            GAME.lapPittedTo.append(55)
        for x in range(2):
            GAME.tyre.append("Soft")
            GAME.tyreRemaining.append(100)
            GAME.ERS.append(100)
            GAME.lap.append(56)
            GAME.lap_.append(56)
            GAME.time.append(0)
            GAME.distance.append(0)
            GAME.racePace.pop(20)
            GAME.racePace.append(205)
            GAME.overtaking.pop(20)
            GAME.overtaking.append(10)
            GAME.lapPittedTo.append(55)
        GAME.pause=1
        GAME.RefreshScreen()
        if GAME.sound==1:
            GAME.Voice(0,"Race Start")
    def MovieFinalLap(self):
        GAME.replay=8
        for x in range(2):
            GAME.positions.pop(0)
        GAME.pause=1
        GAME.RefreshScreen()
    def EndReplay(self):
        if GAME.replay==8 or GAME.replay==7:
            if GAME.teams[GAME.positions[0]]=="APX GP":
                #Win
                if GAME.sound==1:
                    sound_path = os.path.join(os.path.dirname(__file__), "Voicelines", "F1 Movie Audio 4.wav")
                    if os.path.isfile(sound_path):
                        winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
                root.after(500, lambda: GAME.ChangeScreen("F1 Movie 7"))
                root.after(6500, lambda: GAME.ChangeScreen("F1 Movie 8"))
                root.after(17700, lambda: GAME.ChangeScreen("F1 Movie 9"))
                if GAME.sound==1:
                    soundPath = os.path.join(os.path.dirname(__file__), "Voicelines", "F1 Movie Audio 5.wav")
                    if os.path.isfile(soundPath):
                        root.after(17600, lambda: winsound.PlaySound(soundPath, winsound.SND_FILENAME | winsound.SND_ASYNC))
            else:
                #Lose
                GAME.ChangeScreen("F1 Movie 10")
                if GAME.music==1:
                    path = os.path.join(os.path.dirname(__file__), "Music", "Better Luck Next Time.wav")
                    if os.path.isfile(path):
                        winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
            time=54000
        elif GAME.replay==9:
            winner=-1
            index=0
            while index<10 and winner==-1:
                if GAME.positions[index]<2:
                    winner=GAME.positions[index]
                index+=1
            if winner<1:
                GAME.ChangeScreen("Verstappen Wins")
            else:
                GAME.ChangeScreen("Hamilton Wins")
            GAME.DriverCelebration(GAME.drivers[winner])
            time=25000
        elif GAME.replay==3:
            if GAME.positions[0]==6:
                GAME.ChangeScreen("Canada 2011 Victory")
                SoundPath = os.path.join(os.path.dirname(__file__), "Music", "Podium Theme.wav")
            else:
                GAME.ChangeScreen("Canada 2011 Defeat")
                SoundPath = os.path.join(os.path.dirname(__file__), "Music", "Better Luck Next Time.wav")
            if GAME.music==1 and os.path.isfile(SoundPath):
                winsound.PlaySound(SoundPath, winsound.SND_FILENAME | winsound.SND_ASYNC)
            time=10000
        elif GAME.replay==4:
            points=[10,8,6,5,4,3,2,1]
            if 0 not in GAME.positions:
                winner="Lewis Hamilton"
            else:
                if 3 not in GAME.positions:
                    hamiltonPoints=0
                else:
                    pos=GAME.positions.index(3)
                    if pos<8:
                        hamiltonPoints=points[pos]
                    else:
                        hamiltonPoints=0
                pos=GAME.positions.index(0)
                if pos<8:
                    massaPoints=points[pos]
                if massaPoints-hamiltonPoints>6:
                    winner="Felipe Massa"
                else:
                    winner="Lewis Hamilton"
            GAME.ChangeScreen(f"{winner} Victory")
            if winner=="Lewis Hamilton":
                SoundPath = os.path.join(os.path.dirname(__file__), "Music", "United Kingdom National Anthem.wav")
            else:
                SoundPath = os.path.join(os.path.dirname(__file__), "Music", "Brazil National Anthem.wav")
            if GAME.music==1 and os.path.isfile(SoundPath):
                winsound.PlaySound(SoundPath, winsound.SND_FILENAME | winsound.SND_ASYNC)
            time=10000
        elif GAME.replay==5:
            if GAME.positions[0]==0:
                GAME.ChangeScreen("Hakkinen Victory")
            elif GAME.positions[0]==3:
                GAME.ChangeScreen("Schumacher Victory")
            else:
                GAME.ChangeScreen("Random Winner")
            time=10000
            if GAME.teams[GAME.positions[0]]==GAME.team:
                SoundPath = os.path.join(os.path.dirname(__file__), "Music", "Podium Theme.wav")
            elif GAME.screen!="Random Winner":
                SoundPath = os.path.join(os.path.dirname(__file__), "Music", "Better Luck Next Time.wav")
            else:
                time=0
                SoundPath="Random"
            if os.path.isfile(SoundPath) and GAME.music==1:
                winsound.PlaySound(SoundPath, winsound.SND_FILENAME | winsound.SND_ASYNC)
        elif GAME.replay==6:
            if GAME.teams[GAME.positions[0]]=="Toleman":
                SoundPath = os.path.join(os.path.dirname(__file__), "Music", "Brazil National Anthem.wav")
                GAME.ChangeScreen("Senna Celebration")
                if os.path.isfile(SoundPath) and GAME.music==1:
                    winsound.PlaySound(SoundPath, winsound.SND_FILENAME | winsound.SND_ASYNC)
                time=10000
            else:
                time=0
            
        root.after(time, lambda: GAME.ChangeScreen("Title Screen"))
        if GAME.music==1:
            SoundPath = os.path.join(os.path.dirname(__file__), "Music", "F1 Music.wav")
            if os.path.isfile(SoundPath):
                root.after(time, lambda: winsound.PlaySound(SoundPath, winsound.SND_FILENAME | winsound.SND_ASYNC))
    def Instructions(self):
        drivers=[]
        d=0
        if GAME.car1ID in GAME.positions:
            drivers.append(GAME.driver1)
            d+=1
        else:
            drivers.append(0)
        if GAME.car2ID in GAME.positions:
            drivers.append(GAME.driver2)
            d+=1
        else:
            drivers.append(0)
        if d>0:
            GAME.ChangeScreen("Instructions")
            instructions=["Team Orders","Drive in Clean Air","Maintain Position","Stop Team Orders","Use Racing Line","Overtake"]
            for x in range(len(drivers)):
                if drivers[x]!=0:
                    GAME.DisplayDriver(drivers[x],200+(x*640),500)
                    if drivers[x]==GAME.driver1:
                        instructionsGiven=GAME.car1Instructions.copy()
                    else:
                        instructionsGiven=GAME.car2Instructions.copy()
                    GAME.Button("Box",5+(x*1225),550)
                    for i in range(3):
                        if i==0 and GAME.teamOrders==0:
                            GAME.Button("Banned",5+(x*1225),610+(i*60))
                        elif instructions[i] in instructionsGiven:
                            GAME.Button(instructions[i+3],5+(x*1225),610+(i*60))
                        else:
                            GAME.Button(instructions[i],5+(x*1225),610+(i*60))
                    if GAME.replay==5:
                        tyre=tyres[0]
                        canvas.create_image((x*1225)-30, 525, anchor=tk.NW, image=tyre)
                        tyre=tyres[2]
                        canvas.create_image(140+(x*1225), 525, anchor=tk.NW, image=tyre)
                    elif GAME.replay==6:
                        tyre=tyres[4]
                        canvas.create_image(140+(x*1225), 525, anchor=tk.NW, image=tyre)
            GAME.Button("Back",5,30)
            GAME.Button("Tyre Data",1230,30)
        else:
            GAME.pause=0
    def Box(self,driverNumber,tyre):
        GAME.pittingDriver=driverNumber
        if tyre!=0:
            if GAME.pittingDriver==1:
                index=GAME.car1ID
            else:
                index=GAME.car2ID
            GAME.pitLap.pop(index)
            GAME.pitLap.insert(index,GAME.lap[index])
            GAME.pitTyre.pop(index)
            GAME.pitTyre.insert(index,tyre)
            GAME.pause=1
            GAME.RefreshScreen()
            GAME.NextMove()
        else:
            GAME.ChangeScreen("Box")
            for x in range(5):
                if Tyres[x]=="Wet":
                    text=f"{GAME.expectedTyreLife[3]} Laps"
                else:
                    text=f"{GAME.expectedTyreLife[x]} Laps"
                canvas.create_text(100+(x*280), 560, text=text, fill="white", font=("Arial", 30), anchor="nw")
            GAME.Button("Back",5,730)
    def TyreData(self):
        GAME.ChangeScreen("Tyre Data")
        GAME.Button("Back",5,730)
        canvas.create_text(15, 5, text="Name", fill="black", font=("Arial", 30), anchor="nw")
        canvas.create_text(265, 5, text="Tyre", fill="black", font=("Arial", 30), anchor="nw")
        canvas.create_text(415, 5, text="Age", fill="black", font=("Arial", 30), anchor="nw")
        canvas.create_text(515, 5, text="Stops", fill="black", font=("Arial", 30), anchor="nw")
        for x in range(len(GAME.positions)):
            index=GAME.positions[x]
            if x<9:
                canvas.create_text(15, 80+(x*25), text=f"{x+1}. {GAME.drivers[index]}", fill="black", font=("Arial", 15), anchor="nw")
            else:
                canvas.create_text(10, 80+(x*25), text=f"{x+1}. {GAME.drivers[index]}", fill="black", font=("Arial", 15), anchor="nw")
            canvas.create_text(265, 80+(x*25), text=GAME.tyre[index], fill="black", font=("Arial", 15), anchor="nw")
            canvas.create_text(415, 80+(x*25), text=f"{GAME.lap[index]-GAME.lapPittedTo[index]} Laps", fill="black", font=("Arial", 15), anchor="nw")
            canvas.create_text(550, 80+(x*25), text=GAME.stops[index], fill="black", font=("Arial", 15), anchor="nw")
    def RedFlag(self):
        lap=GAME.lap[GAME.positions[0]]
        if lap>=GAME.laps-5 or len(GAME.positions)<=5:
            #End of race
            GAME.EndOfRace()
        else:
            GAME.ChangeScreen("Red Flag")
            root.after(4000, lambda: GAME.RedFlagRestart())
    def RedFlagRestart(self):
        lap=GAME.lap[GAME.positions[0]]+1
        if GAME.wet==1:
            if GAME.rainStops!=0 and GAME.rainStops<=lap+1:
                GAME.rain=0
            if GAME.rain>0:
                GAME.water+=GAME.rain
            elif GAME.water>0:
                GAME.water=round(random.randint(round(GAME.water*500),round(GAME.water*1000))/1000,3)
            if GAME.water>GAME.maxWater:
                GAME.water=GAME.maxWater
        GAME.startLap=lap
        GAME.lap.clear()
        GAME.time.clear()
        GAME.tyreRemaining.clear()
        GAME.lapPittedTo.clear()
        GAME.distance.clear()
        for x in range(len(GAME.drivers)):
            GAME.lap.append(lap)
            GAME.time.append(0)
            GAME.tyreRemaining.append(100)
            GAME.lapPittedTo.append(lap)
            stops=GAME.stops[x]+1
            GAME.stops.pop(x)
            GAME.stops.insert(x,stops)
            if x in GAME.positions:
                GAME.distance.append(GAME.positions.index(x)*-2)
                if GAME.teams[x]!=GAME.team:
                    compounds=GAME.tyreCompoundsUsed[x]+1
                    GAME.tyreCompoundsUsed.pop(x)
                    GAME.tyreCompoundsUsed.insert(x,compounds)
                    if GAME.wet==0 or GAME.water==0 or GAME.rain==0:
                        if GAME.laps-lap<=10:
                            if GAME.tyre[x]=="Soft" and GAME.tyreCompoundsUsed[x]==1:
                                tyre="Medium"
                            elif (GAME.tyre[x]=="Medium" and GAME.tyreCompoundsUsed[x]==1) or random.randint(1,2)==1:
                                tyre="Soft"
                            else:
                                tyre="Medium"
                        else:
                            num=random.randint(1,3)
                            if ((num==2 and GAME.tyre[x]=="Medium") or (num==3 and GAME.tyre[x]=="Hard")) and GAME.tyreCompoundsUsed[x]==1:
                                num-=1
                            elif num==1 and GAME.tyre[x]=="Soft" and GAME.tyreCompoundsUsed[x]==1:
                                num=3
                            if num==1:
                                tyre="Soft"
                            elif num==2:
                                tyre="Medium"
                            else:
                                tyre="Hard"
                        #Pit strategy
                        if tyre=="Soft":
                            tyreLength=GAME.expectedTyreLife[0]
                        elif tyre=="Medium":
                            tyreLength=GAME.expectedTyreLife[1]
                        else:
                            tyreLength=GAME.expectedTyreLife[2]
                        GAME.pitLap.pop(x)
                        GAME.pitTyre.pop(x)
                        if GAME.laps-tyreLength<=3:
                            GAME.pitLap.insert(x,0)
                            GAME.pitTyre.insert(x,0)
                        else:
                            pitLap=lap+tyreLength+random.randint(-2,2)
                            GAME.pitLap.insert(x,pitLap)
                            if GAME.laps-pitLap<=10:
                                if random.randint(1,3)==1:
                                    pitTyre="Medium"
                                else:
                                    pitTyre="Soft"
                            elif GAME.laps-pitLap<=GAME.expectedTyreLife[1]:
                                if random.randint(1,2)==2:
                                    pitTyre="Medium"
                                else:
                                    pitTyre="Hard"
                            else:
                                num=random.randint(1,4)
                                if num==1:
                                    pitTyre="Soft"
                                elif num==4:
                                    pitTyre="Hard"
                                else:
                                    pitTyre="Medium"
                            GAME.pitTyre.insert(x,pitTyre)
                    elif GAME.water>2.5 and GAME.rain>0 and GAME.maxWater>4 and (GAME.rainStops==0 or GAME.rainStops>=lap+5):
                        tyre="Wet"
                    else:
                        tyre="Intermediate"
                    if tyre!=GAME.tyre[x]:
                        compounds=GAME.tyreCompoundsUsed[x]+1
                        GAME.tyreCompoundsUsed.pop(x)
                        GAME.tyreCompoundsUsed.insert(x,compounds)
                    GAME.tyre.pop(x)
                    GAME.tyre.insert(x,tyre)
            else:
                GAME.distance.append(0)
        if GAME.car1ID in GAME.positions or GAME.car2ID in GAME.positions:
            GAME.displayed=1
            GAME.RedFlagMenu()
        else:
            GAME.Start()
    def RedFlagMenu(self):
        GAME.ChangeScreen("Red Flag Menu")
        if GAME.displayed==1:
            driver=GAME.driver1
            index=GAME.car1ID
            if GAME.car1ID not in GAME.positions:
                GAME.displayed=2
        if GAME.displayed==2:
            driver=GAME.driver2
            index=GAME.car2ID
            if GAME.car2ID not in GAME.positions:
                GAME.displayed=3
                GAME.pause=1
                GAME.safety=0
                GAME.RefreshScreen()
                GAME.Start()
        if GAME.displayed<3:
            GAME.DisplayDriver(driver,520,500)
            GAME.Leaderboard()
            for x in range(len(GAME.log)):
                canvas.create_text(500, x*23, text=GAME.log[x], fill="black", font=("Arial", 15), anchor="nw")
            lap=GAME.lap[GAME.positions[0]]
            canvas.create_text(20, 5, text=f"Lap: {lap}/{GAME.laps}", fill="black", font=("Arial", 30), anchor="nw")
            if GAME.water==0:
                canvas.create_text(20, 80, text="Dry Track", fill="black", font=("Arial", 30), anchor="nw")
            else:
                canvas.create_text(20, 80, text=f"{round(GAME.water,2)}mm of water", fill="black", font=("Arial", 30), anchor="nw")
            for x in range(3):
                tyre=tyres[x]
                canvas.image=tyre
                canvas.create_image(510+(300*x), 230, anchor=tk.NW, image=tyre)
                canvas.create_text(650+(300*x), 260, text=(f"{GAME.expectedTyreLife[x]} Laps"), fill="black", font=("Arial", 20), anchor="nw")
            for x in range(2):
                tyre=tyres[x+3]
                canvas.image=tyre
                canvas.create_image(980, 350+(120*x), anchor=tk.NW, image=tyre)
                canvas.create_text(1120, 380+(120*x), text=(f"{GAME.expectedTyreLife[3]} Laps"), fill="black", font=("Arial", 20), anchor="nw")
            tyre=tyres[Tyres.index(GAME.tyre[index])]
            canvas.image=tyre
            canvas.create_image(1200, 590, anchor=tk.NW, image=tyre)
            canvas.create_text(1000, 625, text="Currently On", fill="black", font=("Arial", 20), anchor="nw")
    def SC(self):
        GAME.safety=2
        GAME.pitting=[]
        GAME.SCPitTyre=[]
        GAME.ChangeScreen("Safety Car")
        if GAME.replay==1:
            GAME.replay=9
        elif GAME.replay==3 and GAME.lap[0]>19 and GAME.lap[0]<30:
            GAME.pitLap[1]=36
            GAME.pitTyre[1]="Intermediate"
        if (GAME.lap[GAME.positions[0]]+GAME.safetyLaps>=GAME.laps and GAME.replay==0) or (GAME.replay==9 and GAME.pit==1 and random.randint(1,2)==2):
            GAME.distance=[]
            for x in range(len(GAME.drivers)):
                GAME.distance.append(0)
            if GAME.replay==0:
                root.after(3000, lambda: GAME.EndOfRace())
            else:
                root.after(3000, lambda: GAME.EndReplay())
        else:
            GAME.CalculateTime()
            #Water
            if GAME.wet==1 and GAME.replay==0:
                for x in range(GAME.safetyLaps):
                    lap=GAME.lap[GAME.positions[0]]+x+1
                    if (GAME.rainStops==0 or GAME.rainStops>lap) and GAME.rainStarts<=lap:
                        #Raining
                        if GAME.rain<GAME.maxRain:
                            GAME.rain=random.randint(int(GAME.rain*100),int(GAME.maxRain*100))/100
                        GAME.water+=GAME.rain
                        if GAME.water>GAME.maxWater:
                            GAME.water=GAME.maxWater
                    elif GAME.rainStops<=lap and GAME.rainStops!=0 and GAME.water>0:
                        #Drying
                        GAME.drying=random.randint(int(round(GAME.drying*100)),120)/100
                        GAME.water-=GAME.drying
                        if GAME.water<=0:
                            GAME.water=0
                            GAME.rainStopped=1
            GAME.displayed=1
            root.after(3000, lambda: GAME.SCMenu())
    def SCMenu(self):
        GAME.ChangeScreen("Safety Car Menu")
        if GAME.displayed==1:
            driver=GAME.driver1
            index=GAME.car1ID
            if GAME.car1ID not in GAME.positions:
                GAME.displayed=2
        if GAME.displayed==2:
            driver=GAME.driver2
            index=GAME.car2ID
            if GAME.car2ID not in GAME.positions:
                GAME.displayed=3
                GAME.EndSafetyCar()
        if GAME.displayed<3:
            GAME.DisplayDriver(driver,520,500)
            GAME.Leaderboard()
            for x in range(len(GAME.log)):
                canvas.create_text(500, x*23, text=GAME.log[x], fill="black", font=("Arial", 15), anchor="nw")
            lap=GAME.lap[GAME.positions[0]]+GAME.safetyLaps
            if GAME.replay==9:
                canvas.create_text(20, 5, text="Abu Dhabi 2021", fill="black", font=("Arial", 30), anchor="nw")
            else:
                canvas.create_text(20, 5, text=f"Lap: {lap}/{GAME.laps}", fill="black", font=("Arial", 30), anchor="nw")
                if GAME.water==0:
                    canvas.create_text(20, 80, text="Dry Track", fill="black", font=("Arial", 30), anchor="nw")
                else:
                    canvas.create_text(20, 80, text=f"{round(GAME.water,2)}mm of water", fill="black", font=("Arial", 30), anchor="nw")
            for x in range(3):
                tyre=tyres[x]
                canvas.image=tyre
                canvas.create_image(510+(300*x), 230, anchor=tk.NW, image=tyre)
                canvas.create_text(650+(300*x), 260, text=(f"{GAME.expectedTyreLife[x]} Laps"), fill="black", font=("Arial", 20), anchor="nw")
            for x in range(2):
                tyre=tyres[x+3]
                canvas.image=tyre
                canvas.create_image(980, 350+(120*x), anchor=tk.NW, image=tyre)
                canvas.create_text(1120, 380+(120*x), text=(f"{GAME.expectedTyreLife[3]} Laps"), fill="black", font=("Arial", 20), anchor="nw")
            GAME.Button("Stay Out",980, 620)
            tyre=tyres[Tyres.index(GAME.tyre[index])]
            canvas.image=tyre
            canvas.create_image(1200, 590, anchor=tk.NW, image=tyre)
            canvas.create_text(1320, 625, text=(f"{round(GAME.tyreRemaining[index])}%"), fill="black", font=("Arial", 20), anchor="nw")
    def EndSafetyCar(self):
        GAME.time.append(0)
        GAME.positions.append(-1)
        if GAME.replay==9:
            lap=56
        else:
            lap=GAME.lap[GAME.positions[0]]+GAME.safetyLaps
        lapsLeft=GAME.laps-lap
        pitted=[]
        for x in range(len(GAME.positions)-1):
            pit=0
            index=GAME.positions[x]
            if GAME.teams[index]!=GAME.team and not(GAME.replay==3 and GAME.lap[0]<10):
                if GAME.replay==3 and GAME.lap[0]>50 and GAME.tyre[index]=="Intermediate":
                    pit=1
                elif index<2 and GAME.replay==9:
                    if GAME.time[GAME.positions[1]]>20:
                        pit=1
                    else:
                        pit=1-GAME.pit
                elif GAME.pitLap[index]>0 and GAME.pitLap[index]<=lap+3:
                    pit=1
                elif GAME.time[index]>20 and GAME.time[GAME.positions[x+1]]>20:
                    pit=1
                else:
                    if GAME.wet==0:
                        if GAME.expectedTyreLife[2]*1.5>=lapsLeft:
                            pit=1
                        elif GAME.tyreRemaining[index]<50 and (lapsLeft>=10 or GAME.time[GAME.positions[x+1]]>=17 or random.randint(1,3)==3):
                            pit=1
                        elif GAME.tyreRemaining[index]<70 and (lapsLeft>=15 or GAME.time[GAME.positions[x+1]]>=17 or random.randint(1,3)==3):
                            pit=1
                        elif GAME.tyreRemaining[index]<=95 and GAME.time[GAME.positions[x+1]]>=20:
                            pit=1
                    else:
                        if GAME.water>0 and (GAME.rainStops==0 or GAME.rainStops>lap) and (GAME.tyre[index]=="Soft" or GAME.tyre[index]=="Medium" or GAME.tyre[index]=="Hard"):
                            pit=1
                        elif GAME.water>2.5 and GAME.maxWater>=4 and (GAME.rainStops==0 or GAME.rainStops>lap) and GAME.tyre[index]!="Wet":
                            pit=1
                        elif GAME.tyreRemaining[index]<60:
                            pit=1
                if pit==1:
                    GAME.pitting.append(GAME.drivers[index])
                    if GAME.wet==0:
                        if GAME.expectedTyreLife[2]*1.5>=lapsLeft:
                            if GAME.expectedTyreLife[0]>=lapsLeft and (GAME.tyre[index]!="Soft" or GAME.tyreCompoundsUsed[index]>1):
                                tyre="Soft"
                            elif GAME.expectedTyreLife[1]>=lapsLeft and (GAME.tyre[index]!="Medium" or GAME.tyreCompoundsUsed[index]>1):
                                tyre="Medium"
                            elif GAME.tyre[index]!="Hard" or GAME.tyreCompoundsUsed[index]>1:
                                tyre="Hard"
                            else:
                                tyre="Medium"
                            GAME.pitLap.pop(index)
                            GAME.pitLap.insert(index,0)
                        else:
                            tyre=GAME.pitTyre[index]
                            GAME.pitLap.pop(index)
                            pitLap=lap+GAME.expectedTyreLife[Tyres.index(tyre)]
                            GAME.pitLap.insert(index,pitLap)
                            lapsToDo=GAME.laps-pitLap
                            GAME.pitTyre.pop(index)
                            if lapsToDo<=GAME.expectedTyreLife[0] and (GAME.tyre[index]!="Soft" or GAME.tyreCompoundsUsed[index]>1):
                                GAME.pitTyre.insert(index,"Soft")
                            elif lapsToDo<=GAME.expectedTyreLife[1] and (GAME.tyre[index]!="Medium" or GAME.tyreCompoundsUsed[index]>1):
                                GAME.pitTyre.insert(index,"Medium")
                            elif GAME.tyre[index]!="Hard" or GAME.tyreCompoundsUsed[index]>1:
                                GAME.pitTyre.insert(index,"Hard")
                            else:
                                GAME.pitTyre.insert(index,"Medium")
                    else:
                        if GAME.water>2.5 and GAME.maxWater>=4 and (GAME.rainStops==0 or GAME.rainStops>lap):
                            tyre="Wet"
                        elif GAME.water>0 and (GAME.rainStops==0 or GAME.rainStops>lap):
                            tyre="Intermediate"
                        elif GAME.rainStarts>lap:
                            lapsToDo=GAME.rainStarts-lap
                            if lapsToDo<=GAME.expectedTyreLife[0]:
                                tyre="Soft"
                            elif lapsToDo<=GAME.expectedTyreLife[1]:
                                tyre="Medium"
                            else:
                                tyre="Hard"
                        else:
                            if lapsLeft<=GAME.expectedTyreLife[2]*1.5:
                                if GAME.expectedTyreLife[0]>=lapsLeft and (GAME.tyre[index]!="Soft" or GAME.tyreCompoundsUsed[index]>1):
                                    tyre="Soft"
                                elif GAME.expectedTyreLife[1]>=lapsLeft and (GAME.tyre[index]!="Medium" or GAME.tyreCompoundsUsed[index]>1):
                                    tyre="Medium"
                                elif GAME.tyre[index]!="Hard" or GAME.tyreCompoundsUsed[index]>1:
                                    tyre="Hard"
                                else:
                                    tyre="Medium"
                            else:
                                if (random.randint(1,2)==1 and(GAME.tyre[index]!="Medium" or GAME.tyreCompoundsUsed[index]>1)) or (GAME.tyre[index]=="Hard" or GAME.tyreCompoundsUsed[index]>1):
                                    tyre="Medium"
                                    pitLap=lap+GAME.expectedTyreLife[1]
                                else:
                                    tyre="Hard"
                                    pitLap=lap+GAME.expectedTyreLife[2]
                                lapsToDo=GAME.laps=pitLap
                                GAME.pitLap.pop(index)
                                GAME.pitLap.insert(index,pitLap)
                                GAME.pitTyre.pop(index)
                                if lapsToDo<=GAME.expectedTyreLife[0]:
                                    GAME.pitTyre.insert(index,"Soft")
                                elif lapsToDo<=GAME.expectedTyreLife[1]:
                                    GAME.pitTyre.insert(index,"Medium")
                                else:
                                    GAME.pitTyre.insert(index,"Hard")
                    if GAME.replay==3 and GAME.lap[0]<55 and tyre!="Intermediate" and tyre!="Wet":
                        tyre="Intermediate"
                    elif GAME.replay==3 and GAME.lap[0]>50:
                        if random.randint(1,3)==3:
                            tyre="Medium"
                        else:
                            tyre="Soft"
                    GAME.SCPitTyre.append(tyre)
        GAME.time.pop(len(GAME.time)-1)
        GAME.positions.pop(len(GAME.positions)-1)
        if len(GAME.pitting)>0:
            for x in range(len(GAME.pitting)):
                baseTimeLost = 10
                driver=GAME.pitting[x]
                try:
                    driver=int(driver)
                except:
                    if driver not in pitted:
                        pitted.append(driver)
                        GAME.AddToLog(f"{driver} is pitting.")
                        driverIndex=GAME.drivers.index(driver)
                        GAME.CalculateTime()
                        pos=GAME.positions.index(driverIndex)
                        team=GAME.teams[driverIndex]
                        if GAME.replay==0:
                            with sqlite3.connect(GAME.database) as c:
                                pitStopRating = int(GAME.Sanitise(c.execute('''SELECT Rating FROM Staff WHERE Role="Sporting Director" AND Team=?''', (team,)).fetchone()[0]))
                                role = "Race Engineer 1" if GAME.cars[driverIndex] == 1 else "Race Engineer 2"
                                result = c.execute('''SELECT Rating FROM Staff WHERE Role=? AND Team=?''', (role, team)).fetchone()
                            engineerRating = int(GAME.Sanitise(result[0])) if result else 50
                            pitStopRating += round(engineerRating / 2)
                        else:
                            pitStopRating=120
                        pitStopScore = random.randint(1, pitStopRating)
                        if pitStopScore <= 20:
                            pitStopTime = random.uniform(4.0, 10.0)  # Terrible
                        elif pitStopScore <= 50:
                            pitStopTime = random.uniform(3.0, 5.0)   # Bad
                        elif pitStopScore <= 80:
                            pitStopTime = random.uniform(2.3, 3.0)   # Average
                        elif pitStopScore <= 100:
                            pitStopTime = random.uniform(2.0, 2.6)   # Good
                        else:
                            pitStopTime = random.uniform(1.7, 2.2)   # Amazing
                        if pitStopTime < GAME.bestPitStop[1]:
                            GAME.AddToLog(f"{driver} has just completed a {pitStopTime:.3f} second pit stop, the fastest of the race so far.")
                            GAME.bestPitStop = [GAME.drivers[driverIndex], pitStopTime]
                        if GAME.penalties[driverIndex]>0:
                            penalty=GAME.penalties[driverIndex]
                            GAME.penalties.pop(driverIndex)
                            GAME.penalties.insert(driverIndex,0)
                        else:
                            penalty=0
                        totalTimeLost = baseTimeLost + pitStopTime + penalty
                        timeAccum = 0
                        i = 1
                        while pos + i < len(GAME.positions):
                            next_driver = GAME.positions[pos + i]
                            timeAccum += GAME.time[next_driver]
                            if timeAccum > totalTimeLost:
                                break
                            i += 1
                        if GAME.tyre[driverIndex]!=GAME.SCPitTyre[x]:
                            GAME.tyreCompoundsUsed[driverIndex]+=1
                        newPos = min(pos + i - 1, len(GAME.positions) - 1)
                        distanceLost = round(totalTimeLost/41.67,3)
                        GAME.positions.remove(driverIndex)
                        GAME.positions.insert(newPos, driverIndex)
                        GAME.distance[driverIndex] -= distanceLost
                        GAME.tyre.pop(driverIndex)
                        GAME.tyre.insert(driverIndex,GAME.SCPitTyre[x])
                        GAME.tyreRemaining[driverIndex] = 100
                        GAME.stops[driverIndex] += 1
                        GAME.lapPittedTo.pop(driverIndex)
                        GAME.lapPittedTo.insert(driverIndex,lap)
                        if GAME.pitLap[driverIndex]<=lap+3:
                            GAME.pitLap.pop(driverIndex)
                            GAME.pitLap.insert(driverIndex,0)
                            GAME.pitTyre.pop(driverIndex)
                            GAME.pitTyre.insert(driverIndex,0)
        GAME.distance=[]
        GAME.lap=[]
        GAME.pitting=[]
        for x in range(len(GAME.drivers)):
            GAME.distance.append(0)
            GAME.lap.append(lap)
        GAME.CalculateTime()
        GAME.pause=1
        GAME.safety=0
        GAME.RefreshScreen()
        GAME.NextMove()
    def Leaderboard(self):
        colours=["red","yellow","white","green","blue"]
        for x in range(len(GAME.positions)):
            driver=GAME.drivers[GAME.positions[x]]
            team=GAME.teams[GAME.positions[x]]
            time=GAME.time[GAME.positions[x]]
            if GAME.positions[x]==GAME.fastest[0]:
                colour="#B400FF"
            else:
                colour="white"
            if GAME.safety==0:
                Y=0
            else:
                Y=200
            if x<9:
                canvas.create_text(10, (x*24)+Y, text=f"{x+1}.{driver} {team}", fill=colour, font=("Arial", 15), anchor="nw")
            else:
                canvas.create_text(5, (x*24)+Y, text=f"{x+1}.{driver} {team}", fill=colour, font=("Arial", 15), anchor="nw")
            if GAME.safety<3:
                if x==0:
                    if GAME.replay==9:
                        lap=58
                    else:
                        lap=GAME.lap[GAME.positions[0]]
                        if GAME.replay==7 or GAME.replay==8:
                            if lap<59:
                                lap=56
                            elif lap<63:
                                lap=57
                            elif lap<67:
                                lap=58
                            else:
                                lap=59
                    if GAME.safety==2:
                        canvas.create_text(380, 200+(x*24), text="-", fill=colour, font=("Arial", 15), anchor="nw")
                    elif lap>GAME.laps:
                        canvas.create_text(380, x*24, text="Finished", fill=colour, font=("Arial", 15), anchor="nw")
                    else:
                        canvas.create_text(380, x*24, text=f"Lap {lap}/{GAME.laps}", fill=colour, font=("Arial", 15), anchor="nw")
                else:
                    canvas.create_text(380, (x*24)+Y, text=f"+{time}s", fill=colour, font=("Arial", 15), anchor="nw")
                tyre=GAME.tyre[GAME.positions[x]]
                canvas.create_text(475, (x*24)+Y, text=tyre[0], fill=colours[Tyres.index(tyre)], font=("Arial", 15), anchor="nw")
    def StartRace(self):
        GAME.log=[]
        GAME.ChangeScreen("Race Screen")
        if GAME.sound==1:
            GAME.Voice(0,"Race Start")
        if GAME.replay==2 and GAME.music==1:
            path = os.path.join(os.path.dirname(__file__), "Music", "F1 Movie Theme.wav")
            if os.path.isfile(path):
                root.after(3500, lambda: winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP))
        GAME.Leaderboard()
        GAME.RaceMenu()
        canvas.create_image(499, 193, anchor=tk.NW, image=raceImages[0])
        root.after(1000, lambda: GAME.Start())
        GAME.displayedImage=1
    def AddToLog(self,item):
        GAME.log.append(item)
        if len(GAME.log)>8:
            GAME.log.pop(0)
        GAME.RefreshScreen()
    def RefreshScreen(self):
        GAME.ChangeScreen("Race Screen")
        GAME.RaceMenu()
        GAME.CalculateTime()
        GAME.Leaderboard()
        GAME.crashMessage=[]
        for x in range(len(GAME.log)):
            canvas.create_text(500, x*23, text=GAME.log[x], fill="black", font=("Arial", 15), anchor="nw")
        GAME.RaceImage()
    def RaceImage(self):
        if GAME.replay==4:
            track="2008 Brazil"
        elif GAME.replay==6:
            track="1984 Monaco"
        elif GAME.replay==2 or GAME.replay==9:
            track="2021 Abu Dhabi"
        elif GAME.track=="Nürburgring":
            track="Nurburgring"
        elif GAME.track=="Imola" or GAME.track=="Miami" or GAME.track=="Las Vegas" or GAME.track=="Madrid" or GAME.track=="Hockenheim":
            track=GAME.track
        else:
            track=GAME.raceCountry
        canvas.create_image(497, 193, anchor=tk.NW, image=raceImages[(tracks.index(track)*2)+GAME.displayedImage])
    def RaceMenu(self):
        indexes=[GAME.car1ID,GAME.car2ID]
        drivers=[GAME.driver1,GAME.driver2]
        for x in range(2):
            if indexes[x] in GAME.positions and drivers[x]!=0:
                GAME.Button("Tyre Aggression",5+(x*1132),585)
                GAME.Button("Fuel Aggression",5+(x*1132),650)
                if GAME.ers>0:
                    GAME.Button("ERS Deployment",5+(x*1132),715)
                for y in range(3):
                    if y==0:
                        aggressions=["Conserve","Light","Balanced","Aggressive","Attack"]
                        aggression=aggressions[GAME.tyreAggression[indexes[x]]-1]
                    elif y==1:
                        aggressions=["Conserve","Balanced","Push"]
                        aggression=aggressions[GAME.fuelAggression[indexes[x]]-1]
                    elif GAME.ers>0:
                        
                        if GAME.ers==1:
                            if GAME.ERSdeployment[indexes[x]]==4 and (GAME.ERS[indexes[x]]<50 or GAME.water>=1 or GAME.positions[0]==indexes[x] or GAME.time[indexes[x]]>=1):
                                GAME.ERSdeployment[indexes[x]]=3
                            aggressions=["Recharge","Neutral","Boost","Overtake"]
                        else:
                            aggressions=["Harvest","Neutral","Deployed"]
                        aggression=aggressions[GAME.ERSdeployment[indexes[x]]-1]
                    else:
                        aggression=0
                    if aggression!=0:
                        canvas.create_text(100+(x*1120), 615+(y*65), text=aggression, fill="black", font=("Arial", 20), anchor="nw")
                canvas.create_text(315+(x*430), 585, text=f"{GAME.positions.index(indexes[x])+1}. {drivers[x]}", fill="black", font=("Arial", 25), anchor="nw")
                if GAME.replay==9:
                    lap=58
                else:
                    lap=GAME.lap[indexes[x]]
                if GAME.replay==7 or GAME.replay==8:
                    if lap<59:
                        lap=56
                    elif lap<63:
                        lap=57
                    else:
                        lap=58
                canvas.create_text(315+(x*430), 630, text=f"Lap {lap}", fill="black", font=("Arial", 30), anchor="nw")
                tyre=tyres[Tyres.index(GAME.tyre[indexes[x]])]
                canvas.image=tyre
                canvas.create_image(308+(x*430), 685, anchor=tk.NW, image=tyre)
                canvas.create_text(430+(x*430), 710, text=f"{round(GAME.tyreRemaining[indexes[x]])}%", fill="black", font=("Arial", 30), anchor="nw")
                if GAME.ers>0:
                    image=icons[0]
                    canvas.image=image
                    canvas.create_image(510+(x*430), 685, anchor=tk.NW, image=image)
                    canvas.create_text(540+(x*430), 725, text=f"{round(GAME.ERS[indexes[x]])}%", fill="black", font=("Arial", 12), anchor="nw")
                image=icons[3]
                canvas.image=image
                canvas.create_image(435+(x*430), 628, anchor=tk.NW, image=image)
                canvas.create_text(485+(x*430), 640, text=f"{round(GAME.fuel[indexes[x]],1)}kg", fill="black", font=("Arial", 22), anchor="nw")
                engineTemp=GAME.engineTemperature[indexes[x]]
                if engineTemp<120:
                    canvas.create_text(580+(x*430), 640, text=f"{round(engineTemp)}°C", fill="black", font=("Arial", 22), anchor="nw")
                else:
                    canvas.create_text(580+(x*430), 640, text=f"{round(engineTemp)}°C", fill="red", font=("Arial", 22), anchor="nw")
                if GAME.faults[indexes[x]]=="Minor" or GAME.faults[indexes[x]]=="Major":
                    if GAME.faults[indexes[x]]=="Minor":
                        image=icons[5]
                    else:
                        image=icons[6]
                    canvas.create_image(600+(x*430), 700, anchor=tk.NW, image=image)
                if GAME.penalties[indexes[x]]>0:
                    canvas.create_text(620+(x*430), 600, text=f"{GAME.penalties[indexes[x]]}s", fill="red", font=("Arial", 22), anchor="nw")
        if GAME.pause==0:
            GAME.Button("Pause",670,630)
        else:
            GAME.Button("Play",670,630)
        if GAME.car1ID in GAME.positions or GAME.car2ID in GAME.positions:
            GAME.Button("Helmet",670,685)
        if GAME.water==0:
            image=icons[2]
        elif GAME.water<1:
            image=icons[4]
            canvas.create_text(600, 750, text=f"{round(GAME.water,2)}mm", fill="black", font=("Arial", 15), anchor="nw")
        else:
            image=icons[1]
            canvas.create_text(600, 750, text=f"{round(GAME.water,2)}mm", fill="#0055FF", font=("Arial", 15), anchor="nw")
        canvas.image=image
        canvas.create_image(670, 735, anchor=tk.NW, image=image)
    def Start(self):
        F1=sqlite3.connect(GAME.database)
        c=F1.cursor()
        driversUsed=[]
        if GAME.wet==1:
            grip=10-(GAME.water*7)
            if grip<0:
                grip=0
            GAME.grip.append(grip)
            if GAME.water<=1:
                grip=10
            else:
                grip=10-((GAME.water-1)*2.6)
            GAME.grip.append(grip)
            if GAME.water<=1.5:
                grip=10
            else:
                grip=10-(GAME.water*0.8)
            GAME.grip.append(grip)
        else:
            GAME.grip=[10,10,10]
        driversRemoved=0
        for x in range(len(GAME.positions)):
            reaction=random.randint(GAME.reaction[GAME.positions[x-driversRemoved]]-5,GAME.reaction[GAME.positions[x-driversRemoved]]+5)/100
            if GAME.tyre[GAME.positions[x-driversRemoved]]=="Soft":
                tyrePace=GAME.tyrePace[0]*GAME.grip[0]/10
            elif GAME.tyre[GAME.positions[x-driversRemoved]]=="Medium":
                tyrePace=GAME.tyrePace[1]*GAME.grip[0]/10
            elif GAME.tyre[GAME.positions[x-driversRemoved]]=="Hard":
                tyrePace=GAME.tyrePace[2]*GAME.grip[0]/10
            elif GAME.tyre[GAME.positions[x-driversRemoved]]=="Intermediate":
                tyrePace=0.8*GAME.grip[1]
            else:
                tyrePace=0.2*GAME.grip[2]
            distance=GAME.distance[GAME.positions[x-driversRemoved]]
            distance+=GAME.racePace[GAME.positions[x-driversRemoved]]*tyrePace*reaction/100
            GAME.distance.pop(GAME.positions[x-driversRemoved])
            GAME.distance.insert(GAME.positions[x-driversRemoved],distance)
            index=GAME.positions[x-driversRemoved]
            #Tyre Usage
            if GAME.tyre[index]=="Soft":
                tyreWear=GAME.tyreWear[0]*GAME.tyreAggression[index]/3
            elif GAME.tyre[index]=="Medium":
                tyreWear=GAME.tyreWear[1]*GAME.tyreAggression[index]/3
            elif GAME.tyre[index]=="Hard":
                tyreWear=GAME.tyreWear[2]*GAME.tyreAggression[index]/3
            elif GAME.tyre[index]=="Intermediate" or (GAME.tyre[index]=="Wet" and GAME.replay==5):
                if GAME.water>=1:
                    tyreWear=GAME.tyreWear[3]*GAME.tyreAggression[index]/3
                elif GAME.water>=0.8:
                    tyreWear=GAME.tyreWear[3]*GAME.tyreAggression[index]/2.5
                elif GAME.water>=0.5:
                    tyreWear=GAME.tyreWear[3]*GAME.tyreAggression[index]
                else:
                    tyreWear=GAME.tyreWear[3]*GAME.tyreAggression[index]*3
            else:
                if GAME.water>=4:
                    tyreWear=GAME.tyreWear[3]*GAME.tyreAggression[index]/3
                elif GAME.water>=2.5:
                    tyreWear=GAME.tyreWear[3]*GAME.tyreAggression[index]/2.5
                elif GAME.water>=2:
                    tyreWear=GAME.tyreWear[3]*GAME.tyreAggression[index]
                elif GAME.water>=1.5:
                    tyreWear=GAME.tyreWear[3]*GAME.tyreAggression[index]*2
                else:
                    tyreWear=GAME.tyreWear[3]*GAME.tyreAggression[index]*5
            try:
                t=random.randint(GAME.tyrePreservation[index],200)
            except:
                t=200
            tyreWear=tyreWear*round(((201-t)/100))

            #Fuel Usage
            try:
                fuelUsage=45*GAME.fuelAggression[index]/GAME.laps
            except:
                fuelUsage=90/GAME.laps

            #ERS Usage
            if GAME.ers==1:
                if GAME.ERSdeployment[index]==1:
                    ERS=GAME.ERS[index]+random.randint(30,50)
                    if ERS>100:
                        ERS=100
                    if ERS>90 and GAME.teams[index]!=GAME.team:
                        GAME.ERSdeployment.pop(index)
                        GAME.ERSdeployment.insert(index, 3)
                elif GAME.ERSdeployment[index]==2:
                    ERS=GAME.ERS[index]
                else:
                    ERS=GAME.ERS[index]-random.randint(5,10)
                    if ERS<0:
                        ERS=0
        for x in range(len(GAME.positions)):
            driverID=GAME.positions[x-driversRemoved]
            driver=GAME.drivers[driverID]
            if driver not in driversUsed and x!=0 and GAME.replay==0:
                driversUsed.append(driver)
                if GAME.safety==0:
                    overtake=1
                    out=0
                    while overtake==1 and out==0:
                        overtake=0
                        if GAME.distance[driverID]>GAME.distance[GAME.positions[x-1-driversRemoved]]:
                            aheadID=GAME.positions[x-1-driversRemoved]
                            ahead=GAME.drivers[aheadID]
                            difference=GAME.overtaking[driverID]-GAME.defending[aheadID]
                            if difference>=20:
                                probability=3
                            elif difference>=15:
                                probability=4
                            elif difference>=10:
                                probability=6
                            elif difference>=5:
                                probability=8
                            elif difference>=0:
                                probability=10
                            elif difference>=-5:
                                probability=12
                            elif difference>=-10:
                                probability=15
                            elif difference>=-15:
                                probability=20
                            else:
                                probability=30
                            if random.randint(1,probability)<=2:
                                #Successful overtake
                                if x==1:
                                    message=(driver+" overtook "+ahead+" for the lead!")
                                elif x==2:
                                    message=(driver+" overtook "+ahead+" for 2nd place.")
                                elif x==3:
                                    message=(driver+" overtook "+ahead+" for 3rd place.")
                                elif x==21:
                                    message=(driver+" overtook "+ahead+" for 21st place.")
                                else:
                                    message=(driver+" overtook "+ahead+" for "+str(x)+"th place.")
                                GAME.AddToLog(message)
                                GAME.positions.pop(x-driversRemoved)
                                GAME.positions.insert(x-1-driversRemoved,driverID)
                                overtake=1
                                distance=GAME.distance[GAME.positions[x-driversRemoved]]+(random.randint(100,200)/100)
                                GAME.distance.pop(GAME.positions[x-1-driversRemoved])
                                GAME.distance.insert(GAME.positions[x-1-driversRemoved],distance)
                            else:
                                GAME.distance.pop(x-driversRemoved)
                                distance=GAME.distance[x-1-driversRemoved]-(random.randint(100,200)/100)
                                GAME.distance.insert(x-driversRemoved,distance)
                            if GAME.replay==0:
                                control=GAME.control[driverID]+GAME.control[aheadID]
                                if control<=GAME.risk:
                                    control=GAME.risk+1
                                if random.randint(1,(control-GAME.risk)*3)==1:
                                    if overtake==1:
                                        crasher=ahead
                                        crashedInto=driver
                                    else:
                                        crasher=driver
                                        crashedInto=ahead
                                    severity=random.randint(GAME.risk,150)
                                    if severity>=135:
                                        #Severe
                                        if GAME.playing==0 and GAME.sound==1:
                                            if crasher=="Isack Hadjar":
                                                GAME.Voice(0,"Destroyed The Car")
                                            elif random.randint(1,2)==1:
                                                GAME.Voice(0,"Crash")
                                            else:
                                                GAME.Voice(crasher,"Out")
                                        driversOut=random.randint(1,2)
                                        drivers=[crasher,crashedInto]
                                        GAME.AddToLog(crasher+" crashed into "+crashedInto+", it was a severe crash.")
                                        for y in range(driversOut):
                                            driverOut=random.choice(drivers)
                                            num=random.randint(1,100+GAME.risk)
                                            if num>=150:
                                                #Injured or dead
                                                if random.randint(1,5)==5 and GAME.season>2026:
                                                    #Dead
                                                    GAME.AddToLog(driverOut+" has died.")
                                                    GAME.dead.append(driverOut)
                                                    GAME.safety=3
                                                else:
                                                    #Injured
                                                    GAME.AddToLog(driverOut+" is injured and out of the race.")
                                                    GAME.injured.append(driverOut)
                                                    GAME.safety=3
                                            elif num>=130:
                                                #Injured
                                                GAME.AddToLog(driverOut+" is injured and out of the race.")
                                                GAME.injured.append(driverOut)
                                                if random.randint(1,5)==5 and GAME.Street==0 and GAME.safet<2:
                                                    GAME.safety=2
                                                else:
                                                    GAME.safety=3
                                            elif GAME.street==1:
                                                GAME.AddToLog(driverOut+" is out of the race.")
                                                GAME.safety=3
                                            else:
                                                if GAME.safety<2:
                                                    GAME.safety=2
                                                else:
                                                    GAME.safety=3
                                                GAME.AddToLog(driverOut+" is out of the race.")
                                            GAME.engineDurability.pop(GAME.drivers.index(driverOut))
                                            GAME.engineDurability.insert(GAME.drivers.index(driverOut), 0)
                                            repairBill=GAME.repairBill[GAME.drivers.index(driverOut)]+random.randint(2000000,5000000)
                                            GAME.repairBill.pop(GAME.drivers.index(driverOut))
                                            GAME.repairBill.insert(GAME.drivers.index(driverOut), repairBill)
                                            GAME.positions.remove(GAME.drivers.index(driverOut))
                                            driversRemoved+=1
                                            if driverOut==driver:
                                                out=1
                                        if driversOut==1:
                                            index=GAME.drivers.index(drivers[0])
                                            if GAME.frontWings[index]==1:
                                                GAME.AddToLog(drivers[0]+" has major front wing and chassis damage.")
                                                GAME.frontWings.pop(index)
                                                GAME.frontWings.insert(index, 0)
                                            else:
                                                GAME.AddToLog(drivers[0]+" has major damage to their car.")
                                            damage=random.randint(40,70)
                                            repairBill=GAME.repairBill[index]+(damage*random.randint(10000,100000))
                                            GAME.repairBill.pop(index)
                                            GAME.repairBill.insert(index, repairBill)
                                            damage+=GAME.damage[index]
                                            GAME.damage.pop(index)
                                            engineDurability=round(GAME.engineDurability[index]/2)
                                            GAME.engineDurability.pop(index)
                                            GAME.engineDurability.insert(index, engineDurability)
                                            if damage>=100:
                                                GAME.AddToLog("They are out of the race.")
                                                driversRemoved+=1
                                                GAME.positions.remove(index)
                                                if drivers[0]==driver:
                                                    out=1
                                                if GAME.safety<=1 and random.randint(1,2)==2:
                                                    GAME.safety=2
                                                else:
                                                    GAME.safety=3
                                            elif drivers[0]==crasher:
                                                #Penalty
                                                penalty=GAME.penalties[index]+10
                                                GAME.penalties.pop(index)
                                                GAME.penalties.insert(index, penalty)
                                                GAME.AddToLog(crasher+" has a 10 second penalty.")
                                            GAME.damage.insert(index, damage)
                                    elif severity>=100:
                                        #Damaging
                                        if GAME.playing==0 and GAME.sound==1:
                                            if crasher=="Isack Hadjar":
                                                GAME.Voice(0,"Destroyed The Car")
                                            else:
                                                GAME.Voice(0,"Crash")
                                        GAME.AddToLog(crasher+" crashed into "+crashedInto+", it was a bad crash.")
                                        #Crasher
                                        index=GAME.drivers.index(crasher)
                                        if GAME.frontWings[index]==1:
                                            GAME.AddToLog(crasher+" has front wing and chassis damage.")
                                            GAME.frontWings.pop(index)
                                            GAME.frontWings.insert(index, 0)
                                        else:
                                            GAME.AddToLog(crasher+" has damage to their car.")
                                        damage=random.randint(20,60)
                                        repairBill=GAME.repairBill[index]+(damage*random.randint(10000,100000))
                                        GAME.repairBill.pop(index)
                                        GAME.repairBill.insert(index, repairBill)
                                        damage+=GAME.damage[index]
                                        GAME.damage.pop(index)
                                        engineDurability=round(GAME.engineDurability[index]/2)
                                        GAME.engineDurability.pop(index)
                                        GAME.engineDurability.insert(index, engineDurability)
                                        if damage>=100:
                                            GAME.AddToLog("They are out of the race.")
                                            driversRemoved+=1
                                            if crasher==driver:
                                                out=1
                                            GAME.positions.remove(index)
                                            if GAME.safety<=1 and random.randint(1,2)==2:
                                                GAME.safety=2
                                            else:
                                                GAME.safety=3
                                        else:
                                            #Penalty
                                            penalty=GAME.penalties[index]+5
                                            GAME.penalties.pop(index)
                                            GAME.penalties.insert(index, penalty)
                                            GAME.AddToLog(crasher+" has a 5 second penalty.")
                                        GAME.damage.insert(index, damage)
                                        #Crashed Into
                                        index=GAME.drivers.index(crashedInto)
                                        if GAME.frontWings[index]==1:
                                            GAME.AddToLog(crashedInto+" has front wing and chassis damage.")
                                            GAME.frontWings.pop(index)
                                            GAME.frontWings.insert(index, 0)
                                        else:
                                            GAME.AddToLog(crashedInto+" has damage to their car.")
                                        damage=random.randint(20,60)
                                        repairBill=GAME.repairBill[index]+(damage*random.randint(10000,100000))
                                        GAME.repairBill.pop(index)
                                        GAME.repairBill.insert(index, repairBill)
                                        damage+=GAME.damage[index]
                                        GAME.damage.pop(index)
                                        engineDurability=round(GAME.engineDurability[index]/2)
                                        GAME.engineDurability.pop(index)
                                        GAME.engineDurability.insert(index, engineDurability)
                                        if damage>=100:
                                            GAME.AddToLog("They are out of the race.")
                                            driversRemoved+=1
                                            if crashedInto==driver:
                                                out=1
                                            GAME.positions.remove(index)
                                            if GAME.safety<=1 and random.randint(1,2)==2:
                                                GAME.safety=2
                                            else:
                                                GAME.safety=3
                                        GAME.damage.insert(index, damage)
                                    else:
                                        #Minor
                                        if GAME.playing==0 and GAME.sound==1:
                                            if crasher=="Isack Hadjar":
                                                GAME.Voice(0,"Destroyed The Car")
                                            else:
                                                GAME.Voice(0,"Crash")
                                        GAME.AddToLog(crasher+" crashed into "+crashedInto+".")
                                        #Crasher
                                        index=GAME.drivers.index(crasher)
                                        damage=random.randint(10,30)
                                        repairBill=GAME.repairBill[index]+(damage*random.randint(10000,100000))
                                        GAME.repairBill.pop(index)
                                        GAME.repairBill.insert(index, repairBill)
                                        if GAME.frontWings[index]==1:
                                            if damage>=20:
                                                GAME.AddToLog(crasher+" has front wing damage.")
                                            else:
                                                GAME.AddToLog(crasher+" has minor front wing damage.")
                                            GAME.frontWings.pop(index)
                                            GAME.frontWings.insert(index, 0)
                                        else:
                                            GAME.AddToLog(crasher+" has minor damage to their car.")
                                        damage+=GAME.damage[index]
                                        GAME.damage.pop(index)
                                        engineDurability=round(GAME.engineDurability[index]/2)
                                        GAME.engineDurability.pop(index)
                                        GAME.engineDurability.insert(index, engineDurability)
                                        if damage>=100:
                                            GAME.AddToLog("They are out of the race.")
                                            driversRemoved+=1
                                            if crasher==driver:
                                                out=1
                                            GAME.positions.remove(index)
                                            if GAME.safety<=1 and random.randint(1,2)==2:
                                                GAME.safety=2
                                            else:
                                                GAME.safety=3
                                        GAME.damage.insert(index, damage)
                                        #CrashedInto
                                        index=GAME.drivers.index(crashedInto)
                                        damage=random.randint(10,30)
                                        repairBill=GAME.repairBill[index]+(damage*random.randint(10000,100000))
                                        GAME.repairBill.pop(index)
                                        GAME.repairBill.insert(index, repairBill)
                                        if GAME.frontWings[index]==1:
                                            if damage>=20:
                                                GAME.AddToLog(crashedInto+" has front wing damage.")
                                            else:
                                                GAME.AddToLog(crashedInto+" has minor front wing damage.")
                                            GAME.frontWings.pop(index)
                                            GAME.frontWings.insert(index, 0)
                                        else:
                                            GAME.AddToLog(crashedInto+" has minor damage to their car.")
                                        damage+=GAME.damage[index]
                                        GAME.damage.pop(index)
                                        engineDurability=round(GAME.engineDurability[index]/2)
                                        GAME.engineDurability.pop(index)
                                        GAME.engineDurability.insert(index, engineDurability)
                                        if damage>=100:
                                            GAME.AddToLog("They are out of the race.")
                                            driversRemoved+=1
                                            if crashedInto==driver:
                                                out=1
                                            GAME.positions.remove(index)
                                            if GAME.safety<=1 and random.randint(1,2)==2:
                                                GAME.safety=2
                                            else:
                                                GAME.safety=3
                                        GAME.damage.insert(index, damage)
                                    
        if GAME.safety==2:
            GAME.safetyLaps=random.randint(3,6)
            GAME.thingHappened=1
            GAME.SC()
        elif GAME.safety==3:
            GAME.RedFlag()
        F1.commit()
        F1.close()
        if GAME.safety!=3:
            root.after(100, lambda: GAME.NextMove())
    def YourDriverDied(self,name):
        replacement=0
        with sqlite3.connect(GAME.database) as c:
            f=c.execute("SELECT Name FROM Drivers WHERE Team=? AND Role='Reserve'",(GAME.team,)).fetchall()
            if len(f)==0:
                f=c.execute("SELECT Name FROM Drivers WHERE Team=? AND Role='Junior' AND Age>17",(GAME.team,)).fetchall()
                if len(f)==0:
                    f=c.execute("SELECT Name FROM Drivers WHERE Team='Free Agent' AND Age>17").fetchall()
            replacement=GAME.Sanitise(random.choice(f))
            role=GAME.Sanitise(c.execute("SELECT Role FROM Drivers WHERE Name=?",(name,)).fetchall()[0])
            newTeam=GAME.Sanitise(c.execute("SELECT NewTeam FROM Drivers WHERE Name=?",(replacement,)).fetchall()[0])
            salary=int(GAME.Sanitise(c.execute("SELECT Salary FROM Drivers WHERE Name=?",(replacement,)).fetchall()[0]))
            rating=int(GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Name=?",(replacement,)).fetchall()[0]))
            if rating*50000>salary:
                salary=rating*50000
            c.execute("UPDATE Drivers SET Team=?, Role=?, Salary=? WHERE Name=?",(GAME.team,role,salary,replacement,))
            if newTeam=="0":
                c.execute("UPDATE Drivers SET ContractEnd=? WHERE Name=?",(GAME.season,replacement,))
    def EndOfRace(self):
        #Penalties
        for index in GAME.positions:
            if GAME.penalties[index]>0:
                GAME.distance[index]-=GAME.penalties[index]*41.67
        for x in range (len(GAME.positions)):
            index=GAME.positions[x]
            position=x
            distance=GAME.distance[x]
            while True:
                if position==len(GAME.positions)-1:
                    break
                elif distance<GAME.distance[position+1]:
                    GAME.distance.pop(position)
                    GAME.distance.insert(position+1,distance)
                    position+=1
                else:
                    break
        GAME.CalculateTime()
        #Disqualifications
        if GAME.wet==0:
            disqualified=[]
            for x in range(len(GAME.positions)):
                if GAME.tyreCompoundsUsed[GAME.positions[x]]<2:
                    disqualified.append(x)
            if len(disqualified)>0:
                GAME.ChangeScreen("Breaking News")
                for x in range(len(disqualified)):
                    canvas.create_text(150, 180+(x*50), text=f"{GAME.drivers[GAME.positions[disqualified[x]]]} is disqualified.", fill="white", font=("Arial", 30), anchor="nw")
                for x in range(len(disqualified)):
                    GAME.positions.pop(disqualified[x]-x)
                root.after(4000, lambda: GAME.Podium())
            else:
                GAME.Podium()
        else:
            GAME.Podium()
    def Podium(self):
        GAME.ChangeScreen("Podium")
        GAME.Button("Results",1230,5)
        for i in range(3):
            index=GAME.positions[i]
            driver=GAME.drivers[index]
            if i==0:
                if GAME.music==1:
                    if driver=="Fernando Alonso":
                        path = os.path.join(os.path.dirname(__file__), "Music", "Fernando Alonso Song.wav")
                        if os.path.isfile(path):
                            winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
                    else:
                        country=0
                        team=GAME.teams[GAME.positions[0]]
                        with sqlite3.connect(GAME.database) as c:
                            if len(c.execute("SELECT Country FROM Drivers WHERE Country=? AND Name=?",(GAME.raceCountry,driver,)).fetchall())>0:
                                country=1
                            else:
                                if len(c.execute("SELECT Country FROM Teams WHERE Country=? AND Name=?",(GAME.raceCountry,team,)).fetchall())>0:
                                    country=1
                            if country==1:
                                reputation=int(GAME.Sanitise(c.execute("SELECT Reputation FROM Teams WHERE Name=?",(team,)).fetchall()[0]))
                                reputation+=15
                                if reputation>100:
                                    reputation=100
                                c.execute("UPDATE Teams SET Reputation=? WHERE Name=?",(reputation,team,))
                                path = os.path.join(os.path.dirname(__file__), "Music", f"{GAME.raceCountry} National Anthem.wav")
                                if not os.path.isfile(path):
                                    path = os.path.join(os.path.dirname(__file__), "Music", "Podium Theme.wav")
                                GAME.ChangeScreen(f"{GAME.raceCountry} Flag")
                                GAME.Button("Results",1230,5)
                                GAME.screen="Podium"
                            else:
                                path = os.path.join(os.path.dirname(__file__), "Music", "Podium Theme.wav")
                        if os.path.isfile(path):
                            winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)
                x=520
            elif i==1:
                x=120
            else:
                x=920
            GAME.DisplayDriver(driver,x,500)
    def RaceResults(self):
        GAME.ChangeScreen("Race Results")
        GAME.pointsScored=[]
        for x in range(len(GAME.drivers)):
            GAME.pointsScored.append(0)
        with sqlite3.connect(GAME.database) as conn:
            cursor = conn.cursor()
            pointsSystem=int(GAME.Sanitise(cursor.execute("SELECT True FROM Regulations WHERE Regulation='Old Points System'").fetchall()))
            fastestLapPoint=int(GAME.Sanitise(cursor.execute("SELECT  True FROM Regulations WHERE Regulation='Fastest Lap Point'").fetchall()))
            double=0
            if GAME.race==GAME.races:
                if len(cursor.execute("SELECT Regulation FROM Regulations WHERE Regulation='Double Points On Last Race' AND True=1").fetchall())>0:
                    double=1
            if pointsSystem==0:
                pointsAvailable=[25,18,15,12,10,8,6,4,2,1]
            else:
                pointsAvailable=[10,8,6,5,4,3,2,1]
            for x in range(len(GAME.positions)):
                index=GAME.positions[x]
                try:
                    points=pointsAvailable[x]
                except:
                    points=0
                if points>0:
                    if fastestLapPoint==1 and GAME.positions[x]==GAME.fastest[0]:
                        points+=1
                    if double==1:
                        points=points*2
                    GAME.pointsScored.pop(index)
                    GAME.pointsScored.insert(index,points)
                team=GAME.teams[index]
                if team=="McLaren":
                    colour="#FFA100"
                elif team=="Mercedes":
                    colour="#1AE2CE"
                elif team=="Red Bull":
                    colour="#2400B2"
                elif "Aston Martin" in team:
                    colour="#49C18D"
                elif "Alpine" in team:
                    colour="#FF58FF"
                elif "Williams" in team:
                    colour="#5196FF"
                elif "Ferrari" in team:
                    colour="#EE1818"
                elif "Renault" in team:
                    colour="yellow"
                elif "Audi" in team:
                    colour="#AFB8C1"
                elif "Haas" in team:
                    colour="#D70000"
                elif "Cadillac" in team:
                    colour="#E6E6E6"
                else:
                    colour="white"
                if x<9:
                    if x==0:
                        canvas.create_text(50, 5, text=GAME.track, fill=colour, font=("Arial", 50), anchor="nw")
                    canvas.create_text(50, 80+(x*28), text=f"{x+1}. {GAME.drivers[index]}", fill=colour, font=("Arial", 20), anchor="nw")
                else:
                    canvas.create_text(45, 80+(x*28), text=f"{x+1}. {GAME.drivers[index]}", fill=colour, font=("Arial", 20), anchor="nw")
                if fastestLapPoint==1 and GAME.positions[x]==GAME.fastest[0] and points>0:
                    colour="#B400FF"
                if points==1:
                    canvas.create_text(700, 80+(x*28), text="1 Point", fill=colour, font=("Arial", 20), anchor="nw")
                elif points>9:
                    canvas.create_text(690, 80+(x*28), text=f"{points} Points", fill=colour, font=("Arial", 20), anchor="nw")
                else:
                    canvas.create_text(700, 80+(x*28), text=f"{points} Points", fill=colour, font=("Arial", 20), anchor="nw")
        GAME.DisplayDriver(GAME.drivers[GAME.positions[0]],950,500)
        GAME.Button("Next",1230,5)
    def SaveRace(self):
        if os.path.isfile(GAME.database):
            GAME.actions=3
            if GAME.music==1:
                GAME.StopMusic()
            #Injuries
            if len(GAME.injured)>0:
                for x in range(len(GAME.injured)):
                    with sqlite3.connect(GAME.database) as conn:
                        cursor = conn.cursor()
                        cursor.execute('''UPDATE Drivers SET Condition="Injured" WHERE Name=?''',(GAME.injured[x],))
            teams=[]
            teamPoints=[]
            with sqlite3.connect(GAME.database) as conn:
                cursor = conn.cursor()
                f=cursor.execute('''SELECT Name FROM Teams''').fetchall()
                cursor.execute("UPDATE Player SET Actions=3")
                if len(cursor.execute("SELECT Name FROM Teams WHERE Name='Red Bull'").fetchall())==1:
                    cursor.execute("UPDATE Drivers SET Team='Red Bull' WHERE Team='Racing Bulls' AND Role='Reserve'")
            for x in range(len(f)):
                team=GAME.Sanitise(f[x])
                teams.append(team)
                with sqlite3.connect(GAME.database) as conn:
                    cursor = conn.cursor()
                    teamPoints.append(int(GAME.Sanitise(cursor.execute('''SELECT Points FROM Teams WHERE Name=?''',(team,)).fetchall()[0])))
            for x in range(len(GAME.drivers)):
                if x<len(GAME.positions):
                    index=GAME.positions[x]
                    with sqlite3.connect(GAME.database) as conn:
                        cursor = conn.cursor()
                        if GAME.pointsScored[index]!=0:
                            points=int(GAME.Sanitise(cursor.execute('''SELECT Points FROM Drivers WHERE Name=?''',(GAME.drivers[index],)).fetchall()[0]))
                            points+=GAME.pointsScored[index]
                            cursor.execute('''UPDATE Drivers SET Points=? WHERE Name=?''',(points, GAME.drivers[index],))
                            team=GAME.Sanitise(cursor.execute('''SELECT Team FROM Drivers WHERE Name=?''',(GAME.drivers[index],)).fetchall()[0])
                            if team==GAME.team:
                                P=int(GAME.Sanitise(cursor.execute('''SELECT Points FROM Player''').fetchall()[0]))+GAME.pointsScored[index]
                                cursor.execute('''UPDATE Player SET Points=?''',(P,))
                            teamIndex=teams.index(team)
                            points=teamPoints[teamIndex]+GAME.pointsScored[index]
                            teamPoints.pop(teamIndex)
                            teamPoints.insert(teamIndex,points)
                        position=int(GAME.Sanitise(cursor.execute('''SELECT Position FROM Drivers WHERE Name=?''',(GAME.drivers[index],)).fetchall()[0]))
                        if position==0:
                            position=len(cursor.execute('''SELECT Name FROM Drivers WHERE Position!=0''').fetchall())+1
                            cursor.execute('''UPDATE Drivers SET Position=? WHERE Name=?''',(position, GAME.drivers[index],))
                else:
                    d=[]
                    for y in range(len(GAME.drivers)):
                        if y not in GAME.positions and y not in d:
                            d.append(y)
                            with sqlite3.connect(GAME.database) as conn:
                                cursor = conn.cursor()
                                if int(GAME.Sanitise(cursor.execute('''SELECT Position FROM Drivers WHERE Name=?''',(GAME.drivers[index],)).fetchall()[0]))==0:
                                    position=len(cursor.execute('''SELECT Name FROM Drivers WHERE Position!=0''').fetchall())+1
                                    cursor.execute('''UPDATE Drivers SET Position=? WHERE Name=?''',(position, GAME.drivers[y],))
            #Deaths
            if len(GAME.dead)>0:
                for driver in GAME.dead:
                    with sqlite3.connect(GAME.database) as c:
                        team=GAME.Sanitise(c.execute("SELECT Team FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                    if team==GAME.team:
                        GAME.YourDriverDied(driver)
                    else:
                        GAME.Replace(driver)
                    with sqlite3.connect(GAME.database) as c:
                        c.execute("UPDATE Drivers SET Team='Dead', Role='Dead', Condition='Dead', NewTeam='Dead' WHERE Name=?",(driver,))
            with sqlite3.connect(GAME.database) as conn:
                cursor = conn.cursor()
                f=cursor.execute("SELECT Name FROM Drivers WHERE (Role='1' OR Role='2') AND Position=0").fetchall()
                for x in range(len(f)):
                    position=len(cursor.execute("SELECT Name FROM Drivers WHERE Position!=0").fetchall())+1
                    cursor.execute("UPDATE Drivers SET Position=? WHERE Name=?",(position,GAME.Sanitise(f[x]),))
            for x in range(len(teams)):
                with sqlite3.connect(GAME.database) as conn:
                    cursor = conn.cursor()
                    cursor.execute('''UPDATE Teams SET Points=? WHERE Name=?''',(teamPoints[x],teams[x]))
            for i in range(20):
                for x in range(10):
                    if len(GAME.positions)>x:
                        #Drivers Standings
                        with sqlite3.connect(GAME.database) as conn:
                            cursor = conn.cursor()
                            position=int(GAME.Sanitise(cursor.execute('''SELECT Position FROM Drivers WHERE Name=?''',(GAME.drivers[GAME.positions[x]],)).fetchall()[0]))
                            if position!=1:
                                points=int(GAME.Sanitise(cursor.execute('''SELECT Points FROM Drivers WHERE Name=?''',(GAME.drivers[GAME.positions[x]],)).fetchall()[0]))
                                aheadPoints=int(GAME.Sanitise(cursor.execute('''SELECT Points FROM Drivers WHERE Position=?''',(position-1,)).fetchall()[0]))
                                if points>aheadPoints:
                                    while points>aheadPoints and position!=1:
                                        position-=1
                                        ahead=GAME.Sanitise(cursor.execute('''SELECT Name FROM Drivers WHERE Position=?''',(position,)).fetchall()[0])
                                        cursor.execute('''UPDATE Drivers SET Position=? WHERE Name=?''',(position, GAME.drivers[GAME.positions[x]],))
                                        cursor.execute('''UPDATE Drivers SET Position=? WHERE Name=?''',(position+1, ahead,))
                                        if position!=1:
                                            aheadPoints=int(GAME.Sanitise(cursor.execute('''SELECT Points FROM Drivers WHERE Position=?''',(position-1,)).fetchall()[0]))
                        with sqlite3.connect(GAME.database) as conn:
                            cursor = conn.cursor()
                            #Constructors Standings
                            position=int(GAME.Sanitise(cursor.execute('''SELECT Position FROM Teams WHERE Name=?''',(GAME.teams[GAME.positions[x]],)).fetchall()[0]))
                            if position!=1:
                                points=int(GAME.Sanitise(cursor.execute('''SELECT Points FROM Teams WHERE Name=?''',(GAME.teams[GAME.positions[x]],)).fetchall()[0]))
                                aheadPoints=int(GAME.Sanitise(cursor.execute('''SELECT Points FROM Teams WHERE Position=?''',(position-1,)).fetchall()[0]))
                                if points>aheadPoints:
                                    while points>aheadPoints and position!=1:
                                        position-=1
                                        ahead=GAME.Sanitise(cursor.execute('''SELECT Name FROM Teams WHERE Position=?''',(position,)).fetchall()[0])
                                        cursor.execute('''UPDATE Teams SET Position=? WHERE Name=?''',(position, GAME.teams[GAME.positions[x]],))
                                        cursor.execute('''UPDATE Teams SET Position=? WHERE Name=?''',(position+1, ahead,))
                                        if position!=1:
                                            aheadPoints=int(GAME.Sanitise(cursor.execute('''SELECT Points FROM Teams WHERE Position=?''',(position-1,)).fetchall()[0]))
            if GAME.race==1:
                with sqlite3.connect(GAME.database) as c:
                    zeroPoints=[]
                    f=c.execute("SELECT Name FROM Teams").fetchall()
                    for team in f:
                        team=GAME.Sanitise(team)
                        if int(GAME.Sanitise(c.execute("SELECT Points FROM Teams WHERE Name=?",(team,)).fetchall()[0]))==0:
                            zeroPoints.append(team)
                    for x in range(len(zeroPoints)):
                        found=0
                        pos=0
                        for index in GAME.positions:
                            if found==0:
                                team=GAME.teams[index]
                                if team in zeroPoints:
                                    found=1
                                    position=len(f)-len(zeroPoints)+1
                                    c.execute("UPDATE Teams SET Position=? WHERE Name=?",(position,team,))
                                    zeroPoints.remove(team)
                            if found==0 and pos==0:
                                pos=len(f)-len(zeroPoints)+1
                    if found==0:
                        for x in range(len(f)):
                            team=GAME.Sanitise(c.execute("SELECT Name FROM Teams WHERE Position=?",(x+1,)).fetchall()[0])
                            if team in zeroPoints:
                                c.execute("UPDATE Teams SET Position=? WHERE Name=?",(pos,team,))
                                pos+=1
            #Development
            with sqlite3.connect(GAME.database) as conn:
                cursor = conn.cursor()
                f=cursor.execute('''SELECT Name FROM Drivers WHERE Condition!="Retired" AND Legend=0''').fetchall()
            for x in range(len(f)):
                name=GAME.Sanitise(f[x])
                with sqlite3.connect(GAME.database) as conn:
                    cursor = conn.cursor()
                    team=GAME.Sanitise(cursor.execute("SELECT Team FROM Drivers WHERE Name=?",(name,)))
                    rate=int(GAME.Sanitise(cursor.execute('''SELECT DevelopmentRate FROM Drivers WHERE Name=?''',(name,)).fetchall()[0]))
                    developed=0
                    overtaking=int(GAME.Sanitise(cursor.execute('''SELECT Overtaking FROM Drivers WHERE Name=?''',(name,)).fetchall()[0]))
                    defending=int(GAME.Sanitise(cursor.execute('''SELECT Defending FROM Drivers WHERE Name=?''',(name,)).fetchall()[0]))
                    pace=int(GAME.Sanitise(cursor.execute('''SELECT Pace FROM Drivers WHERE Name=?''',(name,)).fetchall()[0]))
                    experience=int(GAME.Sanitise(cursor.execute('''SELECT Experience FROM Drivers WHERE Name=?''',(name,)).fetchall()[0]))
                    control=int(GAME.Sanitise(cursor.execute('''SELECT Control FROM Drivers WHERE Name=?''',(name,)).fetchall()[0]))
                    reaction=int(GAME.Sanitise(cursor.execute('''SELECT Reaction FROM Drivers WHERE Name=?''',(name,)).fetchall()[0]))
                    rating=int(GAME.Sanitise(cursor.execute('''SELECT Rating FROM Drivers WHERE Name=?''',(name,)).fetchall()[0]))
                    role=GAME.Sanitise(cursor.execute("SELECT Role FROM Drivers WHERE Name=?",(name,)))
                    if rate>0:
                        if team!="Free Agent":
                            if role=="Junior":
                                rate=rate*2
                            elif role=="Reserve":
                                rate=round(rate*1.5)
                            #Overtaking
                            if random.randint(1,450)<=rate:
                                overtaking+=1
                                if random.randint(1,5)==5:
                                    experience+=1
                            #Defending
                            if random.randint(1,450)<=rate:
                                defending+=1
                                if random.randint(1,5)==5:
                                    experience+=1
                            #Pace
                            if random.randint(1,450)<=rate:
                                pace+=1
                                if random.randint(1,5)==5:
                                    experience+=1
                            #Control
                            if random.randint(1,450)<=rate:
                                control+=1
                                if random.randint(1,5)==5:
                                    experience+=1
                            rating=round((overtaking+defending+pace+control+experience+reaction)/6)
                    elif rate<0:
                        if random.randint(-50,-1)>rate:
                            pace-=2
                            if random.randint(1,5)<=2:
                                rating-=1
                        if random.randint(1,2)==2:
                            experience+=1
                            if experience>110:
                                experience=110
                                if random.randint(1,2)==2:
                                    pace+=1
                                    if random.randint(1,3)==3:
                                        rating+=1
                    if random.randint(1,5)==5:
                        experience+=1
                    if experience>110:
                        experience=110
                    if control>99:
                        control=99
                    cursor.execute('''UPDATE Drivers SET Rating=?, Overtaking=?, Defending=?, Pace=?, Experience=?, Control=?, DevelopmentRate=? WHERE Name=?''',(rating, overtaking, defending, pace, experience, control, rate, name,))
            #Engines
            if GAME.race<GAME.races:
                for x in range(len(GAME.engineDurability)):
                    team=GAME.teams[x]
                    car=GAME.cars[x]
                    if GAME.faults[x]==0:
                        durability=GAME.engineDurability[x]-random.randint(round(270/GAME.races)-2,round(270/GAME.races)+2)
                    elif GAME.faults[x]=="Minor":
                        durability=GAME.engineDurability[x]-random.randint(round(320/GAME.races)-2,round(320/GAME.races)+2)
                    elif GAME.faults[x]=="Major":
                        durability=GAME.engineDurability[x]-random.randint(round(380/GAME.races)-10,round(380/GAME.races)+10)
                    else:
                        durability=0
                    if durability<0:
                        durability=0
                    with sqlite3.connect(GAME.database) as conn:
                        cursor = conn.cursor()
                        if (team!=GAME.team and durability<35) or durability==0:
                            #Swap engine
                            if car==1:
                                engine=int(GAME.Sanitise(cursor.execute('''SELECT car1Engine FROM Cars WHERE Team=?''',(team,)).fetchall()[0]))+1
                                cursor.execute('''UPDATE Cars SET car1Engine=?, car1EngineDurability=100 WHERE Team=?''',(engine,team,))
                            else:
                                engine=int(GAME.Sanitise(cursor.execute('''SELECT car2Engine FROM Cars WHERE Team=?''',(team,)).fetchall()[0]))+1
                                cursor.execute('''UPDATE Cars SET car2Engine=?, car2EngineDurability=100 WHERE Team=?''',(engine,team,))
                            if engine>4:
                                money=int(GAME.Sanitise(cursor.execute('''SELECT Money FROM Teams WHERE Name=?''',(team,)).fetchall()[0]))-10000000
                                cursor.execute('''UPDATE Teams SET Money=? WHERE Name=?''',(money,team,))
                                if team==GAME.team:
                                    GAME.money-=10000000
                        elif car==1:
                            cursor.execute('''UPDATE Cars SET car1EngineDurability=? WHERE Team=?''',(durability,team,))
                        else:
                            cursor.execute('''UPDATE Cars SET car2EngineDurability=? WHERE Team=?''',(durability,team,))
                            
            #Repairs
            for x in range(len(GAME.repairBill)):
                if GAME.repairBill[x]>0:
                    team=GAME.teams[x]
                    with sqlite3.connect(GAME.database) as c:
                        money=int(GAME.Sanitise(c.execute("SELECT Money FROM Teams WHERE Name=?",(team,)).fetchall()[0]))-GAME.repairBill[x]
                        c.execute("UPDATE Teams SET Money=? WHERE Name=?",(money,team,))
                    if team==GAME.team:
                        GAME.money=money
                        
            GAME.race+=1
            with sqlite3.connect(GAME.database) as conn:
                cursor = conn.cursor()
                cursor.execute('''UPDATE Player SET Race=?''',(GAME.race,))
                wins=int(GAME.Sanitise(cursor.execute("SELECT Wins FROM Drivers WHERE Name=?",(GAME.drivers[GAME.positions[0]],)).fetchall()))+1
                cursor.execute('''UPDATE Drivers SET Wins=? WHERE Name=?''',(wins,GAME.drivers[GAME.positions[0]],))
                if GAME.teams[GAME.positions[0]]==GAME.team:
                    wins=int(GAME.Sanitise(cursor.execute("SELECT Wins FROM Player").fetchall()))+1
                    cursor.execute('''UPDATE Player SET Wins=?''',(wins,))
                #Expectations
                if len(GAME.expected)==2:
                    positions=[]
                    for x in range(len(GAME.positions)):
                        if GAME.teams[x]==GAME.expected[0]:
                            positions.append(x+1)
                    success=0
                    reputation=int(GAME.Sanitise(cursor.execute('''SELECT Reputation FROM Teams WHERE Name=?''',(GAME.expected[0],)).fetchall()[0]))
                    if GAME.expected[1]=="Double Podium":
                        if len(positions)==2:
                            if positions[0]<=3 and positions[1]<=3:
                                success=1
                                reputation+=random.randint(35,50)
                    elif GAME.expected[1]=="Podium":
                        if len(positions)==2:
                            if positions[0]<=3 or positions[1]<=3:
                                success=1
                                reputation+=random.randint(20,30)
                        elif len(positions)==1:
                            if positions[0]<=3:
                                success=1
                                reputation+=random.randint(20,30)
                    elif GAME.expected[1]=="Top 5":
                        if len(positions)==2:
                            if positions[0]<=5 or positions[1]<=5:
                                success=1
                                reputation+=random.randint(15,20)
                        elif len(positions)==1:
                            if positions[0]<=5:
                                success=1
                                reputation+=random.randint(15,20)
                    elif GAME.expected[1]=="Double Points":
                        if len(positions)==2:
                            if int(GAME.Sanitise(cursor.execute('''SELECT True FROM Regulations WHERE Regulation="Old Points System"''').fetchall()[0]))==0:
                                if positions[0]<=10 and positions[1]<=10:
                                    success=1
                                    reputation+=random.randint(10,20)
                            elif positions[0]<=8 and positions[1]<=8:
                                success=1
                                reputation+=random.randint(10,20)
                    elif GAME.expected[1]=="Points":
                        if int(GAME.Sanitise(cursor.execute('''SELECT True FROM Regulations WHERE Regulation="Old Points System"''').fetchall()[0]))==0:
                            if len(positions)==2:
                                if positions[0]<=10 or positions[1]<=10:
                                    success=1
                                    reputation+=random.randint(5,10)
                            elif len(positions)==1:
                                if positions[0]<=10:
                                    success=1
                                    reputation+=random.randint(5,10)
                        else:
                            if len(positions)==2:
                                if positions[0]<=8 or positions[1]<=8:
                                    success=1
                                    reputation+=random.randint(5,10)
                            elif len(positions)==1:
                                if positions[0]<=8:
                                    success=1
                                    reputation+=random.randint(5,10)
                    else:
                        if len(positions)==2:
                            if positions[0]<=15 or positions[1]<=15:
                                success=1
                                reputation+=random.randint(1,5)
                        elif len(positions)==1:
                            if positions[0]<=15:
                                success=1
                                reputation+=random.randint(1,5)
                    if success==0:
                        reputation-=random.randint(1,40)
                        if reputation<1:
                            reputation=1
                    if reputation>100:
                        reputation=100
                    elif reputation<1:
                        reputation=1
                    cursor.execute('''UPDATE Teams SET Reputation=? WHERE Name=?''',(reputation,GAME.expected[0],))
                    GAME.expectations=[]
                    GAME.expected=[]
            with sqlite3.connect(GAME.database) as c:
                position=int(GAME.Sanitise(c.execute("SELECT Position FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0]))
                if position==1:
                    f=c.execute("SELECT Name FROM Teams WHERE Name!=?",(GAME.team,)).fetchall()
                    for x in range(len(f)):
                        team=GAME.Sanitise(f[x])
                        dragReduction=int(GAME.Sanitise(c.execute("SELECT DragReduction FROM Cars WHERE Team=?",(team,)).fetchall()[0]))
                        if dragReduction<70:
                            dragReduction+=1
                            c.execute("UPDATE Cars SET DragReduction=? WHERE Team=?",(dragReduction,team,))
            GAME.drivers.clear()
            GAME.SaveScreen()
        else:
            GAME.ChangeScreen("Missing Required Files")
    def DisplayLayout(self,track):
        if track!="Imola" and track!="Miami" and track!="Las Vegas" and track!="Madrid":
            with sqlite3.connect(GAME.database) as c:
                track=GAME.Sanitise(c.execute("SELECT Country FROM Tracks WHERE Name=?",(track,)).fetchall())
        try:
            layout=layouts[tracks.index(track)]
            canvas.image=layout
            canvas.create_image(1200,130, anchor=tk.NW, image=layout)
        except:
            pass
    def ReplayObjective(self):
        if GAME.music==1:
            if GAME.replay==2:
                sound_path = os.path.join(os.path.dirname(__file__), "Music", "Lose my mind.wav")
                if os.path.isfile(sound_path):
                    winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
            else:
                GAME.StopMusic()
        GAME.ChangeScreen("Replay Objective")
        if GAME.replay==1 or GAME.replay==4:
            canvas.create_text(370, 350, text="Objective: Win the Championship", fill="white", font=("Arial", 40), anchor="nw")
        else:
            canvas.create_text(400, 350, text="Objective: Win the Race", fill="white", font=("Arial", 40), anchor="nw")
        root.after(3000, lambda: GAME.StartReplay())
    def StartReplay(self):
        self.confidence=[]
        self.positions=[]
        self.tyrePace=[]
        self.tyre=[]
        self.tyreRemaining=[]
        self.engineReliability=[]
        self.lap=[]
        self.lap_=[]
        self.time=[]
        self.distance=[]
        self.currentLapTime=[]
        self.tyreCompoundsUsed=[]
        self.damage=[]
        self.overtaking=[]
        self.defending=[]
        self.control=[]
        self.experience=[]
        self.reaction=[]
        self.DRS=[]
        self.tyreAggression=[]
        self.fuelAggression=[]
        self.car1Instructions=[]
        self.car2Instructions=[]
        self.engineTemperature=[]
        self.ERSdeployment=[]
        self.ERS=[]
        self.tyreWear=[]
        self.grip=[]
        self.frontWings=[]
        self.repairBill=[]
        self.penalties=[]
        self.safety=0
        self.raceFinished=0
        self.pitLap=[]
        self.pitTyre=[]
        self.lapPittedTo=[]
        self.bestPitStop=[-1,100]
        self.skippingLaps=0
        self.thingHappened=0
        self.tyrePreservation=[]
        self.startLap=1
        self.cycles=0
        self.faults=[]
        self.stops=[]
        self.qualifying=0
        self.cooling=[]
        self.strategy=[]
        self.racePace=[]
        self.teamOrders=1
        self.pit=0
        self.fuel=[]
        self.battery=[]
        self.fastest=[-1,0,10]
        if GAME.replay==2:
            GAME.team="APX GP"
            GAME.car1="Sonny Hayes"
            GAME.driver1="Sonny Hayes"
            GAME.car1ID=21
            GAME.car2="Joshua Pearce"
            GAME.driver2="Joshua Pearce"
            GAME.car2ID=20
            GAME.track="The Abu Dhabi Grand Prix"
            GAME.raceCountry="Abu Dhabi"
            GAME.positions=[]
            GAME.drivers=["Max Verstappen","Charles Leclerc","Lando Norris","Lewis Hamilton","George Russell","Oscar Piastri","Fernando Alonso","Carlos Sainz","Sergio Perez",
                          "Daniel Ricciardo","Lance Stroll","Alexander Albon","Yuki Tsunoda","Valtteri Bottas","Nico Hulkenberg","Zhou Guanyu","Kevin Magnussen","Esteban Ocon",
                          "Pierre Gasly","Logan Sargeant","Joshua Pearce","Sonny Hayes"]
            GAME.teams=["Red Bull","Ferrari","McLaren","Mercedes","Mercedes","McLaren","Aston Martin","Ferrari","Red Bull","AlphaTauri","Aston Martin","Williams","AlphaTauri",
                        "Alfa Romeo","Haas","Alfa Romeo","Haas","Alpine","Alpine","Williams","APX GP","APX GP"]
            GAME.cars=[1,1,2,1,2,1,2,2,2,1,1,1,2,1,1,2,2,1,2,2,2,1]
            for x in range(22):
                GAME.positions.append(x)
                GAME.engineDurability.append(100)
                GAME.engineReliability.append(15)
                if x>19:
                    pace=1000
                    GAME.overtaking.append(20)
                else:
                    if x==3:
                        pace=230
                    elif x==4:
                        pace=215
                    else:
                        pace=200-(x*5)
                    GAME.overtaking.append(5)
                GAME.racePace.append(pace)
                GAME.defending.append(0)
                
            GAME.tyrePace=[]
            #Soft
            GAME.tyrePace.append(random.randint(17,20))
            #Medium
            GAME.tyrePace.append(random.randint(10,GAME.tyrePace[0]-4))
            #Hard
            GAME.tyrePace.append(random.randint(2,GAME.tyrePace[1]-4))
            GAME.drs=1
            GAME.ers=2
            GAME.temperature=18
            GAME.length=5.281
            GAME.laps=58
            GAME.overtakeability=5
            GAME.risk=0
            GAME.maxRain=0
            GAME.maxWater=0
            GAME.rain=0
            GAME.water=0
            GAME.wet=0
            GAME.rainStarts=0
            GAME.rainStops=0
            GAME.weatherMessage=[]
            GAME.tyreWear=[6,3,2,20]
            GAME.expectedTyreLife=[12,23,35,5]

            for x in range(len(GAME.drivers)):
                driver=GAME.drivers[x]
                team=GAME.teams[x]
                GAME.tyreRemaining.append(100)
                GAME.faults.append(0)
                GAME.stops.append(0)
                GAME.lap.append(1)
                GAME.lap_.append(1)
                position=int(GAME.positions.index(x))
                GAME.time.append((position-1)*0.5)
                GAME.distance.append((position-1)*-0.8)
                GAME.currentLapTime.append(1.5)
                GAME.tyreCompoundsUsed.append(1)
                GAME.damage.append(0)
                GAME.ERS.append(100)
                GAME.control.append(100)
                GAME.experience.append(80)
                GAME.reaction.append(100)
                GAME.cooling.append(60)
                GAME.tyrePreservation.append(5)
                GAME.engineTemperature.append(85+random.randint(0,15))
                GAME.fuel.append(100)
                GAME.frontWings.append(1)
                GAME.repairBill.append(0)
                GAME.penalties.append(0)
                GAME.lapPittedTo.append(1)
                GAME.DRS.append(35)
                #Strategy
                length=GAME.expectedTyreLife[1]+GAME.expectedTyreLife[2]
                if team==GAME.team:
                    GAME.tyre.append("Placeholder")
                    GAME.tyreAggression.append("Placeholder")
                    GAME.fuelAggression.append("Placeholder")
                    GAME.ERSdeployment.append("Placeholder")
                    GAME.pitLap.append(0)
                    GAME.pitTyre.append(0)
                    GAME.strategy.append(0)
                else:
                    GAME.tyreAggression.append(random.randint(3,5))
                    GAME.fuelAggression.append(3)
                    GAME.ERSdeployment.append(3)
                    GAME.strategy.append(1)
                    if GAME.expectedTyreLife[0]+GAME.expectedTyreLife[1]>=GAME.laps-3:
                        tyreOptions=["Soft","Medium"]
                    elif GAME.expectedTyreLife[0]+GAME.expectedTyreLife[2]>=GAME.laps-3:
                        tyreOptions=["Soft","Hard"]
                    else:
                        tyreOptions=["Medium","Hard"]
                    if position<=5:
                        if random.randint(1,5)==5:
                            tyre=tyreOptions[1]
                        else:
                            tyre=tyreOptions[0]
                    elif position<=10:
                        if random.randint(1,5)>=4:
                            tyre=tyreOptions[1]
                        else:
                            tyre=tyreOptions[0]
                    else:
                        if random.randint(1,2)==2:
                            tyre=tyreOptions[1]
                        else:
                            tyre=tyreOptions[0]
                    if tyre=="Soft":
                        tyreLife=GAME.expectedTyreLife[0]
                    elif tyre=="Medium":
                        tyreLife=GAME.expectedTyreLife[1]
                    else:
                        tyreLife=GAME.expectedTyreLife[2]
                    if length>=GAME.laps-3:
                        pitLap=round(tyreLife)+random.randint(-2,2)
                    else:
                        pitLap=round(tyreLife*1.5)+random.randint(-2,1)
                    if pitLap>GAME.laps/2 and tyre==tyreOptions[0]:
                        pitLap=round(GAME.laps/2)+random.randint(-3,1)
                    if tyre==tyreOptions[0]:
                        pitTyre=tyreOptions[1]
                    else:
                        pitTyre=tyreOptions[0]
                    GAME.tyre.append(tyre)
                    GAME.pitLap.append(pitLap)
                    GAME.pitTyre.append(pitTyre)

            GAME.DisplayReplayGrid()
        elif GAME.replay==1:
            GAME.track="Abu Dhabi"
            GAME.raceCountry="Abu Dhabi"
            GAME.drivers=["Max Verstappen","Lewis Hamilton","Lando Norris","Sergio Perez","Carlos Sainz","Valtteri Bottas","Charles Leclerc","Yuki Tsunoda","Esteban Ocon",
                         "Daniel Ricciardo","Fernando Alonso","Pierre Gasly","Lance Stroll","Antonio Giovinazzi","Sebastian Vettel","Nicholas Latifi","George Russell",
                         "Kimi Raikkonen","Mick Schumacher"]
            GAME.teams=["Red Bull","Mercedes","McLaren","Red Bull","Ferrari","Mercedes","Ferrari","AlphaTauri","Alpine","McLaren","Alpine","AlphaTauri","Aston Martin","Alfa Romeo",
                        "Aston Martin","Williams","Williams","Alfa Romeo","Haas"]
            GAME.cars=[1,1,2,2,2,2,1,2,2,1,1,1,1,2,2,2,1,1,1]
            GAME.racePace=[]
            for driver in GAME.drivers:
                if driver=="Max Verstappen" or driver=="Lewis Hamilton":
                    pace=250
                elif driver=="Sergio Perez" or driver=="Valtteri Bottas":
                    pace=210
                else:
                    pace=200-(GAME.drivers.index(driver)*5)
                GAME.racePace.append(pace)
            GAME.tyreRemaining=[]
            GAME.tyrePreservation=[]
            GAME.overtaking=[]
            GAME.defending=[]
            for x in range(19):
                GAME.positions.append(x)
                GAME.tyrePreservation.append(0)
                GAME.overtaking.append(5)
                GAME.defending.append(5)
            GAME.tyrePace=[]
            #Soft
            GAME.tyrePace.append(random.randint(17,20))
            #Medium
            GAME.tyrePace.append(random.randint(10,GAME.tyrePace[0]-4))
            #Hard
            GAME.tyrePace.append(random.randint(2,GAME.tyrePace[1]-4))
            GAME.drs=1
            GAME.ers=2
            GAME.temperature=18
            GAME.length=5.281
            GAME.laps=58
            GAME.overtakeability=5
            GAME.risk=0
            GAME.maxRain=0
            GAME.maxWater=0
            GAME.rain=0
            GAME.water=0
            GAME.wet=0
            GAME.rainStarts=0
            GAME.rainStops=0
            GAME.weatherMessage=[]
            GAME.tyreWear=[6,3,2,20]
            GAME.expectedTyreLife=[12,23,35,5]
            GAME.rainChance=0
                
            GAME.ChangeScreen("Choose a Team 2021")
        elif GAME.replay==3:
            GAME.track="Montreal"
            GAME.raceCountry="Canada"
            GAME.drivers=["Sebastian Vettel","Fernando Alonso","Felipe Massa","Mark Webber","Lewis Hamilton","Nico Rosberg","Jenson Button","Michael Schumacher","Nick Heidfeld",
                          "Vitaly Petrov","Paul di Resta","Pastor Maldonado","Kamui Kobayashi","Adrian Sutil","Sébastien Buemi","Rubens Barrichello","Pedro de la Rosa",
                          "Jarno Trulli","Heikki Kovalainen","Vitantonio Liuzzi","Timo Glock","Narain Karthikeyan","Jérôme d’Ambrosio"]
            GAME.teams=["Red Bull","Ferrari","Ferrari","Red Bull","McLaren","Mercedes","McLaren","Mercedes","Renault","Renault","Force India","Williams","Sauber","Force India",
                        "Toro Rosso","Williams","Sauber","Lotus","Lotus","HRT","Virgin","HRT","Virgin"]
            GAME.cars=[1,1,2,2,2,2,1,1,1,2,1,1,1,2,1,2,2,1,2,1,1,2,2]
            GAME.racePace=[]
            for driver in GAME.drivers:
                if driver=="Sebastian Vettel":
                    pace=240
                    GAME.overtaking.append(10)
                elif driver=="Jenson Button":
                    pace=200
                    GAME.overtaking.append(5)
                elif driver=="Michael Schumacher" or driver=="Mark Webber":
                    pace=195
                    GAME.overtaking.append(5)
                else:
                    pace=200-(GAME.drivers.index(driver)*5)
                    GAME.overtaking.append(5)
                GAME.racePace.append(pace)
            GAME.tyreRemaining=[]
            GAME.tyrePreservation=[]
            GAME.defending=[]
            GAME.tyrePace=[]
            #Soft
            GAME.tyrePace.append(random.randint(17,20))
            #Medium
            GAME.tyrePace.append(random.randint(10,GAME.tyrePace[0]-4))
            #Hard
            GAME.tyrePace.append(random.randint(2,GAME.tyrePace[1]-4))
            GAME.drs=1
            GAME.ers=2
            GAME.temperature=0
            GAME.length=4.361
            GAME.laps=70
            GAME.overtakeability=3
            GAME.risk=40
            GAME.maxRain=0
            GAME.maxWater=4.5
            GAME.rain=0
            GAME.water=4.5
            GAME.wet=1
            GAME.rainStarts=0
            GAME.rainStops=0
            GAME.weatherMessage=[]
            GAME.tyreWear=[6,3,2,2]
            GAME.expectedTyreLife=[12,23,35,35]
            GAME.rainChance=0
            for x in range(23):
                GAME.positions.append(x)
                GAME.tyrePreservation.append(0)
                GAME.defending.append(5)
                GAME.tyreRemaining.append(100)
                GAME.fuel.append(100)
                GAME.ERS.append(100)
                GAME.strategy.append(0)
                GAME.faults.append(0)
                GAME.stops.append(0)
                GAME.lap.append(5)
                GAME.lap_.append(1)
                GAME.time.append(x*0.5)
                GAME.distance.append(x*-0.8)
                GAME.currentLapTime.append(1.5)
                GAME.tyreCompoundsUsed.append(1)
                GAME.damage.append(0)
                GAME.control.append(100)
                GAME.experience.append(80)
                GAME.reaction.append(100)
                GAME.cooling.append(60)
                GAME.engineTemperature.append(85+random.randint(0,15))
                GAME.frontWings.append(1)
                GAME.repairBill.append(0)
                GAME.penalties.append(0)
                GAME.lapPittedTo.append(1)
                GAME.DRS.append(35)
                GAME.tyre.append("Wet")
                GAME.pitLap.append(0)
                GAME.pitTyre.append(0)
                GAME.engineDurability.append(100)
                GAME.engineReliability.append(15)
                if GAME.teams[x]=="McLaren":
                    GAME.tyreAggression.append("Placeholder")
                    GAME.fuelAggression.append("Placeholder")
                    GAME.ERSdeployment.append("Placeholder")
                else:
                    GAME.tyreAggression.append(random.randint(3,5))
                    GAME.fuelAggression.append(3)
                    GAME.ERSdeployment.append(3)
            GAME.team="McLaren"
            GAME.driver1="Jenson Button"
            GAME.driver2="Lewis Hamilton"
            GAME.car1ID=6
            GAME.car2ID=4
            GAME.events=0
            GAME.BackgroundColour()

            GAME.DisplayReplayGrid()
        elif GAME.replay==4:
            GAME.ChangeScreen("Choose a Team 2008")
        elif GAME.replay==5:
            GAME.ChangeScreen("Choose a Team 2000")
        elif GAME.replay==6:
            GAME.track="Monte Carlo"
            GAME.raceCountry="Monaco"
            GAME.drivers=["Alain Prost","Nigel Mansell","René Arnoux","Nelson Piquet","Patrick Tambay","Derek Warwick","Elio de Angelis","Teo Fabi","Andrea de Cesaris","Jacques Laffite",
                          "Keke Rosberg","Ayrton Senna","Michele Alboreto","Martin Brundle","Eddie Cheever","Riccardo Patrese","Niki Lauda","François Hesnault","Stefan Bellof",
                          "Stefan Bellof","Johnny Cecotto","Jo Gartner","Piercarlo Ghinzani","Philippe Alliot"]
            GAME.teams=["McLaren","Lotus","Ferrari","Brabham","Ferrari","Renault","Lotus","Brabham","Ligier","Williams","Williams","Toleman","Ferrari","Tyrrell","Alfa Romeo",
                        "Alfa Romeo"," McLaren","Ligier","Tyrrell","Spirit","Toleman","Osella","Osella","RAM"]
            GAME.cars=[]
            for team in GAME.teams:
                if GAME.teams.index(team)<len(GAME.cars)-1:
                    GAME.cars.append(2)
                else:
                    GAME.cars.append(1)
            GAME.racePace=[]
            for driver in GAME.drivers:
                if driver=="Ayrton Senna":
                    pace=270
                    GAME.overtaking.append(15)
                    GAME.control.append(100)
                    GAME.confidence.append(40)
                elif driver=="Niki Lauda":
                    pace=190
                    GAME.overtaking.append(5)
                    GAME.control.append(80)
                    GAME.confidence.append(25)
                else:
                    pace=200-(GAME.drivers.index(driver)*5)
                    GAME.overtaking.append(5)
                    GAME.control.append(70)
                    GAME.confidence.append(20)
                GAME.racePace.append(pace)
            GAME.tyreRemaining=[]
            GAME.tyrePreservation=[]
            GAME.defending=[]
            GAME.tyrePace=[]
            #Soft
            GAME.tyrePace.append(random.randint(17,20))
            #Medium
            GAME.tyrePace.append(random.randint(10,GAME.tyrePace[0]-4))
            #Hard
            GAME.tyrePace.append(random.randint(2,GAME.tyrePace[1]-4))
            GAME.drs=0
            GAME.ers=0
            GAME.temperature=10
            GAME.length=3.337
            GAME.laps=78
            GAME.overtakeability=3
            GAME.risk=88
            GAME.maxRain=0
            GAME.maxWater=5.5
            GAME.rain=0
            GAME.water=5.5
            GAME.wet=1
            GAME.rainStarts=0
            GAME.rainStops=0
            GAME.weatherMessage=[]
            GAME.tyreWear=[6,3,2,2]
            GAME.expectedTyreLife=[12,23,35,35]
            GAME.rainChance=0
            GAME.team="Toleman"
            GAME.driver1="Ayrton Senna"
            GAME.driver2="Johnny Cecotto"
            GAME.car1ID=11
            GAME.car2ID=20
            root.configure(background='White')
            for x in range(24):
                    GAME.positions.append(x)
                    GAME.tyrePreservation.append(0)
                    GAME.defending.append(5)
                    GAME.tyreRemaining.append(100)
                    GAME.fuel.append(100)
                    GAME.ERS.append(100)
                    GAME.strategy.append(0)
                    GAME.faults.append(0)
                    GAME.stops.append(0)
                    GAME.lap.append(1)
                    GAME.lap_.append(1)
                    GAME.time.append(x*0.5)
                    GAME.distance.append(x*-0.8)
                    GAME.currentLapTime.append(1.5)
                    GAME.tyreCompoundsUsed.append(1)
                    GAME.damage.append(0)
                    GAME.experience.append(80)
                    GAME.reaction.append(100)
                    GAME.cooling.append(60)
                    GAME.engineTemperature.append(85+random.randint(0,15))
                    GAME.frontWings.append(1)
                    GAME.repairBill.append(0)
                    GAME.penalties.append(0)
                    GAME.lapPittedTo.append(1)
                    GAME.tyre.append("Wet")
                    GAME.pitLap.append(0)
                    GAME.pitTyre.append(0)
                    GAME.engineDurability.append(100)
                    GAME.engineReliability.append(15)
                    GAME.ERSdeployment.append(0)
                    if GAME.teams[x]==GAME.team:
                        GAME.tyreAggression.append("Placeholder")
                        GAME.fuelAggression.append("Placeholder")
                    else:
                        GAME.tyreAggression.append(random.randint(3,5))
                        GAME.fuelAggression.append(3)

            GAME.DisplayReplayGrid()
            

    def AbuDhabi2021(self):
        for x in range(19):
            GAME.tyreRemaining.append(100)
            GAME.fuel.append(100)
            GAME.ERS.append(100)
            GAME.strategy.append(1)
            GAME.faults.append(0)
            GAME.stops.append(0)
            GAME.lap.append(1)
            GAME.lap_.append(1)
            GAME.time.append(x*0.5)
            GAME.distance.append(x*-0.8)
            GAME.currentLapTime.append(1.5)
            GAME.tyreCompoundsUsed.append(1)
            GAME.damage.append(0)
            GAME.control.append(100)
            GAME.experience.append(80)
            GAME.reaction.append(100)
            GAME.cooling.append(60)
            GAME.engineTemperature.append(85+random.randint(0,15))
            GAME.frontWings.append(1)
            GAME.repairBill.append(0)
            GAME.penalties.append(0)
            GAME.lapPittedTo.append(1)
            GAME.DRS.append(35)
            if GAME.teams[x]==GAME.team:
                GAME.tyre.append("Placeholder")
                GAME.pitLap.append(0)
                GAME.pitTyre.append(0)
                GAME.tyreAggression.append("Placeholder")
                GAME.fuelAggression.append("Placeholder")
                GAME.ERSdeployment.append("Placeholder")
            else:
                if GAME.drivers[x]=="Max Verstappen":
                    GAME.tyre.append("Soft")
                    GAME.pitLap.append(13)
                    GAME.pitTyre.append("Hard")
                elif GAME.drivers[x]=="Lewis Hamilton":
                    GAME.tyre.append("Medium")
                    GAME.pitLap.append(15)
                    GAME.pitTyre.append("Hard")
                elif GAME.drivers[x]=="Sergio Perez":
                    GAME.tyre.append("Soft")
                    GAME.pitLap.append(21)
                    GAME.pitTyre.append("Hard")
                elif GAME.drivers[x]=="Valtteri Bottas":
                    GAME.tyre.append("Medium")
                    GAME.pitLap.append(30)
                    GAME.pitTyre.append("Soft")
                else:
                    tyre=Tyres[random.randint(0,2)]
                    GAME.tyre.append(tyre)
                    GAME.pitLap.append(GAME.expectedTyreLife[Tyres.index(tyre)]+random.randint(-3,3))
                    if tyre=="Hard":
                        GAME.pitTyre.append("Medium")
                    else:
                        GAME.pitTyre.append("Hard")
                GAME.tyreAggression.append(random.randint(3,5))
                GAME.fuelAggression.append(3)
                GAME.ERSdeployment.append(3)
                GAME.engineDurability.append(100)
                GAME.engineReliability.append(15)

        GAME.DisplayReplayGrid()
    def DisplayReplayGrid(self):
        GAME.ChangeScreen("Replay Grid")
        if GAME.replay==1:
            race="Abu Dhabi 2021"
        elif GAME.replay==2:
            race="F1: The Movie Replay"
        elif GAME.replay==3:
            race="Canada 2011"
        elif GAME.replay==4:
            race="Brazil 2008"
        elif GAME.replay==5:
            race="Spa 2000"
        else:
            race="Monaco 1984"
        canvas.create_text(100, 10, text=race, fill="black", font=("Arial", 50), anchor="nw")
        for x in range(round(len(GAME.drivers)/2)):
            for y in range(2):
                index=(x*2)+y
                if index<=len(GAME.drivers)-1:
                    canvas.create_text(100+(650*y), 150+(50*x)+(25*y), text=f"{index+1}. {GAME.drivers[index]} {GAME.teams[index]}", fill="black", font=("Arial", 30), anchor="nw")
        GAME.Button("Prepare for Race",1200,725)
    def Spa2000(self):
        GAME.track="Spa"
        GAME.raceCountry="Belgium"
        GAME.drivers=["Mika Hakkinen","Jarno Trulli","Jenson Button","Michael Schumacher","David Coulthard","Ralf Schumacher","Jacques Villeneuve","Heinz-Harald Frentzen",
                      "Johnny Herbert","Rubens Barrichello","Giancarlo Fisichella","Eddie Irvine","Ricardo Zonta","Nick Heidfeld","Pedro Diniz","Pedro de la Rosa","Jean Alesi",
                      "Jean Alesi","Alexander Wurz","Jos Verstappen","Marc Gené","Gastón Mazzacane"]
        GAME.teams=["McLaren","Jordan","Williams","Ferrari","McLaren","Williams","BAR","Jordan","Jaguar","Ferrari","Benneton","Jaguar","BAR","Prost","Sauber","Arrows","Prost",
                    "Sauber","Benneton","Arrows","Minardi","Minardi"]
        GAME.cars=[1,1,2,1,2,1,1,1,1,2,1,2,2,1,1,1,2,2,2,2,1,2]
        GAME.racePace=[]
        for driver in GAME.drivers:
            if driver=="Michael Schumacher":
                pace=240
                GAME.overtaking.append(15)
            elif driver=="Mika Hakkinen":
                pace=230
                GAME.overtaking.append(8)
            elif driver=="David Coulthard" or driver=="Rubens Barrichello":
                pace=210
                GAME.overtaking.append(5)
            else:
                pace=200-(GAME.drivers.index(driver)*5)
                GAME.overtaking.append(5)
            GAME.racePace.append(pace)
        GAME.tyreRemaining=[]
        GAME.tyrePreservation=[]
        GAME.defending=[]
        GAME.tyrePace=[]
        #Soft
        GAME.tyrePace.append(random.randint(17,20))
        #Medium
        GAME.tyrePace.append(random.randint(10,GAME.tyrePace[0]-4))
        #Hard
        GAME.tyrePace.append(random.randint(2,GAME.tyrePace[1]-4))
        GAME.drs=0
        GAME.ers=0
        GAME.temperature=10
        GAME.length=7.004
        GAME.laps=44
        GAME.overtakeability=3
        GAME.risk=0
        GAME.maxRain=0
        GAME.maxWater=4.5
        GAME.rain=0
        GAME.water=3
        GAME.wet=1
        GAME.rainStarts=0
        GAME.rainStops=0
        GAME.weatherMessage=[]
        GAME.tyreWear=[6,0,3,4]
        GAME.expectedTyreLife=[12,0,23,18]
        GAME.rainChance=0
        for x in range(22):
                GAME.positions.append(x)
                GAME.tyrePreservation.append(0)
                GAME.defending.append(5)
                GAME.tyreRemaining.append(100)
                GAME.fuel.append(100)
                GAME.ERS.append(100)
                GAME.strategy.append(0)
                GAME.faults.append(0)
                GAME.stops.append(0)
                GAME.lap.append(1)
                GAME.lap_.append(1)
                GAME.time.append(x*0.5)
                GAME.distance.append(x*-0.8)
                GAME.currentLapTime.append(1.5)
                GAME.tyreCompoundsUsed.append(1)
                GAME.damage.append(0)
                GAME.control.append(100)
                GAME.experience.append(80)
                GAME.reaction.append(100)
                GAME.cooling.append(60)
                GAME.engineTemperature.append(85+random.randint(0,15))
                GAME.frontWings.append(1)
                GAME.repairBill.append(0)
                GAME.penalties.append(0)
                GAME.lapPittedTo.append(1)
                GAME.tyre.append("Wet")
                GAME.pitLap.append(0)
                GAME.pitTyre.append(0)
                GAME.engineDurability.append(100)
                GAME.engineReliability.append(15)
                GAME.ERSdeployment.append(0)
                if GAME.teams[x]==GAME.team:
                    GAME.tyreAggression.append("Placeholder")
                    GAME.fuelAggression.append("Placeholder")
                else:
                    GAME.tyreAggression.append(random.randint(3,5))
                    GAME.fuelAggression.append(3)

        GAME.DisplayReplayGrid()
    def Brazil2008(self):
        GAME.track="Interlagos"
        GAME.raceCountry="Brazil"
        GAME.drivers=["Felipe Massa","Jarno Trulli","Kimi Raikkonen","Lewis Hamilton","Heikki Kovalainen","Fernando Alonso","Sebastian Vettel","Nick Heidfeld","Mark Webber","Timo Glock",
                      "Nico Rosberg","Kazuki Nakajima","Rubens Barrichello","Jenson Button","David Coulthard","Sébastien Bourdais","Nelson Piquet Jr.","Giancarlo Fisichella",
                      "Adrian Sutil","Robert Kubica"]
        GAME.teams=["Ferrari","Toyota","Ferrari","McLaren","McLaren","Renault","Toro Rosso","BMW Sauber","Red Bull","Toyota","Williams","Williams","Honda","Honda","Red Bull","Toro Rosso",
                    "Renault","Force India","Force India","BMW Sauber"]
        GAME.cars=[1,1,2,1,2,1,1,1,1,2,1,2,2,1,2,2,2,1,2,2]
        GAME.racePace=[]
        for driver in GAME.drivers:
            if driver=="Felipe Massa":
                pace=220
                GAME.overtaking.append(30)
            elif driver=="Lewis Hamilton":
                if GAME.team=="McLaren":
                    pace=140
                else:
                    pace=180
                GAME.overtaking.append(5)
            elif driver=="Heikki Kovalainen":
                pace=GAME.racePace[3]-10
                GAME.overtaking.append(5)
            elif driver=="Timo Glock":
                pace=170
                GAME.overtaking.append(5)
            elif driver=="Sebastian Vettel":
                pace=165
                GAME.overtaking.append(5)
            else:
                pace=200-(GAME.drivers.index(driver)*5)
                GAME.overtaking.append(5)
            GAME.racePace.append(pace)
        GAME.tyreRemaining=[]
        GAME.tyrePreservation=[]
        GAME.defending=[]
        GAME.tyrePace=[]
        #Soft
        GAME.tyrePace.append(random.randint(17,20))
        #Medium
        GAME.tyrePace.append(random.randint(10,GAME.tyrePace[0]-4))
        #Hard
        GAME.tyrePace.append(random.randint(2,GAME.tyrePace[1]-4))
        GAME.drs=0
        GAME.ers=0
        GAME.temperature=25
        GAME.length=4.309
        GAME.laps=71
        GAME.overtakeability=4
        GAME.risk=0
        GAME.maxRain=0
        GAME.maxWater=3
        GAME.rain=0
        GAME.water=3
        GAME.wet=1
        GAME.rainStarts=0
        GAME.rainStops=0
        GAME.weatherMessage=[]
        GAME.tyreWear=[6,3,2,2]
        GAME.expectedTyreLife=[12,23,35,35]
        GAME.rainChance=0
        for x in range(20):
                GAME.positions.append(x)
                GAME.tyrePreservation.append(0)
                GAME.defending.append(5)
                GAME.tyreRemaining.append(100)
                GAME.fuel.append(100)
                GAME.ERS.append(100)
                GAME.strategy.append(0)
                GAME.faults.append(0)
                GAME.stops.append(0)
                GAME.lap.append(1)
                GAME.lap_.append(1)
                GAME.time.append(x*0.5)
                GAME.distance.append(x*-0.8)
                GAME.currentLapTime.append(1.5)
                GAME.tyreCompoundsUsed.append(1)
                GAME.damage.append(0)
                GAME.control.append(100)
                GAME.experience.append(80)
                GAME.reaction.append(100)
                GAME.cooling.append(60)
                GAME.engineTemperature.append(85+random.randint(0,15))
                GAME.frontWings.append(1)
                GAME.repairBill.append(0)
                GAME.penalties.append(0)
                GAME.lapPittedTo.append(1)
                GAME.tyre.append("Intermediate")
                GAME.engineDurability.append(100)
                GAME.engineReliability.append(15)
                GAME.ERSdeployment.append(0)
                if GAME.teams[x]==GAME.team:
                    GAME.tyreAggression.append("Placeholder")
                    GAME.fuelAggression.append("Placeholder")
                    GAME.pitLap.append(0)
                    GAME.pitTyre.append(0)
                else:
                    GAME.tyreAggression.append(random.randint(3,5))
                    GAME.fuelAggression.append(3)
                    GAME.pitLap.append(random.randint(11,14))
                    if random.randint(1,3)==3:
                        GAME.pitTyre.append("Medium")
                    else:
                        GAME.pitTyre.append("Hard")

        GAME.DisplayReplayGrid()
    def Reserves(self):
        with sqlite3.connect(GAME.database) as c:
            #Board Finances
            if GAME.money<2000000:
                financial=int(GAME.Sanitise(c.execute("SELECT Financial FROM Player").fetchall()[0]))
                if GAME.money<=0:
                    financial=1
                else:
                    if financial>2:
                        financial=3
                c.execute("UPDATE Player SET Financial=?",(financial,))
            f=c.execute('''SELECT Name FROM Drivers WHERE Role="1" or Role="2"''').fetchall()
            GAME.drivers=[]
            GAME.teams=[]
            GAME.cars=[]
            GAME.engineDurability=[]
            replacements=[]
            unableToRace=[]
            for x in range(len(f)):
                name=GAME.Sanitise(f[x])
                if name==GAME.car1:
                    GAME.car1ID=len(GAME.drivers)
                elif name==GAME.car2:
                    GAME.car2ID=len(GAME.drivers)
                condition=GAME.Sanitise(c.execute('''SELECT Condition FROM Drivers WHERE Name=?''',(name,)).fetchall()[0])
                team=GAME.Sanitise(c.execute('''SELECT Team FROM Drivers WHERE Name=?''',(name,)).fetchall()[0])
                car=int(GAME.Sanitise(c.execute('''SELECT Role FROM Drivers WHERE Name=?''',(name,)).fetchall()[0]))
                if condition=="Well":
                    GAME.drivers.append(name)
                    GAME.teams.append(team)
                    GAME.cars.append(car)
                    if team==GAME.team:
                        if car==1:
                            GAME.car1ID=x-len(unableToRace)
                            GAME.driver1=name
                        else:
                            GAME.car2ID=x-len(unableToRace)
                            GAME.driver2=name
                else:
                        unableToRace.append(name)
                        F=c.execute('''SELECT Name FROM Drivers WHERE Team=? AND Role="Reserve"''',(team,)).fetchall()
                        replacement=0
                        if len(F)>=1:
                            while len(F)>=1 and replacement==0:
                                replacement=random.choice(F)
                                if GAME.Sanitise(replacement) in GAME.drivers:
                                    F.remove(replacement)
                                    replacement=0
                        if replacement==0 and team=="Racing Bulls":
                            F=c.execute('''SELECT Name FROM Drivers WHERE Team="Red Bull" AND Role="Reserve"''').fetchall()
                            if len(F)>=1:
                                while len(F)>=1 and replacement==0:
                                    replacement=random.choice(F)
                                    if GAME.Sanitise(replacement) in GAME.drivers:
                                        F.remove(replacement)
                                        replacement=0
                                    else:
                                        c.execute("UPDATE Drivers SET Team='Racing Bulls' WHERE Name=?",(GAME.Sanitise(replacement),))
                        if replacement==0:
                            replacements.append(0)
                        else:
                            replacement=GAME.Sanitise(replacement)
                            replacements.append(replacement)
                            GAME.drivers.append(replacement)
                            GAME.teams.append(team)
                            GAME.cars.append(car)
        if len(unableToRace)>0:
            GAME.ChangeScreen("Breaking News")
            GAME.screen="Unable To Race"
            y=130
            for x in range(len(unableToRace)):
                y+=50
                canvas.create_text(150, y, text=(unableToRace[x]+" cannot race in the upcoming race."), fill="white", font=("Arial", 30), anchor="nw")
                if replacements[x]!=0:
                    y+=50
                    canvas.create_text(150, y, text=(replacements[x]+" will be replacing them."), fill="white", font=("Arial", 30), anchor="nw")
                    if unableToRace[x]==GAME.car1:
                        GAME.driver1=replacements[x]
                    elif unableToRace[x]==GAME.car2:
                        GAME.driver2=replacements[x]
                elif unableToRace[x]==GAME.car1:
                    GAME.driver1=0
                elif unableToRace[x]==GAME.car2:
                    GAME.driver2=0
            root.after(8000, lambda: GAME.RaceStart())
        else:
            GAME.RaceStart()
    def RaceStart(self):
        GAME.gridPenalties=[]
        GAME.penaltyPlaces=[]
        GAME.pause=0
        with sqlite3.connect(GAME.database) as c:
            race=GAME.Sanitise(c.execute('''SELECT Track FROM Calendar WHERE ID=?''',(GAME.race,)).fetchall()[0])
            country=GAME.Sanitise(c.execute('''SELECT Country FROM Tracks WHERE Name=?''',(race,)).fetchall()[0])
            #Practice
            GAME.rawPace=[]
            corners=GAME.Sanitise(c.execute('''SELECT Corners FROM Tracks WHERE Name=?''',(race,)).fetchall()[0])
            straights=int(GAME.Sanitise(c.execute('''SELECT Straights FROM Tracks WHERE Name=?''',(race,)).fetchall()[0]))
            self.confidence=[]
            GAME.carConfidence=10
            for x in range(len(GAME.drivers)):
                name=GAME.drivers[x]
                team=GAME.teams[x]
                car=GAME.cars[x]
                if corners=="Low":
                    cornering=int(GAME.Sanitise(c.execute('''SELECT LowSpeed FROM Cars WHERE Team=?''',(team,)).fetchall()[0]))
                elif corners=="Medium":
                    cornering=int(GAME.Sanitise(c.execute('''SELECT MediumSpeed FROM Cars WHERE Team=?''',(team,)).fetchall()[0]))
                else:
                    cornering=int(GAME.Sanitise(c.execute('''SELECT HighSpeed FROM Cars WHERE Team=?''',(team,)).fetchall()[0]))
                speed=int(GAME.Sanitise(c.execute('''SELECT DragReduction FROM Cars WHERE Team=?''',(team,)).fetchall()[0]))
                engine=GAME.Sanitise(c.execute('''SELECT Engine FROM Cars WHERE Team=?''',(team,)).fetchall()[0])
                power=int(GAME.Sanitise(c.execute('''SELECT Power FROM Engines WHERE Name=?''',(engine,)).fetchall()[0]))
                if car==1:
                    durability=int(GAME.Sanitise(c.execute('''SELECT car1EngineDurability FROM Cars WHERE Team=?''',(team,)).fetchall()[0]))
                else:
                    durability=int(GAME.Sanitise(c.execute('''SELECT car2EngineDurability FROM Cars WHERE Team=?''',(team,)).fetchall()[0]))
                GAME.engineDurability.append(durability)
                if durability>20:
                    efficiency=round((durability-20)/2)
                    if durability==100:
                        if car==1:
                            engineNumber=int(GAME.Sanitise(c.execute('''SELECT car1Engine FROM Cars WHERE Team=?''',(team,)).fetchall()[0]))
                        else:
                            engineNumber=int(GAME.Sanitise(c.execute('''SELECT car2Engine FROM Cars WHERE Team=?''',(team,)).fetchall()[0]))
                        if engineNumber>4:
                            GAME.gridPenalties.append(name)
                            if engineNumber==5:
                                GAME.penaltyPlaces.append(10)
                            else:
                                GAME.penaltyPlaces.append(5)
                    efficiency=(efficiency//10)+1
                else:
                    efficiency=1
                speed=round(speed*straights*power*efficiency/4000)
                pace=speed+cornering
                pace+=round(int(GAME.Sanitise(c.execute('''SELECT Pace FROM Drivers WHERE Name=?''',(name,)).fetchall()[0]))/3)
                if pace<1:
                    pace=1
                pace=random.randint(round(pace*0.9),round(pace*1.2))
                Confidence=round(pace/5)
                calmness=int(GAME.Sanitise(c.execute('''SELECT Calmness FROM Drivers WHERE Name=?''',(name,)).fetchall()[0]))
                Confidence=round(Confidence*calmness/100)
                Confidence=random.randint(round(Confidence*0.8),round(Confidence*1.5))
                #Driveability
                skill=int(GAME.Sanitise(c.execute('''SELECT Experience FROM Drivers WHERE Name=?''',(name,)).fetchall()[0]))
                skill+=int(GAME.Sanitise(c.execute('''SELECT Control FROM Drivers WHERE Name=?''',(name,)).fetchall()[0]))
                driveability=int(GAME.Sanitise(c.execute('''SELECT Driveability FROM Cars WHERE Team=?''',(team,)).fetchall()[0]))
                if (skill/10)<(25-driveability):
                    #Struggling with car
                    if 25-(skill/10)-driveability<=2:
                        Confidence=round(Confidence/round((random.randint(100,200)/100)))
                        pace=round(pace*0.75)
                        if GAME.teams[x]==GAME.team:
                            GAME.carConfidence-=1
                    elif 25-(skill/10)-driveability<=5:
                        Confidence=round(Confidence/round((random.randint(150,250)/100)))
                        pace=round(pace*0.5)
                        if GAME.teams[x]==GAME.team:
                            GAME.carConfidence-=3
                    else:
                        Confidence=round(Confidence/round((random.randint(250,300)/100)))
                        pace=round(pace*0.3)
                        if GAME.teams[x]==GAME.team:
                            GAME.carConfidence-=5
                rating=int(GAME.Sanitise(c.execute("SELECT Rating FROM Staff WHERE Team=? AND Role=?",(team,f"Race Engineer {car}",)).fetchall()[0]))
                Confidence=round(Confidence*rating/80)
                if team=="Ferrari" and race=="Monza":
                    pace=round(pace*1.2)
                    Confidence=round(Confidence*1.5)
                GAME.rawPace.append(pace)
                GAME.confidence.append(Confidence)
            GAME.raceCountry=GAME.Sanitise(c.execute("SELECT Country FROM Tracks WHERE Name=?",(race,)).fetchall()[0])
        if GAME.driver1 in GAME.drivers:
            car1Confidence=GAME.confidence[GAME.car1ID]
        if GAME.driver2 in GAME.drivers:
            car2Confidence=GAME.confidence[GAME.car2ID]
        self.positions=[]
        self.tyrePace=[]
        self.tyre=[]
        self.tyreRemaining=[]
        self.engineReliability=[]
        self.lap=[]
        self.lap_=[]
        self.time=[]
        self.distance=[]
        self.currentLapTime=[]
        self.tyreCompoundsUsed=[]
        self.damage=[]
        self.overtaking=[]
        self.defending=[]
        self.control=[]
        self.experience=[]
        self.reaction=[]
        self.DRS=[]
        self.tyreAggression=[]
        self.fuelAggression=[]
        self.car1Instructions=[]
        self.car2Instructions=[]
        self.fuel=[]
        self.engineTemperature=[]
        self.ERSdeployment=[]
        self.ERS=[]
        self.tyreWear=[]
        self.grip=[]
        self.frontWings=[]
        self.repairBill=[]
        self.penalties=[]
        self.safety=0
        self.raceFinished=0
        self.pitLap=[]
        self.pitTyre=[]
        self.lapPittedTo=[]
        self.bestPitStop=[-1,100]
        self.drying=0
        self.skippingLaps=0
        self.thingHappened=0
        self.tyrePreservation=[]
        self.startLap=1
        self.injured=[]
        self.dead=[]
        self.expectations=[]
        self.cycles=0
        self.faults=[]
        self.stops=[]
        self.track=race
        self.qualifying=0
        self.cooling=[]
        self.strategy=[]
        self.battery=[]
        self.rainStopped=0
        self.fastest=[-1,0,10]
        GAME.ChangeScreen("Practice")
        GAME.DisplayLayout(race)
        canvas.create_text(20, 125, text=race, fill="white", font=("Arial", 50), anchor="nw")
        if country!=race:
            canvas.create_text(20, 185, text=country, fill="white", font=("Arial", 50), anchor="nw")
        if GAME.carConfidence==10:
            carConfidence="The car feels Great to drive."
        elif GAME.carConfidence==9:
            carConfidence="The car feels Alright to drive."
        elif GAME.carConfidence==8:
            carConfidence="The car doesn't feel Optimal to drive."
        elif GAME.carConfidence>5:
            carConfidence="The car feels Difficult to drive."
        elif GAME.carConfidence>3:
            carConfidence="The car feels Very Difficult to drive."
        elif GAME.carConfidence==2:
            carConfidence="The car feels Extremely Difficult to drive."
        else:
            carConfidence="The car is undriveable."
        canvas.create_text(550, 130, text=carConfidence, fill="white", font=("Arial", 30), anchor="nw")
        if GAME.driver1=="":
            GAME.driver1=0
        if GAME.driver2=="":
            GAME.driver2=0
        GAME.DisplayRaceTeam()
        if GAME.driver1 in GAME.drivers:
            canvas.create_text(300, 290, text=GAME.driver1, fill="white", font=("Arial", 20), anchor="nw")
            canvas.create_text(300, 340, text=("Confidence: "+str(car1Confidence)), fill="white", font=("Arial", 20), anchor="nw")
        if GAME.driver2 in GAME.drivers:
            canvas.create_text(950, 290, text=GAME.driver2, fill="white", font=("Arial", 20), anchor="nw")
            canvas.create_text(950, 340, text=("Confidence: "+str(car2Confidence)), fill="white", font=("Arial", 20), anchor="nw")
        GAME.Button("Qualifying",1200,695)
    def Qualifying(self):
        with sqlite3.connect(GAME.database) as c:
            GAME.rainChance=int(GAME.Sanitise(c.execute('''SELECT RainChance FROM Tracks WHERE Name=?''',(GAME.track,)).fetchall()[0]))
            if random.randint(1,100)<=GAME.rainChance:
                #Wet Qualifying
                weatherMessage="It's wet for Qualifying."
                wet=1
                GAME.rainChance+=15
            else:
                #Dry Qualifying
                weatherMessage="There isn't any rain for Qualifying."
                wet=0
            qualifyingPace=[]
            for x in range(len(GAME.drivers)):
                pace=GAME.rawPace[x]
                driver=GAME.drivers[x]
                team=GAME.teams[x]
                if wet==1:
                    experience=int(GAME.Sanitise(c.execute('''SELECT Experience FROM Drivers WHERE Name=?''',(driver,)).fetchall()[0]))
                    pace=round(pace*experience/100)
                    pace=random.randint(round(pace*0.6),pace)
                qualifyingPace.append(random.randint(pace,round(pace*1.3)))
            for x in range(len(qualifyingPace)):
                highest=-1000000
                highestIndex=-1
                for y in range(len(qualifyingPace)):
                    if qualifyingPace[y]>highest:
                        highest=qualifyingPace[y]
                        highestIndex=y
                qualifyingPace.pop(highestIndex)
                qualifyingPace.insert(highestIndex,0)
                GAME.positions.append(highestIndex)
            #Q1
            f=c.execute("SELECT Name FROM Teams").fetchall()
        eliminations=len(f)-5
        delay=0
        if len(GAME.drivers)>10+eliminations:
            if len(GAME.drivers)<len(f)*2:
                eliminations=len(GAME.drivers)-eliminations-10
            delay=8000
            GAME.ChangeScreen("Q1 Eliminations")
            eliminated=[]
            for x in range(eliminations):
                index=GAME.positions[len(GAME.positions)-1-x]
                eliminated.append(GAME.drivers[index])
            GAME.DisplayEliminations(eliminated,weatherMessage,len(GAME.drivers)+1-eliminations)
        #Q2
        if len(GAME.drivers)>10:
            e=eliminations
            if len(GAME.drivers)<len(f)*2:
                eliminations=len(GAME.drivers)-eliminations-10
            root.after(delay, lambda: GAME.ChangeScreen("Q2 Eliminations"))
            eliminated=[]
            for x in range(eliminations):
                index=GAME.positions[len(GAME.positions)-1-x-e]
                eliminated.append(GAME.drivers[index])
            root.after(delay, lambda i=eliminated: GAME.DisplayEliminations(i,weatherMessage,11))
            delay+=8000
        #Q3
        if len(GAME.drivers)>9:
            drivers=10
        else:
            drivers=len(GAME.drivers)
        root.after(delay, lambda: GAME.Q3(drivers))
    def DisplayEliminations(self,eliminated,w,topPosition):
        if w=="It's wet for Qualifying.":
            canvas.create_text(400, 170, text=w, fill="#2FB3FF", font=("Arial", 50), anchor="nw")
        for x in range(len(eliminated)):
            driver=eliminated[len(eliminated)-x-1]
            Z=75-((len(eliminated)-5)*75)
            GAME.DisplayDriver(driver,(x*200)+Z,500)
            if x%2==0:
                canvas.create_text((x*200)+100+Z, 340, text=str(topPosition+x)+". "+driver, fill="red", font=("Arial", 20), anchor="nw")
            else:
                canvas.create_text((x*200)+100+Z, 290, text=str(topPosition+x)+". "+driver, fill="red", font=("Arial", 20), anchor="nw")
    def Q3(self,drivers):
        GAME.ChangeScreen("Q3 Results")
        delay=0
        for x in range(drivers):
            position=drivers-x
            driver=GAME.drivers[GAME.positions[position-1]]
            if GAME.replay==0:
                with sqlite3.connect(GAME.database) as c:
                    team=GAME.Sanitise(c.execute("SELECT Team FROM Drivers WHERE Name=?",(driver,)).fetchall())
            else:
                team=GAME.teams[GAME.drivers.index(driver)]
            delay+=800
            if position==1:
                colour="#F5C939"
            elif position==2:
                colour="#C8CDD2"
            elif position==3:
                colour="#D79B5A"
            else:
                colour="white"
            root.after(delay, lambda d=driver, p=position, c=colour: canvas.create_text(250, 160+(58*p), text=d, fill=c, font=("Arial", 30), anchor="nw"))
            root.after(delay, lambda t=team, p=position, c=colour: canvas.create_text(820, 160+(58*p), text=t, fill=c, font=("Arial", 30), anchor="nw"))
        delay+=500
        if GAME.sound==1:
            root.after(delay, lambda: GAME.Voice(GAME.drivers[GAME.positions[0]],"Pole"))
        delay+=500
        root.after(delay, lambda: GAME.Button("Prepare for Race",1235,735))
        delay+=500
        root.after(delay, lambda: GAME.QualifyingFinished())
    def QualifyingFinished(self):
        GAME.qualifying=2
    def GridPenalties(self):
        if not GAME.gridPenalties:
            GAME.RacePreparation()
            return
        starting_grid=GAME.positions.copy()
        penalised=dict(zip(GAME.gridPenalties, GAME.penaltyPlaces))
        for driver in list(starting_grid):
            name=GAME.drivers[driver]
            if name in penalised:
                starting_grid.remove(driver)
        for driver in GAME.positions:
            name=GAME.drivers[driver]
            if name in penalised:
                penalty=penalised[name]
                new_index=min(len(starting_grid), GAME.positions.index(driver) + penalty)
                starting_grid.insert(new_index, driver)
        GAME.positions=starting_grid
        GAME.ChangeScreen("Breaking News")
        y=130
        i=0
        for idx, driver in enumerate(GAME.positions):
            name=GAME.drivers[driver]
            if name in penalised:
                if i<10:
                    i+=1
                    place=idx + 1
                    places=penalised[name]
                    suffix={1: "st", 2: "nd", 3: "rd"}.get(place if place < 20 else place % 10, "th")
                    y+=50
                    canvas.create_text(150, y, text=f"{name} has a {places} place grid penalty for", fill="white", font=("Arial", 30), anchor="nw")
                    y+=50
                    if GAME.race==1 and GAME.season==2026:
                        canvas.create_text(150, y, text=f"a 2024 incident, they will be starting the race in {place}{suffix}.", fill="white", font=("Arial", 30), anchor="nw")
                    else:
                        canvas.create_text(150, y, text=f"taking a new engine, they will be starting the race in {place}{suffix}.", fill="white", font=("Arial", 30), anchor="nw")
        root.after(5000, lambda: GAME.RacePreparation())
    def RacePreparation(self):
        #Soft
        GAME.tyrePace.append(random.randint(17,20))
        #Medium
        GAME.tyrePace.append(random.randint(10,GAME.tyrePace[0]-4))
        #Hard
        GAME.tyrePace.append(random.randint(2,GAME.tyrePace[1]-6))
        qualifyingPositions=GAME.positions
        with sqlite3.connect(GAME.database) as c:
            GAME.drs=0
            GAME.ers=int(GAME.Sanitise(c.execute('''SELECT True FROM Regulations WHERE Regulation=="ERS"''').fetchall()[0]))
            GAME.teamOrders=int(GAME.Sanitise(c.execute('''SELECT True FROM Regulations WHERE Regulation=="Team Orders"''').fetchall()[0]))
            GAME.temperature=int(GAME.Sanitise(c.execute('''SELECT Temperature FROM Tracks WHERE Name=?''',(GAME.track,)).fetchall()[0]))
            GAME.length=float(GAME.Sanitise(c.execute('''SELECT Length FROM Tracks WHERE Name=?''',(GAME.track,)).fetchall()[0]))
            GAME.laps=int(GAME.Sanitise(c.execute('''SELECT Laps FROM Tracks WHERE Name=?''',(GAME.track,)).fetchall()[0]))
            GAME.overtakeability=int(GAME.Sanitise(c.execute('''SELECT Overtakeability FROM Tracks WHERE Name=?''',(GAME.track,)).fetchall()[0]))
            GAME.risk=int(GAME.Sanitise(c.execute('''SELECT Risk FROM Tracks WHERE Name=?''',(GAME.track,)).fetchall()[0]))
            GAME.street=int(GAME.Sanitise(c.execute('''SELECT Street FROM Tracks WHERE Name=?''',(GAME.track,)).fetchall()[0]))
            GAME.maxRain=0
            GAME.maxWater=0
            GAME.rain=0
            GAME.water=0
            GAME.wet=0
            GAME.rainStarts=0
            GAME.rainStops=0
            if random.randint(1,100)<=GAME.rainChance:
                #Wet
                num=random.randint(1,4)
                GAME.wet=1
                if num==1:
                   #Raining all race
                    GAME.water=random.randint(6,20)/10
                    GAME.maxRain=random.randint(2,8)
                    GAME.maxWater=random.randint(int(GAME.water*100),550)/100
                    GAME.rain=random.randint(0,GAME.maxRain)/10
                    GAME.maxRain=GAME.maxRain/10
                    GAME.weatherMessage=["It looks like it'll be raining for the entirety of the race.",("There will be "+str(GAME.water)+"mm of water on the track at the start of the race.")]
                elif num==2:
                    #Starts wet and dries
                    GAME.water=random.randint(100,500)/100
                    GAME.rainStops=random.randint(3,GAME.laps)
                    GAME.maxRain=random.randint(20,80)
                    GAME.maxWater=random.randint(int(GAME.water*100),550)/100
                    GAME.rain=random.randint(0,GAME.maxRain)/100
                    GAME.maxRain=GAME.maxRain/100
                    GAME.weatherMessage=[("It looks like it'll be a wet start that'll start to dry around lap "+str(GAME.rainStops)+"."),("There will be "+str(GAME.water)+"mm of water on the track at the start of the race.")]
                elif num==3:
                    #Starts dry and then rains
                    GAME.water=0
                    GAME.rainStarts=random.randint(10,GAME.laps-15)
                    GAME.maxRain=random.randint(20,80)/100
                    GAME.maxWater=random.randint(100,550)/100
                    GAME.weatherMEssage=[("It looks like it'll be a dry start but rain should start around lap "+str(GAME.rainStarts)+".")]
                else:
                    #Starts dry then rains then dries again
                    GAME.water=0
                    GAME.rainStarts=random.randint(10,GAME.laps-30)
                    GAME.rainStops=random.randint(GAME.rainStarts,GAME.laps-10)
                    GAME.maxRain=random.randint(20,80)/100
                    GAME.maxWater=random.randint(100,550)/100
                    GAME.rain=0
                    GAME.weatherMessage=[("It looks like it'll be a dry start but rain should start around lap "+str(GAME.rainStarts)+","),("which is predicted to stop around lap "+str(GAME.rainStops)+".")]
            else:
                #Dry
                GAME.weatherMessage=["We're not expecting any rain during this race."]
            if GAME.temperature<=22:
                GAME.wearConstant=random.randint(30,45)/10
            elif GAME.temperature<30:
                GAME.wearConstant=random.randint(45,55)/10
            else:
                GAME.wearConstant=5.5
            wearVariable=round(random.randint(0,3)/2)
            wearVariable+=int(GAME.Sanitise(c.execute("SELECT TyreWear FROM Player").fetchall()[0]))
            valid=0
            while valid==0:
                valid=1
                GAME.tyreWear=[]
                for x in range(4):
                    if x==0:
                        wear=GAME.wearConstant
                    elif x==1:
                        wear=round(GAME.wearConstant/1.5)
                    elif x==2:
                        wear=round(GAME.wearConstant/2.2)
                    else:
                        wear=round(115/GAME.laps)
                    wear+=wearVariable
                    if wear<1:
                        wear=1
                    GAME.tyreWear.append(wear)
                GAME.expectedTyreLife=[]
                for x in range(3):
                    if valid==1:
                        laps=round(70/GAME.tyreWear[x])
                        if x>0:
                            if laps==GAME.expectedTyreLife[x-1]:
                                wear=70/(laps+2)
                                GAME.tyreWear.pop(x)
                                GAME.tyreWear.insert(x,wear)
                                laps=round(70/wear)
                        if laps>=40:
                            valid=0
                            GAME.wearConstant+=1
                        GAME.expectedTyreLife.append(laps)
                GAME.expectedTyreLife.append(round(70/GAME.tyreWear[3]))
            pace=GAME.rawPace.copy()
            names=GAME.drivers.copy()
            for x in range(len(GAME.drivers)):
                GAME.racePace.append(0)
            for x in range(len(GAME.drivers)):
                highest=-1000000
                highestIndex=0
                highestDriver=""
                for y in range(len(pace)):
                    if pace[y]>highest:
                        highest=pace[y]
                        highestIndex=y
                        highestDriver=names[y]
                GAME.racePace.pop(GAME.drivers.index(highestDriver))
                GAME.racePace.insert(GAME.drivers.index(highestDriver),250-(x*8)+random.randint(-5,5))
                pace.pop(highestIndex)
                names.pop(highestIndex)
            #Strategy
            length=GAME.expectedTyreLife[1]+GAME.expectedTyreLife[2]
            if GAME.wet==1:
                standardStrategy=0
            else:
                if length*1.5>=GAME.laps-3:
                    standardStrategy=1
                elif length>=GAME.laps:
                    standardStrategy=1.5
                else:
                    standardStrategy=2
            for x in range(len(GAME.drivers)):
                driver=GAME.drivers[x]
                team=GAME.teams[x]
                GAME.tyreRemaining.append(100)
                GAME.faults.append(0)
                GAME.stops.append(0)
                engine=GAME.Sanitise(c.execute('''SELECT Engine FROM Cars WHERE Team=?''',(team,)).fetchall()[0])
                GAME.engineReliability.append(int(GAME.Sanitise(c.execute('''SELECT Reliability FROM Engines WHERE Name=?''',(engine,)).fetchall()[0])))
                GAME.lap.append(1)
                GAME.lap_.append(1)
                position=int(GAME.positions.index(x))
                GAME.time.append((position-1)*0.5)
                GAME.distance.append((position-1)*-0.8)
                GAME.currentLapTime.append(1.5)
                GAME.tyreCompoundsUsed.append(1)
                GAME.damage.append(0)
                GAME.ERS.append(100)
                GAME.overtaking.append(int(GAME.Sanitise(c.execute('''SELECT Overtaking FROM Drivers WHERE Name=?''',(driver,)).fetchall()[0])))
                GAME.defending.append(int(GAME.Sanitise(c.execute('''SELECT Defending FROM Drivers WHERE Name=?''',(driver,)).fetchall()[0])))
                GAME.control.append(int(GAME.Sanitise(c.execute('''SELECT Control FROM Drivers WHERE Name=?''',(driver,)).fetchall()[0])))
                GAME.experience.append(int(GAME.Sanitise(c.execute('''SELECT Experience FROM Drivers WHERE Name=?''',(driver,)).fetchall()[0])))
                GAME.reaction.append(int(GAME.Sanitise(c.execute('''SELECT Reaction FROM Drivers WHERE Name=?''',(driver,)).fetchall()[0])))
                GAME.cooling.append(int(GAME.Sanitise(c.execute('''SELECT Cooling FROM Cars WHERE Team=?''',(team,)).fetchall()[0])))
                GAME.tyrePreservation.append(int(GAME.Sanitise(c.execute('''SELECT TyrePreservation FROM Cars WHERE Team=?''',(team,)).fetchall()[0])))
                GAME.engineTemperature.append(85+random.randint(0,15))
                GAME.fuel.append(100)
                GAME.frontWings.append(1)
                GAME.repairBill.append(0)
                GAME.penalties.append(0)
                GAME.lapPittedTo.append(1)
                GAME.battery.append(8)
                #Strategy
                if team==GAME.team:
                    GAME.tyre.append("Placeholder")
                    GAME.tyreAggression.append("Placeholder")
                    GAME.fuelAggression.append("Placeholder")
                    GAME.ERSdeployment.append("Placeholder")
                    GAME.pitLap.append(0)
                    GAME.pitTyre.append(0)
                    GAME.strategy.append(0)
                else:
                    GAME.tyreAggression.append(random.randint(3,5))
                    GAME.fuelAggression.append(3)
                    GAME.ERSdeployment.append(3)
                    if GAME.wet==1:
                        GAME.strategy.append(0)
                        GAME.pitLap.append(0)
                        GAME.pitTyre.append(0)
                        if GAME.water==0:
                            if GAME.rainStarts<GAME.expectedTyreLife[0]:
                                GAME.tyre.append("Soft")
                            elif GAME.rainStarts<GAME.expectedTyreLife[1]:
                                GAME.tyre.append("Medium")
                            else:
                                if GAME.rainStarts>=GAME.expectedTyreLife[2]:
                                    GAME.tyre.append("Medium")
                                else:
                                    num=random.randint(1,3)
                                    if num==1:
                                        GAME.tyre.append("Soft")
                                    elif num==2:
                                        GAME.tyre.append("Medium")
                                    else:
                                        GAME.tyre.append("Hard")
                        elif GAME.water>=2.5:
                            GAME.tyre.append("Wet")
                        else:
                            GAME.tyre.append("Intermediate")
                    elif GAME.track=="Monte Carlo" and random.randint(1,50)==50 and GAME.positions.index(x)>9:
                        GAME.strategy.append(1)
                        GAME.pitLap.append(1)
                        GAME.tyre.append("Soft")
                        if random.randint(1,5)<=3:
                            GAME.pitTyre.append("Medium")
                        else:
                            GAME.pitTyre.append("Hard")
                    else:
                        if standardStrategy==1.5:
                            if random.randint(1,5)<4:
                                strategy=1
                            else:
                                strategy=2
                        elif random.randint(1,12)==12:
                            strategy=3-standardStrategy
                        else:
                            strategy=standardStrategy
                        GAME.strategy.append(strategy)
                        if strategy==2:
                            num=random.randint(1,10)
                            if position<=5:
                                if num<=5:
                                    tyre="Soft"
                                elif num<=9:
                                    tyre="Medium"
                                else:
                                    tyre="Hard"
                            elif position<=10:
                                if num<=3:
                                    tyre="Soft"
                                elif num<=8:
                                    tyre="Medium"
                                else:
                                    tyre="Hard"
                            else:
                                if num==1:
                                    tyre="Soft"
                                elif num<=5:
                                    tyre="Medium"
                                else:
                                    tyre="Hard"
                            if tyre=="Soft":
                                tyreLife=GAME.expectedTyreLife[0]
                            elif tyre=="Medium":
                                tyreLife=GAME.expectedTyreLife[1]
                            else:
                                tyreLife=GAME.expectedTyreLife[2]
                            if tyreLife+length>=GAME.laps:
                                pitLap=(GAME.laps*tyreLife/(tyreLife+length))+random.randint(-2,2)
                                if pitLap+GAME.expectedTyreLife[0]+GAME.expectedTyreLife[1]>=GAME.laps and random.randint(1,4)>1:
                                    if tyre=="Soft":
                                        pitTyre="Medium"
                                    else:
                                        pitTyre="Soft"
                                elif pitLap+GAME.expectedTyreLife[0]+GAME.expectedTyreLife[2]>=GAME.laps and random.randint(1,4)>1:
                                    if tyre=="Soft":
                                        pitTyre="Hard"
                                    elif tyre=="Hard" or random.randint(1,2)==1:
                                        pitTyre="Soft"
                                    else:
                                        pitTyre="Hard"
                                else:
                                    if tyre=="Medium":
                                        pitTyre="Hard"
                                    elif tyre=="Hard" or random.randint(1,2)==1:
                                        pitTyre="Medium"
                                    else:
                                        pitTyre="Hard"
                                if pitTyre=="Soft":
                                    pitTyreLife=GAME.expectedTyreLife[0]
                                elif pitTyre=="Medium":
                                    pitTyreLife=GAME.expectedTyreLife[1]
                                else:
                                    pitTyreLife=GAME.expectedTyreLife[2]
                                if tyreLife+pitTyreLife+GAME.expectedTyreLife[0]+3>GAME.laps:
                                    totalLength=tyreLife+pitTyreLife+GAME.expectedTyreLife[0]
                                    pitLap=round(GAME.laps*pitLap/totalLength)+random.randint(-1,2)
                            else:
                                pitLap=round(tyreLife*1.5)+random.randint(-2,1)
                                if (pitLap+GAME.expectedTyreLife[0]+GAME.expectedTyreLife[1])*1.5>=GAME.laps and random.randint(1,4)>1:
                                    if tyre=="Soft":
                                        pitTyre="Medium"
                                    else:
                                        pitTyre="Soft"
                                elif (pitLap+GAME.expectedTyreLife[0]+GAME.expectedTyreLife[2])*1.5>=GAME.laps and random.randint(1,4)>1:
                                    if tyre=="Soft":
                                        pitTyre="Hard"
                                    elif tyre=="Hard" or random.randint(1,2)==1:
                                        pitTyre="Soft"
                                    else:
                                        pitTyre="Hard"
                                else:
                                    if tyre=="Medium":
                                        pitTyre="Hard"
                                    elif tyre=="Hard" or random.randint(1,2)==1:
                                        pitTyre="Medium"
                                    else:
                                        pitTyre="Hard"
                        else:
                            #1 Stop
                            if GAME.expectedTyreLife[0]+GAME.expectedTyreLife[1]>=GAME.laps-3:
                                tyreOptions=["Soft","Medium"]
                            elif GAME.expectedTyreLife[0]+GAME.expectedTyreLife[2]>=GAME.laps-3:
                                tyreOptions=["Soft","Hard"]
                            else:
                                tyreOptions=["Medium","Hard"]
                            if position<=5:
                                if random.randint(1,5)==5:
                                    tyre=tyreOptions[1]
                                else:
                                    tyre=tyreOptions[0]
                            elif position<=10:
                                if random.randint(1,5)>=4:
                                    tyre=tyreOptions[1]
                                else:
                                    tyre=tyreOptions[0]
                            else:
                                if random.randint(1,2)==2:
                                    tyre=tyreOptions[1]
                                else:
                                    tyre=tyreOptions[0]
                            if tyre=="Soft":
                                tyreLife=GAME.expectedTyreLife[0]
                            elif tyre=="Medium":
                                tyreLife=GAME.expectedTyreLife[1]
                            else:
                                tyreLife=GAME.expectedTyreLife[2]
                            if length>=GAME.laps-3:
                                pitLap=round(tyreLife)+random.randint(-2,2)
                            else:
                                pitLap=round(tyreLife*1.5)+random.randint(-2,1)
                            if pitLap>GAME.laps/2 and tyre==tyreOptions[0]:
                                pitLap=round(GAME.laps/2)+random.randint(-3,1)
                            if tyre==tyreOptions[0]:
                                pitTyre=tyreOptions[1]
                            else:
                                pitTyre=tyreOptions[0]
                        GAME.tyre.append(tyre)
                        GAME.pitLap.append(pitLap)
                        GAME.pitTyre.append(pitTyre)
        GAME.driver=1
        GAME.ChooseStartingTyres()
    def ChooseStartingTyres(self):
        GAME.ChangeScreen("Choose Tyres")
        if GAME.replay==1:
            GAME.weatherMessage=["Abu Dhabi 2021"]
        elif GAME.replay==2:
            GAME.weatherMessage=["F1 THE MOVIE"]
        if len(GAME.weatherMessage)==1:
            canvas.create_text(20, 10, text=GAME.weatherMessage[0], fill="black", font=("Arial", 40), anchor="nw")
        else:
            for x in range(len(GAME.weatherMessage)):
                canvas.create_text(20, 5+(x*40), text=GAME.weatherMessage[x], fill="black", font=("Arial", 30), anchor="nw")
        canvas.create_text(1250, 10, text=(str(GAME.laps)+" Laps"), fill="black", font=("Arial", 40), anchor="nw")
        canvas.create_text(230, 200, text=("Estimated: "+str(GAME.expectedTyreLife[0])+" Laps"), fill="black", font=("Arial", 20), anchor="nw")
        if GAME.replay==5:
            canvas.create_text(230, 420, text=("Not Available"), fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(1180, 380, text=("Not Available"), fill="black", font=("Arial", 20), anchor="nw")
        else:
            canvas.create_text(230, 420, text=("Estimated: "+str(GAME.expectedTyreLife[1])+" Laps"), fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(1180, 380, text=("Estimated: "+str(GAME.expectedTyreLife[3])+" Laps"), fill="black", font=("Arial", 20), anchor="nw")
        canvas.create_text(230, 630, text=("Estimated: "+str(GAME.expectedTyreLife[2])+" Laps"), fill="black", font=("Arial", 20), anchor="nw")
        canvas.create_text(1180, 620, text=("Estimated: "+str(GAME.expectedTyreLife[3])+" Laps"), fill="black", font=("Arial", 20), anchor="nw")
        if GAME.driver==1 and GAME.car1ID in GAME.positions:
            driver=GAME.driver1
        else:
            driver=GAME.driver2
        GAME.DisplayDriver(driver,520,500)
    def ChooseStartingAggression(self):
        GAME.ChangeScreen("Choose Aggression")
        for x in range(3):
            if GAME.ers==0 and x==2:
                GAME.Button("ERS Disabled",210,645)
            else:
                GAME.Button("Length Selector",210,125+(260*x))
                if x==0:
                    aggressions=["Conserve","Light","Balanced","Aggressive","Attack"]
                elif x==1:
                    aggressions=["Conserve","Balanced","Push"]
                elif GAME.ers==1:
                    aggressions=["Recharge","Neutral","Boost"]
                else:
                    aggressions=["Harvest","Neutral","Deployed"]
                canvas.create_text(300,132+(260*x), text=aggressions[GAME.aggressions[x]-1], fill="black", font=("Arial", 20), anchor="nw")
        if GAME.driver==1 and GAME.car1ID in GAME.positions:
            driver=GAME.driver1
        else:
            driver=GAME.driver2
        GAME.DisplayDriver(driver,900,500)
        if driver==GAME.driver1 and GAME.car2ID in GAME.positions:
            GAME.Button("Next",510,730)
        else:
            GAME.Button("Start Race",510,730)
    def CarRanking(self):
        F1=sqlite3.connect(GAME.database)
        c=F1.cursor()
        c.execute('''SELECT Name FROM Teams''')
        f=c.fetchall()
        teams=[]
        scores=[]
        for x in range(len(f)):
            team=GAME.Sanitise(f[x])
            teams.append(team)
            score=0
            c.execute('''SELECT DragReduction FROM Cars WHERE Team=?''',(team,))
            score+=int(GAME.Sanitise(c.fetchall()[0]))*3
            c.execute('''SELECT LowSpeed FROM Cars WHERE Team=?''',(team,))
            score+=int(GAME.Sanitise(c.fetchall()[0]))*3
            c.execute('''SELECT MediumSpeed FROM Cars WHERE Team=?''',(team,))
            score+=int(GAME.Sanitise(c.fetchall()[0]))*3
            c.execute('''SELECT HighSpeed FROM Cars WHERE Team=?''',(team,))
            score+=int(GAME.Sanitise(c.fetchall()[0]))*3
            c.execute('''SELECT TyrePreservation FROM Cars WHERE Team=?''',(team,))
            score+=int(GAME.Sanitise(c.fetchall()[0]))*2
            c.execute('''SELECT Cooling FROM Cars WHERE Team=?''',(team,))
            score+=int(GAME.Sanitise(c.fetchall()[0]))
            scores.append(score)
        for x in range(len(scores)):
            highest=0
            highestIndex=-1
            for y in range(len(scores)):
                if scores[y]>highest:
                    highest=scores[y]
                    highestIndex=y
            scores.pop(highestIndex)
            c.execute('''UPDATE Cars SET Ranking=? WHERE Team=?''',(x+1, teams[highestIndex],))
            teams.pop(highestIndex)
        F1.commit()
        F1.close()
    def Standings(self,final):
        GAME.ChangeScreen("Standings")
        if final==1:
            GAME.screen="Final Standings"
        with sqlite3.connect(GAME.database) as c:
            f=c.execute('''SELECT Name FROM Teams''').fetchall()
            if GAME.race<=GAME.races:
                racesLeft=GAME.races-GAME.race+1
                pointsSystem=int(GAME.Sanitise(c.execute("SELECT True FROM Regulations WHERE Regulation='Old Points System'").fetchall()))
                double=int(GAME.Sanitise(c.execute("SELECT True FROM Regulations WHERE Regulation='Double Points On Last Race'").fetchall()))
                fastestLapPoint=int(GAME.Sanitise(c.execute("SELECT True FROM Regulations WHERE Regulation='Fastest Lap Point'").fetchall()))
                if pointsSystem==0:
                    constructorsPoints=(43+fastestLapPoint)*(racesLeft+double)
                    driversPoints=(25+fastestLapPoint)*(racesLeft+double)
                else:
                    constructorsPoints=(18+fastestLapPoint)*(racesLeft+double)
                    driversPoints=(10+fastestLapPoint)*(racesLeft+double)
            else:
                constructorsPoints=0
                driversPoints=0
            won=0
            for x in range(len(f)):
                name=GAME.Sanitise(c.execute('''SELECT Name FROM Teams WHERE Position=?''',(x+1,)).fetchall()[0])
                points=int(GAME.Sanitise(c.execute('''SELECT Points FROM Teams WHERE Position=?''',(x+1,)).fetchall()[0]))
                if x==0:
                    colour="#F5C939"
                    firstPoints=points
                    if name in steam:
                        appearance=name
                    else:
                        appearance=GAME.Sanitise(c.execute("SELECT Appearance FROM Teams WHERE Name=?",(name,)).fetchall()[0])
                    if appearance!="0":
                        if appearance in steam:
                            logo=logos[steam.index(appearance)-1]
                        else:
                            try:
                                logo=sponsorLogos[sponsors.index(appearance)]
                            except:
                                logo=0
                        if logo!=0:
                            canvas.image=logo
                            canvas.create_image(280, 500, anchor=tk.NW, image=logo)
                elif firstPoints-points>=constructorsPoints and GAME.race<=GAME.races:
                    if x==1:
                        won=1
                    if won==1:
                        colour="#DADADA"
                    else:
                        colour="#B60000"
                elif x==1:
                    colour="#C8CDD2"
                elif x==2:
                    colour="#D79B5A"
                else:
                    colour="white"
                engine=GAME.Sanitise(c.execute('''SELECT Engine FROM Cars WHERE Team=?''',(name,)).fetchall()[0])
                if engine=="Red Bull":
                    engine="Ford RBPT"
                if engine in name:
                    engine=""
                fullName=f"{name} {engine}"
                if len(fullName)>30:
                    fullName=name
                if x<9:
                    canvas.create_text(150, 130+(x*25), text=f"{x+1}. {fullName}", fill=colour, font=("Arial", 15), anchor="nw")
                else:
                    canvas.create_text(145, 130+(x*25), text=f"{x+1}. {fullName}", fill=colour, font=("Arial", 15), anchor="nw")
                if points==1:
                    canvas.create_text(500, 130+(x*25), text="1 Point", fill=colour, font=("Arial", 15), anchor="nw")
                elif points<10:
                    canvas.create_text(500, 130+(x*25), text=f"{points} Points", fill=colour, font=("Arial", 15), anchor="nw")
                elif points<100:
                    canvas.create_text(495, 130+(x*25), text=f"{points} Points", fill=colour, font=("Arial", 15), anchor="nw")
                elif points<1000:
                    canvas.create_text(490, 130+(x*25), text=f"{points} Points", fill=colour, font=("Arial", 15), anchor="nw")
                else:
                    canvas.create_text(485, 130+(x*25), text=f"{points} Points", fill=colour, font=("Arial", 15), anchor="nw")
        f=c.execute('''SELECT Name FROM Drivers WHERE Position!=0''').fetchall()
        won=0
        for x in range(len(f)):
            if x<26:
                points=int(GAME.Sanitise(c.execute('''SELECT Points FROM Drivers WHERE Position=?''',(x+1,)).fetchall()[0]))
                if x==0:
                    colour="#F5C939"
                    firstPoints=points
                elif firstPoints-points>=driversPoints and GAME.race<=GAME.races:
                    if x==1:
                        won=1
                    if won==1:
                        colour="#DADADA"
                    else:
                        colour="#B60000"
                elif x==1:
                    colour="#C8CDD2"
                elif x==2:
                    colour="#D79B5A"
                else:
                    colour="white"
                name=GAME.Sanitise(c.execute('''SELECT Name FROM Drivers WHERE Position=?''',(x+1,)).fetchall()[0])
                team=GAME.Sanitise(c.execute('''SELECT Team FROM Drivers WHERE Position=?''',(x+1,)).fetchall()[0])
                if team=="Dead":
                    team=""
                if x<9:
                    canvas.create_text(770, 130+(x*25), text=f"{x+1}. {name} {team}", fill=colour, font=("Arial", 15), anchor="nw")
                else:
                    canvas.create_text(765, 130+(x*25), text=f"{x+1}. {name} {team}", fill=colour, font=("Arial", 15), anchor="nw")
                if points==1:
                    canvas.create_text(1290, 130+(x*25), text="1 Point", fill=colour, font=("Arial", 15), anchor="nw")
                elif points<10:
                    canvas.create_text(1290, 130+(x*25), text=f"{points} Points", fill=colour, font=("Arial", 15), anchor="nw")
                elif points<100:
                     canvas.create_text(1285, 130+(x*25), text=f"{points} Points", fill=colour, font=("Arial", 15), anchor="nw")
                else:
                    canvas.create_text(1280, 130+(x*25), text=f"{points} Points", fill=colour, font=("Arial", 15), anchor="nw")
        if GAME.team in steam:
            appearance=GAME.team
        else:
            appearance=GAME.Sanitise(c.execute("SELECT Appearance FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0])
        if appearance!="0":
            if appearance in steam:
                logo=logos[steam.index(appearance)-1]
            else:
                try:
                    logo=sponsorLogos[sponsors.index(appearance)]
                except:
                    logo=0
            if logo!=0:
                canvas.image=logo
                canvas.create_image(1300, 5, anchor=tk.NW, image=logo)
        if final==0:
            GAME.Button("Back",5,730)
        else:
            GAME.Button("End Season",1200,730)
    def WinterHiring(self):
        with sqlite3.connect(GAME.database) as c:
            teams=c.execute("SELECT Name FROM Teams").fetchall()
        GAME.DriverHiring(teams)
        GAME.StaffHiring(teams)
    def DriverHiring(self,teams):
        for x in range(len(teams)):
            with sqlite3.connect(GAME.database) as c:
                team=GAME.Sanitise(c.execute("SELECT Name FROM Teams WHERE Position=?",(x+1,)).fetchall()[0])
                for y in range(2):
                    if len(c.execute("SELECT Name FROM Drivers WHERE Team=? AND Role=?",(team,str(y+1),)).fetchall())==0:
                        try:
                            newTeam=GAME.Sanitise(c.execute("SELECT NewTeam FROM Drivers WHERE Team=? AND Role=?",(team,str(y+1),)).fetchall()[0])
                            if newTeam=="0":
                                contractEnd=int(GAME.Sanitise(c.execute("SELECT ContractEnd FROM Drivers WHERE Team=? AND Role=?",(team,str(y+1),)).fetchall()[0]))
                                if contractEnd<=GAME.season:
                                    hire=2
                                else:
                                    hire=0
                            elif newTeam==team:
                                role=GAME.Sanitise(c.execute("SELECT NewRole FROM Drivers WHERE Team=? AND Role=?",(team,str(y+1),)).fetchall()[0])
                                if role==str(y+1):
                                    hire=0
                                else:
                                    hire=1
                        except:
                            hire=1
                        if hire==1:
                            f=c.execute("SELECT Name FROM Drivers WHERE Team='Free Agent' AND Age>17").fetchall()
                        elif hire==2:
                            f=c.execute("SELECT Name FROM Drivers WHERE Team=? AND Role=?",(team,str(y+1),)).fetchall()
                        if hire==1 or hire==2:
                            name=GAME.Sanitise(random.choice(f))
                            salary=int(GAME.Sanitise(c.execute("SELECT Salary FROM Drivers WHERE Name=?",(name,)).fetchall()[0]))
                            if salary<2000000:
                                salary=2000000
                            c.execute("UPDATE Drivers SET Team=?, Role=?, Salary=?, ContractEnd=? WHERE Name=?",(team,str(y+1),salary,GAME.season+1,name,))
    def StaffHiring(self, teams):
        roles = ["Technical Director", "Sporting Director", "Race Engineer 1", "Race Engineer 2"]
        for x in range(4):
            for y in range(12):
                GAME.GeneratePeople(roles[x])
        with sqlite3.connect(GAME.database) as conn:
            c = conn.cursor()
            for x in range(len(teams)):
                team = GAME.Sanitise(
                    c.execute("SELECT Name FROM Teams WHERE Position=?", (x + 1,)).fetchall()[0]
                )
                for y, role in enumerate(roles):
                    
                    f = c.execute("SELECT Name FROM Staff WHERE Team=? AND Role=?", (team, role)).fetchall()
                    
                    if len(f) == 0:
                        if y < 2:
                            name = GAME.Sanitise(
                                random.choice(
                                    c.execute("SELECT Name FROM Staff WHERE Team='Free Agent' AND Role=?", (role,)).fetchall()
                                )
                            )
                        else:
                            name = GAME.Sanitise(
                                random.choice(
                                    c.execute("SELECT Name FROM Staff WHERE Team='Free Agent' AND (Role='Race Engineer' OR Role='Race Engineer 1' OR Role='Race Engineer 2')").fetchall()
                                )
                            )
                        salary = int(GAME.Sanitise(
                            c.execute("SELECT Salary FROM Staff WHERE Name=?", (name,)).fetchall()[0]
                        ))
                        if salary < 1000000:
                            salary = 1000000

                        c.execute("UPDATE Staff SET Team=?, Role=?, Salary=? WHERE Name=?", (team, role, salary, name))
            conn.commit()
    def NewCars(self):
        with sqlite3.connect(GAME.database) as c:
            GAME.season+=1
            GAME.race=0
            c.execute('''UPDATE Player SET Race=0, Season=?''',(GAME.season,))
            regulationChange=int(GAME.Sanitise(c.execute('''SELECT RegulationChange FROM Player''').fetchall()[0]))
            if regulationChange==GAME.season:
                championships=int(GAME.Sanitise(c.execute("SELECT Championships FROM Player").fetchall()[0]))
                #Aerodynamic Changes
                if GAME.team!="Red Bull" and GAME.team!="Racing Bulls":
                    if len(c.execute('''SELECT Name FROM Teams WHERE Name="Red Bull" OR Name="Racing Bulls"''').fetchall())==2:
                        R=int(GAME.Sanitise(c.execute('''SELECT Research FROM Cars WHERE Team="Red Bull"''').fetchall()[0]))
                        r=int(GAME.Sanitise(c.execute('''SELECT Research FROM Cars WHERE Team="Racing Bulls"''').fetchall()[0]))
                        if R<r:
                            num=R
                            R=r
                            r=num
                            c.execute('''UPDATE Cars SET Research=? WHERE Team="Red Bull"''',(R,))
                            c.execute('''UPDATE Cars SET Research=? WHERE Team="Racing Bulls"''',(r,))
                f=c.execute('''SELECT Name FROM Teams''').fetchall()
                for x in range(len(f)):
                    research=c.execute("SELECT Research FROM Cars WHERE Research!=-1").fetchall()
                    highest=0
                    for y in range(len(research)):
                        r=int(GAME.Sanitise(research[y]))
                        if r>highest:
                            highest=r
                    team=GAME.Sanitise(c.execute("SELECT Team FROM Cars WHERE Research=?",(highest,)).fetchall()[0])

                    #Driveability
                    highest=random.randint(2,19)
                    d=random.randint(2,19)
                    if d>highest:
                        highest=d
                        
                    stats=[]
                    for y in range(6):
                        stat=0
                        for z in range(9):
                            if x<=z+1 and stat==0 and random.randint(1,5)<5 and not (team==GAME.team and championships>1 and z==0) and not (team==GAME.team and championships>4 and z==1):
                                stat=60-(z*4)
                        if stat==0:
                            stat=24
                        stats.append(stat)
                    c.execute("UPDATE Cars SET DragReduction=?, LowSpeed=?, MediumSpeed=?, HighSpeed=?, Cooling=?, TyrePreservation=?, Research=-1, Driveability=? WHERE Team=?",(stats[0],stats[1],stats[2],stats[3],stats[4],stats[5],highest,team,))
                c.execute("UPDATE Cars SET Research=1")
                
                #Engine Changes
                f=c.execute('''SELECT Name FROM Engines''').fetchall()
                engines=[]
                research=[]
                for x in range(len(f)):
                    name=GAME.Sanitise(f[x])
                    r=int(GAME.Sanitise(c.execute('''SELECT Research FROM Engines WHERE Name=?''',(name,)).fetchall()[0]))
                    manufacturer=GAME.Sanitise(c.execute("SELECT Manufacturer FROM Engines WHERE Name=?",(name,)).fetchall()[0])
                    if len(c.execute("SELECT Name FROM Staff WHERE Role='Technical Director' AND Rating=100 AND Team=?",(manufacturer,)).fetchall())>0:
                        r=random.randint(r,round(r*3.5))
                    research.append(r)
                for x in range(len(f)):
                    highest=0
                    highestIndex=0
                    for y in range(len(f)):
                        name=GAME.Sanitise(f[y])
                        r=research[y]
                        if r>highest:
                            highest=r
                            highestIndex=y
                    engine=GAME.Sanitise(f[highestIndex])
                    if engine not in engines:
                        engines.append(engine)
                    f.pop(highestIndex)
                    research.pop(highestIndex)
                for x in range(len(engines)):
                    for y in range(2):
                        stat=0
                        for z in range(10):
                            if stat==0 and ((x<=z and random.randint(1,3)==3) or random.randint(1,10)==10):
                                stat=10-z
                        if y==0:
                            c.execute("UPDATE Engines SET Power=? WHERE Name=?",(stat,engines[x],))
                        else:
                            c.execute("UPDATE Engines SET Reliability=? WHERE Name=?",(stat,engines[x],))
                c.execute("UPDATE Engines SET Research=1")
                c.execute("UPDATE Engines SET Power=1 WHERE Power=0")
                c.execute("UPDATE Engines SET Reliability=1 WHERE Reliability=0")
                regulationChange+=3
                c.execute('''UPDATE Player SET RegulationChange=?''',(regulationChange,))
            else:
                teams=c.execute("SELECT Name FROM Teams").fetchall()
                for x in range(len(teams)):
                    team=GAME.Sanitise(teams[x])
                    position=int(GAME.Sanitise(c.execute("SELECT Position FROM  Teams WHERE Name=?",(team,)).fetchall()[0]))
                    for y in range(6):
                        statChange=round(position*1.3)+random.randint(-15,10)
                        if y==0:
                            stat=int(GAME.Sanitise(c.execute("SELECT DragReduction FROM Cars WHERE Team=?",(team,)).fetchall()[0]))
                        elif y==1:
                            stat=int(GAME.Sanitise(c.execute("SELECT LowSpeed FROM Cars WHERE Team=?",(team,)).fetchall()[0]))
                        elif y==2:
                            stat=int(GAME.Sanitise(c.execute("SELECT MediumSpeed FROM Cars WHERE Team=?",(team,)).fetchall()[0]))
                        elif y==3:
                            stat=int(GAME.Sanitise(c.execute("SELECT HighSpeed FROM Cars WHERE Team=?",(team,)).fetchall()[0]))
                        elif y==4:
                            stat=int(GAME.Sanitise(c.execute("SELECT Cooling FROM Cars WHERE Team=?",(team,)).fetchall()[0]))
                        else:
                            stat=int(GAME.Sanitise(c.execute("SELECT TyrePreservation FROM Cars WHERE Team=?",(team,)).fetchall()[0]))
                        stat+=statChange
                        if stat<1:
                            stat=1
                        if y==0:
                            c.execute("UPDATE Cars SET DragReduction=? WHERE Team=?",(stat,team,))
                        elif y==1:
                            c.execute("UPDATE Cars SET LowSpeed=? WHERE Team=?",(stat,team,))
                        elif y==2:
                            c.execute("UPDATE Cars SET MediumSpeed=? WHERE Team=?",(stat,team,))
                        elif y==3:
                            c.execute("UPDATE Cars SET HighSpeed=? WHERE Team=?",(stat,team,))
                        elif y==4:
                            c.execute("UPDATE Cars SET Cooling=? WHERE Team=?",(stat,team,))
                        else:
                            c.execute("UPDATE Cars SET TyrePreservation=? WHERE Team=?",(stat,team,))
                    driveability=int(GAME.Sanitise(c.execute("SELECT Driveability FROM Cars WHERE Team=?",(team,)).fetchall()[0]))+random.randint(-3,3)
                    if driveability<1:
                        driveability=1
                    elif driveability>20:
                        driveability=20
                    c.execute("UPDATE Cars SET Driveability=? WHERE Team=?",(driveability,team,))
    def Update(self):
        drivers=[]
        with sqlite3.connect(GAME.database) as c:
            #Drivers
            f=c.execute("SELECT Name FROM Drivers WHERE Pace<0 AND Condition!='Dead' AND Legend=0 AND Team!=? AND NewTeam!=?",(GAME.team,GAME.team,)).fetchall()
            if len(f)>0:
                for x in range(len(f)):
                    c.execute("UPDATE Drivers SET Team='Retired', Role='Retired', Condition='Retired' AND ContractEnd=0 WHERE Name=?",(GAME.Sanitise(f[x]),))
            c.execute("UPDATE Drivers SET Condition='Well' WHERE Condition='Ill' OR Condition='Injured'")
            if len(c.execute("SELECT Name FROM Drivers WHERE NewTeam!='0'").fetchall())>0:
                c.execute("UPDATE Drivers SET Team='Free Agent', Role='Free Agent', ContractEnd=0 WHERE ContractEnd<=? AND Team!='Retired' AND Condition!='Legend'",(GAME.season,))
                drivers=c.execute("SELECT Name FROM Drivers WHERE Condition='Well'").fetchall()
        if len(drivers)>0:
            for x in range(len(drivers)):
                with sqlite3.connect(GAME.database) as c:
                    name=GAME.Sanitise(drivers[x])
                    if len(c.execute("SELECT Name FROM Drivers WHERE Name=? AND NewTeam!='0'",(name,)).fetchall())>0:
                        team=GAME.Sanitise(c.execute("SELECT NewTeam FROM Drivers WHERE Name=?",(name,)).fetchall()[0])
                        if team=="Retired":
                            c.execute("UPDATE Drivers SET Team='Retired', Role='Retired', Condition='Retired' WHERE Name=?",(name,))
                        else:
                            salary=int(GAME.Sanitise(c.execute("SELECT NewSalary FROM Drivers WHERE Name=?",(name,)).fetchall()[0]))
                            if salary==0:
                                salary=int(GAME.Sanitise(c.execute("SELECT Salary FROM Drivers WHERE Name=?",(name,)).fetchall()[0]))
                            role=GAME.Sanitise(c.execute("SELECT NewRole FROM Drivers WHERE Name=?",(name,)).fetchall()[0])
                            if role=="0":
                                role=GAME.Sanitise(c.execute("SELECT Role FROM Drivers WHERE Name=?",(name,)).fetchall()[0])
                            if role=="Reserve" or role=="Junior" or len(c.execute("SELECT Name FROM Drivers WHERE Name!=? AND Team=? AND ((Role=? AND NewTeam='0' AND ContractEnd>?) OR (NewTeam=? AND NewRole=?))",(name,team,role,GAME.season,team,role,)).fetchall())==0:
                                c.execute("UPDATE Drivers SET Team=?, Role=?, Salary=? WHERE Name=?",(team,role,salary,name,))
                            else:
                                c.execute("UPDATE Drivers SET Team='Free Agent', Role='Free Agent', ContractEnd=0 WHERE Name=?",(name,))
                if int(GAME.Sanitise(c.execute("SELECT Legend FROM Drivers WHERE Name=?",(name,)).fetchall()[0]))==0:
                    GAME.Age(name)
            with sqlite3.connect(GAME.database) as c:
                c.execute("UPDATE Drivers SET NewTeam='0', NewRole='0', NewSalary=0")
                c.execute("UPDATE Drivers SET Team='Retired', Role='Retired', Condition='Retired' WHERE Team='Free Agent' AND Age>39 AND Condition!='Dead' AND Legend=0")

                #Staff
                c.execute("UPDATE Staff SET Team='Free Agent' WHERE NewTeam='0'")
                c.execute("DELETE FROM Staff WHERE NewTeam='Team Principal'")
                staff=c.execute("SELECT Name FROM Staff WHERE NewTeam!='0'").fetchall()
                for x in range(len(staff)):
                    name=GAME.Sanitise(staff[x])
                    team=GAME.Sanitise(c.execute("SELECT NewTeam FROM Staff WHERE Name=?",(name,)).fetchall()[0])
                    salary=int(GAME.Sanitise(c.execute("SELECT NewSalary FROM Staff WHERE Name=?",(name,)).fetchall()[0]))
                    if salary==0:
                        salary=int(GAME.Sanitise(c.execute("SELECT Salary FROM Staff WHERE Name=?",(name,)).fetchall()[0]))
                    role=GAME.Sanitise(c.execute("SELECT NewRole FROM Staff WHERE Name=?",(name,)).fetchall()[0])
                    if role=="0":
                        role=GAME.Sanitise(c.execute("SELECT Role FROM Staff WHERE Name=?",(name,)).fetchall()[0])
                    if len(c.execute("SELECT Name FROM Staff WHERE Name!=? AND NewTeam=? AND NewRole=? AND Team=?",(name,team,role,team,)).fetchall())==0:
                        c.execute("UPDATE Staff SET Team=?, Role=?, Salary=? WHERE Name=?",(team,role,salary,name,))
                    else:
                        c.execute("UPDATE Staff SET Team='Free Agent' WHERE Name=?",(name,))
                c.execute("UPDATE Staff SET NewTeam='0', NewRole='0', NewSalary=0")

            #Teams
            with sqlite3.connect(GAME.database) as c:
                if len(c.execute("SELECT Regulation FROM Regulations WHERE Regulation='Reduced Winner Windtunnel Time' AND True=1").fetchall())>0:
                    team=GAME.Sanitise(c.execute("SELECT Name FROM Teams WHERE PreviousPosition=1").fetchall()[0])
                    research=int(GAME.Sanitise(c.execute("SELECT Research FROM Cars WHERE Team=?",(team,)).fetchall()[0]))
                    if research>1:
                        research=random.randint(round(research*0.4),research)
                        c.execute("UPDATE Cars SET Research=? WHERE Team=?",(research,team,))
                teams=c.execute("SELECT Name FROM Teams").fetchall()
                for x in range(len(teams)):
                    c.execute("UPDATE Teams SET PreviousPosition=? WHERE Position=?",(x+1,x+1,))
                c.execute("UPDATE Teams SET Points=0, PressConferences=0")
                c.execute("UPDATE Drivers SET Points=0, Position=0")
                c.execute("UPDATE Cars SET Car1Engine=1, Car1EngineDurability=100, Car2Engine=1, Car2EngineDurability=100")

                #Engines
                nextEngine=GAME.Sanitise(c.execute("SELECT NextYearEngine FROM Player").fetchall()[0])
                if nextEngine!="0":
                    if nextEngine!="Honda":
                        c.execute("UPDATE Engines SET Manufacturer='None' WHERE Name='Honda' AND Manufacturer=?",(GAME.team,))
                    c.execute("UPDATE Cars SET Engine=? WHERE Team=?",(nextEngine,GAME.team,))
                    c.execute("UPDATE Player SET NextYearEngine=0")
                regulationChange=int(GAME.Sanitise(c.execute("SELECT RegulationChange FROM Player").fetchall()[0]))
                if regulationChange!=GAME.season+1:
                    f=c.execute("SELECT Name FROM Engines").fetchall()
                    for x in range(len(f)):
                        engine=GAME.Sanitise(f[x])
                        if len(c.execute("SELECT Name FROM Engines WHERE Name=? AND Manufacturer!='None'",(engine,)).fetchall())==0 and engine!="Honda":
                            F=c.execute("SELECT Team FROM Cars WHERE Engine=?",(engine,)).fetchall()
                            if len(F)>0:
                                for y in F:
                                    team=GAME.Sanitise(y)
                                    if random.randint(1,2)==1:
                                        e="Mercedes"
                                    else:
                                        e="Ferrari"
                                    c.execute("UPDATE Cars SET Engine=? WHERE Team=?",(e,team,))
                            c.execute("DELETE FROM Engines WHERE Name=?",(engine,))
                        else:
                            power=int(GAME.Sanitise(c.execute("SELECT Power FROM Engines WHERE Name=?",(engine,)).fetchall()[0]))
                            if power<10:
                                power+=1
                            reliability=int(GAME.Sanitise(c.execute("SELECT Reliability FROM Engines WHERE Name=?",(engine,)).fetchall()[0]))
                            if reliability<10:
                                reliability+=1
                            battery=int(GAME.Sanitise(c.execute("SELECT Battery FROM Engines WHERE Name=?",(engine,)).fetchall()[0]))
                            battery+=random.randint(-1,2)
                            if battery<1:
                                battery=1
                            elif battery>10:
                                battery=10
                            c.execute("UPDATE Engines SET Power=?, Reliability=?, Battery=? WHERE Name=?",(power,reliability,battery,engine,))
                #Tyres
                c.execute("UPDATE Player SET TyreWear=?",(random.randint(-1,1),))
        GAME.WinterHiring()
        with sqlite3.connect(GAME.database) as c:
            GAME.race+=1
            c.execute("UPDATE Player SET Race=?",(GAME.race,))
    def Age(self,name):
        with sqlite3.connect(GAME.database) as c:
            age=int(GAME.Sanitise(c.execute("SELECT Age FROM Drivers WHERE Name=?",(name,)).fetchall()[0]))+1
            c.execute("UPDATE Drivers SET Age=? WHERE Name=?",(age,name,))
            developmentRate=int(GAME.Sanitise(c.execute("SELECT DevelopmentRate FROM Drivers WHERE Name=?",(name,)).fetchall()[0]))
            if developmentRate>0:
                developmentRate-=random.randint(1,15)
            elif developmentRate==0:
                if random.randint(1,5)<=2:
                    developmentRate=-1
            else:
                developmentRate-=random.randint(1,6)
            c.execute("UPDATE Drivers SET DevelopmentRate=? WHERE Name=?",(developmentRate,name,))
    def RuleVote(self):
        with sqlite3.connect(GAME.database) as c:
            regulationChange=int(GAME.Sanitise(c.execute("SELECT RegulationChange FROM Player").fetchall()[0]))
            regulations=c.execute('''SELECT Regulation FROM Regulations''').fetchall()
            regulation=GAME.Sanitise(random.choice(regulations))
            state=int(GAME.Sanitise(c.execute('''SELECT True FROM Regulations WHERE Regulation=?''',(regulation,)).fetchall()[0]))
            if regulation=="ERS":
                while True:
                    GAME.proposed=random.randint(0,2)
                    if GAME.proposed!=state:
                        break
            else:
                GAME.proposed=1-state
            if regulation=="Double Points On Last Race":
                if state==0:
                    message="that double points are awarded on the final race to make a more interesting season finale."
                else:
                    message="removing double points from the final race simplify the championship."
            elif regulation=="Team Orders":
                if state==0:
                    message="allowing team orders in order to have more interesting team strategies."
                else:
                    message="banning team orders so that drivers all have a fair chance at the championship."
            elif regulation=="Reduced Winner Windtunnel Time":
                if state==0:
                    message="reducing the windtunnel time of the team that won the previous year's Constructors' Championship."
                else:
                    message="revoking the decision to reduce windtunnel time for 1st place in the Constructors' Championship."
            elif regulation=="Old Points System":
                if state==0:
                    message="bringing back the points system from 2009 and before in order to increase the value of points."
                else:
                    message="bringing back the points system from 2010 onwards in order to make it easier for more teams to score points."
            elif regulation=="ERS":
                if GAME.proposed==1:
                    message="bringing back ERS to make the races more interesting."
                elif GAME.proposed==0:
                    message="getting rid of ERS in order to have more pure racing."
                else:
                    message="bringing back the old ERS system."
            elif regulation=="Fastest Lap Point":
                if state==0:
                    message="bring back the fastest lap point for more interesting race."
                elif state==1:
                    message="removing the fastest lap point for simpler racing."
        GAME.ChangeScreen("Rule Vote")
        canvas.create_text(10, 150, text="The FIA is proposing", fill="#DADADA", font=("Arial", 20), anchor="nw")
        canvas.create_text(10, 180, text=message, fill="#DADADA", font=("Arial", 20), anchor="nw")
        GAME.Button("Vote Against",350,450)
        GAME.Button("Vote For",890,450)
        GAME.vote=0
        GAME.displayed=message
        GAME.regulation=regulation
    def Voted(self):
        GAME.ChangeScreen("Rule Vote")
        GAME.Button("Start Season",1200,600)
        canvas.create_text(10, 150, text="The FIA is proposing", fill="#DADADA", font=("Arial", 20), anchor="nw")
        canvas.create_text(10, 180, text=GAME.displayed, fill="#DADADA", font=("Arial", 20), anchor="nw")
        with sqlite3.connect(GAME.database) as c:
            teams=c.execute('''SELECT Name FROM Teams''').fetchall()
        votes=[]
        votesFor=0
        for x in range(len(teams)):
            team=GAME.Sanitise(teams[x])
            if team==GAME.team:
                if GAME.vote=="For":
                    votes.append(1)
                else:
                    votes.append(0)
            else:
                votes.append(random.randint(0,1))
            if votes[x]==1:
                votesFor+=1
                vote="For"
            else:
                vote="Against"
            if x<round(len(teams)/2):
                canvas.create_text(10, 230+(50*x), text=f"{team}: {vote}", fill="#DADADA", font=("Arial", 30), anchor="nw")
            else:
                canvas.create_text(725, 230+(50*(x-round(len(teams)/2))), text=f"{team}: {vote}", fill="#DADADA", font=("Arial", 30), anchor="nw")
        if votesFor>=len(teams)/2:
            vote="for"
        else:
            vote="against"
        canvas.create_text(10, 650, text=f"The majority voted {vote} the rule change.", fill="#DADADA", font=("Arial", 50), anchor="nw")
        with sqlite3.connect(GAME.database) as c:
            if vote=="for":
                c.execute("UPDATE Regulations SET True=? WHERE Regulation=?",(GAME.proposed,GAME.regulation,))
            GAME.race+=1
            c.execute("UPDATE Player SET Race=?",(GAME.race,))
    def ChangeTeam(self):
        with sqlite3.connect(GAME.database) as c:
            moving=GAME.Sanitise(c.execute("SELECT MovingTo FROM Player").fetchall()[0])
        if moving=="0":
            GAME.done=0
            #Fired?
            GAME.fired=0
            u=0
            d=0
            with sqlite3.connect(GAME.database) as c:
                warnings=int(GAME.Sanitise(c.execute("SELECT Warnings FROM Player").fetchall()[0]))
                position=int(GAME.Sanitise(c.execute("SELECT Position FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0]))
                previousPosition=int(GAME.Sanitise(c.execute("SELECT PreviousPosition FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0]))
                last=len(c.execute("SELECT Name FROM Teams").fetchall())
                if (previousPosition==0 or position<=previousPosition) and position!=last:
                    performance="Happy"
                elif position<=previousPosition+1 and position!=last:
                    performance="Unhappy"
                    u+=1
                else:
                    performance="Disappointed"
                    d+=1
                financial=int(GAME.Sanitise(c.execute("SELECT Financial FROM Player").fetchall()[0]))
                if financial>=4:
                    financial="Happy"
                elif financial>=2:
                    financial="Unhappy"
                    u+=1
                else:
                    financial="Disappointed"
                    financialColour="#FF0000"
                    d+=1
                management=int(GAME.Sanitise(c.execute("SELECT Management FROM Player").fetchall()[0]))
                if management==3:
                    management="Happy"
                elif management==2:
                    management="Unhappy"
                    u+=1
                else:
                    management="Disappointed"
                    d+=1
            if d>=2:
                approval="Lost Confidence"
            elif d==1 and u>=1:
                approval="Disappointed"
            elif d==1 or u>1:
                approval="Unhappy"
            elif u==1:
                approval="Satisfied"
            else:
                approval="Happy"
            if approval=="Lost Confidence":
                GAME.fired=1
            elif approval=="Disappointed" or approval=="Unhappy":
                warnings+=1
                if approval=="Disappointed":
                    warnings+=1
                if warnings>3:
                    GAME.fired=1
                else:
                    with sqlite3.connect(GAME.database) as c:
                        c.execute("UPDATE Player SET Warnings=?",(warnings,))
            if GAME.fired==0:
                with sqlite3.connect(GAME.database) as c:
                    champion=0
                    financial=int(GAME.Sanitise(c.execute("SELECT Financial FROM Player").fetchall()[0]))
                    management=int(GAME.Sanitise(c.execute("SELECT Management FROM Player").fetchall()[0]))
                    if position==1:
                        champion+=1
                    elif len(c.execute("SELECT Team FROM Drivers WHERE Position=1 AND Team=?",(GAME.team,)).fetchall())>0:
                        champion+=1
                    if champion>0:
                        warnings-=champion
                        if warnings<0:
                            warnings=0
                        financial+=round(1.5*champion)
                        if financial>5:
                            financial=5
                        c.execute("UPDATE Player SET Financial=?, Management=3, Warnings=?",(financial,warnings,))
                    else:
                        if financial<5:
                            financial+=1
                        if management<3:
                            management+=1
                        c.execute("UPDATE Player SET Financial=?, Management=?",(financial,management,))
                    regulationChange=int(GAME.Sanitise(c.execute("SELECT RegulationChange FROM Player").fetchall()[0]))
                if regulationChange==GAME.season+1:
                    GAME.done=1
        else:
            #Move Offer Accepted
            GAME.done=1
            with sqlite3.connect(GAME.database) as c:
                c.execute("UPDATE Teams SET TeamPrincipal='None' WHERE Name=?",(GAME.team,))
                GAME.oldTeam=GAME.team
                GAME.team=moving
                c.execute("UPDATE Player SET Team=?, Financial=5, Management=3, Warnings=0",(GAME.team,))
                c.execute("UPDATE Teams SET TeamPrincipal=? WHERE Name=?",(GAME.name,GAME.team,))
                research=int(GAME.Sanitise(c.execute("SELECT Research FROM Cars WHERE Team=?",(GAME.team,)).fetchall()[0]))
                GAME.money=int(GAME.Sanitise(c.execute("SELECT Money FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0]))
                if research>1:
                    research=random.randint(research*5,research*15)
                    c.execute("UPDATE Cars SET Research=? WHERE Team=?",(research,GAME.team,))
                else:
                    GAME.money+=25000000
                    income=int(GAME.Sanitise(c.execute("SELECT Income FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0]))*2
                    c.execute("UPDATE Teams SET Money=?, Income=? WHERE Name=?",(GAME.money,income,GAME.team,))
                c.execute("UPDATE Player SET MovingTo=0")
            GAME.BackgroundColour()
        if GAME.done==0:
            with sqlite3.connect(GAME.database) as c:
                position=int(GAME.Sanitise(c.execute("SELECT Position FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0]))
                teams=c.execute("SELECT Name FROM Teams").fetchall()
            if position==12 and GAME.fired==0:
                GAME.race+=1
                with sqlite3.connect(GAME.database) as c:
                    c.execute("UPDATE Player SET Race=?",(GAME.race,))
                GAME.RaceTime()
            else:
                GAME.screen="Change Team"
                canvas.delete('all')
                root.configure(background='#F2F2F2')
                with sqlite3.connect(GAME.database) as c:
                    f=c.execute('''SELECT Name FROM Teams''').fetchall()
                    canvas.create_text(10, 5, text="Constructors' Standings", fill="black", font=("Arial", 30), anchor="nw")
                    canvas.create_text(10, 500, text=f"Choose Your Team for {GAME.season+1}", fill="black", font=("Arial", 30), anchor="nw")
                    for x in range(len(f)):
                        name=GAME.Sanitise(c.execute('''SELECT Name FROM Teams WHERE Position=?''',(x+1,)).fetchall()[0])
                        if name=="McLaren":
                            name="McLaren Mastercard F1 Team"
                        elif name=="Ferrari":
                            name="Scuderia Ferrari HP"
                        elif name=="Red Bull":
                            name="Oracle Red Bull Racing"
                        elif name=="Mercedes":
                            name="Mercedes-AMG Petronas F1 Team"
                        elif name=="Aston Martin":
                            name="Aston Martin Aramco F1 Team"
                        elif name=="Haas":
                            name="TGR Haas F1 Team"
                        elif name=="Racing Bulls":
                            name="Visa Cash App Racing Bulls"
                        elif name=="Williams":
                            name="Atlassian Williams F1 Team"
                        elif name=="Audi":
                            name="Audi Revolut F1 Team"
                        else:
                            engine=GAME.Sanitise(c.execute('''SELECT Engine FROM Cars WHERE Team=?''',(name,)).fetchall()[0])
                            if engine=="Red Bull":
                                engine="Ford RBPT"
                                if "ford" in name.lower():
                                    engine=""
                                else:
                                    engine="Ford RBPT"
                            if engine in name:
                                engine=""
                            sponsor=GAME.Sanitise(c.execute("SELECT Sponsor FROM Teams WHERE Position=?",(x+1,)).fetchall()[0])
                            if sponsor=="0":
                                sponsor=""
                            elif sponsor=="Visa & Cash App":
                                sponsor="Visa Cash App"
                            if sponsor in name:
                                sponsor=""
                            name=f"{sponsor} {name} {engine}"
                        if x<9:
                            canvas.create_text(50, 100+(x*25), text=f"{x+1}. {name}", fill="black", font=("Arial", 15), anchor="nw")
                        else:
                            canvas.create_text(45, 100+(x*25), text=f"{x+1}. {name}", fill="black", font=("Arial", 15), anchor="nw")
                GAME.options=[]
                if position==12 and GAME.fired==1:
                    position=10
                    i=2
                else:
                    i=len(teams)-position+1
                if len(teams)<12:
                    i+=1
                for x in range(i):
                    if x==0:
                        team=GAME.team
                    else:
                        pos=position+x
                        if pos>len(teams):
                            team="Create New Team"
                        else:
                            with sqlite3.connect(GAME.database) as c:
                                team=GAME.Sanitise(c.execute("SELECT Name FROM Teams WHERE Position=?",(pos,)).fetchall()[0])
                    GAME.options.append(team)
                    if x<6:
                        X=550
                        Y=130*x
                    else:
                        X=1000
                        Y=130*(x-6)
                    if team=="Create New Team":
                        appearance="0"
                    elif team in steam:
                        appearance=team
                    else:
                        with sqlite3.connect(GAME.database) as c:
                            appearance=GAME.Sanitise(c.execute("SELECT Appearance FROM Teams WHERE Name=?",(team,)).fetchall()[0])
                    if appearance!="0":
                        try:
                            GAME.BackgroundColour()
                            if appearance in steam:
                                logo=logos[steam.index(appearance)-1]
                            else:
                                logo=sponsorLogos[sponsors.index(appearance)]
                            canvas.image=logo
                            canvas.create_image(X, Y, anchor=tk.NW, image=logo)
                        except:
                            appearance="0"
                    if appearance=="0":
                        canvas.create_text(X-(len(team)*4)+55, Y+45, text=team, fill="black", font=("Arial", 12), anchor="nw")
                    if x==0:
                        if GAME.fired==0:
                            button="Stay"
                        else:
                            button="Fired"
                    elif team=="Create New Team":
                        button="Create"
                    else:
                        button="Move"
                    GAME.Button(button,X+150,Y+30)
        else:
            GAME.race+=1
            with sqlite3.connect(GAME.database) as c:
                c.execute("UPDATE Player SET Race=?",(GAME.race,))
            GAME.RaceTime()
    def RaceTime(self):
        GAME.legendAvailable=0
        if GAME.race==0:
            #Pre-season
            if GAME.season==2026:
                GAME.done=1
            else:
                GAME.done=0
            GAME.PreSeason()
        elif GAME.race==1:
            GAME.Reserves()
        elif GAME.race<=GAME.races:
            GAME.ActionRound()
        elif GAME.race==GAME.races+1:
            GAME.Championships()
        elif GAME.race==GAME.races+2:
            GAME.RuleVote()
        elif GAME.race==GAME.races+3:
            GAME.Update()
            GAME.RaceTime()
        elif GAME.race==GAME.races+4:
            GAME.ChangeTeam()
        elif GAME.race==GAME.races+5:
            GAME.NewCars()
            GAME.RaceTime()
    def Championships(self):
        GAME.done=0
        GAME.ChangeScreen("Championships")
        with sqlite3.connect(GAME.database) as c:
            driver=GAME.Sanitise(c.execute("SELECT Name FROM Drivers WHERE Position=1").fetchall()[0])
            team=GAME.Sanitise(c.execute("SELECT Team FROM Drivers WHERE Position=1").fetchall()[0])
            constructor=GAME.Sanitise(c.execute("SELECT Name FROM Teams WHERE Position=1").fetchall()[0])
        GAME.DisplayDriver(driver,120,500)
        canvas.create_text(570, 10, text=GAME.season, fill="black", font=("Algerian", 100), anchor="nw")
        canvas.create_text(30, 150, text="Drivers' Champion:", fill="black", font=("Arial", 40), anchor="nw")
        canvas.create_text(30, 200, text=driver, fill="black", font=("Arial", 40), anchor="nw")
        canvas.create_text(820, 150, text="Constructors' Champion:", fill="black", font=("Arial", 40), anchor="nw")
        canvas.create_text(880, 400, text=constructor, fill="black", font=("Arial", 60), anchor="nw")
        if constructor in steam:
            GAME.BackgroundColour()
            appearance=constructor
        else:
            with sqlite3.connect(GAME.database) as c:
                appearance=GAME.Sanitise(c.execute("SELECT Appearance FROM Teams WHERE Name=?",(constructor,)).fetchall()[0])
        if appearance!="0":
            if appearance in steam:
                logo=logos[steam.index(appearance)-1]
            else:
                logo=sponsorLogos[sponsors.index(appearance)]
            canvas.image=logo
            canvas.create_image(980, 500, anchor=tk.NW, image=logo)
        with sqlite3.connect(GAME.database) as c:
            GAME.race+=1
            c.execute("UPDATE Player SET Race=?",(GAME.race,))
            c.execute("INSERT into History (Year, Driver, Constructor) VALUES (?, ?, ?)",(GAME.season,driver,constructor,))
            championships=int(GAME.Sanitise(c.execute("SELECT Championships FROM Drivers WHERE Position=1").fetchall()[0]))+1
            if championships==1:
                canvas.create_text(30, 250, text=f"First World Championship!", fill="black", font=("Arial", 40), anchor="nw")
            else:
                canvas.create_text(30, 250, text=f"{championships} Championships!", fill="black", font=("Arial", 40), anchor="nw")
                if len(c.execute("SELECT Name FROM Drivers WHERE Championships>=?",(championships,)).fetchall())==0:
                    canvas.create_text(30, 300, text="New World Record!", fill="black", font=("Arial", 40), anchor="nw")
            c.execute("UPDATE Drivers SET Championships=? WHERE Position=1",(championships,))
            if team==GAME.team:
                c.execute("UPDATE Player SET Championships=?",(int(GAME.Sanitise(c.execute("SELECT Championships FROM Player").fetchall()[0]))+1,))
            if constructor==GAME.team:
                c.execute("UPDATE Player SET Championships=?",(int(GAME.Sanitise(c.execute("SELECT Championships FROM Player").fetchall()[0]))+1,))
        if GAME.sound==1:
            GAME.Voice(driver,"Champion")
        else:
            root.after(10000, lambda: GAME.Standings(1))
    def DriverCelebration(self,driver):
        path=os.path.join(os.path.dirname(__file__), "Sound Effects", f"{driver} Celebration.wav")
        if os.path.isfile(path):
            winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)
            with contextlib.closing(wave.open(path, 'r')) as f:
                frames=f.getnframes()
                rate=f.getframerate()
                duration=frames/float(rate)
                delay=round(duration*1000)
            root.after(delay, lambda: GAME.Anthem(driver))
        else:
            GAME.Anthem(driver)
    def Anthem(self,driver):
        if GAME.replay==9:
            if driver=="Lewis Hamilton":
                country="United Kingdom"
            else:
                country="Netherlands"
        else:
            with sqlite3.connect(GAME.database) as c:
                country=GAME.Sanitise(c.execute("SELECT Country FROM Teams WHERE Position=1").fetchall()[0])
        path=os.path.join(os.path.dirname(__file__), "Music", f"{country} National Anthem.wav")
        if os.path.isfile(path):
            winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)
        if GAME.replay==0:
            root.after(10000, lambda: GAME.Standings(1))
    def ChangeScreen(self,screen):
        GAME.screen=screen
        canvas.delete('all')
        if screen=="Title Screen":
            GAME.team=0
            GAME.BackgroundColour()
        elif screen=="Tyre Data" or screen=="Replacing" or screen=="Replacement" or screen=="Sponsor Negotiation" or screen=="Replay Grid":
            screen="Grey Screen"
        elif screen=="Data" or screen=="Scouting":
            screen="Board Room"
        elif screen=="View Contracts" or screen=="Junior & Reserve Drivers" or screen=="Staff List" or screen=="Starter Drivers" or screen=="Rookies" or screen=="Reserve Options":
            screen="Driver List"
        elif screen=="Choose Experienced Driver" or screen=="Choose Rookie" or screen=="Choose Renewal":
            screen="Contract Name"
        elif screen=="New Tyres":
            screen="Choose Tyres"
        elif screen=="calendar":
            screen="Calendar"
        elif screen=="Upgrade":
            if f"{GAME.team} Upgrade" in Images:
                screen=f"{GAME.team} Upgrade"
        elif screen=="Car Data" or screen=="Team Data" or screen=="Achievements" or screen=="Team Management":
            screen="Data Background"
        elif screen not in Images:
            screen="Blank Screen"
        imageOnCanvas = canvas.create_image(0, 0, anchor=tk.NW, image=images[Images.index(screen)])
    def Settings(self):
        GAME.ChangeScreen("Settings")
        GAME.Button("Back",5,730)
        canvas.create_text(10, 5, text="Settings", fill="black", font=("Arial", 50), anchor="nw")
        canvas.create_text(10, 200, text="Sound", fill="black", font=("Arial", 30), anchor="nw")
        image=icons[GAME.sound+8]
        canvas.image=image
        canvas.create_image(150, 200, anchor=tk.NW, image=image)
        canvas.create_text(10, 400, text="Music", fill="black", font=("Arial", 30), anchor="nw")
        image=icons[GAME.music+8]
        canvas.image=image
        canvas.create_image(150, 400, anchor=tk.NW, image=image)
    def ReplayScreen(self):
        GAME.screen="Replay screen"
    def OnClick(self, event):
        if GAME.screen=="Title Screen":
            GAME.replay=0
            GAME.screen="Opening Menu"
            GAME.Button("New Game",500,575)
            GAME.Button("Load Game",735,575)
            GAME.Button("Play Legends",500,645)
            GAME.Button("Replay",735, 645)
            image=icons[7]
            canvas.image=image
            canvas.create_image(1295, 710, anchor=tk.NW, image=image)
            GAME.database="F1 Manager 26 Save Data 1.db"
        elif GAME.screen=="Opening Menu":
            if event.x>=500 and event.x<=700 and event.y>=575 and event.y<=625:
                GAME.database=1
                GAME.StartNewGame()
            elif event.x>=735 and event.x<=935 and event.y>=575 and event.y<=625 and GAME.newGame==0:
                GAME.SelectSave()
            elif event.x>=500 and event.x<=700 and event.y>=645 and event.y<=695:
                GAME.legends=1
                GAME.StartNewGame()
            elif event.x>=735 and event.x<=935 and event.y>=645 and event.y<=695:
                GAME.ChangeScreen("Replay Screen")
                GAME.Button("Canada 2011",320,270)
                GAME.Button("Brazil 2008",320,395)
                GAME.Button("Spa 2000",320,520)
                GAME.Button("Monaco 1984",320,645)
                GAME.Button("Back",5,730)
                root.after(400, lambda: GAME.ReplayScreen())
            elif event.x>=1295 and event.x<=1345 and event.y>=710 and event.y<=760:
                GAME.Settings()
        elif GAME.screen=="Welcome screen":
            if event.x>=54 and event.x<=250 and event.y>=718 and event.y<=765:
                GAME.ChangeScreen("Get Name")
                GAME.name=GAME.Sanitise(simpledialog.askstring(" ", "Limit: 20 characters"))
                valid=GAME.Validate(GAME.name)
                if valid==1:
                    GAME.ChangeScreen("Get Country 1")
        elif GAME.screen=="Get Country 1":
            change=0
            if event.x>=25 and event.x<=354 and event.y>=293 and event.y<=458:
                GAME.country="United Kingdom"
            elif event.x>=446 and event.x<=695 and event.y>=294 and event.y<=460:
                GAME.country="France"
            elif event.x>=751 and event.x<=1001 and event.y>=297 and event.y<=462:
                GAME.country="Germany"
            elif event.x>=1096 and event.x<=1344 and event.y>=297 and event.y<=461:
                GAME.country="Spain"
            elif event.x>=25 and event.x<=352 and event.y>=510 and event.y<=682:
                GAME.country="United States of America"
            elif event.x>=392 and event.x<=737 and event.y>=514 and event.y<=683:
                GAME.country="Canada"
            elif event.x>=757 and event.x<=998 and event.y>=514 and event.y<=683:
                GAME.country="Brazil"
            elif event.x>=1053 and event.x<=1402 and event.y>=513 and event.y<=686:
                GAME.country="Australia"
            elif event.x>=1206 and event.x<=1402 and event.y>=725 and event.y<=771:
                #Button
                change=1
                GAME.ChangeScreen("Get Country 2")
            if change==0 and GAME.country!="":
                GAME.ChangeScreen("Choose a Team")
        elif GAME.screen=="Get Country 2":
            change=0
            if event.x>=77 and event.x<=332 and event.y>=292 and event.y<=457:
                GAME.country="Italy"
            elif event.x>=485 and event.x<=652 and event.y>=291 and event.y<=458:
                GAME.country="Vatican City"
            elif event.x>=747 and event.x<=1006 and event.y>=295 and event.y<=467:
                GAME.country="Japan"
            elif event.x>=1093 and event.x<=1355 and event.y>=298 and event.y<=469:
                GAME.country="Austria"
            elif event.x>=77 and event.x<=336 and event.y>=509 and event.y<=682:
                GAME.country="China"
            elif event.x>=444 and event.x<=699 and event.y>=514 and event.y<=683:
                GAME.country="India"
            elif event.x>=748 and event.x<=1005 and event.y>=512 and event.y<=681:
                GAME.country="South Africa"
            elif event.x>=1119 and event.x<=1341 and event.y>=512 and event.y<=687:
                GAME.country="Monaco"
            elif event.x>=1206 and event.x<=1402 and event.y>=725 and event.y<=771:
                #Button
                change=1
                GAME.ChangeScreen("Get Country 1")
            if change==0 and GAME.country!="":
                GAME.ChangeScreen("Choose a Team")
        elif GAME.screen=="Choose a Team":
            if event.x>=100 and event.x<=400 and event.y>=160 and event.y<=320:
                GAME.team="McLaren"
            elif event.x>=650 and event.x<=800 and event.y>=155 and event.y<=320:
                GAME.team="Mercedes"
            elif event.x>=1020 and event.x<=1385 and event.y>=170 and event.y<=300:
                GAME.team="Red Bull"
            elif event.x>=80 and event.x<=420 and event.y>=320 and event.y<=480:
                GAME.team="Ferrari"
            elif event.x>=490 and event.x<=955 and event.y>=390 and event.y<=445:
                GAME.team="Williams"
            elif event.x>=1045 and event.x<=1415 and event.y>=335 and event.y<=480:
                GAME.team="Racing Bulls"
            elif event.x>=10 and event.x<=510 and event.y>=495 and event.y<=620:
                GAME.team="Aston Martin"
            elif event.x>=635 and event.x<=795 and event.y>=470 and event.y<=620:
                GAME.team="Haas"
            elif event.x>=1155 and event.x<=1285 and event.y>=480 and event.y<=610:
                GAME.team="Audi"
            elif event.x>=75 and event.x<=395 and event.y>=615 and event.y<=775:
                GAME.team="Alpine"
            elif event.x>=595 and event.x<=850 and event.y>=625 and event.y<=770:
                GAME.team="Cadillac"
            elif event.x>=1000 and event.x<=1410 and event.y>=630 and event.y<=760:
                #Create a team
                GAME.team="Create"
            if GAME.team=="Create":
                GAME.CreateTeam()
            elif GAME.team!="":
                GAME.newTeam=0
                GAME.BackgroundColour()
                if os.path.isfile("F1 Manager 26 Driver Data.json") and os.path.isfile(GAME.database):
                    GAME.FillDatabase()
                    F1=sqlite3.connect(GAME.database)
                    c=F1.cursor()
                    c.execute("UPDATE Teams SET TeamPrincipal=? WHERE Name=?",(GAME.name,GAME.team,))
                    c.execute('''SELECT Name FROM Drivers WHERE Team=? AND Role="1"''',(GAME.team,))
                    GAME.car1=GAME.Sanitise(c.fetchall()[0])
                    c.execute('''SELECT Name FROM Drivers WHERE Team=? AND Role="2"''',(GAME.team,))
                    GAME.car2=GAME.Sanitise(c.fetchall()[0])
                    F1.commit()
                    F1.close()
                    GAME.WelcomeToTeam()
                else:
                    GAME.ChangeScreen("Missing Required Files")
        elif GAME.screen=="Choose Engine 1":
            if event.y>=190 and event.y<=615:
                if event.x>=30 and event.x<=465:
                    GAME.engine="Mercedes"
                elif event.x>=490 and event.x<=945:
                    GAME.engine="Ferrari"
                elif event.x>=970 and event.x<=1400:
                    GAME.engine="Audi"
            if GAME.engine!="":
                if GAME.season==2026:
                    with sqlite3.connect(GAME.database) as F1:
                        F1.execute("UPDATE Cars SET Engine=? WHERE Team=?",(GAME.engine,GAME.team,))
                    GAME.ChangeScreen("Choose Sponsor")
                else:
                    GAME.CreateNewTeam()
        elif GAME.screen=="Choose Sponsor":
            if event.x>=67 and event.x<=643 and event.y>=211 and event.y<=382:
                GAME.sponsor="Tesco"
            elif event.x>=768 and event.x<=1419 and event.y>=169 and event.y<=429:
                GAME.sponsor="Games Workshop"
            elif event.x>=429 and event.x<=1028 and event.y>=490 and event.y<=662:
                GAME.sponsor="Opera GX"
            if GAME.sponsor!="":
                GAME.TeamData()
        elif GAME.screen=="Welcome To Team":
            if event.x>=1237 and event.x<=1436 and event.y>=721 and event.y<=769:
                if GAME.season==2026:
                    GAME.race=0
                    with sqlite3.connect(GAME.database) as F1:
                        F1.execute("UPDATE Player SET Race=0")
                else:
                    GAME.oldTeam=0
                GAME.RaceTime()
        elif GAME.screen=="Pre-Season Testing":
            if event.x>=1200 and event.x<=1400 and event.y>=700 and event.y<=750:
                GAME.Calendar()
        elif GAME.screen=="calendar":
            if event.x>=1200 and event.x<=1400 and event.y>=700 and event.y<=750:
                GAME.race=1
                with sqlite3.connect(GAME.database) as F1:
                    F1.execute("UPDATE Player SET Race=1")
                GAME.Income()
                GAME.SaveScreen()
        elif GAME.screen=="Save Screen":
            if event.y>=630 and event.y<=720:
                if event.x>=370 and event.x<=705:
                    #Next
                    GAME.RaceTime()
                elif event.x>=730 and event.x<=1070:
                    #Quit
                    if GAME.music==1:
                        sound_path = os.path.join(os.path.dirname(__file__), "Music", "F1 Music.wav")
                        if os.path.isfile(sound_path):
                            winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
                    GAME.ChangeScreen("Title Screen")
        elif GAME.screen=="Practice":
            if event.x>=1200 and event.x<=1400 and event.y>=700 and event.y<=750 and GAME.qualifying==0:
                GAME.qualifying=1
                root.after(1200, lambda: GAME.Qualifying())
                if GAME.music==1:     
                    sound_path = os.path.join(os.path.dirname(__file__), "Music", "The Chain F1.wav")
                    if os.path.isfile(sound_path):
                        winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
        elif GAME.screen=="Q3 Results":
            if event.x>=1235 and event.x<=1435 and event.y>=735 and event.y<=785 and GAME.qualifying==2:
                if GAME.replay>0:
                    GAME.driver=1
                    GAME.ChooseStartingTyres()
                else:
                    GAME.GridPenalties()
        elif GAME.screen=="Choose Tyres":
            tyre=0
            if GAME.driver1 in GAME.drivers:
                GAME.car1ID=GAME.drivers.index(GAME.driver1)
            else:
                GAME.car1ID=-1
            if GAME.driver2 in GAME.drivers:
                GAME.car2ID=GAME.drivers.index(GAME.driver2)
            else:
                GAME.car2ID=-1
            if event.x>=5 and event.x<=220 and event.y>=110 and event.y<=320:
                tyre="Soft"
            elif event.x>=5 and event.x<=220 and event.y>=330 and event.y<=540:
                tyre="Medium"
            elif event.x>=5 and event.x<=220 and event.y>=545 and event.y<=780:
                tyre="Hard"
            elif event.x>=945 and event.x<=1160 and event.y>=280 and event.y<=505:
                tyre="Intermediate"
            elif event.x>=945 and event.x<=1160 and event.y>=535 and event.y<=760:
                tyre="Wet"
            if tyre!=0:
                if GAME.driver==1 and GAME.car1ID in GAME.positions:
                    index=GAME.car1ID
                else:
                    index=GAME.car2ID
                GAME.tyre.pop(index)
                GAME.tyre.insert(index,tyre)
                if GAME.driver==1 and GAME.driver2 in GAME.drivers:
                    GAME.driver=2
                    GAME.ChooseStartingTyres()
                else:
                    GAME.aggressions=[3,2,2]
                    GAME.driver=1
                    GAME.ChooseStartingAggression()
        elif GAME.screen=="Choose Aggression":
            modify=0
            attribute=-1
            if event.x>=215 and event.x<=235:
                modify=-1
            elif event.x>=485 and event.x<=505:
                modify=1
            if event.y>=125 and event.y<=175:
                attribute=0
            elif event.y>=385 and event.y<=435:
                attribute=1
            elif event.y>=645 and event.y<=695:
                attribute=2
            if modify!=0 and attribute!=-1:
                aggression=GAME.aggressions[attribute]
                aggression+=modify
                if aggression<1:
                    aggression=1
                elif attribute>0 and aggression>3:
                    aggression=3
                elif aggression>5:
                    aggression=5
                GAME.aggressions.pop(attribute)
                GAME.aggressions.insert(attribute,aggression)
                GAME.ChooseStartingAggression()
            elif event.x>=510 and event.x<=710 and event.y>=730 and event.y<=780:
                if GAME.driver==1 and GAME.car1ID in GAME.positions:
                    index=GAME.car1ID
                else:
                    index=GAME.car2ID
                GAME.tyreAggression.pop(index)
                GAME.tyreAggression.insert(index,GAME.aggressions[0])
                GAME.fuelAggression.pop(index)
                GAME.fuelAggression.insert(index,GAME.aggressions[1])
                GAME.ERSdeployment.pop(index)
                GAME.ERSdeployment.insert(index,GAME.aggressions[2])
                if GAME.driver==1 and GAME.driver2 in GAME.drivers:
                    GAME.driver=2
                    GAME.ChooseStartingAggression()
                else:
                    GAME.StartRace()
        elif GAME.screen=="Race Screen":
            if GAME.car1ID in GAME.positions:
                #Driver 1
                if event.x>=5 and event.x<=30:
                    #Down
                    if event.y>=585 and event.y<=650:
                        #Tyre Aggression
                        aggression=GAME.tyreAggression[GAME.car1ID]-1
                        if aggression>=1:
                            GAME.tyreAggression.pop(GAME.car1ID)
                            GAME.tyreAggression.insert(GAME.car1ID,aggression)
                            GAME.RefreshScreen()
                    elif event.y>=650 and event.y<=710:
                        #Fuel Aggression
                        aggression=GAME.fuelAggression[GAME.car1ID]-1
                        if aggression>=1:
                            GAME.fuelAggression.pop(GAME.car1ID)
                            GAME.fuelAggression.insert(GAME.car1ID,aggression)
                            GAME.RefreshScreen()
                    elif event.y>=711:
                        #ERS Deployment
                        deployment=GAME.ERSdeployment[GAME.car1ID]-1
                        if deployment>=1:
                            GAME.ERSdeployment.pop(GAME.car1ID)
                            GAME.ERSdeployment.insert(GAME.car1ID,deployment)
                            GAME.RefreshScreen()
                elif event.x>=275 and event.x<=300:
                    #Up
                    if event.y>=585 and event.y<=650:
                        #Tyre Aggression
                        aggression=GAME.tyreAggression[GAME.car1ID]+1
                        if aggression<=5:
                            GAME.tyreAggression.pop(GAME.car1ID)
                            GAME.tyreAggression.insert(GAME.car1ID,aggression)
                            GAME.RefreshScreen()
                    elif event.y>=650 and event.y<=710:
                        #Fuel Aggression
                        aggression=GAME.fuelAggression[GAME.car1ID]+1
                        if aggression<=3:
                            GAME.fuelAggression.pop(GAME.car1ID)
                            GAME.fuelAggression.insert(GAME.car1ID,aggression)
                            GAME.RefreshScreen()
                    elif event.y>=711:
                        #ERS Deployment
                        deployment=GAME.ERSdeployment[GAME.car1ID]+1
                        if deployment==4 and (GAME.positions.index(GAME.car1ID)==0 or GAME.ERS[GAME.car1ID]<50 or GAME.time[GAME.car1ID]>=1 or GAME.lap[GAME.car1ID]==GAME.startLap or GAME.ers==2 or GAME.water>=1):
                            deployment=3
                        if deployment<=4:
                            GAME.ERSdeployment.pop(GAME.car1ID)
                            GAME.ERSdeployment.insert(GAME.car1ID,deployment)
                            GAME.RefreshScreen()
            if GAME.car2ID in GAME.positions:
                #Driver 2
                if event.x>=1135 and event.x<=1160:
                    #Down
                    if event.y>=585 and event.y<=650:
                        #Tyre Aggression
                        aggression=GAME.tyreAggression[GAME.car2ID]-1
                        if aggression>=1:
                            GAME.tyreAggression.pop(GAME.car2ID)
                            GAME.tyreAggression.insert(GAME.car2ID,aggression)
                            GAME.RefreshScreen()
                    elif event.y>=650 and event.y<=710:
                        #Fuel Aggression
                        aggression=GAME.fuelAggression[GAME.car2ID]-1
                        if aggression>=1:
                            GAME.fuelAggression.pop(GAME.car2ID)
                            GAME.fuelAggression.insert(GAME.car2ID,aggression)
                            GAME.RefreshScreen()
                    elif event.y>=711:
                        #ERS Deployment
                        deployment=GAME.ERSdeployment[GAME.car2ID]-1
                        if deployment>=1:
                            GAME.ERSdeployment.pop(GAME.car2ID)
                            GAME.ERSdeployment.insert(GAME.car2ID,deployment)
                            GAME.RefreshScreen()
                elif event.x>=1410 and event.x<=1435:
                    #Up
                    if event.y>=585 and event.y<=650:
                        #Tyre Aggression
                        aggression=GAME.tyreAggression[GAME.car2ID]+1
                        if aggression<=5:
                            GAME.tyreAggression.pop(GAME.car2ID)
                            GAME.tyreAggression.insert(GAME.car2ID,aggression)
                            GAME.RefreshScreen()
                    elif event.y>=650 and event.y<=710:
                        #Fuel Aggression
                        aggression=GAME.fuelAggression[GAME.car2ID]+1
                        if aggression<=3:
                            GAME.fuelAggression.pop(GAME.car2ID)
                            GAME.fuelAggression.insert(GAME.car2ID,aggression)
                            GAME.RefreshScreen()
                    elif event.y>=711:
                        #ERS Deployment
                        deployment=GAME.ERSdeployment[GAME.car2ID]+1
                        if deployment==4 and (GAME.positions.index(GAME.car2ID)==0 or GAME.ERS[GAME.car2ID]<50 or GAME.time[GAME.car2ID]>=1 or GAME.lap[GAME.car2ID]==GAME.startLap or GAME.ers==2 or GAME.water>=1):
                            deployment=3
                        if deployment<=4:
                            GAME.ERSdeployment.pop(GAME.car2ID)
                            GAME.ERSdeployment.insert(GAME.car2ID,deployment)
                            GAME.RefreshScreen()
            if event.x>=670 and event.x<=715 and event.y>=630 and event.y<=675:
                #Pause/Play
                if GAME.pause==1:
                    GAME.pause=0
                elif GAME.pause==0:
                    GAME.pause=1
                GAME.RefreshScreen()
            elif event.x>=670 and event.x<=715 and event.y>=685 and event.y<=730:
                #Helmet Button
                GAME.pause=2
        elif GAME.screen=="Instructions":
            instruction=0
            driver=0
            if event.x>=5 and event.x<=205 and GAME.car1ID in GAME.positions:
                #Driver 1
                driver=1
                if event.y>=550 and event.y<=600:
                    instruction="Box"
                elif event.y>=610 and event.y<=660 and GAME.teamOrders==1:
                    instruction="Team Orders"
                elif event.y>=670 and event.y<=720:
                    instruction="Drive in Clean Air"
                elif event.y>=730 and event.y<=780:
                    instruction="Maintain Position"
            elif event.x>=1230 and event.x<=1430 and GAME.car2ID in GAME.positions:
                #Driver 2
                driver=2
                if event.y>=550 and event.y<=600:
                    instruction="Box"
                elif event.y>=610 and event.y<=660 and GAME.teamOrders==1:
                    instruction="Team Orders"
                elif event.y>=670 and event.y<=720:
                    instruction="Drive in Clean Air"
                elif event.y>=730 and event.y<=780:
                    instruction="Maintain Position"
            if instruction!=0:
                if instruction=="Box":
                    if GAME.replay==5:
                        if event.x<=105:
                            tyre="Soft"
                        elif event.x<=205:
                            tyre="Hard"
                        elif event.x<=1330:
                            tyre="Soft"
                        else:
                            tyre="Hard"
                    elif GAME.replay==6:
                        tyre="Wet"
                    else:
                        tyre=0
                    GAME.Box(driver,tyre)
                else:
                    if driver==1:
                        if instruction in GAME.car1Instructions:
                            GAME.car1Instructions.remove(instruction)
                        else:
                            GAME.car1Instructions.append(instruction)
                    else:
                        if instruction in GAME.car2Instructions:
                            GAME.car2Instructions.remove(instruction)
                        else:
                            GAME.car2Instructions.append(instruction)
                    GAME.Instructions()
            elif event.x>=5 and event.x<=205 and event.y>=30 and event.y<=80:
                #Back
                GAME.pause=1
                GAME.RefreshScreen()
                GAME.NextMove()
            elif event.x>=1230 and event.x<=1430 and event.y>=30 and event.y<=80:
                #Tyre Data
                GAME.TyreData()
        elif GAME.screen=="Box":
            if event.y>=200 and event.y<=630:
                tyre=0
                if event.x>=20 and event.x<=300:
                    tyre="Soft"
                elif event.x>=320 and event.x<=580:
                    tyre="Medium"
                elif event.x>=600 and event.x<=860:
                    tyre="Hard"
                elif event.x>=880 and event.x<=1140:
                    tyre="Intermediate"
                elif event.x>=1160 and event.x<=1400:
                    tyre="Wet"
                if tyre!=0:
                    if GAME.pittingDriver==1:
                        index=GAME.car1ID
                    else:
                        index=GAME.car2ID
                    GAME.pitLap.pop(index)
                    GAME.pitLap.insert(index,GAME.lap[index])
                    GAME.pitTyre.pop(index)
                    GAME.pitTyre.insert(index,tyre)
                    GAME.pause=1
                    GAME.RefreshScreen()
                    GAME.NextMove()
            elif event.x>=5 and event.x<=205 and event.y>=730 and event.y<=780:
                #Back
                GAME.Instructions()
        elif GAME.screen=="Tyre Data":
            if event.x>=5 and event.x<=205 and event.y>=730 and event.y<=780:
                GAME.Instructions()
        elif GAME.screen=="Podium":
            if event.x>=1230 and event.x<=1430 and event.y>=5 and event.y<=55:
                GAME.RaceResults()
        elif GAME.screen=="Race Results":
            if event.x>=1230 and event.x<=1430 and event.y>=5 and event.y<=55:
                GAME.SaveRace()
        elif GAME.screen=="Board Room":
            if event.x>=400 and event.x<=600 and event.y>=510 and event.y<=560:
                #Standings
                GAME.Standings(0)
            elif event.x>=950 and event.x<=1150 and event.y>=650 and event.y<=700:
                #Data
                GAME.ChangeScreen("Data")
                GAME.Button("Team Data",400,510)
                GAME.Button("Car Data",350,580)
                GAME.Button("Team Management",300,650)
                GAME.Button("Calendar",820,510)
                GAME.Button("Achievements",870,580)
                GAME.Button("History",920,650)
                GAME.Button("Back",5,730)
                GAME.DisplayMoney()
                GAME.BoardRoomLogo()
            elif event.x>=820 and event.x<=1020 and event.y>=510 and event.y<=560 and GAME.action==0 and GAME.money>0:
                #Upgrade
                GAME.maximumUpgradePoints=round(GAME.money/1500000)
                if GAME.maximumUpgradePoints>10:
                    GAME.maximumUpgradePoints=10
                if GAME.maximumUpgradePoints==10:
                    if GAME.races<20:
                        GAME.maximumPoints=12
                    elif GAME.races<23:
                        GAME.maximumPoints=11
                    reduced=0
                    with sqlite3.connect(GAME.database) as c:
                        if len(c.execute("SELECT Name FROM Teams WHERE Name=? AND PreviousPosition=1",(GAME.team,)).fetchall())>0:
                            if len(c.execute("SELECT Regulation FROM Regulations WHERE Regulation='Reduced Winner Windtunnel Time' AND True=1").fetchall())>0:
                                GAME.maximumUpgradePoints-=2
                                reduced=1
                                if GAME.maximumUpgradePoints<1:
                                    GAME.maximumUpgradePoints=1
                    if GAME.money>=55000000:
                        extra=(GAME.money-50000000)//5000000
                        if reduced==1:
                            extra=round(extra/1.5)
                        GAME.maximumUpgradePoints+=extra
                    rating=int(GAME.Sanitise(c.execute("SELECT Rating FROM Staff WHERE Team=? AND Role='Technical Director'",(GAME.team,)).fetchall()[0]))
                    if rating>90:
                        extra=rating-90
                        if reduced==1:
                            extra=round(extra/1.5)
                        GAME.maximumUpgradePoints+=extra
                if GAME.maximumUpgradePoints>(round(GAME.money/3))//500000:
                    GAME.maximumUpgradePoints=(round(GAME.money/3))//500000
                GAME.remainingUpgradePoints=GAME.maximumUpgradePoints
                GAME.upgradePoints=[]
                for x in range(7):
                    GAME.upgradePoints.append(0)
                GAME.UpgradePage()
            elif event.x>=350 and event.x<=550 and event.y>=580 and event.y<=630:
                if GAME.action==0:
                    #Scouting
                    GAME.ChangeScreen("Scouting")
                    GAME.Button("View Contracts",400,510)
                    GAME.Button("Scout Drivers",350,580)
                    GAME.Button("Scout Technical Directors",820,510)
                    GAME.Button("Scout Sporting Directors",870,580)
                    GAME.Button("Scout Race Engineers",920,650)
                    with sqlite3.connect(GAME.database) as c:
                        unableToRace=len(c.execute("SELECT Name FROM Drivers WHERE Team=? AND Condition!='Well'",(GAME.team,)).fetchall())
                        if unableToRace>0 and len(c.execute("SELECT Name FROM Drivers WHERE Team=? AND Role='Reserve'",(GAME.team,)).fetchall())<unableToRace:
                            GAME.Button("Hire Reserve",300,650)
                    GAME.Button("Back",5,730)
                    GAME.DisplayMoney()
                    GAME.BoardRoomLogo()
                else:
                    GAME.ViewContracts()
            elif event.x>=870 and event.x<=1070 and event.y>=580 and event.y<=630:
                #Research
                with sqlite3.connect(GAME.database) as c:
                    if int(GAME.Sanitise(c.execute("SELECT RegulationChange FROM Player").fetchall()[0]))==GAME.season+1:
                        nextEngine=GAME.Sanitise(c.execute("SELECT NextYearEngine FROM Player").fetchall()[0])
                        manufacturedEngine=c.execute("SELECT Name FROM Engines WHERE Manufacturer=?",(GAME.team,)).fetchall()
                        if len(manufacturedEngine)==0:
                            manufacturedEngine=0
                        else:
                            manufacturedEngine=GAME.Sanitise(manufacturedEngine[0])
                        if (manufacturedEngine!=0 and(nextEngine=="0" or nextEngine==manufacturedEngine)) or nextEngine=="Honda":
                            if GAME.action==0:
                                GAME.ChangeScreen("Select Research Type")
                                GAME.Button("Aerodynamic Regulations",350,450)
                                GAME.Button("Engine Regulations",890,450)
                                GAME.Button("Back",5,730)
                                GAME.DisplayMoney()
                            else:
                                GAME.ResearchEngine()
                        else:
                            if GAME.action==0:
                                GAME.AerodynamicResearch()
            elif event.x>=620 and event.x<=820 and event.y>=412 and event.y<=462:
                #Next Race
                GAME.Reserves()
            elif event.x>=300 and event.x<=500 and event.y>=650 and event.y<=700:
                if GAME.swappable==1:
                    #Swap Drivers
                    GAME.options=[GAME.car1,GAME.car2]
                    GAME.displayedName=0
                    GAME.SelectDriverToReplace()
                else:
                    #Hire Reserve
                    with sqlite3.connect(GAME.database) as c:
                        unableToRace=len(c.execute("SELECT Name FROM Drivers WHERE Team=? AND Condition!='Well'",(GAME.team,)).fetchall())
                        if GAME.team=="Racing Bulls" and len(c.execute("SELECT Name FROM Teams WHERE Name='Red Bull'").fetchall())>0:
                            team="Red Bull"
                        else:
                            team=GAME.team
                        reserves=len(c.execute("SELECT Name FROM Drivers WHERE Team=? AND Role='Reserve'",(team,)).fetchall())
                    if unableToRace>0 and reserves<unableToRace:
                        GAME.HireReserve()
            elif event.x>=5 and event.x<=205 and event.y>=730 and event.y<=780:
                #Quit
                GAME.ChangeScreen("Title Screen")
                if GAME.music==1:
                    SoundPath = os.path.join(os.path.dirname(__file__), "Music", "F1 Music.wav")
                    if os.path.isfile(SoundPath):
                        winsound.PlaySound(SoundPath, winsound.SND_FILENAME | winsound.SND_ASYNC)
        elif (GAME.screen=="Standings" or GAME.screen=="Data" or GAME.screen=="Team Data" or GAME.screen=="Car Data" or GAME.screen=="Achievements"
              or GAME.screen=="History" or GAME.screen=="Upgrade" or GAME.screen=="Select Research Type" or GAME.screen=="Scouting"
              or GAME.screen=="View Contracts" or GAME.screen=="Junior & Reserve Drivers" or GAME.screen=="Driver List" or GAME.screen=="Staff List" or GAME.screen=="Contract Name"
              or GAME.screen=="Contract" or GAME.screen=="Replacing" or GAME.screen=="Replacement" or GAME.screen=="Renewal" or GAME.screen=="Team Management"
              or GAME.screen=="Reserve Options") and event.x>=5 and event.x<=205 and event.y>=730 and event.y<=780:
            GAME.Menu()
        elif GAME.screen=="Data":
            if event.x>=400 and event.x<=600 and event.y>=510 and event.y<=560:
                #Team Data
                GAME.ChangeScreen("Team Data")
                GAME.DisplayLogo()
                with sqlite3.connect(GAME.database) as c:
                    country=GAME.Sanitise(c.execute("SELECT Country FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0])
                    position=int(GAME.Sanitise(c.execute("SELECT Position FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0]))
                    if position==1 or position==21:
                        suffix1="st"
                    elif position==2 or position==22:
                        suffix1="nd"
                    elif position==3 or position==23:
                        suffix1="rd"
                    else:
                        suffix1="th"
                    previousPosition=int(GAME.Sanitise(c.execute("SELECT PreviousPosition FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0]))
                    if previousPosition==1 or previousPosition==21:
                        suffix2="st"
                    elif previousPosition==2 or previousPosition==22:
                        suffix2="nd"
                    elif previousPosition==3 or previousPosition==23:
                        suffix2="rd"
                    else:
                        suffix2="th"
                    sponsor=GAME.Sanitise(c.execute("SELECT Sponsor FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0])
                    if sponsor=="0":
                        sponsor="None"
                    else:
                        logo=sponsorLogos[sponsors.index(sponsor)]
                        canvas.image=logo
                        canvas.create_image(380+(len(sponsor)*30), 420, anchor=tk.NW, image=logo)
                    reputation=GAME.Sanitise(c.execute("SELECT Reputation FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0])
                    regulationChange=int(GAME.Sanitise(c.execute("SELECT RegulationChange FROM Player").fetchall()))
                canvas.create_text(40, 10, text=GAME.team, fill="white", font=("Arial", 100), anchor="nw")
                canvas.create_text(40, 200, text=f"Team Principal: {GAME.name}", fill="white", font=("Arial", 40), anchor="nw")
                canvas.create_text(40, 280, text=f"Home Country: {country}", fill="white", font=("Arial", 40), anchor="nw")
                canvas.create_text(40, 360, text=f"Position: {position}{suffix1}", fill="white", font=("Arial", 40), anchor="nw")
                if previousPosition!=0:
                    canvas.create_text(880, 360, text=f"{GAME.season-1} Position: {previousPosition}{suffix2}", fill="white", font=("Arial", 40), anchor="nw")
                canvas.create_text(40, 440, text=f"Title Sponsor: {sponsor}", fill="white", font=("Arial", 40), anchor="nw")
                canvas.create_text(1000, 440, text=f"Reputation: {reputation}", fill="white", font=("Arial", 40), anchor="nw")
                canvas.create_text(40, 520, text=f"Year: {GAME.season}", fill="white", font=("Arial", 40), anchor="nw")
                canvas.create_text(40, 600, text=f"Next Regulation Cycle: {regulationChange}", fill="white", font=("Arial", 40), anchor="nw")
                GAME.DisplayMoney()
                GAME.Button("Back",5,730)
            elif event.x>=350 and event.x<=550 and event.y>=580 and event.y<=630:
                #Car Data
                GAME.CarData()
            elif event.x>=820 and event.x<=1020 and event.y>=510 and event.y<=560:
                #Calendar
                GAME.ChangeScreen("Calendar")
                canvas.create_text(570, 10, text=f"{GAME.season} Season", fill="#F5C939", font=("Arial", 40), anchor="nw")
                GAME.Button("Back",5,725)
                with sqlite3.connect(GAME.database) as c:
                    f=c.execute("SELECT Track FROM Calendar").fetchall()
                    for x in range(len(f)//5):
                        for y in range(5):
                            GAME.CalendarDisplay(x,y,GAME.Sanitise(f[(x*5)+y]))
                    for z in range(len(f)%5):
                        GAME.CalendarDisplay(len(f)//5,z,GAME.Sanitise(f[((len(f)//5)*5)+z]))
                canvas.create_text(250, 600, text=f"Next Race: {GAME.Sanitise(f[GAME.race-1])}", fill="#C4C4C4", font=("Arial", 50), anchor="nw")
            elif event.x>=870 and event.x<=1070 and event.y>=580 and event.y<=630:
                #Achievements
                GAME.ChangeScreen("Achievements")
                GAME.DisplayLogo()
                GAME.DisplayMoney()
                GAME.Button("Back",5,730)
                with sqlite3.connect(GAME.database) as c:
                    points=int(GAME.Sanitise(c.execute("SELECT Points FROM Player").fetchall()[0]))
                    wins=int(GAME.Sanitise(c.execute("SELECT Wins FROM Player").fetchall()[0]))
                    championships=int(GAME.Sanitise(c.execute("SELECT Championships FROM Player").fetchall()[0]))
                canvas.create_text(40, 10, text="Achievements", fill="white", font=("Arial", 100), anchor="nw")
                canvas.create_text(40, 200, text=f"Name: {GAME.name}", fill="white", font=("Arial", 40), anchor="nw")
                canvas.create_text(40, 280, text=f"Current Team: {GAME.team}", fill="white", font=("Arial", 40), anchor="nw")
                canvas.create_text(40, 360, text=f"Seasons: {GAME.season-2025}", fill="white", font=("Arial", 40), anchor="nw")
                canvas.create_text(40, 440, text=f"Points: {points}", fill="white", font=("Arial", 40), anchor="nw")
                if wins>0:
                    canvas.create_text(40, 520, text=f"Wins: {wins}", fill="white", font=("Arial", 40), anchor="nw")
                if championships>0:
                    canvas.create_text(40, 600, text=f"Championships: {championships}", fill="white", font=("Arial", 40), anchor="nw")
            elif event.x>=920 and event.x<=1120 and event.y>=650 and event.y<=700:
                #History
                GAME.ChangeScreen("History")
                GAME.Button("Back",5,730)
                canvas.create_text(400, 135, text="Year", fill="black", font=("Arial", 20), anchor="nw")
                canvas.create_text(470, 135, text="Driver", fill="black", font=("Arial", 20), anchor="nw")
                canvas.create_text(750, 135, text="Constructor", fill="black", font=("Arial", 20), anchor="nw")
                for x in range(25):
                    year=GAME.season-25+x
                    with sqlite3.connect(GAME.database) as c:
                        driver=GAME.Sanitise(c.execute("SELECT Driver FROM History WHERE Year=?",(year,)).fetchall()[0])
                        constructor=GAME.Sanitise(c.execute("SELECT Constructor FROM History WHERE Year=?",(year,)).fetchall()[0])
                    canvas.create_text(400, 160+(x*25), text=year, fill="black", font=("Arial", 20), anchor="nw")
                    canvas.create_text(470, 160+(x*25), text=driver, fill="black", font=("Arial", 20), anchor="nw")
                    canvas.create_text(750, 160+(x*25), text=constructor, fill="black", font=("Arial", 20), anchor="nw")
            elif event.x>=300 and event.x<=500 and event.y>=650 and event.y<=700:
                #Team Management
                GAME.ChangeScreen("Team Management")
                GAME.DisplayLogo()
                GAME.DisplayMoney()
                GAME.Button("Back",5,730)
                canvas.create_text(40, 10, text="Team Management", fill="white", font=("Arial", 100), anchor="nw")
                canvas.create_text(40, 200, text="Board Approval:", fill="white", font=("Arial", 40), anchor="nw")
                canvas.create_text(40, 280, text="Performance:", fill="white", font=("Arial", 40), anchor="nw")
                canvas.create_text(40, 360, text="Financial:", fill="white", font=("Arial", 40), anchor="nw")
                canvas.create_text(40, 440, text="Management:", fill="white", font=("Arial", 40), anchor="nw")
                d=0
                u=0
                with sqlite3.connect(GAME.database) as c:
                    position=int(GAME.Sanitise(c.execute("SELECT Position FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0]))
                    previousPosition=int(GAME.Sanitise(c.execute("SELECT PreviousPosition FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0]))
                    last=len(c.execute("SELECT Name FROM Teams").fetchall())
                    if (previousPosition==0 or position<=previousPosition) and position!=last:
                        performance="Happy"
                        performanceColour="#00FF00"
                    elif position<=previousPosition+1 and position!=last:
                        performance="Unhappy"
                        performanceColour="#FF8000"
                        u+=1
                    else:
                        performance="Disappointed"
                        performanceColour="#FF0000"
                        d+=1
                    financial=int(GAME.Sanitise(c.execute("SELECT Financial FROM Player").fetchall()[0]))
                    if financial>=4:
                        financial="Happy"
                        financialColour="#00FF00"
                    elif financial>=2:
                        financial="Unhappy"
                        financialColour="#FF8000"
                        u+=1
                    else:
                        financial="Disappointed"
                        financialColour="#FF0000"
                        d+=1
                    management=int(GAME.Sanitise(c.execute("SELECT Management FROM Player").fetchall()[0]))
                    if management==3:
                        management="Happy"
                        managementColour="#00FF00"
                    elif management==2:
                        management="Unhappy"
                        managementColour="#FF8000"
                        u+=1
                    else:
                        management="Disappointed"
                        managementColour="#FF0000"
                        d+=1
                    warnings=int(GAME.Sanitise(c.execute("SELECT Warnings FROM Player").fetchall()[0]))
                if d>=2:
                    approval="Lost Confidence"
                    approvalColour="#CC0000"
                elif d==1 and u>1:
                    approval="Disappointed"
                    approvalColour="#FF0000"
                elif d==1 or u>1:
                    approval="Unhappy"
                    approvalColour="#FF8000"
                elif u==1:
                    approval="Satisfied"
                    approvalColour="white"
                else:
                    approval="Happy"
                    approvalColour="#00FF00"
                canvas.create_text(440, 200, text=approval, fill=approvalColour, font=("Arial", 40), anchor="nw")
                canvas.create_text(380, 280, text=performance, fill=performanceColour, font=("Arial", 40), anchor="nw")
                canvas.create_text(280, 360, text=financial, fill=financialColour, font=("Arial", 40), anchor="nw")
                canvas.create_text(380, 440, text=management, fill=managementColour, font=("Arial", 40), anchor="nw")
                if warnings>0:
                    canvas.create_text(880, 200, text="Warnings:", fill="white", font=("Arial", 40), anchor="nw")
                    if warnings==1:
                        colour="white"
                    elif warnings==2:
                        colour="#FF8000"
                    else:
                        colour="#FF0000"
                    canvas.create_text(1150, 200, text=warnings, fill=colour, font=("Arial", 40), anchor="nw")
        elif GAME.screen=="Car Data":
            engine=0
            if event.x>=960 and event.x<=1160 and event.y>=320 and event.y<=370:
                engine=1
            elif event.x>=1180 and event.x<=1380 and event.y>=320 and event.y<=370:
                engine=2
            if engine!=0:
                with sqlite3.connect(GAME.database) as c:
                    if engine==1:
                        if int(GAME.Sanitise(c.execute("SELECT car1EngineDurability FROM Cars WHERE Team=?",(GAME.team,)).fetchall()[0]))==100:
                            num=0
                        else:
                            num=int(GAME.Sanitise(c.execute("SELECT car1Engine FROM Cars WHERE Team=?",(GAME.team,)).fetchall()[0]))+1
                            c.execute("UPDATE Cars SET car1Engine=?, car1EngineDurability=100 WHERE Team=?",(num,GAME.team,))
                    else:
                        if int(GAME.Sanitise(c.execute("SELECT car2EngineDurability FROM Cars WHERE Team=?",(GAME.team,)).fetchall()[0]))==100:
                            num=0
                        else:
                            num=int(GAME.Sanitise(c.execute("SELECT car2Engine FROM Cars WHERE Team=?",(GAME.team,)).fetchall()[0]))+1
                            c.execute("UPDATE Cars SET car2Engine=?, car2EngineDurability=100 WHERE Team=?",(num,GAME.team,))
                    if num>4:
                        GAME.money-=10000000
                        c.execute("UPDATE Teams SET Money=? WHERE Name=?",(GAME.money,GAME.team,))
                GAME.CarData()
        elif GAME.screen=="Upgrade":
            if event.x>=1150 and event.x<=1650 and event.y>=500 and event.y<=550:
                if GAME.maximumUpgradePoints!=GAME.remainingUpgradePoints:
                    GAME.action=1
                    driveability=0
                    GAME.money-=(GAME.maximumUpgradePoints-GAME.remainingUpgradePoints)*500000
                    with sqlite3.connect(GAME.database) as c:
                        rating=int(GAME.Sanitise(c.execute('''SELECT Rating FROM Staff WHERE Team=? AND Role="Technical Director"''',(GAME.team,)).fetchall()[0]))
                        c.execute("UPDATE Teams SET Money=? WHERE Name=?",(GAME.money,GAME.team,))
                    for x in range(len(GAME.upgradePoints)):
                        if GAME.upgradePoints[x]>0:
                            if x<4:
                                driveability+=round(random.randint(-250*GAME.upgradePoints[x],100*GAME.upgradePoints[x])/1000)
                            if x!=6:
                                stat=round(random.randint(-1,round((rating**2)*GAME.upgradePoints[x]/4000))/3)
                                with sqlite3.connect(GAME.database) as c:
                                    if x==0:
                                        stat+=int(GAME.Sanitise(c.execute("SELECT DragReduction FROM Cars WHERE Team=?",(GAME.team,)).fetchall()[0]))
                                        c.execute("UPDATE Cars SET DragReduction=? WHERE Team=?",(stat,GAME.team,))
                                    elif x==1:
                                        stat+=int(GAME.Sanitise(c.execute("SELECT LowSpeed FROM Cars WHERE Team=?",(GAME.team,)).fetchall()[0]))
                                        c.execute("UPDATE Cars SET LowSpeed=? WHERE Team=?",(stat,GAME.team,))
                                    elif x==2:
                                        stat+=int(GAME.Sanitise(c.execute("SELECT MediumSpeed FROM Cars WHERE Team=?",(GAME.team,)).fetchall()[0]))
                                        c.execute("UPDATE Cars SET MediumSpeed=? WHERE Team=?",(stat,GAME.team,))
                                    elif x==3:
                                        stat+=int(GAME.Sanitise(c.execute("SELECT HighSpeed FROM Cars WHERE Team=?",(GAME.team,)).fetchall()[0]))
                                        c.execute("UPDATE Cars SET HighSpeed=? WHERE Team=?",(stat,GAME.team,))
                                    elif x==4:
                                        stat+=int(GAME.Sanitise(c.execute("SELECT Cooling FROM Cars WHERE Team=?",(GAME.team,)).fetchall()[0]))
                                        c.execute("UPDATE Cars SET Cooling=? WHERE Team=?",(stat,GAME.team,))
                                    elif x==5:
                                        stat+=int(GAME.Sanitise(c.execute("SELECT TyrePreservation FROM Cars WHERE Team=?",(GAME.team,)).fetchall()[0]))
                                        c.execute("UPDATE Cars SET TyrePreservation=? WHERE Team=?",(stat,GAME.team,))
                            else:
                                driveability+=round(random.randint(-5,5*GAME.upgradePoints[x])/8)
                    if driveability!=0:
                        with sqlite3.connect(GAME.database) as c:
                            driveability+=int(GAME.Sanitise(c.execute("SELECT Driveability FROM Cars WHERE Team=?",(GAME.team,)).fetchall()[0]))
                            if driveability<1:
                                driveability=1
                            elif driveability>20:
                                driveability=20
                            c.execute("UPDATE Cars SET Driveability=? WHERE Team=?",(driveability,GAME.team,))
                    if GAME.sound==1:
                        sound_path = os.path.join(os.path.dirname(__file__), "Sound Effects", "Upgrade Sound.wav")
                        if os.path.isfile(sound_path):
                            winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
                    GAME.Menu()
            else:
                modify=0
                attribute=-1
                if event.x>=50 and event.x<=80:
                    modify="-"
                elif event.x>=525 and event.x<=550:
                    modify="+"
                if event.y>=180 and event.y<=230:
                    attribute=0
                elif event.y>=250 and event.y<=300:
                    attribute=1
                elif event.y>=320 and event.y<=370:
                    attribute=2
                elif event.y>=390 and event.y<=440:
                    attribute=3
                elif event.y>=460 and event.y<=510:
                    attribute=4
                elif event.y>=530 and event.y<=580:
                    attribute=5
                elif event.y>=600 and event.y<=650:
                    attribute=6
                elif event.y>=670 and event.y<=720 and len(GAME.upgradePoints)==8:
                    attribute=7
                if modify!=0 and attribute!=-1:
                    upgradePoints=GAME.upgradePoints[attribute]
                    if modify=="+":
                        if GAME.remainingUpgradePoints>0:
                            upgradePoints+=1
                            GAME.remainingUpgradePoints-=1
                    elif upgradePoints>0:
                        upgradePoints-=1
                        GAME.remainingUpgradePoints+=1
                    GAME.upgradePoints.pop(attribute)
                    GAME.upgradePoints.insert(attribute,upgradePoints)
                    GAME.UpgradePage()
        elif GAME.screen=="Select Research Type":
            if event.x>=350 and event.x<=550 and event.y>=450 and event.y<=500:
                GAME.AerodynamicResearch()
            elif event.x>=890 and event.x<=1190 and event.y>=450 and event.y<=500:
                GAME.ResearchEngine()
        elif GAME.screen=="Scouting":
            if event.x>=400 and event.x<=600 and event.y>=510 and event.y<=560:
                #View Contracts
                GAME.ViewContracts()
            elif event.x>=350 and event.x<=550 and event.y>=580 and event.y<=630:
                #Scout Drivers
                GAME.scouting="Driver"
                with sqlite3.connect(GAME.database) as c:
                    f=c.execute("SELECT Name FROM Drivers WHERE (Team=? AND Role='1' AND ContractEnd>? AND NewTeam='0') OR (NewTeam=? AND NewRole='1')",(GAME.team,GAME.season,GAME.team,)).fetchall()
                    if len(f)>0:
                        f=c.execute("SELECT Name FROM Drivers WHERE (Team=? AND Role='2' AND ContractEnd>? AND NewTeam='0') OR (NewTeam=? AND NewRole='2')",(GAME.team,GAME.season,GAME.team,)).fetchall()
                        if len(f)>0:
                            f=c.execute("SELECT Name FROM Drivers WHERE (Team=? AND Role='Rerve' AND ContractEnd>? AND NewTeam='0') OR (NewTeam=? AND NewRole='Reserve')",(GAME.team,GAME.season,GAME.team,)).fetchall()
                            if len(f)<2:
                                f=[]
                            else:
                                f=c.execute("SELECT Name FROM Drivers WHERE (Team=? AND Role='Junior' AND ContractEnd>? AND NewTeam='0') OR (NewTeam=? AND NewRole='Junior')",(GAME.team,GAME.season,GAME.team,)).fetchall()
                                if len(f)<3:
                                    f=[]
                                    GAME.scouting="Junior Driver"
                if len(f)==0:
                    Drivers=GAME.DriverSuitability(GAME.team)
                    if len(Drivers)>0:
                        minimumRating=GAME.MinimumRating()
                        GAME.ChangeScreen("Driver List")
                        GAME.Button("Back",5,730)
                        GAME.Button("Propose Contract",1220,730)
                        drivers=[]
                        for x in range(len(Drivers)):
                            with sqlite3.connect(GAME.database) as c:
                                if int(GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Name=?",(Drivers[x],)).fetchall()[0]))>=minimumRating:
                                    drivers.append(Drivers[x])
                        if len(drivers)>0:
                            if len(drivers)>10:
                                d=drivers.copy()
                                drivers=[]
                                for x in range(10):
                                    driver=random.choice(d)
                                    d.remove(driver)
                                    drivers.append(driver)
                            canvas.create_text(150, 100, text="Name", fill="black", font=("Arial", 20), anchor="nw")
                            canvas.create_text(450, 100, text="Team", fill="black", font=("Arial", 20), anchor="nw")
                            canvas.create_text(650, 100, text="Age", fill="black", font=("Arial", 20), anchor="nw")
                            canvas.create_text(720, 100, text="Role", fill="black", font=("Arial", 20), anchor="nw")
                            canvas.create_text(900, 100, text="Rating", fill="black", font=("Arial", 20), anchor="nw")
                            canvas.create_text(1000, 100, text="Salary", fill="black", font=("Arial", 20), anchor="nw")
                            canvas.create_text(1120, 100, text="Contract End", fill="black", font=("Arial", 20), anchor="nw")
                            for x in range(len(drivers)):
                                driver=drivers[x]
                                with sqlite3.connect(GAME.database) as c:
                                    salary="$"+str("{:,}".format(int(GAME.Sanitise(c.execute("SELECT Salary FROM Drivers WHERE Name=?",(driver,)).fetchall()[0]))))
                                    if salary=="$0":
                                        salary="-"
                                    contractEnd=GAME.Sanitise(c.execute("SELECT ContractEnd FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                                    rating=GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                                    team=GAME.Sanitise(c.execute("SELECT Team FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                                    role=GAME.Sanitise(c.execute("SELECT Role FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                                    if role=="1" or role=="2":
                                        role="Driver"
                                    elif role!="Free Agent":
                                        role=role+" Driver"
                                    age=GAME.Sanitise(c.execute("SELECT Age FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                                canvas.create_text(150, 150+(x*50), text=driver, fill="black", font=("Arial", 20), anchor="nw")
                                canvas.create_text(450, 150+(x*50), text=team, fill="black", font=("Arial", 20), anchor="nw")
                                canvas.create_text(650, 150+(x*50), text=age, fill="black", font=("Arial", 20), anchor="nw")
                                canvas.create_text(720, 150+(x*50), text=role, fill="black", font=("Arial", 20), anchor="nw")
                                canvas.create_text(920, 150+(x*50), text=rating, fill="black", font=("Arial", 20), anchor="nw")
                                canvas.create_text(1000, 150+(x*50), text=salary, fill="black", font=("Arial", 20), anchor="nw")
                                if contractEnd=="0":
                                    contractEnd="-"
                                canvas.create_text(1200, 150+(x*50), text=contractEnd, fill="black", font=("Arial", 20), anchor="nw")
                            GAME.options=drivers.copy()
                        else:
                            GAME.Menu()
                    else:
                        GAME.Menu()
            elif event.x>=820 and event.x<=1020 and event.y>=510 and event.y<=560:
                #Scout Technical Directors
                with sqlite3.connect(GAME.database) as c:
                    f=c.execute("SELECT Name FROM Staff WHERE NewTeam=? AND Role='Technical Director'",(GAME.team,)).fetchall()
                if len(f)==0:
                    GAME.ScoutStaff("Technical Director")
            elif event.x>=870 and event.x<=1070 and event.y>=580 and event.y<=630:
                #Scout Sporting Directors
                with sqlite3.connect(GAME.database) as c:
                    f=c.execute("SELECT Name FROM Staff WHERE NewTeam=? AND Role='Sporting Director'",(GAME.team,)).fetchall()
                if len(f)==0:
                    GAME.ScoutStaff("Sporting Director")
            elif event.x>=920 and event.x<=1120 and event.y>=650 and event.y<=700:
                #Scout Race Engineers
                with sqlite3.connect(GAME.database) as c:
                    f=c.execute("SELECT Name FROM Staff WHERE NewTeam=? AND NewRole='Race Engineer 1'",(GAME.team,)).fetchall()
                    if len(f)==1:
                        f=c.execute("SELECT Name FROM Staff WHERE NewTeam=? AND NewRole='Race Engineer 2'",(GAME.team,)).fetchall()
                if len(f)==0:
                    GAME.ScoutStaff("Race Engineer")
            elif event.x>=300 and event.x<=500 and event.y>=650 and event.y<=700:
                #Hire Reserve
                with sqlite3.connect(GAME.database) as c:
                    unableToRace=len(c.execute("SELECT Name FROM Drivers WHERE Team=? AND Condition!='Well'",(GAME.team,)).fetchall())
                    if GAME.team=="Racing Bulls" and len(c.execute("SELECT Name FROM Teams WHERE Name='Red Bull'").fetchall())>0:
                        team="Red Bull"
                    else:
                        team=GAME.team
                    reserves=len(c.execute("SELECT Name FROM Drivers WHERE Team=? AND Role='Reserve'",(team,)).fetchall())
                    if unableToRace>0 and reserves<unableToRace:
                        GAME.HireReserve()
        elif GAME.screen=="View Contracts":
            if event.x>=600 and event.x<=800 and event.y>=730 and event.y<=780:
                with sqlite3.connect(GAME.database) as c:
                    f=c.execute("SELECT Name FROM Drivers WHERE (Role='Reserve' OR Role='Junior') AND Team=?",(GAME.team,)).fetchall()
                    if len(f)==0 and GAME.team=="Racing Bulls":
                        f=c.execute("SELECT Name FROM Drivers WHERE (Role='Reserve' OR Role='Junior') AND Team='Red Bull'").fetchall()
                if len(f)>0:
                    GAME.ChangeScreen("Junior & Reserve Drivers")
                    GAME.Button("Back",5,730)
                    GAME.Button("Other Contracts",600,730)
                    GAME.Button("Renew",1000,730)
                    GAME.Button("Promote",1220,730)
                    canvas.create_text(150, 100, text="Name", fill="black", font=("Arial", 20), anchor="nw")
                    canvas.create_text(550, 100, text="Role", fill="black", font=("Arial", 20), anchor="nw")
                    canvas.create_text(820, 100, text="Age", fill="black", font=("Arial", 20), anchor="nw")
                    canvas.create_text(900, 100, text="Rating", fill="black", font=("Arial", 20), anchor="nw")
                    canvas.create_text(1000, 100, text="Salary", fill="black", font=("Arial", 20), anchor="nw")
                    canvas.create_text(1120, 100, text="Contract End", fill="black", font=("Arial", 20), anchor="nw")
                    counter=0
                    #Reserve Drivers
                    drivers=[]
                    roles=[]
                    with sqlite3.connect(GAME.database) as c:
                        if GAME.team=="Racing Bulls":
                            f=c.execute("SELECT Name FROM Drivers WHERE Role='Reserve' AND Team='Red Bull'").fetchall()
                        else:
                            f=[]
                        if len(f)==0:
                            f=c.execute("SELECT Name FROM Drivers WHERE Role='Reserve' AND Team=?",(GAME.team,)).fetchall()
                        for x in range(len(f)):
                            drivers.append(GAME.Sanitise(f[x]))
                            roles.append("Reserve Driver")
                        if GAME.team=="Red Bull":
                            f=c.execute("SELECT Name FROM Drivers WHERE Team='Racing Bulls'").fetchall()
                            for x in range(len(f)):
                                drivers.append(GAME.Sanitise(f[x]))
                                roles.append("Racing Bulls Driver")
                    if len(drivers)>0:
                        for x in range(len(drivers)):
                            driver=drivers[x]
                            with sqlite3.connect(GAME.database) as c:
                                salary="$"+str("{:,}".format(int(GAME.Sanitise(c.execute("SELECT Salary FROM Drivers WHERE Name=?",(driver,)).fetchall()[0]))))
                                contractEnd=GAME.Sanitise(c.execute("SELECT ContractEnd FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                                rating=GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                                age=GAME.Sanitise(c.execute("SELECT Age FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                            canvas.create_text(150, 150+(counter*50), text=driver, fill="black", font=("Arial", 20), anchor="nw")
                            canvas.create_text(550, 150+(counter*50), text=roles[x], fill="black", font=("Arial", 20), anchor="nw")
                            canvas.create_text(820, 150+(counter*50), text=age, fill="black", font=("Arial", 20), anchor="nw")
                            canvas.create_text(920, 150+(counter*50), text=rating, fill="black", font=("Arial", 20), anchor="nw")
                            canvas.create_text(1000, 150+(counter*50), text=salary, fill="black", font=("Arial", 20), anchor="nw")
                            if contractEnd=="0":
                                contractEnd="-"
                            canvas.create_text(1200, 150+(counter*50), text=contractEnd, fill="black", font=("Arial", 20), anchor="nw")
                            counter+=1
                    #Junior Drivers
                    juniors=[]
                    with sqlite3.connect(GAME.database) as c:
                        if GAME.team=="Racing Bulls":
                            f=c.execute("SELECT Name FROM Drivers WHERE Role='Junior' AND Team='Red Bull'").fetchall()
                        else:
                            f=[]
                        if len(f)==0:
                            f=c.execute("SELECT Name FROM Drivers WHERE Role='Junior' AND Team=?",(GAME.team,)).fetchall()
                        for x in range(len(f)):
                            juniors.append(GAME.Sanitise(f[x]))
                        if GAME.team=="Racing Bulls":
                            f=c.execute("SELECT Name FROM Drivers WHERE Role='Junior' AND Team='Red Bull'").fetchall()
                            for x in range(len(f)):
                                juniors.append(GAME.Sanitise(f[x]))
                    if len(juniors)>0:
                        for x in range(len(f)):
                            driver=juniors[x]
                            with sqlite3.connect(GAME.database) as c:
                                salary="$"+str("{:,}".format(int(GAME.Sanitise(c.execute("SELECT Salary FROM Drivers WHERE Name=?",(driver,)).fetchall()[0]))))
                                contractEnd=GAME.Sanitise(c.execute("SELECT ContractEnd FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                                rating=GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                                age=GAME.Sanitise(c.execute("SELECT Age FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                            canvas.create_text(150, 150+(counter*50), text=driver, fill="black", font=("Arial", 20), anchor="nw")
                            canvas.create_text(550, 150+(counter*50), text="Junior Driver", fill="black", font=("Arial", 20), anchor="nw")
                            canvas.create_text(820, 150+(counter*50), text=age, fill="black", font=("Arial", 20), anchor="nw")
                            canvas.create_text(920, 150+(counter*50), text=rating, fill="black", font=("Arial", 20), anchor="nw")
                            canvas.create_text(1000, 150+(counter*50), text=salary, fill="black", font=("Arial", 20), anchor="nw")
                            canvas.create_text(1200, 150+(counter*50), text=contractEnd, fill="black", font=("Arial", 20), anchor="nw")
                            counter+=1
            elif event.x>=1200 and event.x<=1400 and event.y>=730 and event.y<=780:
                #Renew
                with sqlite3.connect(GAME.database) as c:
                    GAME.options=[]
                    for x in range(2):
                        f=c.execute("SELECT Name FROM Drivers WHERE Team=? AND Role=? AND ContractEnd=?",(GAME.team,str(x+1),GAME.season,)).fetchall()
                        if len(f)==1:
                            if len(c.execute("SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole=?",(GAME.team,str(x+1),)).fetchall())==0:
                                driver=GAME.Sanitise(f[0])
                                if not (GAME.season==2026 and (driver=="Max Verstappen" or driver=="Charles Leclerc" or driver=="Oscar Piastri") and GAME.race<20):
                                    GAME.options.append(driver)
                    roles=["Technical Director","Sporting Director","Race Engineer 1","Race Engineer 2"]
                    for x in range(4):
                        f=c.execute("SELECT Name FROM Staff WHERE Team=? AND Role=? AND NewTeam='0'",(GAME.team,roles[x],)).fetchall()
                        if len(f)==1:
                            if len(c.execute("SELECT Name FROM Staff WHERE NewTeam=? AND NewRole=?",(GAME.team,roles[x],)).fetchall())==0:
                                GAME.options.append(GAME.Sanitise(f[0]))
                if len(GAME.options)>0:
                    GAME.displayed=0
                    GAME.SelectRenewal()
        elif GAME.screen=="Junior & Reserve Drivers":
            if event.x>=600 and event.x<=800 and event.y>=730 and event.y<=780:
                GAME.ViewContracts()
            elif event.x>=1000 and event.x<=1200 and event.y>=730 and event.y<=780:
                #Renew
                with sqlite3.connect(GAME.database) as c:
                    GAME.options=[]
                    #Reserves
                    if GAME.team=="Racing Bulls":
                        f=c.execute("SELECT Name FROM Drivers WHERE Team='Red Bull' AND Role='Reserve' AND ContractEnd=?",(GAME.season,)).fetchall()
                    else:
                        f=[]
                    if len(f)==0:
                        f=c.execute("SELECT Name FROM Drivers WHERE Team=? AND Role='Reserve' AND ContractEnd=?",(GAME.team,GAME.season,)).fetchall()
                    if len(f)>0:
                        for x in range(len(f)):
                            if len(c.execute("SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole='Reserve'",(GAME.team,)).fetchall())<2:
                                GAME.options.append(GAME.Sanitise(f[x]))
                    #Juniors
                    if GAME.team=="Racing Bulls":
                        f=c.execute("SELECT Name FROM Drivers WHERE Team='Red Bull' AND Role='Junior' AND ContractEnd=?",(GAME.season,)).fetchall()
                    else:
                        f=[]
                    if len(f)==0:
                        f=c.execute("SELECT Name FROM Drivers WHERE Team=? AND Role='Junior' AND ContractEnd=?",(GAME.team,GAME.season,)).fetchall()
                    if len(f)>0:
                        for x in range(len(f)):
                            if len(c.execute("SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole='Reserve'",(GAME.team,)).fetchall())<3:
                                GAME.options.append(GAME.Sanitise(f[x]))
                if len(GAME.options)>0:
                    GAME.displayed=0
                    GAME.SelectRenewal()
            elif event.x>=1220 and event.x<=1420 and event.y>=730 and event.y<=780:
                #Promote
                with sqlite3.connect(GAME.database) as c:
                    GAME.options=[]
                    GAME.roles=[]
                    #Reserves
                    if GAME.team=="Racing Bulls":
                        f=c.execute("SELECT Name FROM Drivers WHERE Team='Red Bull' AND Role='Reserve' AND NewTeam='0'").fetchall()
                    else:
                        f=[]
                    if len(f)==0:
                        f=c.execute("SELECT Name FROM Drivers WHERE Team=? AND Role='Reserve' AND NewTeam='0'",(GAME.team,)).fetchall()
                    if len(f)>0:
                        for x in range(len(f)):
                            if len(c.execute("SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole='Reserve'",(GAME.team,)).fetchall())<2:
                                GAME.options.append(GAME.Sanitise(f[x]))
                                GAME.roles.append("Reserve")
                    #Juniors
                    if GAME.team=="Racing Bulls":
                        f=c.execute("SELECT Name FROM Drivers WHERE Team='Red Bull' AND Role='Junior' AND NewTeam='0' AND Age>16").fetchall()
                    else:
                        f=[]
                    if len(f)==0:
                        f=c.execute("SELECT Name FROM Drivers WHERE Team=? AND Role='Junior' AND NewTeam='0' AND Age>16",(GAME.team,)).fetchall()
                    if len(f)>0:
                        for x in range(len(f)):
                            if len(c.execute("SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole='Junior'",(GAME.team,)).fetchall())<3:
                                GAME.options.append(GAME.Sanitise(f[x]))
                                GAME.roles.append("Junior")
                    #Racing Bulls
                    if GAME.team=="Red Bull":
                        f=c.execute("SELECT Name FROM Drivers WHERE Team='Racing Bulls' AND (Role='1' OR Role='2') AND NewTeam='0'").fetchall()
                    if len(f)>0:
                        for x in range(len(f)):
                            if len(c.execute("SELECT Name FROM Drivers WHERE NewTeam='Red Bull' AND (NewRole='1' OR NewRole='2')").fetchall())<2:
                                GAME.options.append(GAME.Sanitise(f[x]))
                                GAME.roles.append("Reserve")
                if len(GAME.options)>0:
                    GAME.displayedName=0
                    GAME.scouting="Driver"
                    GAME.promoting=1
                    GAME.SelectContractName()
        elif GAME.screen=="Driver List" or GAME.screen=="Staff List":
            if event.x>=1220 and event.x<=1420 and event.y>=730 and event.y<=780:
                GAME.displayedName=0
                GAME.promoting=0
                GAME.SelectContractName()
        elif GAME.screen=="Contract Name":
            if event.x>=155 and event.x<=215 and event.y>=380 and event.y<=510:
                #Back
                if GAME.displayedName==0:
                    GAME.displayedName=len(GAME.options)-1
                else:
                    GAME.displayedName-=1
                GAME.SelectContractName()
            elif event.x>=870 and event.x<=940 and event.y>=375 and event.y<=515:
                #Forward
                if GAME.displayedName==len(GAME.options)-1:
                    GAME.displayedName=0
                else:
                    GAME.displayedName+=1
                GAME.SelectContractName()
            elif event.x>=1100 and event.x<=1300 and event.y>=420 and event.y<=470:
                #Propose Contract
                if GAME.scouting=="Driver" or GAME.scouting=="Junior Driver":
                    with sqlite3.connect(GAME.database) as c:
                        GAME.scoutingAge=int(GAME.Sanitise(c.execute("SELECT Age FROM Drivers WHERE Name=?",(GAME.options[GAME.displayedName],)).fetchall()[0]))
                    if GAME.scoutingAge>16:
                        GAME.role=GAME.car1
                    else:
                        GAME.role="Junior"
                elif GAME.scouting=="Race Engineer":
                    with sqlite3.connect(GAME.database) as c:
                        if len(c.execute("SELECT Name FROM Staff WHERE NewTeam=? AND NewRole='Race Engineer 1'",(GAME.team,)).fetchall())==0:
                            GAME.role=GAME.car1
                        else:
                            GAME.role=GAME.car2
                else:
                    GAME.role=GAME.scouting
                if GAME.promoting==0:
                    GAME.salary=500000
                    GAME.contractLength=1
                else:
                    with sqlite3.connect(GAME.database) as c:
                        minimumSalary=int(GAME.Sanitise(c.execute("SELECT Salary FROM Drivers WHERE Name=?",(GAME.options[GAME.displayedName],)).fetchall()[0]))
                        rating=int(GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Name=?",(GAME.options[GAME.displayedName],)).fetchall()[0]))
                        GAME.salary=random.randint(rating*37500,rating*70000)
                        if GAME.salary<minimumSalary:
                            GAME.salary=minimumSalary
                        contractEnd=int(GAME.Sanitise(c.execute("SELECT ContractEnd FROM Drivers WHERE Name=?",(GAME.options[GAME.displayedName],)).fetchall()[0]))
                        if contractEnd>GAME.season:
                            GAME.contractLength=contractEnd-GAME.season
                        else:
                            GAME.contractLength=1
                GAME.ContractParameters()
        elif GAME.screen=="Contract Parameters":
            if event.x>=800 and event.x<=1000 and event.y>=490 and event.y<=540:
                #Propose Contract
                name=GAME.options[GAME.displayedName]
                if GAME.scouting=="Driver" or GAME.scouting=="Junior Driver":
                    with sqlite3.connect(GAME.database) as c:
                        contractEnd=int(GAME.Sanitise(c.execute("SELECT ContractEnd FROM Drivers WHERE Name=?",(name,)).fetchall()[0]))
                    if contractEnd==GAME.season and GAME.promoting==0:
                        resigned=GAME.Resign(name)
                    else:
                        resigned=0
                    if resigned==0:
                        if GAME.promoting==1:
                            wantedSalary=0
                            currentSalary=0
                        else:
                            if random.randint(1,15)==15:
                                GAME.action=1
                            with sqlite3.connect(GAME.database) as c:
                                currentSalary=int(GAME.Sanitise(c.execute('''SELECT Salary FROM Drivers WHERE Name=?''',(name,)).fetchall()[0]))
                                rating=int(GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Name=?",(name,)).fetchall()[0]))
                            if GAME.role==GAME.car1 or GAME.role==GAME.car2:
                                wantedSalary=random.randint(rating*37500,rating*250000)
                            else:
                                wantedSalary=random.randint(rating*4000,rating*6000)
                        if GAME.salary<wantedSalary or GAME.salary<currentSalary:
                            GAME.ChangeScreen("Contract Rejected")
                            root.after(3000, lambda: GAME.EndScouting())
                        else:
                            if contractEnd==0:
                                GAME.buyout=0
                            else:
                                GAME.buyout=(contractEnd-GAME.season)*currentSalary
                            if GAME.role==GAME.car1 or GAME.role==GAME.car2:
                                if GAME.role==GAME.car1:
                                    role="1"
                                else:
                                    role="2"
                                with sqlite3.connect(GAME.database) as c:
                                    try:
                                        ContractEnd=int(GAME.Sanitise(c.execute("SELECT ContractEnd FROM Drivers WHERE Team=? AND Role=? AND NewTeam='0'",(GAME.team,role,)).fetchall()[0]))
                                    except:
                                        ContractEnd=GAME.season
                                    if ContractEnd>GAME.season:
                                        Salary=int(GAME.Sanitise(c.execute("SELECT Salary FROM Drivers WHERE Team=? AND Role=?",(GAME.team,role,)).fetchall()[0]))
                                        GAME.buyout+=Salary*(ContractEnd-GAME.season)
                            GAME.ChangeScreen("Contract")
                            if GAME.promoting==0:
                                GAME.Button("Hire",800,660)
                            else:
                                GAME.Button("Promote",800,660)
                            GAME.Button("Back",5,730)
                            if GAME.team in steam:
                                appearance=GAME.team
                            else:
                                with sqlite3.connect(GAME.database) as c:
                                    appearance=GAME.Sanitise(c.execute("SELECT Appearance FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0])
                            if appearance!="0":
                                if appearance in steam:
                                    logo=logos[steam.index(appearance)-1]
                                else:
                                    logo=sponsorLogos[sponsors.index(appearance)]
                                canvas.image=logo
                                canvas.create_image(900, 80, anchor=tk.NW, image=logo)
                            if GAME.role==GAME.car1 or GAME.role==GAME.car2:
                                role="Driver"
                            else:
                                role=GAME.role+" Driver"
                            salary="{:,}".format(GAME.salary)
                            buyout="{:,}".format(GAME.buyout)
                            canvas.create_text(445, 80, text=name, fill="black", font=("Arial", 40), anchor="nw")
                            canvas.create_text(445, 550, text=f"Salary: ${salary}", fill="black", font=("Arial", 30), anchor="nw")
                            canvas.create_text(445, 590, text=f"Buyout: ${buyout}", fill="black", font=("Arial", 30), anchor="nw")
                            if GAME.contractLength==1:
                                canvas.create_text(445, 630, text="1 Season", fill="black", font=("Arial", 30), anchor="nw")
                            else:
                                canvas.create_text(445, 630, text=f"{GAME.contractLength} Seasons", fill="black", font=("Arial", 30), anchor="nw")
                            canvas.create_text(795, 300, text=role, fill="black", font=("Arial", 25), anchor="nw")
                            GAME.DisplayDriver(name,450,250)
                    else:
                        GAME.EndScouting()
                else:
                    rehired=0
                    with sqlite3.connect(GAME.database) as c:
                        rating=int(GAME.Sanitise(c.execute("SELECT Rating FROM Staff WHERE Name=?",(name,)).fetchall()[0]))
                        currentSalary=int(GAME.Sanitise(c.execute("SELECT Salary FROM Staff WHERE Name=?",(name,)).fetchall()[0]))
                        oldTeam=GAME.Sanitise(c.execute("SELECT Team FROM Staff WHERE Name=?",(name,)).fetchall()[0])
                        if GAME.Sanitise(c.execute("SELECT Team FROM Staff WHERE Name=?",(name,)).fetchall()[0])!="Free Agent":
                            if random.randint(1,5)==5:
                                if GAME.scouting=="Race Engineer":
                                    oldRole=GAME.Sanitise(c.execute("SELECT Role FROM Staff WHERE Name=?",(name,)).fetchall()[0])
                                    if len(c.execute("SELECT Name FROM Staff WHERE NewRole=? AND NewTeam=?",(oldRole,oldTeam,)).fetchall())==0:
                                        rehired=1
                                elif len(c.execute("SELECT Name FROM Staff WHERE Role=? AND NewTeam=?",(GAME.scouting,oldTeam,)).fetchall())==0:
                                    oldRole=GAME.scouting
                                    rehired=1
                    if rehired==1:
                        GAME.news.append(f"BREAKING NEWS! {oldTeam} has extended their contract with")
                        GAME.news.append(f"{name} as a {GAME.scouting}.")
                        with sqlite3.connect(GAME.database) as c:
                            c.execute("UPDATE Staff SET NewTeam=?, NewRole=?, NewSalary=? WHERE Name=?",(oldTeam,oldRole,currentSalary,name,))
                        GAME.EndScouting()
                    else:
                        wantedSalary=random.randint(rating*20000,rating*50000)
                        if GAME.salary<wantedSalary or GAME.salary<currentSalary:
                            GAME.ChangeScreen("Contract Rejected")
                            root.after(3000, lambda: GAME.EndScouting())
                        else:
                            GAME.ChangeScreen("Contract")
                            GAME.Button("Hire",800,660)
                            GAME.Button("Back",5,730)
                            if GAME.team in steam:
                                appearance=GAME.team
                            else:
                                with sqlite3.connect(GAME.database) as c:
                                    appearance=GAME.Sanitise(c.execute("SELECT Appearance FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0])
                            if appearance!="0":
                                if appearance in steam:
                                    logo=logos[steam.index(appearance)-1]
                                else:
                                    logo=sponsorLogos[sponsors.index(appearance)]
                                canvas.image=logo
                                canvas.create_image(900, 80, anchor=tk.NW, image=logo)
                            salary="{:,}".format(GAME.salary)
                            canvas.create_text(445, 80, text=name, fill="black", font=("Arial", 40), anchor="nw")
                            canvas.create_text(445, 550, text=f"Salary: ${salary}", fill="black", font=("Arial", 30), anchor="nw")
                            canvas.create_text(445, 590, text=f"Rating: {rating}", fill="black", font=("Arial", 30), anchor="nw")
                            canvas.create_text(445, 300, text=GAME.scouting, fill="black", font=("Arial", 50), anchor="nw")
            else:
                modify=0
                attribute=0
                if event.x>=55 and event.x<=75:
                    modify="-"
                elif event.x>=525 and event.x<=550:
                    modify="+"
                if event.y>=335 and event.y<=375:
                    attribute=1
                elif event.y>=480 and event.y<=525:
                    attribute=2
                elif event.y>=630 and event.y<=675:
                    attribute=3
                if modify!=0 and attribute!=0:
                    with sqlite3.connect(GAME.database) as c:
                        if attribute==1:
                            #Role
                            GAME.roleOptions=[GAME.car1,GAME.car2]
                            if len(c.execute("SELECT Name FROM Drivers WHERE Name=? AND Role='Reserve'",(GAME.options[GAME.displayedName],)).fetchall())==0:
                                if len(c.execute("SELECT Name FROM Drivers WHERE Name=? AND Age<17",(GAME.options[GAME.displayedName],)).fetchall())==0:
                                    GAME.roleOptions.append("Reserve")
                                else:
                                    GAME.roleOptions.append("Junior")
                            if GAME.scouting=="Driver" or GAME.scouting=="Junior Driver":
                                if modify=="+":
                                    looped=0
                                    role=GAME.role
                                    while True:
                                        try:
                                            role=GAME.roleOptions[GAME.roleOptions.index(role)+1]
                                        except:
                                            if looped==0:
                                                role=GAME.roleOptions[0]
                                                looped=1
                                            else:
                                                looped=2
                                                break
                                        if role==GAME.car1 and len(c.execute("SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole='1'",(GAME.team,)).fetchall())==0:
                                            break
                                        elif role==GAME.car2 and len(c.execute("SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole='2'",(GAME.team,)).fetchall())==0:
                                            break
                                        elif role=="Reserve" and len(c.execute("SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole='Reserve'",(GAME.team,)).fetchall())<2:
                                            break
                                        elif role=="Junior" and len(c.execute("SELECT Name FROM Drivers WHERE NewTeam=? AND NewRole='Junior'",(GAME.team,)).fetchall())<3:
                                            break
                                    if looped<2:
                                        GAME.role=role
                            elif GAME.scouting=="Race Engineer":
                                if GAME.role==GAME.car1:
                                    if len(c.execute("SELECT Name FROM Staff WHERE NewTeam=? AND NewRole='Race Engineer 2'",(GAME.team,)).fetchall())==0:
                                        GAME.role=GAME.car2
                                elif len(c.execute("SELECT Name FROM Staff WHERE NewTeam=? AND NewRole='Race Engineer 1'",(GAME.team,)).fetchall())==0:
                                    GAME.role=GAME.car1
                        elif attribute==2:
                            #Salary
                            if GAME.promoting==0:
                                if GAME.salary<200000:
                                    amount=100000
                                elif GAME.salary<5000000:
                                    amount=500000
                                elif GAME.salary<10000000:
                                    amount=1000000
                                elif GAME.salary<20000000:
                                    amount=2000000
                                else:
                                    amount=5000000
                                if modify=="+":
                                    GAME.salary+=amount
                                else:
                                    GAME.salary-=amount
                        elif GAME.scouting=="Driver":
                            if GAME.promoting==1:
                                with sqlite3.connect(GAME.database) as c:
                                    contractEnd=int(GAME.Sanitise(c.execute("SELECT ContractEnd FROM Drivers WHERE Name=?",(GAME.options[GAME.displayedName],)).fetchall()[0]))
                                    if contractEnd>GAME.season:
                                        minimumLength=contractEnd-GAME.season
                                        maximumLength=contractEnd-GAME.season
                                        if maximumLength<3:
                                            maximumLength=3
                                    else:
                                        minimumLength=1
                                        maximumLength=3
                            else:
                                minimumLength=1
                                maximumLength=3
                            if modify=="+":
                                if GAME.contractLength<maximumLength:
                                    GAME.contractLength+=1
                            elif GAME.contractLength>minimumLength:
                                GAME.contractLength-=1
                    GAME.ContractParameters()
        elif GAME.screen=="Contract":
            if event.x>=800 and event.x<=1000 and event.y>=660 and event.y<=710:
                if GAME.scouting=="Driver":
                    with sqlite3.connect(GAME.database) as c:
                        if len(c.execute("SELECT Age FROM Drivers WHERE Name=? AND Age<17",(GAME.options[GAME.displayedName],)).fetchall())>0:
                            GAME.role="Junior Driver"
                    if GAME.role==GAME.car1:
                        role="1"
                    elif GAME.role==GAME.car2:
                        role="2"
                    elif GAME.role=="Junior Driver":
                        role="Junior"
                    else:
                        role="Reserve"
                    contractEnd=GAME.season+GAME.contractLength
                    with sqlite3.connect(GAME.database) as c:
                        c.execute('''UPDATE Drivers SET NewTeam=?, NewRole=?, NewSalary=?, ContractEnd=? WHERE Name=?''',(GAME.team, role, GAME.salary, contractEnd, GAME.options[GAME.displayedName],))
                        if GAME.buyout>0:
                            GAME.money-=GAME.buyout
                            c.execute('''UPDATE Teams SET Money=? WHERE Name=?''',(GAME.money,GAME.team,))
                            if role=="1" or role=="2":
                                c.execute("UPDATE Drivers SET ContractEnd=? WHERE Team=? AND Role=? AND NewTeam='0'",(GAME.season,GAME.team,role,))
                else:
                    if GAME.scouting=="Race Engineer":
                        if GAME.role==GAME.car1:
                            role="Race Engineer 1"
                        else:
                            role="Race Engineer 2"
                    else:
                        role=GAME.role
                    with sqlite3.connect(GAME.database) as c:
                        c.execute('''UPDATE Staff SET NewTeam=?, NewRole=?, NewSalary=? WHERE Name=?''',(GAME.team, role, GAME.salary, GAME.options[GAME.displayedName],))
                if GAME.sound==1:
                    path=os.path.join(os.path.dirname(__file__), "Sound Effects", "Sign Contract Sound.wav")
                    if os.path.isfile(path):
                        winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)
                GAME.EndScouting()
        elif GAME.screen=="Starter Drivers":
            if event.x>=600 and event.x<=800 and event.y>=730 and event.y<=780:
                GAME.displayedName=0
                GAME.SelectDriver()
        elif GAME.screen=="Choose Driver":
            if event.x>=155 and event.x<=215 and event.y>=380 and event.y<=510:
                #Back
                if GAME.displayedName==0:
                    GAME.displayedName=len(GAME.options)-1
                else:
                    GAME.displayedName-=1
                GAME.SelectDriver()
            elif event.x>=870 and event.x<=940 and event.y>=375 and event.y<=515:
                #Forward
                if GAME.displayedName==len(GAME.options)-1:
                    GAME.displayedName=0
                else:
                    GAME.displayedName+=1
                GAME.SelectDriver()
            elif event.x>=1100 and event.x<=1300 and event.y>=420 and event.y<=470:
                #Hire
                with sqlite3.connect(GAME.database) as c:
                    if GAME.car1=="":
                        GAME.car1=GAME.options[GAME.displayedName]
                        role="1"
                    else:
                        GAME.car2=GAME.options[GAME.displayedName]
                        role="2"
                    c.execute("UPDATE Drivers SET Team=?, Role=?, ContractEnd=2026, NewTeam='0' WHERE Name=?",(GAME.team,role,GAME.options[GAME.displayedName],))
                if GAME.car2=="":
                    GAME.DisplayDriverMarket()
                elif GAME.team=="Marlboro Ferrari" or GAME.team=="Vodafone McLaren" or GAME.team=="West McLaren":
                    if GAME.team=="Malboro Ferrari":
                        GAME.engine="Ferrari"
                    else:
                        GAME.engine="Mercedes"
                    with sqlite3.connect(GAME.database) as c:
                        c.execute("UPDATE Cars SET Engine=? WHERE Team=?",(GAME.engine,GAME.team,))
                    GAME.TeamData()
                else:
                    GAME.ChangeScreen("Choose Engine 1")
        elif GAME.screen=="Next Engine":
            if event.x>=155 and event.x<=215 and event.y>=480 and event.y<=610:
                #Back
                if GAME.displayed==0:
                    GAME.displayed=len(GAME.options)-1
                else:
                    GAME.displayed-=1
                GAME.NextEngine()
            elif event.x>=870 and event.x<=940 and event.y>=475 and event.y<=615:
                #Forward
                if GAME.displayed==len(GAME.options)-1:
                    GAME.displayed=0
                else:
                    GAME.displayed+=1
                GAME.NextEngine()
            elif event.x>=1100 and event.x<=1300 and event.y>=520 and event.y<=570:
                #Choose
                engineChoice=GAME.options[GAME.displayed]
                with sqlite3.connect(GAME.database) as c:
                    if engineChoice=="No Change":
                        c.execute('''UPDATE Player SET NextYearEngine=?''',(GAME.engine,))
                    else:
                        c.execute('''UPDATE Player SET NextYearEngine=?''',(engineChoice,))
                        if engineChoice==GAME.team and len(c.execute("SELECT Name FROM Engines WHERE Manufacturer=?",(GAME.team,)).fetchall())==0:
                            c.execute("UPDATE Engines SET Manufacturer='None' WHERE Manufacturer=?",(GAME.team,))
                            c.execute('''INSERT into Engines (Name, Manufacturer, Power, Reliability, Research) VALUES (?, ?, 0, 0, 1)''',(GAME.team,GAME.team,))
                            reputation=int(GAME.Sanitise(c.execute('''SELECT Reputation FROM Teams WHERE Name=?''',(GAME.team,)).fetchall()[0]))+5
                            c.execute('''UPDATE Teams SET Reputation=? WHERE Name=?''',(reputation,GAME.team,))
                        else:
                            if engineChoice=="Honda":
                                c.execute("UPDATE Engines SET Manufacturer=? WHERE Name='Honda'",(GAME.team,))
                            if len(c.execute('''SELECT Name FROM Engines WHERE Name=?''',(GAME.team,)).fetchall())>0:
                                c.execute('''DELETE FROM Engines WHERE Name=?''',(GAME.team,))
                                reputation=int(GAME.Sanitise(c.execute('''SELECT Reputation FROM Teams WHERE Name=?''',(GAME.team,)).fetchall()[0]))-5
                                if reputation<1:
                                    c.execute('''UPDATE Teams SET Reputation=1 WHERE Name=?''',(GAME.team,))
                                else:
                                    c.execute('''UPDATE Teams SET Reputation=? WHERE Name=?''',(reputation,GAME.team,))
                GAME.Menu()
        elif GAME.screen=="Expectations":
            if event.x>=155 and event.x<=215 and event.y>=480 and event.y<=610:
                #Back
                if GAME.displayed==0:
                    GAME.displayed=len(GAME.options)-1
                else:
                    GAME.displayed-=1
                GAME.Expectations()
            elif event.x>=870 and event.x<=940 and event.y>=475 and event.y<=615:
                #Forward
                if GAME.displayed==len(GAME.options)-1:
                    GAME.displayed=0
                else:
                    GAME.displayed+=1
                GAME.Expectations()
            elif event.x>=1100 and event.x<=1300 and event.y>=520 and event.y<=570:
                #Choose
                GAME.expected=[GAME.team,GAME.options[GAME.displayed]]
                GAME.Menu()
        elif GAME.screen=="Replacing" or GAME.screen=="Replacement":
            if event.x>=255 and event.x<=315 and event.y>=135 and event.y<=255:
                #Back
                if GAME.displayed==0:
                    GAME.displayed=len(GAME.options)-1
                else:
                    GAME.displayed-=1
                if GAME.screen=="Replacing":
                    GAME.SelectDriverToReplace()
                else:
                    GAME.SelectReplacement()
            elif event.x>=975 and event.x<=1035 and event.y>=125 and event.y<=260:
                #Forward
                if GAME.displayed==len(GAME.options)-1:
                    GAME.displayed=0
                else:
                    GAME.displayed+=1
                if GAME.screen=="Replacing":
                    GAME.SelectDriverToReplace()
                else:
                    GAME.SelectReplacement()
            elif event.x>=1100 and event.x<=1300 and event.y>=170 and event.y<=220:
                #Choose
                if GAME.screen=="Replacing":
                    GAME.replacing=GAME.options[GAME.displayed]
                    GAME.options=[]
                    with sqlite3.connect(GAME.database) as c:
                        if GAME.team=="Red Bull":
                            for x in range(2):
                                try:
                                    GAME.options.append(GAME.Sanitise(c.execute("SELECT Name FROM Drivers WHERE Team='Racing Bulls' AND Role=?",(str(x+1),)).fetchall()[0]))
                                except:
                                    q=7
                        elif GAME.team=="Racing Bulls":
                            f=c.execute("SELECT Name FROM Drivers WHERE Role='Reserve' AND Team='Red Bull'").fetchall()
                            for x in range(len(f)):
                                GAME.options.append(GAME.Sanitise(f[x]))
                        f=c.execute("SELECT Name FROM Drivers WHERE Role='Reserve' AND Team=?",(GAME.team,)).fetchall()
                        for x in range(len(f)):
                            GAME.options.append(GAME.Sanitise(f[x]))
                    GAME.displayedName=0
                    GAME.SelectReplacement()
                else:
                    replacement=GAME.options[GAME.displayed]
                    with sqlite3.connect(GAME.database) as c:
                        seat=GAME.Sanitise(c.execute("SELECT Role FROM Drivers WHERE Name=?",(GAME.replacing,)).fetchall())
                        role=GAME.Sanitise(c.execute("SELECT Role FROM Drivers WHERE Name=?",(replacement,)).fetchall())
                        c.execute("UPDATE Drivers SET Team=?, Role=? WHERE Name=?",(GAME.team,seat,replacement,))
                        c.execute("UPDATE Drivers SET Role=? WHERE Name=?",(role,GAME.replacing,))
                        if GAME.team=="Red Bull" and role!="Reserve":
                            c.execute("UPDATE Drivers SET Team='Racing Bulls' WHERE Name=?",(GAME.replacing,))
                        elif GAME.team=="Racing Bulls":
                            if len(c.execute("SELECT Name FROM Teams WHERE Name='Red Bull'").fetchall())==1:
                                c.execute("UPDATE Drivers SET Team='Red Bull' WHERE Name=?",(GAME.replacing,))
                    if seat=="1":
                        GAME.car1=replacement
                    else:
                        GAME.car2=replacement
                    GAME.Menu()
        elif GAME.screen=="Rule Vote":
            if GAME.vote==0:
                if event.x>=350 and event.x<=550 and event.y>=450 and event.y<=500:
                    #Against
                    GAME.vote="Against"
                elif event.x>=890 and event.x<=1090 and event.y>=450 and event.y<=500:
                    #For
                    GAME.vote="For"
                if GAME.vote!=0:
                    GAME.Voted()
            elif event.x>=1200 and event.x<=1400 and event.y>=600 and event.y<=650:
                GAME.RaceTime()
        elif GAME.screen=="Choose Renewal":
            if event.x>=155 and event.x<=215 and event.y>=380 and event.y<=510:
                #Back
                if GAME.displayed==0:
                    GAME.displayed=len(GAME.options)-1
                else:
                    GAME.displayed-=1
                GAME.SelectRenewal()
            elif event.x>=870 and event.x<=940 and event.y>=375 and event.y<=515:
                #Forward
                if GAME.displayed==len(GAME.options)-1:
                    GAME.displayed=0
                else:
                    GAME.displayed+=1
                GAME.SelectRenewal()
            elif event.x>=1100 and event.x<=1300 and event.y>=420 and event.y<=470:
                #Choose
                GAME.contractLength=1
                GAME.Renewal()
        elif GAME.screen=="Renewal":
            if event.y>=380 and event.y<=425 and (GAME.role=="1" or GAME.role=="2" or GAME.role=="Reserve" or GAME.role=="Junior"):
                if event.x>=50 and event.x<=75:
                    #Back
                    if GAME.contractLength<2:
                        GAME.contractLength=1
                    else:
                        GAME.contractLength-=1
                    GAME.Renewal()
                elif event.x>=325 and event.x<=345:
                    #Forward
                    if GAME.contractLength>2:
                        GAME.contractLength=3
                    else:
                        GAME.contractLength+=1
                    GAME.Renewal()
            elif event.x>=800 and event.x<=1000 and event.y>=660 and event.y<=710:
                #Renew
                with sqlite3.connect(GAME.database) as c:
                    if GAME.role=="1" or GAME.role=="2" or GAME.role=="Reserve" or GAME.role=="Junior":
                        if (GAME.role=="Reserve" or GAME.role=="Junior") and GAME.team=="Racing Bulls" and len(c.execute("SELECT Name FROM Teams WHERE Name='Red Bull'").fetchall())>0:
                            team="Red Bull"
                        else:
                            team=GAME.team
                        c.execute("UPDATE Drivers SET NewTeam=?, NewRole=?, NewSalary=?, ContractEnd=? WHERE Name=?",(team,GAME.role,GAME.salary,GAME.season+GAME.contractLength,GAME.options[GAME.displayed],))
                    else:
                        c.execute("UPDATE Staff SET NewTeam=?, NewRole=?, NewSalary=? WHERE Name=?",(GAME.team,GAME.role,GAME.salary,GAME.options[GAME.displayed],))
                if GAME.sound==1:
                    path=os.path.join(os.path.dirname(__file__), "Sound Effects", "Sign Contract Sound.wav")
                    if os.path.isfile(path):
                        winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)
                GAME.Menu()
        elif GAME.screen=="New Tyres":
            tyre=0
            if event.x>=5 and event.x<=220 and event.y>=110 and event.y<=320:
                tyre="Soft"
            elif event.x>=5 and event.x<=220 and event.y>=330 and event.y<=540:
                tyre="Medium"
            elif event.x>=5 and event.x<=220 and event.y>=545 and event.y<=780:
                tyre="Hard"
            elif event.x>=945 and event.x<=1160 and event.y>=280 and event.y<=505:
                tyre="Intermediate"
            elif event.x>=945 and event.x<=1160 and event.y>=535 and event.y<=760:
                tyre="Wet"
            if tyre!=0:
                if GAME.tyre[GAME.car1ID]=="Placeholder":
                    driver=1
                    index=GAME.car1ID
                else:
                    driver=2
                    index=GAME.car2ID
                if tyre!=GAME.tyre[index]:
                    compounds=GAME.tyreCompoundsUsed[index]+1
                    GAME.tyreCompoundsUsed.pop(index)
                    GAME.tyreCompoundsUsed.insert(index,compounds)
                GAME.tyre.pop(index)
                GAME.tyre.insert(index,tyre)
                if driver==1 and GAME.car2ID in GAME.positions:
                    GAME.ChooseNewTyres()
                else:
                    GAME.pause=1
                    GAME.Start()
        elif GAME.screen=="Final Standings":
            if event.x>=1200 and event.x<=1400 and event.y>=730 and event.y<=780:
                if GAME.sound==1:
                    GAME.StopMusic()
                GAME.RaceTime()
        elif GAME.screen=="Change Team":
            if GAME.done==0:
                GAME.done=1
            else:
                column=-1
                row=-1
                if event.x>=700 and event.x<=930:
                    column=0
                elif event.x>=1150 and event.x<=1650:
                    column=1
                if event.y<=50:
                    row=0
                elif event.y>=160 and event.y<=210:
                    row=1
                elif event.y>=290 and event.y<=340:
                    row=2
                elif event.y>=420 and event.y<=470:
                    row=3
                elif event.y>=550 and event.y<=600:
                    row=4
                elif event.y>=680 and event.y<=730:
                    row=5
                if column!=-1 and row!=-1:
                    i=row+(column*6)
                    if len(GAME.options)>i and (GAME.fired==0 or i!=0):
                        GAME.oldTeam=GAME.team
                        GAME.team=GAME.options[i]
                        GAME.BackgroundColour()
                        if GAME.oldTeam==GAME.team:
                            GAME.oldTeam=0
                        if GAME.team=="Create New Team":
                            root.configure(background='black')
                            GAME.CreateTeam()
                        else:
                            GAME.race+=1
                            with sqlite3.connect(GAME.database) as c:
                                if GAME.oldTeam!=0:
                                    c.execute("UPDATE Player SET Team=?, Financial=5, Management=3, Warnings=0",(GAME.team,))
                                    c.execute("UPDATE Teams SET TeamPrincipal=? WHERE Name=?",(GAME.name,GAME.team,))
                                    c.execute("UPDATE Teams SET TeamPrincipal='None' WHERE Name=?",(GAME.oldTeam,))
                                c.execute("UPDATE Player SET Race=?",(GAME.race,))
                            GAME.BackgroundColour()
                            GAME.RaceTime()
        elif GAME.screen=="Sponsor Negotiation":
            choice=0
            if event.x>=350 and event.x<=550 and event.y>=450 and event.y<=500:
                #Decline
                choice="Decline"
            elif event.x>=890 and event.x<=1090 and event.y>=450 and event.y<=500:
                #Accept
                choice="Accept"
                GAME.sponsor=GAME.displayed
                with sqlite3.connect(GAME.database) as c:
                    c.execute("UPDATE Teams SET Sponsor=? WHERE Name=?",(GAME.sponsor,GAME.team,))
                    c.execute("UPDATE Sponsors SET Team='None' WHERE Team=?",(GAME.team,))
                    c.execute("UPDATE Sponsors SET Team=? WHERE Name=?",(GAME.team,GAME.sponsor,))
                GAME.news.append(f"BREAKING NEWS! {GAME.team} has signed {GAME.sponsor}")
                GAME.news.append(f"as their Title Sponsor for the {GAME.season} season.")
            if choice!=0:
                GAME.PreSeasonEvents()
        elif GAME.screen=="Replay screen":
            if event.x>=5 and event.x<=205 and event.y>=730 and event.y<=780:
                GAME.ChangeScreen("Title Screen")
            elif event.x>=320 and event.x<=1120:
                if event.y>=20 and event.y<=120:
                    GAME.replay=2
                elif event.y>=145 and event.y<=245:
                    GAME.replay=1
                elif event.y>=270 and event.y<=370:
                    GAME.replay=3
                elif event.y>=395 and event.y<=495:
                    GAME.replay=4
                elif event.y>=520 and event.y<=620:
                    GAME.replay=5
                elif event.y>=645 and event.y<=745:
                    GAME.replay=6
                if GAME.replay!=0:
                    GAME.ReplayObjective()
        elif GAME.screen=="Safety Car Menu":
            tyre=-1
            if event.y>=235 and event.y<=325:
                if event.x>=515 and event.x<=605:
                    tyre="Soft"
                elif event.x>=810 and event.x<=910:
                    tyre="Medium"
                elif event.x>=1110 and event.x<=1210:
                    tyre="Hard"
            if event.x>=980 and event.x<=1080:
                if event.y>=350 and event.y<=450:
                    tyre="Intermediate"
                elif event.y>=475 and event.y<=565:
                    tyre="Wet"
            if event.x>=980 and event.x<=1180 and event.y>=620 and event.y<=670:
                tyre=0
            if tyre!=-1:
                if tyre!=0:
                    if GAME.displayed==1:
                        GAME.pitting.append(GAME.driver1)
                    else:
                        GAME.pitting.append(GAME.driver2)
                    GAME.SCPitTyre.append(tyre)
                    if GAME.replay==9 and GAME.displayed==1:
                        GAME.pit=1
                if GAME.displayed==1:
                    GAME.displayed=2
                    GAME.SCMenu()
                else:
                    GAME.EndSafetyCar()
        elif GAME.screen=="Red Flag Menu":
            tyre=-1
            if event.y>=235 and event.y<=325:
                if event.x>=515 and event.x<=605:
                    tyre="Soft"
                elif event.x>=810 and event.x<=910:
                    tyre="Medium"
                elif event.x>=1110 and event.x<=1210:
                    tyre="Hard"
            if event.x>=980 and event.x<=1080:
                if event.y>=350 and event.y<=450:
                    tyre="Intermediate"
                elif event.y>=475 and event.y<=565:
                    tyre="Wet"
            if tyre!=-1:
                if GAME.displayed==1:
                    index=GAME.car1ID
                else:
                    index=GAME.car2ID
                if tyre!=GAME.tyre[index]:
                    GAME.tyreCompoundsUsed[index]+=1
                    GAME.tyre.pop(index)
                    GAME.tyre.insert(index,tyre)
                if GAME.displayed==1:
                    GAME.displayed=2
                    GAME.RedFlagMenu()
                else:
                    GAME.pause=1
                    GAME.safety=0
                    GAME.RefreshScreen()
                    GAME.Start()
        elif GAME.screen=="Team Offer":
            choice=0
            if event.x>=350 and event.x<=550 and event.y>=550 and event.y<=600:
                #Decline
                choice="Decline"
            elif event.x>=890 and event.x<=1090 and event.y>=550 and event.y<=600:
                #Accept
                choice="Accept"
                with sqlite3.connect(GAME.database) as c:
                    c.execute("UPDATE Player SET MovingTo=?",(GAME.offer,))
            if choice!=0:
                GAME.Menu()
        elif GAME.screen=="Choose a Team 2021":
            if event.x>405:
                GAME.team="Mercedes"
                GAME.car1="Lewis Hamilton"
                GAME.car2="Valtteri Bottas"
                GAME.car1ID=1
                GAME.car2ID=5
            else:
                GAME.team="Red Bull"
                GAME.car1="Max Verstappen"
                GAME.car2="Sergio Perez"
                GAME.car1ID=0
                GAME.car2ID=3
            GAME.driver1=GAME.car1
            GAME.driver2=GAME.car2
            GAME.BackgroundColour()
            GAME.AbuDhabi2021()
        elif GAME.screen=="Reserve Options":
            if event.x>=1150 and event.x<=1350:
                if event.y>=140 and event.y<=190+((len(GAME.options)-1)*60):
                    button=(event.y-140)//60
                    if event.y<=190+(button*60):
                        #Hire
                        with sqlite3.connect(GAME.database) as c:
                            driver=GAME.options[button]
                            contractEnd=int(GAME.Sanitise(c.execute("SELECT ContractEnd FROM Drivers WHERE Name=?",(driver,)).fetchall()[0]))
                            if contractEnd==0:
                                contractEnd=GAME.season
                            salary=int(GAME.Sanitise(c.execute("SELECT Salary FROM Drivers WHERE Name=?",(driver,)).fetchall()[0]))
                            if salary<3000000:
                                salary=3000000
                            c.execute("UPDATE Drivers SET Team=?, Role='Reserve', Salary=?, ContractEnd=? WHERE Name=?",(GAME.team,salary,contractEnd,driver,))
                        GAME.Menu()
        elif GAME.screen=="Replay Grid":
            if event.x>=1200 and event.x<=1400 and event.y>=725 and event.y<=775:
                GAME.aggressions=[3,2,2]
                GAME.driver=1
                if GAME.replay==1 or GAME.replay==2:
                    GAME.ChooseStartingTyres()
                else:
                    GAME.ChooseStartingAggression()
        elif GAME.screen=="Choose a Team 2000":
            GAME.team=0
            if event.x>=1200:
                GAME.team="Ferrari"
                GAME.driver1="Michael Schumacher"
                GAME.driver2="Rubens Barrichello"
                GAME.car1ID=3
                GAME.car2ID=9
            elif event.x<=240:
                GAME.team="McLaren"
                GAME.driver1="Mika Hakkinen"
                GAME.driver2="David Coulthard"
                GAME.car1ID=0
                GAME.car2ID=4
            if GAME.team!=0:
                GAME.BackgroundColour()
                GAME.Spa2000()
        elif GAME.screen=="Choose a Team 2008":
            if event.x>405:
                GAME.team="Ferrari"
                GAME.driver1="Felipe Massa"
                GAME.driver2="Kimi Raikkonen"
                GAME.car1ID=0
                GAME.car2ID=2
            else:
                GAME.team="McLaren"
                GAME.driver1="Lewis Hamilton"
                GAME.driver2="Heikki Kovalainen"
                GAME.car1ID=3
                GAME.car2ID=4
            GAME.BackgroundColour()
            GAME.Brazil2008()
        elif GAME.screen=="Settings":
            if event.x>=5 and event.x<=205 and event.y>=730 and event.y<=780:
                GAME.ChangeScreen("Title Screen")
            if event.x>=150 and event.x<=200 and event.y>=200 and event.y<=250:
                GAME.sound=1-GAME.sound
                if GAME.sound==0:
                    GAME.StopMusic()
                    GAME.music=0
                GAME.Settings()
            elif event.x>=150 and event.x<=200 and event.y>=400 and event.y<=450 and GAME.sound==1:
                GAME.music=1-GAME.music
                if GAME.music==0:
                    GAME.StopMusic()
                else:
                    sound_path = os.path.join(os.path.dirname(__file__), "Music", "F1 Music.wav")
                    if os.path.isfile(sound_path):
                        winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
                GAME.Settings()
        elif GAME.screen=="Select Save File":
            if event.x>=265 and event.x<=1160 and event.y>=260 and event.y<=600 and GAME.loaded==1:
                GAME.database=f"F1 Manager 26 Save Data {GAME.database}.db"
                GAME.LoadGame()
            elif event.x>=1210 and event.x<=1325 and event.y>=330 and event.y<=480:
                GAME.database+=1
                GAME.ViewSave()
            elif event.x>=5 and event.x<=205 and event.y>=730 and event.y<=780:
                GAME.ChangeScreen("Title Screen")
        elif GAME.screen=="Calendar":
            if event.x>=5 and event.x<=205 and event.y>=720 and event.y<=770:
                GAME.Menu()
    def SaveScreen(self):
        if os.path.isfile(GAME.database):
            GAME.ChangeScreen("Save Screen")
        else:
            GAME.ChangeScreen("Missing Required Files")
    def CarData(self):
        GAME.CarRanking()
        GAME.ChangeScreen("Car Data")
        GAME.DisplayLogo()
        canvas.create_text(40, 5, text="Aero Ranking", fill="white", font=("Arial", 100), anchor="nw")
        with sqlite3.connect(GAME.database) as c:
            f=c.execute("SELECT Name FROM Teams").fetchall()
            for x in range(len(f)):
                team=GAME.Sanitise(c.execute("SELECT Team FROM Cars WHERE Ranking=?",(x+1,)).fetchall()[0])
                engine=GAME.Sanitise(c.execute('''SELECT Engine FROM Cars WHERE Team=?''',(team,)).fetchall()[0])
                if engine=="Red Bull":
                    if "ford" in team.lower():
                        engine=""
                    else:
                        engine="Ford RBPT"
                if engine in team:
                     engine=""
                if x<9:
                    canvas.create_text(40, 150+(x*45), text=f"{x+1}. {team} {engine}", fill="white", font=("Arial", 30), anchor="nw")
                else:
                    canvas.create_text(35, 150+(x*45), text=f"{x+1}. {team} {engine}", fill="white", font=("Arial", 30), anchor="nw")
        if GAME.engine=="Red Bull":
            engine="Ford RBPT"
        else:
            engine=GAME.engine
        canvas.create_text(870, 150, text=f"Engine: {engine}", fill="white", font=("Arial", 40), anchor="nw")
        with sqlite3.connect(GAME.database) as c:
            EN1=int(GAME.Sanitise(c.execute("SELECT car1Engine FROM Cars WHERE Team=?",(GAME.team,)).fetchall()[0]))
            EN2=int(GAME.Sanitise(c.execute("SELECT car2Engine FROM Cars WHERE Team=?",(GAME.team,)).fetchall()[0]))
            if str(EN1)[len(str(EN1))-1]=="1":
                suffix1="st"
            elif str(EN1)[len(str(EN1))-1]=="2":
                suffix1="nd"
            elif str(EN1)[len(str(EN1))-1]=="3":
                suffix1="rd"
            else:
                suffix1="th"
            if str(EN2)[len(str(EN2))-1]=="1":
                suffix2="st"
            elif str(EN2)[len(str(EN2))-1]=="2":
                suffix2="nd"
            elif str(EN2)[len(str(EN2))-1]=="3":
                suffix2="rd"
            else:
                suffix2="th"
            ED1=int(GAME.Sanitise(c.execute("SELECT car1EngineDurability FROM Cars WHERE Team=?",(GAME.team,)).fetchall()[0]))
            ED2=int(GAME.Sanitise(c.execute("SELECT car2EngineDurability FROM Cars WHERE Team=?",(GAME.team,)).fetchall()[0]))
        canvas.create_text(870, 200, text=f"Car 1: {EN1}{suffix1} Engine {ED1}%", fill="white", font=("Arial", 40), anchor="nw")
        canvas.create_text(870, 250, text=f"Car 2: {EN2}{suffix2} Engine {ED2}%", fill="white", font=("Arial", 40), anchor="nw")
        #Engine Ranking
        canvas.create_text(870, 375, text="Engine Ranking", fill="white", font=("Arial", 40), anchor="nw")
        with sqlite3.connect(GAME.database) as c:
            f=c.execute("SELECT Name FROM Engines WHERE Power>0").fetchall()
            scores=[]
            engines=[]
            i=len(f)
            for x in range(i):
                engine=GAME.Sanitise(f[x])
                score=int(GAME.Sanitise(c.execute("SELECT Power FROM Engines WHERE Name=?",(engine,)).fetchall()[0]))*5
                score+=int(GAME.Sanitise(c.execute("SELECT Reliability FROM Engines WHERE Name=?",(engine,)).fetchall()[0]))*3
                score+=int(GAME.Sanitise(c.execute("SELECT Battery FROM Engines WHERE Name=?",(engine,)).fetchall()[0]))*4
                scores.append(score)
            for x in range(i):
                highest=0
                highestIndex=0
                for y in range(len(f)):
                    if scores[y]>highest:
                        highest=scores[y]
                        highestIndex=y
                engine=GAME.Sanitise(f[highestIndex])
                if engine=="Red Bull":
                    engine="Ford RBPT"
                engines.append(engine)
                f.pop(highestIndex)
                scores.pop(highestIndex)
            for x in range(i):
                canvas.create_text(870, 445+(x*45), text=f"{x+1}. {engines[x]}", fill="white", font=("Arial", 30), anchor="nw")
        GAME.Button("Switch Engine 1",960,320)
        GAME.Button("Switch Engine 2",1180,320)
        GAME.Button("Back",5,730)
        GAME.DisplayMoney()
    def UpgradePage(self):
        GAME.ChangeScreen("Upgrade")
        GAME.DisplayLogo()
        GAME.DisplayMoney()
        for x in range(len(GAME.upgradePoints)):
            GAME.Button("Upgrade Attribute",50,180+(x*70))
            canvas.create_text(90, 190+(x*70), text=GAME.attributes[x], fill="black", font=("Arial", 20), anchor="nw")
            if GAME.upgradePoints[x]==1:
                canvas.create_text(410, 190+(x*70), text="1 Point", fill="black", font=("Arial", 20), anchor="nw")
            else:
                canvas.create_text(410, 190+(x*70), text=f"{GAME.upgradePoints[x]} Points", fill="black", font=("Arial", 20), anchor="nw")
        canvas.create_text(1080, 160, text="Remaining Available", fill="black", font=("Arial", 30), anchor="nw")
        canvas.create_text(1120, 200, text="Upgrade Points:", fill="black", font=("Arial", 30), anchor="nw")
        canvas.create_text(1220, 240, text=GAME.remainingUpgradePoints, fill="black", font=("Arial", 40), anchor="nw")
        canvas.create_text(1080, 330, text=f"Cost: ${'{:,}'.format((GAME.maximumUpgradePoints-GAME.remainingUpgradePoints)*500000)}", fill="black", font=("Arial", 30), anchor="nw")
        GAME.Button("Upgrade",1150,500)
        GAME.Button("Back",5,730)
    def AerodynamicResearch(self):
        GAME.ChangeScreen("Research")
        GAME.DisplayMoney()
        GAME.DisplayLogo()
        maxResearch=(round(GAME.money/3)//100000)*100000
        try:
            research=int(simpledialog.askstring(" ", f"Maximum ${'{:,}'.format(maxResearch)}"))
        except:
            research=0
        if research<1 or research>maxResearch:
            GAME.Menu()
        else:
            GAME.money-=research
            with sqlite3.connect(GAME.database) as c:
                rating=int(GAME.Sanitise(c.execute('''SELECT Rating FROM Staff WHERE Team=? AND Role="Technical Director"''',(GAME.team,)).fetchall()[0]))
                research=research*(rating**3)*random.randint(2,3)
                if len(c.execute("SELECT Name FROM Engines WHERE Manufacturer=?",(GAME.team,)).fetchall())>0:
                    research=round(research*1.5)
                research+=int(GAME.Sanitise(c.execute('''SELECT Research FROM Cars WHERE Team=?''',(GAME.team,)).fetchall()[0]))
                c.execute('''UPDATE Cars SET Research=? WHERE Team=?''',(research, GAME.team,))
                c.execute('''UPDATE Teams SET Money=? WHERE Name=?''',(GAME.money, GAME.team,))
            GAME.action=1
            GAME.Menu()
    def ResearchEngine(self):
        GAME.ChangeScreen("Research")
        GAME.DisplayMoney()
        GAME.DisplayLogo()
        try:
            research=int(simpledialog.askstring(" ", "Engine Research"))
        except:
            research=0
        if research<1:
            GAME.Menu()
        else:
            GAME.money-=research
            with sqlite3.connect(GAME.database) as c:
                engine=GAME.Sanitise(c.execute("SELECT Name FROM Engines WHERE Manufacturer=?",(GAME.team,)).fetchall()[0])
                rating=int(GAME.Sanitise(c.execute('''SELECT Rating FROM Staff WHERE Team=? AND Role="Technical Director"''',(GAME.team,)).fetchall()[0]))
                research=research*(rating**3)*random.randint(2,3)
                if engine=="Honda":
                    research=round(research*1.5)
                research+=int(GAME.Sanitise(c.execute('''SELECT Research FROM Engines WHERE Name=?''',(engine,)).fetchall()[0]))
                c.execute('''UPDATE Engines SET Research=? WHERE Name=?''',(research, engine,))
                c.execute('''UPDATE Teams SET Money=? WHERE Name=?''',(GAME.money, GAME.team,))
            GAME.Menu()
    def ViewContracts(self):
        GAME.ChangeScreen("View Contracts")
        GAME.Button("Back",5,730)
        canvas.create_text(150, 100, text="Name", fill="black", font=("Arial", 20), anchor="nw")
        canvas.create_text(550, 100, text="Role", fill="black", font=("Arial", 20), anchor="nw")
        canvas.create_text(820, 100, text="Age", fill="black", font=("Arial", 20), anchor="nw")
        canvas.create_text(900, 100, text="Rating", fill="black", font=("Arial", 20), anchor="nw")
        canvas.create_text(1000, 100, text="Salary", fill="black", font=("Arial", 20), anchor="nw")
        canvas.create_text(1120, 100, text="Contract End", fill="black", font=("Arial", 20), anchor="nw")
        counter=0
        #Drivers
        for x in range(2):
            if x==0:
                driver=GAME.car1
            else:
                driver=GAME.car2
            with sqlite3.connect(GAME.database) as c:
                salary="$"+str("{:,}".format(int(GAME.Sanitise(c.execute("SELECT Salary FROM Drivers WHERE Name=?",(driver,)).fetchall()[0]))))
                newTeam=GAME.Sanitise(c.execute("SELECT NewTeam FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                if newTeam=="0" or newTeam==GAME.team:
                    contractEnd=GAME.Sanitise(c.execute("SELECT ContractEnd FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                else:
                    contractEnd=GAME.season
                rating=GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                age=GAME.Sanitise(c.execute("SELECT Age FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
            canvas.create_text(150, 150+(counter*50), text=driver, fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(550, 150+(counter*50), text="Driver", fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(820, 150+(counter*50), text=age, fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(920, 150+(counter*50), text=rating, fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(1000, 150+(counter*50), text=salary, fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(1200, 150+(counter*50), text=contractEnd, fill="black", font=("Arial", 20), anchor="nw")
            counter+=1
        #Staff
        staff=["Technical Director","Sporting Director","Race Engineer 1","Race Engineer 2"]
        for x in range(4):
            with sqlite3.connect(GAME.database) as c:
                name=GAME.Sanitise(c.execute("SELECT Name FROM Staff WHERE Role=? AND Team=?",(staff[x],GAME.team,)).fetchall()[0])
                salary="$"+str("{:,}".format(int(GAME.Sanitise(c.execute("SELECT Salary FROM Staff WHERE Name=?",(name,)).fetchall()[0]))))
                contractEnd=GAME.season
                if GAME.Sanitise(c.execute("SELECT NewTeam FROM Staff WHERE Name=?",(name,)).fetchall()[0])==GAME.team:
                    contractEnd+=1
                rating=GAME.Sanitise(c.execute("SELECT Rating FROM Staff WHERE Name=?",(name,)).fetchall()[0])
            if x>1:
                role="Race Engineer"
            else:
                role=staff[x]
            canvas.create_text(150, 150+(counter*50), text=name, fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(550, 150+(counter*50), text=role, fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(920, 150+(counter*50), text=rating, fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(1000, 150+(counter*50), text=salary, fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(1200, 150+(counter*50), text=contractEnd, fill="black", font=("Arial", 20), anchor="nw")
            counter+=1
        with sqlite3.connect(GAME.database) as c:
            if len(c.execute("SELECT Name FROM Drivers WHERE (Role='Reserve' OR Role='Junior') AND Team=?",(GAME.team,)).fetchall())>0:
                GAME.Button("Reserve & Junior Drivers",600,730)
            elif GAME.team=="Racing Bulls":
                if len(c.execute("SELECT Name FROM Drivers WHERE (Role='Reserve' OR Role='Junior') AND Team='Red Bull'").fetchall())>0:
                    GAME.Button("Reserve & Junior Drivers",600,730)
        GAME.Button("Renew",1220,730)
    def MinimumRating(self):
        GAME.ChangeScreen("Minimum Rating")
        try:
            minimumRating=int(GAME.Sanitise(simpledialog.askstring(" ", "Minimum Rating:")))
        except:
            minimumRating=0
        return(minimumRating)
    def ScoutStaff(self,role):
        GAME.scouting=role
        Staff=GAME.StaffSuitability(GAME.team,role)
        if len(Staff)>0:
            minimumRating=GAME.MinimumRating()
            GAME.ChangeScreen("Staff List")
            GAME.Button("Back",5,730)
            GAME.Button("Propose Contract",1220,730)
            staff=[]
            for x in range(len(Staff)):
                with sqlite3.connect(GAME.database) as c:
                    if int(GAME.Sanitise(c.execute("SELECT Rating FROM Staff WHERE Name=?",(Staff[x],)).fetchall()[0]))>=minimumRating:
                        staff.append(Staff[x])
            if len(staff)>0:
                if len(staff)>10:
                    s=staff.copy()
                    staff=[]
                    for x in range(10):
                        name=random.choice(s)
                        s.remove(name)
                        staff.append(name)
                canvas.create_text(150, 100, text="Name", fill="black", font=("Arial", 20), anchor="nw")
                canvas.create_text(450, 100, text="Team", fill="black", font=("Arial", 20), anchor="nw")
                canvas.create_text(780, 100, text="Rating", fill="black", font=("Arial", 20), anchor="nw")
                canvas.create_text(900, 100, text="Salary", fill="black", font=("Arial", 20), anchor="nw")
                canvas.create_text(1100, 100, text="Contract End", fill="black", font=("Arial", 20), anchor="nw")
                for x in range(len(staff)):
                    name=staff[x]
                    with sqlite3.connect(GAME.database) as c:
                        salary="$"+str("{:,}".format(int(GAME.Sanitise(c.execute("SELECT Salary FROM Staff WHERE Name=?",(name,)).fetchall()[0]))))
                        if salary=="$0":
                            salary="-"
                        team=GAME.Sanitise(c.execute("SELECT Team FROM Staff WHERE Name=?",(name,)).fetchall()[0])
                        if team=="Free Agent":
                            contractEnd="-"
                        else:
                            contractEnd=GAME.season
                        rating=GAME.Sanitise(c.execute("SELECT Rating FROM Staff WHERE Name=?",(name,)).fetchall()[0])
                    canvas.create_text(150, 150+(x*50), text=name, fill="black", font=("Arial", 20), anchor="nw")
                    canvas.create_text(450, 150+(x*50), text=team, fill="black", font=("Arial", 20), anchor="nw")
                    canvas.create_text(800, 150+(x*50), text=rating, fill="black", font=("Arial", 20), anchor="nw")
                    canvas.create_text(900, 150+(x*50), text=salary, fill="black", font=("Arial", 20), anchor="nw")
                    canvas.create_text(1150, 150+(x*50), text=contractEnd, fill="black", font=("Arial", 20), anchor="nw")
                GAME.options=staff.copy()
            else:
                GAME.Menu()
        else:
            GAME.Menu()
    def SelectContractName(self):
        GAME.ChangeScreen("Contract Name")
        GAME.Button("Name Selector",150,350)
        if GAME.promoting==0:
            GAME.Button("Propose Contract",1100,420)
        else:
            GAME.Button("Promote",1100,420)
        GAME.Button("Back",5,730)
        GAME.DisplayMoney()
        canvas.create_text(250, 420, text=GAME.options[GAME.displayedName], fill="black", font=("Arial", 40), anchor="nw")
    def ContractParameters(self):
        GAME.ChangeScreen("Contract Parameters")
        GAME.DisplayMoney()
        GAME.DisplayLogo()
        name=GAME.options[GAME.displayedName]
        canvas.create_text(10, 50, text=name, fill="black", font=("Arial", 50), anchor="nw")
        data=[]
        if GAME.scouting=="Driver" or GAME.scouting=="Junior Driver":
            if GAME.role=="Junior" or GAME.role=="Reserve":
                data.append(f"{GAME.role} Driver")
            else:
                data.append(f"Replacing {GAME.role}")
            data.append("$"+str("{:,}".format(GAME.salary)))
            if GAME.contractLength==1:
                data.append("1 Year")
            else:
                data.append(str(GAME.contractLength)+" Years")
        else:
            if GAME.scouting=="Race Engineer":
                data.append("Paired with "+GAME.role)
            else:
                data.append(GAME.role)
            data.append("$"+str("{:,}".format(GAME.salary)))
            data.append("1 Year")
        for x in range(3):
            GAME.Button("Upgrade Attribute",50,330+(x*150))
            canvas.create_text(100, 340+(x*150), text=data[x], fill="black", font=("Arial", 20), anchor="nw")
        if GAME.promoting==0:
            GAME.Button("Propose Contract",800,490)
        else:
            GAME.Button("Promote",800,490)
    def EndScouting(self):
        if len(GAME.news)>0:
            GAME.ChangeScreen("Breaking News")
            for x in range(len(GAME.news)):
                canvas.create_text(150, 180+(x*30), text=GAME.news[x], fill="white", font=("Arial", 20), anchor="nw")
            GAME.news=[]
            root.after(3500, lambda: GAME.Menu())
        else:
            GAME.Menu()
    def SelectDriverToReplace(self):
        GAME.ChangeScreen("Replacing")
        GAME.Button("Back",5,730)
        GAME.Button("Choose",1100,170)
        GAME.DisplayDriver(GAME.car1,200,500)
        GAME.DisplayDriver(GAME.car2,920,500)
        canvas.create_text(350, 10, text="Select Driver to Replace", fill="black", font=("Arial", 50), anchor="nw")
        GAME.Button("Name Selector",250,100)
        try:
            canvas.create_text(350, 170, text=GAME.options[GAME.displayed], fill="black", font=("Arial", 40), anchor="nw")
        except:
            GAME.displayed=0
            canvas.create_text(350, 170, text=GAME.options[GAME.displayed], fill="black", font=("Arial", 40), anchor="nw")
    def SelectReplacement(self):
        GAME.ChangeScreen("Replacement")
        GAME.Button("Back",5,730)
        GAME.Button("Choose",1100,170)
        if len(GAME.options)==1:
            GAME.displayed=0
            GAME.DisplayDriver(GAME.options[0],500,500)
        else:
            for x in range(len(GAME.options)):
                GAME.DisplayDriver(GAME.options[x],200+((720/(len(GAME.options)-1))*x),500)
        canvas.create_text(350, 10, text="Select Replacement", fill="black", font=("Arial", 50), anchor="nw")
        GAME.Button("Name Selector",250,100)
        canvas.create_text(350, 170, text=GAME.options[GAME.displayed], fill="black", font=("Arial", 40), anchor="nw")
    def BackgroundColour(self):
        if GAME.team==0:
            root.configure(background="black")
        elif GAME.team=="McLaren":
            root.configure(background="#FFA100")
        elif GAME.team=="Red Bull":
            root.configure(background='#2400B2')
        elif "Aston Martin" in GAME.team:
            root.configure(background="#49C18D")
        elif "Alpine" in GAME.team:
            root.configure(background='#FF58FF')
        elif "Williams" in GAME.team:
            root.configure(background="#5196FF")
        elif "Racing Bulls" in GAME.team or "Honda" in GAME.team:
            root.configure(background="White")
        elif "Haas" in GAME.team:
            root.configure(background="#D70000")
        elif "Ferrari" in GAME.team:
            root.configure(background="#EE1818")
        elif "Renault" in GAME.team:
            root.configure(background="yellow")
        elif "Audi" in GAME.team:
            root.configure(background='#AFB8C1')
        elif GAME.team=="West McLaren" or GAME.team=="Vodafone McLaren":
            root.configure(background='#DADADA')
        else:
            root.configure(background="black")
    def StartNewGame(self):
        GAME.drivers=[]
        GAME.database=1
        while True:
            database=f"F1 Manager 26 Save Data {GAME.database}.db"
            try:
                c=sqlite3.connect(database)
                race=GAME.Sanitise(c.execute("SELECT Race FROM Player").fetchall())
                if len(race)==0:
                    break
                elif int(race)<0:
                    break
                else:
                    GAME.database+=1
            except:
                break
        try:
            c.execute("DROP TABLE Teams")
            c.execute("DROP TABLE Drivers")
            c.execute("DROP TABLE Staff")
            c.execute("DROP TABLE Regulations")
            c.execute("DROP TABLE Engines")
            c.execute("DROP TABLE Cars")
            c.execute("DROP TABLE Sponsors")
            c.execute("DROP TABLE Calendar")
            c.execute("DROP TABLE Tracks")
            c.execute("DROP TABLE Player")
            c.execute("DROP TABLE History")
            c.execute("DROP TABLE Buyers")
            c.execute("DROP TABLE TeamPrincipals")
        except:
            pass
        GAME.database=f"F1 Manager 26 Save Data {GAME.database}.db"
        c.execute('''CREATE TABLE Teams(Name str, Appearance str,OriginalName st, Position int, Points int, Money int, Income int, TeamPrincipal str, Country str, Reputation int, Sponsor str, PreviousPosition int, PressConferences int)''')
        c.execute('''CREATE TABLE Drivers(Name str, Appearance str, Team str, Role str, Country str, Position int, Points int, Salary int, Condition str, Rating int, Overtaking int, Defending int, Pace int, Experience int, Control int, Reaction int, Calmness int, Age int, Marketability int, DevelopmentRate int, ContractEnd int, NewTeam str, NewSalary int, NewRole str, Championships int, Wins int, Legend int)''')
        c.execute('''CREATE TABLE Staff(Name str, Team str, Role str, Rating int, Salary int, Morale int, Country str, NewTeam str, NewSalary int, NewRole str)''')
        c.execute('''CREATE TABLE Regulations(Regulation str, True int)''')
        c.execute('''CREATE TABLE Engines(Name str, Manufacturer str, Power int, Reliability int, Battery int, Research int)''')
        c.execute('''CREATE TABLE Cars(Team str, Engine str, DragReduction int, LowSpeed int, MediumSpeed int, HighSpeed int, Cooling int, TyrePreservation int, car1Engine int, car1EngineDurability int, car2Engine int, car2EngineDurability int, Research int, Ranking int, Driveability int)''')
        c.execute('''CREATE TABLE Sponsors(Name str, Team str, Pay int)''')
        c.execute('''CREATE TABLE Calendar(ID int, Track str)''')
        c.execute('''CREATE TABLE Tracks(Name str, Country str, Length float, Laps int, Risk int, RainChance int, Temperature int, Corners str, Straights int, Sprint int, Street int, Overtakeability int)''')
        c.execute('''CREATE TABLE Player(Name str, Country str, Team str, newTeam int, Season int, Race int, RegulationChange int, Points int, Wins int, Championships int, NextYearEngine str, Actions int, Financial int, Management int, Warnings int, TyreWear int, MovingTo str)''')
        c.execute('''CREATE TABLE History(Year int, Driver str, Constructor str)''')
        c.execute('''CREATE TABLE Buyers(Name str, Country str)''')
        c.execute('''CREATE TABLE TeamPrincipals(Name str, Team str)''')
        c.commit()
        c.close()
        GAME.ChangeScreen("Welcome screen")
    def CreateTeam(self):
        GAME.ChangeScreen("Get Team Name")
        GAME.team=GAME.Sanitise(simpledialog.askstring(" ", "Limit: 20 characters"))
        teams=["mclaren","ferrari","red bull","mercedes","aston martin","alpine","haas","racing bulls","williams","audi","honda","cadillac","renault","gazoo racing","ford","create new team",
               "legend","hp","oracle","petronas","aramco","bwt","visa & cash app","atlassian","revolut","Gazoo Racing","placeholder","team principal","dead","player"]
        valid=GAME.Validate(GAME.team)
        if valid==1:
            with sqlite3.connect(GAME.database) as c:
                if len(c.execute("SELECT Name FROM Teams WHERE Name=?",(GAME.team,)).fetchall())>0:
                    valid=0
        if valid==1:
            for x in range(len(teams)):
                if teams[x] in GAME.team.lower() and not(GAME.team=="Marlboro Ferrari" or GAME.team=="Vodafone McLaren" or GAME.team=="West McLaren"):
                    valid=0
        if valid==1:
            GAME.BackgroundColour()
            if GAME.season==2026:
                GAME.newTeam=1
                if os.path.isfile("F1 Manager 26 Driver Data.json") and os.path.isfile(GAME.database):
                    GAME.FillDatabase()
                    GAME.DriverMarket()
                else:
                    GAME.ChangeScreen("Missing Required Files")
            else:
                GAME.ChangeScreen("Choose Engine 1")
    def CreateNewTeam(self):
        with sqlite3.connect(GAME.database) as c:
            c.execute("UPDATE Player SET Team=?",(GAME.team,))
            pos=len(c.execute("SELECT Name FROM Teams").fetchall())+1
            c.execute('''INSERT into Teams (Name, Appearance, OriginalName, Position, Points, Money, Income, TeamPrincipal, Country, Reputation, Sponsor, PreviousPosition) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(GAME.team, 0, "Player", pos, 12, 5000000, 1000000, GAME.name, GAME.country, 50, 0, 0))
            f=c.execute("SELECT Name FROM Drivers WHERE Team='Free Agent' AND Age>17 AND Condition='Well'").fetchall()
            if len(f)<2:
                for x in range(2-len(f)):
                    Name=GAME.GenerateName()
                    if GAME.gender=="Male":
                        appearance="Man "+str(random.randint(1,3))
                    else:
                        appearance="Woman "+str(random.randint(1,2))
                    Overtaking=random.randint(20,85)
                    Defending=random.randint(20,85)
                    Pace=random.randint(20,85)
                    Experience=random.randint(0,60)
                    Control=random.randint(20,85)
                    Reaction=random.randint(20,85)
                    Rating=round((Overtaking+Defending+Pace+Experience+Control+Reaction)/6)
                    c.execute('''INSERT into Drivers (Name, Appearance,Team, Role, Country, Position, Points, Salary, Condition, Rating, Overtaking, Defending, Pace, Experience, Control, Reaction, Calmness, Age, Marketability, DevelopmentRate, ContractEnd, NewTeam, NewSalary, NewRole, Championships, Wins) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(Name, appearance, "Free Agent", "Free Agent", random.choice(GAME.countries), 0, 0, 0, "Well", Rating, Overtaking, Defending, Pace, Experience, Control, Reaction, random.randint(0,100), 18, random.randint(50,95), random.randint(70,100), 0, 0, 0, 0, 0, 0))
                f=c.execute("SELECT Name FROM Drivers WHERE Team='Free Agent' AND Age>17").fetchall()
            for x in range(2):
                name=random.choice(f)
                f.remove(name)
                name=GAME.Sanitise(name)
                salary=int(GAME.Sanitise(c.execute("SELECT Salary FROM Drivers WHERE Name=?",(name,)).fetchall()[0]))
                if salary<1000000:
                    c.execute("UPDATE Drivers SET Salary=1000000 WHERE Name=?",(name,))
                c.execute("UPDATE Drivers SET Team=?, Role=?, ContractEnd=? WHERE Name=?",(GAME.team,str(x+1),GAME.season,name,))
            raceEngineer1=GAME.GenerateName()
            raceEngineer2=GAME.GenerateName()
            technicalDirector=GAME.GenerateName()
            sportingDirector=GAME.GenerateName()
            c.execute('''INSERT into Staff (Name , Team , Role , Rating , Salary , Morale , Country , NewTeam , NewSalary , NewRole ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(raceEngineer1, GAME.team, "Race Engineer 1", 70, 500000, 0, random.choice(GAME.countries), 0, 0, 0))
            c.execute('''INSERT into Staff (Name , Team , Role , Rating , Salary , Morale , Country , NewTeam , NewSalary , NewRole ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(raceEngineer2, GAME.team, "Race Engineer 2", 70, 500000, 0, random.choice(GAME.countries), 0, 0, 0))
            c.execute('''INSERT into Staff (Name , Team , Role , Rating , Salary , Morale , Country , NewTeam , NewSalary , NewRole ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(technicalDirector, GAME.team, "Technical Director", 70, 500000, 0, random.choice(GAME.countries), 0, 0, 0))
            c.execute('''INSERT into Staff (Name , Team , Role , Rating , Salary , Morale , Country , NewTeam , NewSalary , NewRole ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(sportingDirector, GAME.team, "Sporting Director", 70, 500000, 0, random.choice(GAME.countries), 0, 0, 0))
            c.execute('''INSERT into Cars (Team, Engine, DragReduction, LowSpeed, MediumSpeed, HighSpeed, Cooling, TyrePreservation, car1Engine, car1EngineDurability, car2Engine, car2EngineDurability, Research, Ranking, Driveability) VALUES (?, ?, 30, 30, 30, 30, 30, 30, 1, 100, 1, 100, 0, 12, 12)''',(GAME.team, GAME.engine))
            GAME.race+=1
            c.execute("UPDATE Teams SET TeamPrincipal=? WHERE Name=?",(GAME.name,GAME.team,))
            c.execute("UPDATE Teams SET TeamPrincipal='None' WHERE Name=?",(GAME.oldTeam,))
            c.execute("UPDATE Player SET Race=?",(GAME.race,))
        GAME.RaceTime()
    def DriverMarket(self):
        GAME.ChangeScreen("Blank Screen")
        canvas.create_text(250, 350, text=f"{GAME.team} needs some drivers.", fill="white", font=("Arial", 40), anchor="nw")
        root.after(5000, lambda: GAME.DisplayDriverMarket())
    def DisplayDriverMarket(self):
        GAME.ChangeScreen("Starter Drivers")
        drivers=["Jack Doohan","Alex Dunne","Yuki Tsunoda","Paul Aron","Mick Schumacher","Leonardo Fornaroli","Victor Martins","Zhou Guanyu"]
        teams=["Alpine","McLaren","Red Bull","Alpine","Free Agent","Invicta","Williams","Ferrari"]
        if GAME.car1!="":
            teams.pop(drivers.index(GAME.car1))
            drivers.remove(GAME.car1)
        canvas.create_text(150, 100, text="Name", fill="black", font=("Arial", 20), anchor="nw")
        canvas.create_text(450, 100, text="Team", fill="black", font=("Arial", 20), anchor="nw")
        canvas.create_text(650, 100, text="Age", fill="black", font=("Arial", 20), anchor="nw")
        canvas.create_text(720, 100, text="Role", fill="black", font=("Arial", 20), anchor="nw")
        canvas.create_text(900, 100, text="Rating", fill="black", font=("Arial", 20), anchor="nw")
        canvas.create_text(1000, 100, text="Salary", fill="black", font=("Arial", 20), anchor="nw")
        canvas.create_text(1120, 100, text="Contract End", fill="black", font=("Arial", 20), anchor="nw")
        for x in range(len(drivers)):
            driver=drivers[x]
            team=teams[x]
            with sqlite3.connect(GAME.database) as c:
                salary="$"+str("{:,}".format(int(GAME.Sanitise(c.execute("SELECT Salary FROM Drivers WHERE Name=?",(driver,)).fetchall()[0]))))
                rating=GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                age=int(GAME.Sanitise(c.execute("SELECT Age FROM Drivers WHERE Name=?",(driver,)).fetchall()[0]))-1
            canvas.create_text(150, 150+(x*50), text=driver, fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(450, 150+(x*50), text=team, fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(650, 150+(x*50), text=age, fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(720, 150+(x*50), text="Driver", fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(920, 150+(x*50), text=rating, fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(1000, 150+(x*50), text=salary, fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(1200, 150+(x*50), text="2025", fill="black", font=("Arial", 20), anchor="nw")
        GAME.options=drivers.copy()
        GAME.Button("Choose Driver",600,730)
    def SelectDriver(self):
        GAME.ChangeScreen("Choose Driver")
        GAME.Button("Name Selector",150,350)
        GAME.Button("Hire",1100,420)
        canvas.create_text(250, 420, text=GAME.options[GAME.displayedName], fill="black", font=("Arial", 40), anchor="nw")
    def Rookies(self):
        GAME.ChangeScreen("Rookies")
        drivers=["Gabriel Bortoleto","Isack Hadjar","Paul Aron","Oliver Bearman"]
        teams=["Invicta","Campos","Hitech","Prema"]
        canvas.create_text(150, 100, text="Name", fill="black", font=("Arial", 20), anchor="nw")
        canvas.create_text(450, 100, text="Team", fill="black", font=("Arial", 20), anchor="nw")
        canvas.create_text(650, 100, text="Age", fill="black", font=("Arial", 20), anchor="nw")
        canvas.create_text(720, 100, text="Role", fill="black", font=("Arial", 20), anchor="nw")
        canvas.create_text(900, 100, text="Rating", fill="black", font=("Arial", 20), anchor="nw")
        for x in range(len(drivers)):
            driver=drivers[x]
            team=teams[x]
            with sqlite3.connect(GAME.database) as c:
                rating=GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                age=int(GAME.Sanitise(c.execute("SELECT Age FROM Drivers WHERE Name=?",(driver,)).fetchall()[0]))-1
            canvas.create_text(150, 150+(x*50), text=driver, fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(450, 150+(x*50), text=team, fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(650, 150+(x*50), text=age, fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(720, 150+(x*50), text="F2 Driver", fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(920, 150+(x*50), text=rating, fill="black", font=("Arial", 20), anchor="nw")
        GAME.options=drivers.copy()
        GAME.Button("Choose Driver",600,730)
    def SelectRenewal(self):
        GAME.ChangeScreen("Choose Renewal")
        GAME.Button("Name Selector",150,350)
        GAME.Button("Renew",1100,420)
        canvas.create_text(250, 420, text=GAME.options[GAME.displayed], fill="black", font=("Arial", 40), anchor="nw")
    def Renewal(self):
        name=GAME.options[GAME.displayed]
        driver=0
        with sqlite3.connect(GAME.database) as c:
            try:
                GAME.role=GAME.Sanitise(c.execute("SELECT Role FROM Drivers WHERE Name=?",(name,)).fetchall()[0])
                if GAME.role=="1" or GAME.role=="2":
                    role="Driver"
                else:
                    role=f"{GAME.role} Driver"
                GAME.salary=int(GAME.Sanitise(c.execute("SELECT Salary FROM Drivers WHERE Name=?",(name,)).fetchall()[0]))
                rating=int(GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Name=?",(name,)).fetchall()[0]))
                if GAME.role=="Junior":
                    minimumSalary=rating*10000
                else:
                    minimumSalary=rating*37500
                if minimumSalary>GAME.salary:
                    GAME.salary=minimumSalary
                driver=1
            except:
                GAME.role=GAME.Sanitise(c.execute("SELECT Role FROM Staff WHERE Name=?",(name,)).fetchall()[0])
                if GAME.role=="Race Engineer 1" or GAME.role=="Race Engineer 2":
                    role="Race Engineer"
                else:
                    role=GAME.role
                GAME.salary=int(GAME.Sanitise(c.execute("SELECT Salary FROM Staff WHERE Name=?",(name,)).fetchall()[0]))
                rating=int(GAME.Sanitise(c.execute("SELECT Rating FROM Staff WHERE Name=?",(name,)).fetchall()[0]))
        GAME.ChangeScreen("Contract")
        GAME.screen="Renewal"
        GAME.Button("Renew",800,660)
        GAME.Button("Back",5,730)
        if GAME.team in steam:
            appearance=GAME.team
        else:
            with sqlite3.connect(GAME.database) as c:
                appearance=GAME.Sanitise(c.execute("SELECT Appearance FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0])
        if appearance!="0":
            if appearance in steam:
                logo=logos[steam.index(appearance)-1]
            else:
                logo=sponsorLogos[sponsors.index(appearance)]
            canvas.image=logo
            canvas.create_image(900, 80, anchor=tk.NW, image=logo)
        salary="{:,}".format(GAME.salary)
        canvas.create_text(445, 80, text=name, fill="black", font=("Arial", 40), anchor="nw")
        canvas.create_text(445, 550, text=f"Salary: ${salary}", fill="black", font=("Arial", 30), anchor="nw")
        canvas.create_text(445, 590, text=f"Rating: {rating}", fill="black", font=("Arial", 30), anchor="nw")
        if GAME.contractLength==1:
            canvas.create_text(445, 630, text="1 Season", fill="black", font=("Arial", 30), anchor="nw")
        else:
            canvas.create_text(445, 630, text=f"{GAME.contractLength} Seasons", fill="black", font=("Arial", 30), anchor="nw")
        if driver==0:
            canvas.create_text(445, 300, text=role, fill="black", font=("Arial", 50), anchor="nw")
        else:
            GAME.Button("Length Selector",50,380)
            if GAME.contractLength==1:
                canvas.create_text(100, 390, text="1 Season", fill="black", font=("Arial", 20), anchor="nw")
            else:
                canvas.create_text(100, 390, text=f"{GAME.contractLength} Seasons", fill="black", font=("Arial", 20), anchor="nw")
            canvas.create_text(800, 300, text=role, fill="black", font=("Arial", 25), anchor="nw")
            GAME.DisplayDriver(name,450,250)
    def SelectSave(self):
        GAME.database=1
        GAME.ViewSave()
    def ViewSave(self):
        GAME.loaded=0
        GAME.ChangeScreen("Select Save File")
        valid=1
        if os.path.isfile(f"F1 Manager 26 Save Data {GAME.database}.db"):
            c=sqlite3.connect(f"F1 Manager 26 Save Data {GAME.database}.db")
            race=c.execute("SELECT Race FROM Player").fetchall()
            if len(race)==0:
                valid=0
            else:
                race=int(GAME.Sanitise(race[0]))
                if race<0:
                    valid=0
                else:
                    team=GAME.Sanitise(c.execute("SELECT Team FROM Player").fetchall()[0])
                    if team=="McLaren":
                        colour="#FFA100"
                    elif team=="Mercedes":
                        colour="#1AE2CE"
                    elif team=="Red Bull":
                        colour="#2400B2"
                    elif "Aston Martin" in team:
                        colour="#49C18D"
                    elif "Alpine" in team:
                        colour="#FF58FF"
                    elif "Racing Bulls" in team or "Honda" in team:
                        colour="white"
                    elif "Williams" in team:
                        colour="#5196FF"
                    elif "Ferrari" in team:
                        colour="#EE1818"
                    elif "Renault" in team:
                        colour="yellow"
                    elif "Audi" in team:
                        colour="#AFB8C1"
                    elif "Haas" in team:
                        colour="#D70000"
                    elif "Cadillac" in team:
                        colour="#E6E6E6"
                    else:
                        colour="#DADADA"
                    canvas.create_text(400, 300, text=GAME.Sanitise(c.execute("SELECT Name FROM Player").fetchall()[0]), fill=colour, font=("Arial", 50), anchor="nw")
                    canvas.create_text(400, 370, text=GAME.Sanitise(c.execute("SELECT Season FROM Player").fetchall()[0]), fill=colour, font=("Arial", 50), anchor="nw")
                    try:
                        canvas.create_text(400, 440, text=GAME.Sanitise(c.execute("SELECT Track FROM Calendar WHERE ID=?",(race,)).fetchall()[0]), fill=colour, font=("Arial", 50), anchor="nw")
                    except:
                        if race==0:
                            canvas.create_text(400, 440, text="Pre-Season", fill=colour, font=("Arial", 50), anchor="nw")
                        else:
                            canvas.create_text(400, 440, text="Post-Season", fill=colour, font=("Arial", 50), anchor="nw")
                    canvas.create_text(400, 510, text=team, fill=colour, font=("Arial", 50), anchor="nw")
                    if team in steam:
                        appearance=team
                    else:
                        appearance=GAME.Sanitise(c.execute("SELECT Appearance FROM Teams WHERE Name=?",(team,)).fetchall()[0])
                    if appearance!="0":
                        if appearance in steam:
                            logo=logos[steam.index(appearance)-1]
                        else:
                            try:
                                logo=sponsorLogos[sponsors.index(appearance)]
                            except:
                                logo=0
                        if logo!=0:
                            canvas.image=logo
                            canvas.create_image(1050, 270, anchor=tk.NW, image=logo)
                    if len(c.execute("SELECT Name FROM Drivers WHERE Legend!=0").fetchall())>0:
                        canvas.create_text(275, 265, text="Legends", fill="#F5C939", font=("Algerian", 30), anchor="nw")
            c.commit()
            c.close()
        else:
            valid=0
        if valid==0:
            if os.path.isfile(f"F1 Manager 26 Save Data {GAME.database}.db"):
                os.remove(f"F1 Manager 26 Save Data {GAME.database}.db")
            GAME.SelectSave()
        else:
            GAME.Button("Back",5,730)
            root.after(300, lambda: GAME.SaveReady())
    def SaveReady(self):
        GAME.loaded=1
    def LoadGame(self):
        GAME.drivers=[]
        with sqlite3.connect(GAME.database) as c:
            GAME.name=GAME.Sanitise(c.execute('''SELECT Name FROM Player''').fetchall()[0])
            GAME.country=GAME.Sanitise(c.execute('''SELECT Country FROM Player''').fetchall()[0])
            GAME.team=GAME.Sanitise(c.execute('''SELECT Team FROM Player''').fetchall()[0])
            GAME.newTeam=int(GAME.Sanitise(c.execute('''SELECT newTeam FROM Player''').fetchall()[0]))
            GAME.season=int(GAME.Sanitise(c.execute('''SELECT Season FROM Player''').fetchall()[0]))
            GAME.race=int(GAME.Sanitise(c.execute('''SELECT Race FROM Player''').fetchall()[0]))
            GAME.money=int(GAME.Sanitise(c.execute('''SELECT Money FROM Teams WHERE Name=?''',(GAME.team,)).fetchall()[0]))
            GAME.engine=GAME.Sanitise(c.execute('''SELECT Engine FROM Cars WHERE Team=?''',(GAME.team,)).fetchall()[0])
            GAME.car1=GAME.Sanitise(c.execute('''SELECT Name FROM Drivers WHERE Team=? AND Role="1"''',(GAME.team,)).fetchall()[0])
            GAME.car2=GAME.Sanitise(c.execute('''SELECT Name FROM Drivers WHERE Team=? AND Role="2"''',(GAME.team,)).fetchall()[0])
            GAME.position=int(GAME.Sanitise(c.execute('''SELECT Position FROM Teams WHERE Name=?''',(GAME.team,)).fetchall()[0]))
            GAME.sponsor=GAME.Sanitise(c.execute('''SELECT Sponsor FROM Teams WHERE Name=?''',(GAME.team,)).fetchall()[0])
            GAME.actions=int(GAME.Sanitise(c.execute("SELECT Actions FROM Player").fetchall()[0]))
            GAME.races=len(c.execute("SELECT Track FROM Calendar").fetchall())
            if GAME.races==0:
                GAME.races=24
            if len(c.execute("SELECT Name FROM Teams WHERE Name='Red Bull'").fetchall())==1:
                c.execute("UPDATE Drivers SET Team='Red Bull' WHERE Team='Racing Bulls' AND Role='Reserve'")
            if len(c.execute("SELECT Name FROM Drivers WHERE Legend!=0").fetchall())>0:
                GAME.legends=1
        if GAME.music==1:
            GAME.StopMusic()
        GAME.BackgroundColour()
        GAME.RaceTime()
    def DisplayTeam(self,team):
        for x in range(2):
            with sqlite3.connect(GAME.database) as c:
                driver=GAME.Sanitise(c.execute("SELECT Name FROM Drivers WHERE Team=? AND Role=?",(team,str(x+1),)).fetchall()[0])
            GAME.DisplayDriver(driver,200+(x*640),500)
            if GAME.screen==(team+" Display") or GAME.screen=="Generic Display":
                canvas.create_text(950-(650-(650*x)), 340, text=driver, fill="black", font=("Arial", 20), anchor="nw")
    def DisplayDriver(self,driver,x,y):
            with sqlite3.connect(GAME.database) as c:
                if GAME.screen=="Contract":
                    team=GAME.team
                elif GAME.replay>0:
                    team=GAME.teams[GAME.drivers.index(driver)]
                else:
                    try:
                        team=GAME.teams[GAME.drivers.index(driver)]
                    except:
                        team=GAME.Sanitise(c.execute("SELECT Team FROM Drivers WHERE Name=?",(driver,)).fetchall())
                if driver=="Sonny Hayes" or driver=="Joshua Pearce":
                    team=driver
                elif team=="AlphaTauri" and GAME.replay>0:
                    team="Racing Bulls"
                elif team=="McLaren":
                    if GAME.replay==3 or GAME.replay==4:
                        team="Vodafone McLaren"
                    elif GAME.replay==5:
                        team="West McLaren"
                elif team=="Ferrari":
                    if GAME.replay==5 or GAME.replay==4:
                        team="Marlboro Ferrari"
            if team in steam:
                if os.path.isfile(os.path.join(os.path.dirname(__file__), "Suits", (f"{team} Suit.png"))):
                    index=steam.index(team)
                    suit=GAME.suits[index]
                else:
                    suit=GAME.suits[0]
                    index=0
            else:
                try:
                    appearance=GAME.Sanitise(c.execute("SELECT Appearance FROM Teams WHERE Name=?",(team,)).fetchall()[0])
                except:
                    appearance="0"
                if appearance=="0":
                    suit=GAME.suits[0]
                    index=0
                elif appearance in steam:
                    if os.path.isfile(os.path.join(os.path.dirname(__file__), "Suits", (f"{appearance} Suit.png"))):
                        index=steam.index(appearance)
                        suit=GAME.suits[index]
                    else:
                        suit=GAME.suits[0]
                        index=0
                else:
                    try:
                        suit=sponsorSuits[sponsors.index(appearance)]
                    except:
                        suit=GAME.suits[0]
            canvas.image=suit
            canvas.create_image(x, y, anchor=tk.NW, image=suit)
            if driver!="Sonny Hayes" and driver!="Joshua Pearce":
                if driver=="Lewis Hamilton" and (GAME.replay==3 or GAME.replay==4):
                    driver="Young Hamilton"
                try:
                    X=xDif[index]
                    Y=yDif[index]
                except:
                    X=xDif[0]
                    Y=yDif[0]
                if driver=="Liam Lawson":
                    Y-=15
                elif driver=="Esteban Ocon" or driver=="Isack Hadjar":
                    Y-=10
                elif driver=="Jack Doohan":
                    Y+=8
                    X+=4
                elif driver=="Zhou Guanyu":
                    Y-=8
                    X-=5
                elif driver=="Kevin Magnussen":
                    Y-=15
                elif driver=="Sergio Perez":
                    X-=7
                elif driver=="Gabriel Bortoleto":
                    Y-=7
                if driver in driverHeads:
                    head=driver
                else:
                    try:
                        head=GAME.Sanitise(c.execute("SELECT Appearance FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                    except:
                        head="Man 3"
                head=heads[driverHeads.index(head)]
                canvas.image=head
                canvas.create_image(x+X, y-Y, anchor=tk.NW, image=head)
    def DisplayRaceTeam(self):
        if GAME.driver1!=0:
            GAME.DisplayDriver(GAME.driver1,200,500)
        if GAME.driver2!=0:
            GAME.DisplayDriver(GAME.driver2,840,500)
    def WelcomeToTeam(self):
        GAME.ChangeScreen("Welcome To Team")
        with sqlite3.connect(GAME.database) as c:
            GAME.engine=GAME.Sanitise(c.execute("SELECT Engine FROM Cars WHERE Team=?",(GAME.team,)).fetchall()[0])
            GAME.sponsor=GAME.Sanitise(c.execute("SELECT Sponsor FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0])
        X=400
        if len(GAME.team)>10:
            X-100
        canvas.create_text(400, 50, text=("Welcome to "+GAME.team), fill="black", font=("Algerian", 40), anchor="nw")
        GAME.DisplayLogo()
        GAME.DisplayTeam(GAME.team)
    def DisplayLogo(self):
        if GAME.team in steam:
            appearance=GAME.team
        else:
            with sqlite3.connect(GAME.database) as c:
                appearance=GAME.Sanitise(c.execute("SELECT Appearance FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0])
        if appearance!="0":
            if appearance in steam:
                logo=logos[steam.index(appearance)-1]
            else:
                try:
                    logo=sponsorLogos[sponsors.index(appearance)]
                except:
                    logo=0
            if logo!=0:
                canvas.image=logo
                canvas.create_image(1250, 30, anchor=tk.NW, image=logo)
                
    def DisplayGridLoop(self,position):
        F1=sqlite3.connect(GAME.database)
        c=F1.cursor()
        try:
            c.execute('''SELECT Name FROM Teams WHERE PreviousPosition=?''',(position,))
            team=GAME.Sanitise(c.fetchall()[0])
        except:
            c.execute('''SELECT Name FROM Teams WHERE PreviousPosition=0''')
            F=c.fetchall()
            team=GAME.Sanitise(F[len(GAME.newTeams)])
            GAME.newTeams.append(team)
        F1.commit()
        F1.close()
        screen=team+" Display"
        if screen not in Images:
            screen="Generic Display"
        GAME.ChangeScreen(screen)
        GAME.DisplayTeam(team)
        if screen=="Generic Display":
            canvas.create_text(700-(len(team)*25), 100, text=team, fill="white", font=("Arial", 80), anchor="nw")
    def DisplayGrid(self):
        if GAME.music==1:
            sound_path = os.path.join(os.path.dirname(__file__), "Music", "F1 Theme.wav")
            if os.path.isfile(sound_path):
                winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
        GAME.ChangeScreen("Blank Screen")
        canvas.create_text(80, 250, text=f"The {GAME.season} Grid", fill="white", font=("Arial", 150), anchor="nw")
        GAME.newTeams=[]
        with sqlite3.connect(GAME.database) as F1:
            f = F1.execute("SELECT Name FROM Teams").fetchall()
        time=round(71500/(len(f)+1))
        delay_ms=time
        for idx, _ in enumerate(f, start=0):
            root.after(delay_ms, lambda i=idx: GAME.DisplayGridLoop(len(f)-i))
            delay_ms+=time
        root.after(delay_ms, lambda: GAME.ChangeScreen("Blank Screen"))
    def WelcomeToSeason(self):
        canvas.create_text(110, 150, text=f"Welcome to the {GAME.season} season.", fill="white", font=("Arial", 70), anchor="nw")
        with sqlite3.connect(GAME.database) as F1:
            regulationChange=int(GAME.Sanitise(F1.execute("SELECT RegulationChange FROM Player").fetchall()))
        if regulationChange==GAME.season+1:
            canvas.create_text(30, 500, text="This is the last season of this regulation cycle.", fill="white", font=("Arial", 50), anchor="nw")
    def PreSeason(self):
        GAME.news=[]
        GAME.BackgroundColour()
        if GAME.done==1:
            GAME.DisplayGrid()
            root.after(72500, lambda: GAME.WelcomeToSeason())
            root.after(77500, lambda: GAME.PreSeasonTesting())
        elif GAME.oldTeam!=0:
            GAME.WelcomeToTeam()
        else:
            GAME.SponsorNegotiation()
    def SponsorNegotiation(self):
        done=0
        if GAME.actions==3:
            if GAME.team!="McLaren" and GAME.team!="Ferrari" and GAME.team!="Red Bull" and GAME.team!="Mercedes" and GAME.team!="Aston Martin" and GAME.team!="Alpine" and GAME.team!="Haas" and GAME.team!="Racing Bulls" and GAME.team!="Williams" and GAME.team!="Audi":
                with sqlite3.connect(GAME.database) as c:
                    c.execute("UPDATE Player SET Actions=2")
                    GAME.actions=2
                    currentSponsor=GAME.Sanitise(c.execute("SELECT Sponsor FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0])
                    position=int(GAME.Sanitise(c.execute("SELECT Position FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0]))
                    score=(12-position)+round(int(GAME.Sanitise(c.execute("SELECT Reputation FROM Teams WHERE Name=?",(GAME.team,)).fetchall()[0]))/10)
                    maximumPay=score*3800
                    if maximumPay<40000 and random.randint(1,25)>=position:
                        maximumPay=40000
                    try:
                        currentPay=int(GAME.Sanitise(c.execute("SELECT Pay FROM Sponsors WHERE Team=?",(GAME.team,)).fetchall()[0]))
                    except:
                        currentPay=0
                    if currentPay<maximumPay:
                        f=c.execute("SELECT Name FROM Sponsors WHERE Team='None' AND Pay<=? AND Pay>=?",(maximumPay,currentPay,)).fetchall()
                        if len(f)>0:
                            sponsor=GAME.Sanitise(random.choice(f))
                            GAME.displayed=sponsor
                            GAME.ChangeScreen("Sponsor Negotiation")
                            canvas.create_text(30, 200, text=f"{sponsor} would like to become your Title Sponsor for the {GAME.season} Season.", fill="black", font=("Arial", 30), anchor="nw")
                            GAME.Button("Decline",350,450)
                            GAME.Button("Accept",890,450)
                            logo=sponsorLogos[sponsors.index(sponsor)]
                            canvas.image=logo
                            canvas.create_image(675, 380, anchor=tk.NW, image=logo)
                        else:
                            done=1
                    else:
                        done=1
            else:
                done=1
        else:
            done=1
        if done==1:
            GAME.PreSeasonEvents()
    def PreSeasonTesting(self):
        GAME.CarRanking()
        GAME.ChangeScreen("Pre-Season Testing")
        with sqlite3.connect(GAME.database) as F1:
            f=F1.execute("SELECT Name FROM Teams").fetchall()
        canvas.create_text(300, 50, text="Pre-Season Testing suggests", fill="white", font=("Arial", 50), anchor="nw")
        canvas.create_text(250, 150, text="these are the current car rankings:", fill="white", font=("Arial", 50), anchor="nw")
        for x in range(len(f)):
            with sqlite3.connect(GAME.database) as F1:
                team=GAME.Sanitise(F1.execute('''SELECT Team FROM Cars WHERE Ranking=?''',(x+1,)).fetchall())
            if x<round(len(f)/2):
                canvas.create_text(10, 280+(50*x), text=(str(x+1)+". "+team), fill="white", font=("Arial", 30), anchor="nw")
            elif x<9:
                canvas.create_text(725, 280+(50*(x-round(len(f)/2))), text=(str(x+1)+". "+team), fill="white", font=("Arial", 30), anchor="nw")
            else:
                canvas.create_text(715, 280+(50*(x-round(len(f)/2))), text=(str(x+1)+". "+team), fill="white", font=("Arial", 30), anchor="nw")
        GAME.Button("Next",1200,695)
    def PreSeasonEvents(self):
        if GAME.actions>=2:
            F1=sqlite3.connect(GAME.database)
            c=F1.cursor()
            c.execute("UPDATE Teams SET Reputation=20 WHERE Reputation<20")
            if GAME.season==2028:
                c.execute('''INSERT into Engines (Name, Manufacturer, Power, Reliability, Battery, Research) VALUES ("General Motors", "Cadillac", 0, 0, 0, 1)''')
            elif GAME.season==2029:
                GAME.news.append("BREAKING NEWS! Cadillac are now producing their own General Motors engines.")
                c.execute("UPDATE Cars SET Engine='General Motors' WHERE Team='Cadillac'")
            c.execute('''INSERT into TeamPrincipals (Name, Team) VALUES (?, "None")''',(GAME.GenerateName(),))
            #Team Principal Replacement
            f=c.execute("SELECT Name FROM Teams WHERE TeamPrincipal='None'").fetchall()
            if len(f)>0:
                for x in range(len(f)):
                    team=GAME.Sanitise(f[x])
                    name=GAME.Sanitise(random.choice(c.execute("SELECT Name FROM TeamPrincipals WHERE Team='None'").fetchall()))
                    GAME.news.append(f"BREAKING NEWS! {name} is the new Team Principal of {team}.")
                    c.execute("UPDATE Teams SET TeamPrincipal=? WHERE Name=?",(name,team,))
                    c.execute("UPDATE TeamPrincipals SET Team=? WHERE Name=?",(team,name,))
            buyer=0
            if random.randint(1,4)>=2 and GAME.season!=2026:
                    #Team Acquired
                    f=c.execute('''SELECT Name FROM Teams WHERE Name!="Ferrari" AND Name!="McLaren" AND Name!="Mercedes" AND Name!=? AND OriginalName!="Player"''',(GAME.team,)).fetchall()
                    team=random.choice(f)
                    if GAME.Sanitise(team)=="Cadillac" and GAME.season<2030:
                        f.remove(team)
                        team=random.choice(f)
                    team=GAME.Sanitise(team)
                    if team=="Red Bull":
                        team=GAME.Sanitise(random.choice(f))
                    williams=0
                    if team=="Williams":
                        williams=1
                    elif GAME.Sanitise(c.execute("SELECT OriginalName FROM Teams WHERE Name=?",(team,)).fetchall()[0])=="Williams":
                        williams=1
                    if team=="Red Bull":
                        num=5
                    else:
                        num=random.randint(1,5)
                    if (num==1 and len(team)<15) or williams==1:
                        #Partnership
                        c.execute('''SELECT Name FROM Buyers''')
                        f=c.fetchall()
                        if len(f)<=0:
                            c.execute('''SELECT Name FROM Sponsors WHERE Team="None"''')
                            f=c.fetchall()
                            if len(f)>=1:
                                buyer=GAME.Sanitise(f[0])
                                c.execute('''DELETE FROM Sponsors WHERE Name=?''',(buyer,))
                                c.execute('''INSERT into Buyers (Name, Country) VALUES (?, 0)''',(buyer,))
                            else:
                                buyers=["BMW","Lotus","Amazon","Force India","Ford","Tesla","Benneton","Honda","Alfa Romeo","Renault","Porsche","Kia","Mazda","Lamborghini","Volkswagen"]
                                c.execute('''SELECT Name FROM Teams''')
                                f=c.fetchall()
                                buyer=random.choice(buyers)
                                buy=1
                                for x in range(len(f)):
                                    if GAME.Sanitise(f[x])==buyer:
                                        buy=0
                                if buy==0:
                                    while buy==0:
                                        buyer=random.choice(buyers)
                                        buy=1
                                        for x in range(len(f)):
                                            if GAME.Sanitise(f[x])==buyer:
                                                buy=0
                                c.execute('''INSERT into Buyers (Name, Country) VALUES (?, 0)''',(buyer,))
                        else:
                            buyer=GAME.Sanitise(random.choice(f))
                        if williams==1:
                            name=buyer+" Williams"
                        else:
                            name=buyer+" "+team
                        if name==GAME.team:
                            name=name+" Racing"
                        GAME.news.append(f"BREAKING NEWS! {team} has formed a partnership with {buyer}")
                        GAME.news.append(f"forming the {name} Formula 1 team.")
                        F1.commit()
                        F1.close()
                        GAME.TeamAcquired(team,name)
                        F1=sqlite3.connect(GAME.database)
                        c=F1.cursor()
                        if GAME.Sanitise(c.execute("SELECT Appearance FROM Teams WHERE Name=?",(name,)).fetchall()[0])=="0":
                            c.execute("UPDATE Teams SET Appearance=? WHERE Name=?",(name,name,))
                        c.execute('''DELETE FROM Buyers WHERE Name=?''',(buyer,))
                    elif num==2:
                        #Sponsor
                        f=c.execute('''SELECT Sponsor FROM Teams WHERE Name=?''',(team,)).fetchall()
                        buyer=GAME.Sanitise(f[0])
                        if buyer=="0":
                            num=3
                            #Acquirement
                            c.execute('''SELECT Name FROM Buyers''')
                            f=c.fetchall()
                            if len(f)<=0:
                                c.execute('''SELECT Name FROM Sponsors WHERE Team="None"''')
                                f=c.fetchall()
                                buyer=GAME.Sanitise(f[0])
                                c.execute('''DELETE FROM Sponsors WHERE Name=?''',(buyer,))
                                c.execute('''INSERT into Buyers (Name, Country) VALUES (?, 0)''',(buyer,))
                            else:
                                buyer=GAME.Sanitise(random.choice(f))
                                c.execute('''SELECT Country FROM Buyers WHERE Name=?''',(buyer,))
                                f=c.fetchall()
                                if len(f)>=1:
                                    country=GAME.Sanitise(f[0])
                                    c.execute('''INSERT into Buyers (Name, Country) VALUES (?, ?)''',(buyer, country))
                                else:
                                    buyers=["BMW","Lotus","Amazon","Force India","Ford","Tesla","Benneton","Honda","Alfa Romeo","Renault","Porsche","Kia","Mazda","Lamborghini","Volkswagen"]
                                    c.execute('''SELECT Name FROM Teams''')
                                    f=c.fetchall()
                                    buyer=random.choice(buyers)
                                    buy=1
                                    for x in range(len(f)):
                                        if GAME.Sanitise(f[x])==buyer:
                                            buy=0
                                    if buy==0:
                                        while buy==0:
                                            buyer=random.choice(buyers)
                                            buy=1
                                            for x in range(len(f)):
                                                if GAME.Sanitise(f[x])==buyer:
                                                    buy=0
                                    c.execute('''INSERT into Buyers (Name, Country) VALUES (?, 0)''',(buyer,))
                            c.execute('''SELECT Country FROM Buyers WHERE Name=?''',(buyer,))
                            f=c.fetchall()
                            country=GAME.Sanitise(f[0])
                            c.execute('''DELETE FROM Buyers WHERE Name=?''',(buyer,))
                            if buyer==GAME.team:
                                buyer=buyer+" Racing"
                            GAME.news.append(f"BREAKING NEWS! {buyer} has bought {team}.")
                            F1.commit()
                            F1.close()
                            GAME.TeamAcquired(team,buyer)
                            F1=sqlite3.connect(GAME.database)
                            c=F1.cursor()
                            c.execute('''UPDATE Teams SET Appearance=?, Country=? WHERE Name=?''',(name, country, name,))
                        else:
                            c.execute('''DELETE FROM Sponsors WHERE Name=?''',(buyer,))
                            if buyer=="Visa & Cash App":
                                buyer="Visa"
                            GAME.news.append(f"BREAKING NEWS! {team} has been acquired by their sponsor, {buyer}.")
                            F1.commit()
                            F1.close()
                            if buyer==GAME.team:
                                name=f"{buyer} Racing"
                            else:
                                name=buyer
                            GAME.TeamAcquired(team,name)
                            F1=sqlite3.connect(GAME.database)
                            c=F1.cursor()
                            c.execute("UPDATE Teams SET Appearance=? WHERE Name=?",(buyer,name,))
                            f=c.execute('''SELECT Money FROM Teams WHERE Name=?''',(name,)).fetchall()
                            money=int(GAME.Sanitise(f[0]))
                            money+=30000000
                            c.execute('''UPDATE Teams SET Money=?, Sponsor=0 WHERE Name=?''',(money, name,))
                    else:
                        #Acquirement
                        f=c.execute('''SELECT Name FROM Buyers''').fetchall()
                        F1.commit()
                        F1.close()
                        F1=sqlite3.connect(GAME.database)
                        c=F1.cursor()
                        if len(f)<=0:
                            f=c.execute('''SELECT Name FROM Sponsors WHERE Team="None"''').fetchall()
                            if len(f)>=1:
                                buyer=GAME.Sanitise(f[0])
                                c.execute('''DELETE FROM Sponsors WHERE Name=?''',(buyer,))
                                c.execute('''INSERT into Buyers (Name, Country) VALUES (?, 0)''',(buyer,))
                            else:
                                buyers=["BMW","Lotus","Amazon","Force India","Ford","Tesla","Benneton","Honda","Alfa Romeo","Renault","Porsche","Kia","Mazda","Lamborghini","Volkswagen"]
                                f=c.execute('''SELECT Name FROM Teams''').fetchall()
                                buyer=random.choice(buyers)
                                buy=1
                                for x in range(len(f)):
                                    if GAME.Sanitise(f[x])==buyer:
                                        buy=0
                                if buy==0:
                                    while buy==0:
                                        buyer=random.choice(buyers)
                                        buy=1
                                        for x in range(len(f)):
                                            if GAME.Sanitise(f[x])==buyer:
                                                buy=0
                                c.execute('''INSERT into Buyers (Name, Country) VALUES (?, 0)''',(buyer,))
                        else:
                            buyer=GAME.Sanitise(random.choice(f))
                            f=c.execute('''SELECT Country FROM Buyers WHERE Name=?''',(buyer,)).fetchall()
                            country=GAME.Sanitise(f[0])
                            c.execute('''UPDATE Teams SET Country=? WHERE Name=?''',(country, buyer,))
                        if buyer==GAME.team:
                            name=buyer+" Racing"
                        else:
                            name=buyer
                        GAME.news.append(f"BREAKING NEWS! {buyer} has bought {team}.")
                        F1.commit()
                        F1.close()
                        GAME.TeamAcquired(team,name)
                        F1=sqlite3.connect(GAME.database)
                        c=F1.cursor()
                        c.execute('''SELECT Country FROM Buyers WHERE Name=?''',(buyer,))
                        f=c.fetchall()
                        country=GAME.Sanitise(f[0])
                        c.execute('''UPDATE Teams SET Appearance=?, Country=? WHERE Name=?''',(name, country, name,))
                        c.execute('''DELETE FROM Buyers WHERE Name=?''',(buyer,))
                        name=buyer
                    if buyer=="Ford" and num>2 and len(c.execute("SELECT Name FROM Engines WHERE Name='Red Bull'").fetchall())>0:
                        c.execute("UPDATE Engines SET Name='Ford' WHERE Name='Red Bull'")
                        c.execute("UPDATE Cars SET Engine='Ford' WHERE Engine='Red Bull'")
                        c.execute("UPDATE Cars SET Engine='Ford' WHERE Team=?",(name,))
            if GAME.season!=2026:
                #Sponsor Negotiation
                f=c.execute("SELECT Name FROM Teams WHERE Sponsor='0' AND Name!=?",(GAME.team,)).fetchall()
                teamsSigned=[]
                F1.commit()
                F1.close()
                F1=sqlite3.connect(GAME.database)
                c=F1.cursor()
                for x in range(len(f)):
                    if random.randint(1,3)>1:
                        team=GAME.Sanitise(f[x])
                        teamsSigned.append(team)
                        sponsor=GAME.Sanitise(c.execute("SELECT Name FROM Sponsors WHERE Team='None' AND Name!=?",(GAME.team,)).fetchall()[0])
                        GAME.news.append(f"BREAKING NEWS! {team} has signed {sponsor}")
                        GAME.news.append(f"as their Title Sponsor for the {GAME.season} season.")
                        c.execute("UPDATE Teams SET Sponsor=? WHERE Name=?",(sponsor,team,))
                        c.execute("UPDATE Sponsors SET Team=? WHERE Name=?",(team,sponsor,))
                if random.randint(1,2)==2:
                    team=GAME.Sanitise(random.choice(c.execute("SELECT Name FROM Teams WHERE Name!='McLaren' AND Name!='Ferrari' AND Name!='Red Bull' AND Name!='Mercedes' AND Name!='Aston Martin' AND Name!='Alpine' AND Name!='Haas' AND Name!='Racing Bulls' AND Name!='Williams' AND Name!='Audi' AND Name!=?",(GAME.team,)).fetchall()))
                    if team not in teamsSigned:
                        oldSponsor=GAME.Sanitise(c.execute("SELECT Sponsor FROM Teams WHERE Name=?",(team,)).fetchall()[0])
                        sponsor=GAME.Sanitise(c.execute("SELECT Name FROM Sponsors WHERE Team='None'").fetchall()[0])
                        GAME.news.append(f"BREAKING NEWS! {team} has signed {sponsor}")
                        GAME.news.append(f"as their Title Sponsor for the {GAME.season} season.")
                        c.execute("UPDATE Teams SET Sponsor=? WHERE Name=?",(sponsor,team,))
                        c.execute("UPDATE Sponsors SET Team=? WHERE Name=?",(team,sponsor,))
                        c.execute("UPDATE Sponsors SET Team='None' WHERE Name=?",(oldSponsor,))
                #Engine change
                newEngines=[]
                if buyer=="Honda":
                    GAME.news.append(f"{name} has switched to using their own Honda engines.")
                    f=c.execute("SELECT Team FROM Cars WHERE Engine='Honda'").fetchall()
                    if len(f)>0:
                        if random.randint(1,2)==1:
                            engine="Mercedes"
                        else:
                            engine="Ferrari"
                        c.execute("UPDATE Cars SET Engine=? WHERE Engine='Honda'",(engine,))
                        for x in range(len(f)):
                            GAME.news.append(f"{GAME.Sanitise(f[x])} has switched to using {engine} engines.")
                    c.execute('''UPDATE Cars SET Engine="Honda" WHERE Team=?''',(name,))
                    c.execute("UPDATE Engines SET Manufacturer=? WHERE Name='Honda'",(name,))
                #New Engine
                f=c.execute('''SELECT Name FROM Teams WHERE Name!="Cadillac"''').fetchall()
                regulationChange=int(GAME.Sanitise(c.execute("SELECT RegulationChange FROM Player").fetchall()[0]))
                if regulationChange==GAME.season+1 and GAME.season>2026 and len(c.execute("SELECT Name FROM Engines").fetchall())<6:
                    if random.randint(1,4)>1:
                        team=GAME.Sanitise(random.choice(f))
                        if len(c.execute("SELECT Name FROM Engines WHERE Manufacturer=?",(team,)).fetchall())==0 and team!="Racing Bulls" and team!=GAME.team and "Honda" not in team:
                            if "Alpine" in team and len(c.execute("SELECT Name FROM Engines WHERE Name='Renault'").fetchall())==0 and len(c.execute("SELECT Name FROM Teams WHERE Name='Renault'").fetchall())==0:
                                engine="Renault"
                            else:
                                engine=team
                            if len(c.execute("SELECT Name FROM Engines WHERE Name=?",(engine,)).fetchall())==0:
                                c.execute('''INSERT into Engines (Name, Manufacturer, Power, Reliability, Battery, Research) VALUES (?, ?, 0, 0, 0, 1)''',(engine,team,))
                elif len(c.execute("SELECT Name FROM Engines WHERE Research>1").fetchall())==0:
                    engines=c.execute("SELECT Name FROM Engines WHERE Manufacturer!='None' AND Power>0").fetchall()
                    for x in range(len(engines)):
                        engine=GAME.Sanitise(engines[x])
                        manufacturer=GAME.Sanitise(c.execute("SELECT Manufacturer FROM Engines WHERE Name=?",(engine,)).fetchall()[0])
                        if len(c.execute("SELECT Team FROM Cars WHERE Team=? AND Engine=?",(manufacturer,engine,)).fetchall())==0:
                            GAME.news.append(f"BREAKING NEWS! {manufacturer} are now producing their own engines.")
                            c.execute("UPDATE Cars SET Engine=? WHERE Team=?",(engine,manufacturer,))
                            newEngines.append(manufacturer)

                #Engine Change
                team=GAME.Sanitise(random.choice(f))
                old=GAME.Sanitise(c.execute('''SELECT Engine FROM Cars WHERE Team=?''',(team,)).fetchall()[0])
                if old not in team and team!=GAME.team and team not in newEngines:
                    rb=0
                    if team=="Racing Bullls":
                        if len(c.execute("SELECT Name FROM Teams WHERE Name='Red Bull'").fetchall())==1:
                            rb=1
                    if rb==0:
                        if old=="Red Bull":
                            old="Ford RBPT"
                        honda=1-len(c.execute("SELECT Team FROM Cars WHERE Engine='Honda'").fetchall())
                        if honda==0:
                            engine=GAME.Sanitise(random.choice(c.execute('''SELECT Name FROM Engines WHERE Name!="Red Bull" AND Name!=? AND Name!="Honda" AND Power>0''',(old,)).fetchall()))
                        else:
                            engine=GAME.Sanitise(random.choice(c.execute('''SELECT Name FROM Engines WHERE Name!="Red Bull" AND Name!=? AND Power>0''',(old,)).fetchall()))
                        c.execute('''UPDATE Cars SET Engine=? WHERE Team=?''',(engine, team,))
                        c.execute("UPDATE Engines SET Manufacturer='None' WHERE Manufacturer=?",(team,))
                        if engine=="Honda":
                            c.execute("UPDATE Engines SET Manufacturer=? WHERE Name='Honda'",(team,))
                        GAME.news.append(f"BREAKING NEWS! {team} has switched from {old}")
                        GAME.news.append(f"to {engine} for their engines.")
                        
            c.execute("UPDATE Player SET Actions=1")
            GAME.actions=1
            F1.commit()
            F1.close()
        GAME.done=1
        if len(GAME.news)>0:
            GAME.ChangeScreen("Breaking News")
            for x in range(len(GAME.news)):
                canvas.create_text(150, 180+(x*30), text=GAME.news[x], fill="white", font=("Arial", 20), anchor="nw")
            GAME.news=[]
            root.after(10000, lambda: GAME.PreSeason())
        else:
            GAME.PreSeason()
    def HireReserve(self):
        GAME.ChangeScreen("Reserve Options")
        GAME.Button("Back",5,730)
        GAME.options=[]
        with sqlite3.connect(GAME.database) as c:
            f=c.execute("SELECT Name FROM Drivers WHERE Team=? AND Role='Junior' AND Age>17",(GAME.team,)).fetchall()
            if len(f)>0:
                for driver in f:
                    GAME.options.append(GAME.Sanitise(driver))
            if len(GAME.options)<3:
                f=c.execute("SELECT Name FROM Drivers WHERE Team='Free Agent' AND Age>17").fetchall()
                for x in range(3-len(GAME.options)):
                    driver=random.choice(f)
                    f.remove(driver)
                    GAME.options.append(GAME.Sanitise(driver))
            if len(GAME.options)==0:
                GAME.Menu()
            else:
                canvas.create_text(150, 100, text="Name", fill="black", font=("Arial", 20), anchor="nw")
                canvas.create_text(450, 100, text="Team", fill="black", font=("Arial", 20), anchor="nw")
                canvas.create_text(650, 100, text="Age", fill="black", font=("Arial", 20), anchor="nw")
                canvas.create_text(750, 100, text="Rating", fill="black", font=("Arial", 20), anchor="nw")
                canvas.create_text(850, 100, text="Salary", fill="black", font=("Arial", 20), anchor="nw")
                canvas.create_text(980, 100, text="Contract End", fill="black", font=("Arial", 20), anchor="nw")
                for x in range(len(GAME.options)):
                    driver=GAME.options[x]
                    team=GAME.Sanitise(c.execute("SELECT Team FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                    age=GAME.Sanitise(c.execute("SELECT Age FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                    rating=GAME.Sanitise(c.execute("SELECT Rating FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                    salary=int(GAME.Sanitise(c.execute("SELECT Salary FROM Drivers WHERE Name=?",(driver,)).fetchall()[0]))
                    if salary<3000000:
                        salary=3000000
                    salary="$"+str("{:,}".format(salary))
                    if team=="Free Agent":
                        contractEnd=GAME.season
                    else:
                        contractEnd=GAME.Sanitise(c.execute("SELECT ContractEnd FROM Drivers WHERE Name=?",(driver,)).fetchall()[0])
                    canvas.create_text(150, 150+(x*60), text=driver, fill="black", font=("Arial", 20), anchor="nw")
                    canvas.create_text(450, 150+(x*60), text=team, fill="black", font=("Arial", 20), anchor="nw")
                    canvas.create_text(650, 150+(x*60), text=age, fill="black", font=("Arial", 20), anchor="nw")
                    canvas.create_text(750, 150+(x*60), text=rating, fill="black", font=("Arial", 20), anchor="nw")
                    canvas.create_text(850, 150+(x*60), text=salary, fill="black", font=("Arial", 20), anchor="nw")
                    canvas.create_text(1050, 150+(x*60), text=contractEnd, fill="black", font=("Arial", 20), anchor="nw")
                    GAME.Button("Hire",1150,140+(x*60))
    def TeamData(self):
        #Team Data
        F1=sqlite3.connect(GAME.database)
        c=F1.cursor()
        GAME.driversChosen=[GAME.driver1,GAME.driver2]
        for x in range(2):
            c.execute('''UPDATE Drivers SET Team=?, Role=?, Salary=? WHERE Name=?''',(GAME.team,x+1,2000000,GAME.driversChosen[x],))
        c.execute('''UPDATE Sponsors SET Team=? WHERE Name=?''',(GAME.team,GAME.sponsor,))
        c.execute('''INSERT into Teams (Name, Appearance, OriginalName, Position, Points, Money, Income, TeamPrincipal, Country, Reputation, Sponsor, PreviousPosition) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(GAME.team, 0, "Player", 12, 0, 5000000, 1000000, GAME.name, GAME.country, 50, GAME.sponsor, 0))
        #Staff Data
        F1.commit()
        F1.close()
        raceEngineer1=GAME.GenerateName()
        raceEngineer2=GAME.GenerateName()
        technicalDirector=GAME.GenerateName()
        sportingDirector=GAME.GenerateName()
        F1=sqlite3.connect(GAME.database)
        c=F1.cursor()
        c.execute('''INSERT into Staff (Name , Team , Role , Rating , Salary , Morale , Country , NewTeam , NewSalary , NewRole ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(raceEngineer1, GAME.team, "Race Engineer 1", 70, 500000, 0, random.choice(GAME.countries), 0, 0, 0))
        c.execute('''INSERT into Staff (Name , Team , Role , Rating , Salary , Morale , Country , NewTeam , NewSalary , NewRole ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(raceEngineer2, GAME.team, "Race Engineer 2", 70, 500000, 0, random.choice(GAME.countries), 0, 0, 0))
        c.execute('''INSERT into Staff (Name , Team , Role , Rating , Salary , Morale , Country , NewTeam , NewSalary , NewRole ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(technicalDirector, GAME.team, "Technical Director", 70, 500000, 0, random.choice(GAME.countries), 0, 0, 0))
        c.execute('''INSERT into Staff (Name , Team , Role , Rating , Salary , Morale , Country , NewTeam , NewSalary , NewRole ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(sportingDirector, GAME.team, "Sporting Director", 70, 500000, 0, random.choice(GAME.countries), 0, 0, 0))
        F1.commit()
        F1.close()
        GAME.WelcomeToTeam()
    def Button(self,button,x,y):
        button=buttons[Buttons.index(button)]
        canvas.image=button
        canvas.create_image(x, y, anchor=tk.NW, image=button)
    def Calendar(self):
        calendar=[]
        GAME.ChangeScreen("calendar")
        with sqlite3.connect(GAME.database) as F1:
                F1.execute("DELETE FROM Calendar")
                if GAME.season==2026:
                    GAME.races=22
                    calendar=["Albert Park","Shanghai","Suzuka","Miami","Montreal","Monte Carlo","Catalunya","Red Bull Ring","Silverstone",
                              "Spa","Hungaroring","Zandvoort","Monza","Madrid","Baku","Marina Bay","Austin","Mexico City","Interlagos",
                              "Las Vegas","Qatar","Abu Dhabi"]
                else:
                    if random.randint(1,3)==3:
                        opener="Sakhir"
                    else:
                        opener="Albert Park"
                    calendar.append(opener)
                    tracks=[opener,"Suzuka","Interlagos","Silverstone","Monza","Monte Carlo"]
                    finale=random.randint(1,6)
                    if finale<5:
                        finale="Abu Dhabi"
                    elif finale==5:
                        finale="Suzuka"
                    else:
                        finale="Interlagos"
                    if GAME.races==18:
                        GAME.races+=random.randint(-1,2)
                    elif GAME.races==17:
                        GAME.races+=random.randint(0,2)
                    elif GAME.races==24:
                        GAME.races+=random.randint(-2,0)
                    elif GAME.races==25:
                        GAME.races+=random.randint(-2,0)
                    else:
                        GAME.races+=random.randint(-2,2)
                    if finale not in tracks:
                        tracks.append(finale)
                    Tracks=F1.execute("SELECT Name FROM Tracks WHERE Name!='Abu Dhabi' AND Name!=? AND Name!=?",(opener,finale,)).fetchall()
                    for x in range(GAME.races-len(tracks)):
                        track=GAME.Sanitise(random.choice(Tracks))
                        if track in tracks or (track=="Nürburgring" and "Hockenheim" in tracks) or (track=="Hockenheim" and "Nürburgring" in tracks):
                            while track in tracks  or (track=="Nürburgring" and "Hockenheim" in tracks) or (track=="Hockenheim" and "Nürburgring" in tracks):
                                track=GAME.Sanitise(random.choice(Tracks))
                        tracks.append(track)
                    for x in range(GAME.races-2):
                        track=random.choice(tracks)
                        tracks.remove(track)
                        if track==finale or track in calendar:
                            while track==finale or track in calendar:
                                track=random.choice(tracks)
                                tracks.remove(track)
                        calendar.append(track)
                    calendar.append(finale)
                for x in range(GAME.races):
                    F1.execute("INSERT into Calendar (ID, Track) VALUES(?, ?)",(x+1,calendar[x],))
        canvas.create_text(570, 10, text=f"{GAME.season} Calendar", fill="#F5C939", font=("Arial", 40), anchor="nw")
        delay=500
        for x in range(GAME.races//5):
            for y in range(5):
                track=calendar[(x*5)+y]
                root.after(delay, lambda a=x, b=y, t=track: GAME.CalendarDisplay(a, b, t))
                delay+=500
        for z in range(GAME.races%5):
            track=calendar[((GAME.races//5)*5)+z]
            root.after(delay, lambda a=GAME.races//5, b=z, t=track: GAME.CalendarDisplay(a, b, t))
            delay+=500
        root.after(delay, lambda: GAME.Button("Next",1200,695))
    def CalendarDisplay(self,a,b,track):
        x=265+(190*b)
        y=205+(71*a)
        number=(a*5)+b+1
        if number>9:
            x-=5
        if number<GAME.race:
            colour="#B60000"
        elif number==GAME.race:
            colour="green"
        else:
            colour="#DADADA"
        canvas.create_text(x, y, text=(f"{number}. {track}"), fill=colour, font=("Arial", 15), anchor="nw")
    def Voice(self, subject, line):
        try:
            if not (((line=="Overtake" or line=="Lead") and GAME.replay==2) or GAME.pause==3 or GAME.replay==8 or GAME.replay==9 or GAME.replay==6):
                GAME.playing=1
                delay=0
                if subject!=0:
                    name_path=os.path.join(os.path.dirname(__file__), "Names", subject+".wav")
                    if  os.path.isfile(name_path):
                        if line!="Overtake":
                            winsound.PlaySound(name_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
                            with contextlib.closing(wave.open(name_path, 'r')) as f:
                                frames=f.getnframes()
                                rate=f.getframerate()
                                duration=frames / float(rate)
                                delay=round((duration - 0.1) * 1000)
                    else:
                        subject=-1
                if subject!=-1 or line=="Champion":
                    if line=="Overtake":
                        if subject=="Lewis Hamilton":
                            line=-1
                            vo_path=os.path.join(os.path.dirname(__file__), "Voicelines","Through Goes Hamilton.wav")
                        else:
                            vo_path=os.path.join(os.path.dirname(__file__), "Voicelines",f"Overtake {random.randint(1,2)}.wav")
                    else:
                        vo_path=os.path.join(os.path.dirname(__file__), "Voicelines", line + ".wav")
                    with contextlib.closing(wave.open(vo_path, 'r')) as f:
                        frames=f.getnframes()
                        rate=f.getframerate()
                        duration=frames / float(rate)
                        d=delay + round((duration-0.1)*1000)
                    root.after(delay, lambda: winsound.PlaySound(vo_path, winsound.SND_FILENAME | winsound.SND_ASYNC))
                    if line=="Overtake" and os.path.isfile(name_path):
                        root.after(d, lambda: winsound.PlaySound(name_path, winsound.SND_FILENAME | winsound.SND_ASYNC))
                        with contextlib.closing(wave.open(name_path, 'r')) as f:
                            frames=f.getnframes()
                            rate=f.getframerate()
                            duration=frames/float(rate)
                            delay=d+round(duration*1000)
                        root.after(delay-50, lambda: GAME.StopMusic())
                    else:
                        delay=d
                root.after(delay, lambda: GAME.VoiceDone())
                if line=="Champion":
                    root.after(delay, lambda: GAME.DriverCelebration(subject))
        except:
            pass
    def VoiceDone(self):
        GAME.playing=0
GAME=Game()

if os.path.isfile("F1 Manager 26 Save Data 1.db"):
    F1=sqlite3.connect("F1 Manager 26 Save Data 1.db")
    c=F1.cursor()
    try:
        GAME.race=int(GAME.Sanitise(c.execute('''SELECT Race FROM Player''').fetchall()[0]))
        F1.commit()
        F1.close()
        if GAME.race==-1:
            GAME.newGame=1
            os.remove("F1 Manager 26 Save Data 1.db")
        else:
            GAME.newGame=0
    except:
        GAME.race=-1
        try:
            os.remove("F1 Manager 26 Save Data 1.db")
            GAME.newGame=1
        except:
            GAME.newGame=1
else:
    GAME.newGame=1

print("GAME LOADING...")
root = tk.Tk()
root.title("F1 Manager 26")
root.configure(background='black')

#Music
if GAME.music==1:
    sound_path = os.path.join(os.path.dirname(__file__), "Music", "F1 Music.wav")
    if os.path.isfile(sound_path):
        winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
#Images
missingFiles=0
Images=["Title Screen","Welcome screen","Get Name","Get Country 1","Get Country 2","Choose a Team","Get Team Name","Choose Engine 1",
        "Choose Sponsor","Welcome To Team","Blank Screen","McLaren Display","Ferrari Display","Red Bull Display","Mercedes Display","Aston Martin Display","Alpine Display",
        "Haas Display","Racing Bulls Display","Williams Display","Generic Display","Save Screen","Practice","Breaking News","Q1 Eliminations","Q2 Eliminations",
        "Q3 Results","Choose Tyres","Choose Aggression","Race Screen","Instructions","Board Room","History","Upgrade","Select Research Type","Research","Driver List","Minimum Rating",
        "Contract Name","Contract Parameters","Contract","Contract Rejected","Press Conference","Championships","Rule Vote","Red Flag","Safety Car","Audi Display","Cadillac Display",
        "BMW Display","Amazon Display","Force India Display","Ford Display","Tesla Display","Benneton Display","Honda Display","Renault Display","Porsche Display","Kia Display",
        "Mazda Display","Lamborghini Display","Volkswagen Display","Volvo Display","JLR Display","Gazoo Racing Display","Lotus Display","Replay Screen","F1 Movie 1","F1 Movie 2",
        "F1 Movie 3","F1 Movie 4","F1 Movie 5","F1 Movie 6","F1 Movie 7","F1 Movie 8","F1 Movie 9","F1 Movie 10","Safety Car Menu","Red Flag Menu","Choose a Team 2021","Latifi Crash",
        "Hamilton Wins","Verstappen Wins","Canada 2011 Victory","Canada 2011 Defeat","Choose a Team 2000","Schumacher Victory","Hakkinen Victory","Senna Celebration",
        "Choose a Team 2008","Lewis Hamilton Victory","Felipe Massa Victory","Settings","Sponsor Review","Grey Screen","Box","Select Save File","Calendar","Standings",
        "McLaren Upgrade","Mercedes Upgrade","Red Bull Upgrade","Ferrari Upgrade","Williams Upgrade","Racing Bulls Upgrade","Aston Martin Upgrade","Haas Upgrade","Audi Upgrade",
        "Alpine Upgrade","Cadillac Upgrade","Data Background","United Kingdom Flag","United States of America Flag","Brazil Flag","Italy Flag","Japan Flag","Germany Flag",
        "Monaco Flag","Netherlands Flag","Spain Flag","Australia Flag","Austria Flag","Missing Required Files"]
images=[]
for x in range(len(Images)):
    path = os.path.join(os.path.dirname(__file__), "Screens", (Images[x]+".png"))
    if os.path.isfile(path):
        images.append(tk.PhotoImage(file=path))
    else:
        images.append(0)
        missingFiles=1
driverHeads=["Max Verstappen","Lando Norris","Charles Leclerc","Oscar Piastri","Carlos Sainz","George Russell","Lewis Hamilton","Fernando Alonso","Pierre Gasly","Nico Hulkenberg",
             "Yuki Tsunoda","Lance Stroll","Esteban Ocon","Alexander Albon","Oliver Bearman","Liam Lawson","Jack Doohan","Gabriel Bortoleto","Isack Hadjar","Kimi Antonelli",
             "Franco Colapinto","Frederik Vesti","Jak Crawford","Victor Martins","Mick Schumacher","Valtteri Bottas","Zhou Guanyu","Antonio Giovinazzi","Arvid Lindblad","Pato Oward",
             "Ayumu Iwasa","Stoffel Vandoorne","Paul Aron","Ryo Hirakawa","Doriane Pin","Abbi Pulling","Juan Manuel Fangio","Michael Schumacher","Ayrton Senna","Alain Prost",
             "Jackie Stewart","Niki Lauda","Sergio Perez","Alex Dunne","Kevin Magnussen","Logan Sargeant","Sebastian Vettel","Daniel Ricciardo","Kimi Raikkonen","Jenson Button",
             "Nigel Mansell","Nicholas Latifi","Mika Hakkinen","David Coulthard","Luke Browning","Leonardo Fornaroli","Rubens Barrichello","Jim Clark","Young Hamilton",
             "Felipe Massa","Heikki Kovalainen","Johnny Cecotto","Colton Herta","Freddie Slater","Kush Maini","Theo Pourchaire"]
for x in range(3):
    driverHeads.append(f"Man {x+1}")
    if x<2:
        driverHeads.append(f"Woman {x+1}")
heads=[]
for x in range(len(driverHeads)):
    path = os.path.join(os.path.dirname(__file__), "Heads", (driverHeads[x]+" Head.png"))
    if os.path.isfile(path):
        heads.append(tk.PhotoImage(file=path))
    else:
        missingFiles=1
steam=["Player","McLaren","Ferrari","Red Bull","Mercedes","Aston Martin","Alpine","Haas","Racing Bulls","Williams","Audi","Renault","Lotus","Force India","Vodafone McLaren",
       "Marlboro Ferrari","West McLaren","Gazoo Racing","Cadillac","BMW","Amazon","Ford","Tesla","Benneton","Honda","Porsche","Kia","Mazda","Lamborghini","Volkswagen","Volvo","JLR",
       "Alfa Romeo"]
xDif=[90,82,88,95,110,95,92,100,95,90,105,102,100,85,95,97,95,98,95]
yDif=[115,90,95,108,105,87,90,70,122,80,108,52,145,105,80,100,85,50,88]
path = os.path.join(os.path.dirname(__file__), "Suits", ("Created Team Suit.png"))
GAME.suits=[tk.PhotoImage(file=path)]
logos=[]
for x in range(len(steam)-1):
    path = os.path.join(os.path.dirname(__file__), "Suits", (steam[x+1]+" Suit.png"))
    if os.path.isfile(path):
        GAME.suits.append(tk.PhotoImage(file=path))
    else:
        GAME.suits.append(GAME.suits[0])
    team=steam[x+1]
    if "Ferrari" in team:
        team="Ferrari"
    elif "McLaren" in team and team!="McLaren":
        team="Classic McLaren"
    path = os.path.join(os.path.dirname(__file__), "Logos", (team+" Logo.png"))
    if os.path.isfile(path):
        logos.append(tk.PhotoImage(file=path))
    else:
        missingFiles=1
steam.append("Sonny Hayes")
path = os.path.join(os.path.dirname(__file__), "Suits", ("Sonny Hayes.png"))
if os.path.isfile(path):
    GAME.suits.append(tk.PhotoImage(file=path))
else:
    missingFiles=1
steam.append("Joshua Pearce")
path = os.path.join(os.path.dirname(__file__), "Suits", ("Joshua Pearce.png"))
if os.path.isfile(path):
    GAME.suits.append(tk.PhotoImage(file=path))
else:
    missingFiles=1
sponsors=["HP","Oracle","Petronas","Aramco","BWT","MoneyGram","Visa & Cash App","Atlassian","Adidas","Microsoft","Tesco","EA","Games Workshop","Disney","Opera GX","Coca Cola",
          "NVIDIA","Google","Netflix","IBM","McDonald","Uber","Virgin","Vodafone","Mastercard","Visa","Revolut","Apple","Gazoo Racing","Marlboro"]
sponsorLogos=[]
sponsorSuits=[]
for x in range(len(sponsors)):
    path = os.path.join(os.path.dirname(__file__), "Suits", (sponsors[x]+" Suit.png"))
    if os.path.isfile(path):
        sponsorSuits.append(tk.PhotoImage(file=path))
    elif sponsors[x]=="Mastercard" or sponsors[x]=="Petronas" or sponsors[x]=="Oracle" or sponsors[x]=="HP" or sponsors[x]=="Atlassian" or sponsors[x]=="Visa & Cash App":
        sponsorSuits.append(0)
    else:
        missingFiles=1
    path = os.path.join(os.path.dirname(__file__), "Logos", (sponsors[x]+" Logo.png"))
    if os.path.isfile(path):
        sponsorLogos.append(tk.PhotoImage(file=path))
    else:
        missingFiles=1
Buttons=["Next","Quit","Qualifying","Prepare for Race","Tyre Aggression","Fuel Aggression","ERS Deployment","Pause","Play","Helmet","Box","Back","Team Orders","Stop Team Orders",
         "Drive in Clean Air","Use Racing Line","Maintain Position","Overtake","Tyre Data","Results","Upgrade Car","Research","Standings","Data","Scouting","Team Data","Car Data",
         "Calendar","Achievements","History","Switch Engine 1","Switch Engine 2","Next Race","Upgrade Attribute","Upgrade","Aerodynamic Regulations","Engine Regulations",
         "View Contracts","Scout Drivers","Scout Technical Directors","Scout Sporting Directors","Scout Race Engineers","Renew","Reserve & Junior Drivers","Other Contracts",
         "Promote","Propose Contract","Name Selector","Hire","Choose Driver","Choose Engine","Choose","Swap Drivers","End Season","Vote For","Vote Against","Start Season",
         "Length Selector","Stay","Move","Create","Accept","Decline","Team Management","Fired","Stay Out","Start Race","ERS Disabled","Banned","Hire Reserve","Canada 2011",
         "Brazil 2008","Monaco 1984","Spa 2000","New Game","Load Game","Play Legends","Replay"]
buttons=[]
for x in range(len(Buttons)):
    path = os.path.join(os.path.dirname(__file__), "Buttons", (Buttons[x]+" Button.png"))
    if os.path.isfile(path):
        buttons.append(tk.PhotoImage(file=path))
    else:
        missingFiles=1
tracks=["Australia","China","Japan","Bahrain","Saudi Arabia","Miami","Imola","Monaco","Spain","Canada","Austria","United Kingdom","Belgium","Hungary","Netherlands","Italy",
        "Azerbaijan","Singapore","United States of America","Mexico","Brazil","Las Vegas","Qatar","Abu Dhabi","Madrid","Turkey","Nurburgring","Hockenheim","1984 Monaco","2008 Brazil",
        "Portugal","2021 Abu Dhabi"]
layouts=[]
path=os.path.join(os.path.dirname(__file__), "Race Images", "Lights.png")
raceImages=[tk.PhotoImage(file=path)]
for x in range(len(tracks)):
    path = os.path.join(os.path.dirname(__file__), "Layouts", (tracks[x]+" Layout.png"))
    if os.path.isfile(path):
        layouts.append(tk.PhotoImage(file=path))
    i=1
    for y in range(2):
        path=os.path.join(os.path.dirname(__file__), "Race Images", (f"{tracks[x]} {y+1}.png"))
        if os.path.isfile(path):
            raceImages.append(tk.PhotoImage(file=path))
        else:
            missingFiles=1
Tyres=["Soft","Medium","Hard","Intermediate","Wet"]
tyres=[]
for x in range(len(Tyres)):
    path = os.path.join(os.path.dirname(__file__), "Tyres", (Tyres[x]+" Tyre.png"))
    if os.path.isfile(path):
        tyres.append(tk.PhotoImage(file=path))
    else:
        missingFiles=1
Icons=["ERS Battery","Raindrop","Sunshine","Fuel Tank","Cloud","Minor Fault","Major Fault","Settings","Muted","Unmuted"]
icons=[]
for x in range(len(Icons)):
    path = os.path.join(os.path.dirname(__file__), "Icons", (Icons[x]+".png"))
    if os.path.isfile(path):
        icons.append(tk.PhotoImage(file=path))
    else:
        missingFiles=1
canvas = tk.Canvas(root, width=1440, height=810)
canvas.pack()
try:
    imageOnCanvas = canvas.create_image(0, 0, anchor=tk.NW, image=images[0])
except:
    pass
if not os.path.isfile("F1 Manager 26 Driver Data.json"):
    missingFiles=1
if missingFiles==1:
    if images[Images.index("Missing Required Files")]==0:
        canvas.delete('all')
        GAME.screen="Missing Required Files"
        canvas.create_text(400, 300, text="Missing Required Files", fill="red", font=("Arial", 50), anchor="nw")
    else:
        GAME.ChangeScreen("Missing Required Files")
canvas.bind("<Button-1>", GAME.OnClick)
root.mainloop()
