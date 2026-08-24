import json
import random

class Beast:
    def __init__(self, name, health, attackDamage, difficulty):
        self.name = name
        self.health = health
        self.attackDamage = attackDamage
        self.difficulty = difficulty

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class EarlyBeast(Beast):
    pass

class MidgameBeast(Beast):
    pass

class EndgameBeast(Beast):
    pass

class Boss(Beast):
    pass

gloomfang = EarlyBeast("Gloomfang", 15, 10, "Easy")
thornback = EarlyBeast("Thornback", 25, 35, "Easy")
ashcrawler = EarlyBeast("Ashcrawler", 35, 65, "Easy")

vexmax = MidgameBeast("Vexmax", 95, 105, "Medium")
dreadhorn = MidgameBeast("Dreadhorn", 105, 110, "Medium")
mirewretch = MidgameBeast("Mirewretch", 120, 115, "Medium")

stonecrusher = EndgameBeast("Stonecrusher", 125, 120, "Hard")
voidclaw = EndgameBeast("Voidclaw", 100, 135, "Hard")
emberstalker = EndgameBeast("Emberstalker", 150, 55, "Hard")

ravakor = Boss("Ravakor", 350, 400, "Impossible")
 
earlyBeasts = [gloomfang, thornback, ashcrawler]
midgamebeasts = [vexmax, dreadhorn, mirewretch]
endgamebeasts = [stonecrusher, voidclaw, emberstalker]
theBoss = [ravakor]

# Beasts
midEnemy = midgamebeasts + earlyBeasts
endEnemy = endgamebeasts + midgamebeasts + earlyBeasts
finalBoss = theBoss + endgamebeasts + midgamebeasts + earlyBeasts

try:
    with open("save.json", "r") as f:
        data = json.load(f)
        level = data["level"]
        experience = data["experience"]

except (json.JSONDecodeError, FileNotFoundError, KeyError):
    data = {"level": 1, "experience": 0}
    level = data["level"]
    experience = data["experience"]
    with open("save.json", "w") as f:
        json.dump(data, f, indent=4)

if level < 10:
    enemy = random.choice(earlyBeasts)
elif level < 30:
    enemy = random.choice(midEnemy)
elif level < 50:
    enemy = random.choice(endEnemy)
else:
    enemy = random.choice(finalBoss)

enemyHealth = enemy.health
enemyAttackPower = enemy.attackDamage

def get_enemy():
    try:
        with open("save.json", "r") as f:
            data = json.load(f)
            level = data["level"]
            experience = data["experience"]

    except (json.JSONDecodeError, FileNotFoundError, KeyError):
        data = {"level": 1, "experience": 0}
        level = data["level"]
        experience = data["experience"]
        with open("save.json", "w") as f:
            json.dump(data, f, indent=4)
    
    if level < 10:
        enemy = random.choice(earlyBeasts)
    elif level < 30:
        enemy = random.choice(midEnemy)
    elif level < 50:
        enemy = random.choice(endEnemy)
    else:
        enemy = random.choice(finalBoss)
    
    beast = {
        "enemy_name": enemy.name,
        "enemy_health": enemy.health,
        "enemy_init_health": enemy.health,
        "enemy_atk": enemy.attackDamage,
        "enemy_difficulty": enemy.difficulty
    }
    return beast
    
    
