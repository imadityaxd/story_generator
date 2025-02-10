import random

titles =['The Last Code of Eternity', 'Cybernetic Rebellion', "The Time Traveller's Paradox", "Breaking The Rules"]
heroes = ["Naruto Uzumaki", "Kakashi Hatake","Neji", "Hinata","Jiraya", "Lady Tsunade", "Minato Uzumaki"]
villains=["Madara Uchiha", "Itachi Uchiha", "Sasuke Uchiha", "Kasime", "Orochimaru"]
locations=["Leaf Village","Sound Village","Land of Birds","River Of Seperation"]
missions=["Rescue Sasuke", "Silent the Snake","Cursed Warrior","Capturing Kurama"]

def generate_story():
    title = random.choice(titles)
    hero = random.choice(heroes)
    villain = random.choice(villains)
    mission = random.choice(missions)
    location = random.choice(locations)

    return {
        "title":title,
        "hero":hero,
        "villain":villain,
        "location":location,
        "mission":mission,

    }