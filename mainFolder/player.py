import json

try:
    with open("mainFolder/save.json", "r") as f:
        data = json.load(f)
        level = data["level"]
        experience = data["experience"]

except (json.JSONDecodeError, FileNotFoundError, KeyError):
    data = {"level": 1, "experience": 0}
    level = data["level"]
    experience = data["experience"]
    with open("mainFolder/save.json", "w") as f:
        json.dump(data, f, indent=4)

if level < 2:
    playerHealth = playerInitialHealth = 20
    playerAttackPower = 20
elif level < 5:
    playerHealth = playerInitialHealth = 40
    playerAttackPower = 30
elif level < 10:
    playerHealth = playerInitialHealth = 60
    playerAttackPower = 40
elif level < 15:
    playerHealth = playerInitialHealth = 80
    playerAttackPower = 60
elif level < 20:
    playerHealth = playerInitialHealth = 100
    playerAttackPower = 75
elif level < 30:
    playerHealth = playerInitialHealth = 110
    playerAttackPower = 90
elif level < 40:
    playerHealth = playerInitialHealth = 120
    playerAttackPower = 100
elif level < 50:
    playerHealth = playerInitialHealth = 130
    playerAttackPower = 120
elif level < 55:
    playerHealth = playerInitialHealth = 150
    playerAttackPower = 150
elif level < 60:
    playerHealth = playerInitialHealth = 180
    playerAttackPower = 170
elif level < 75:
    playerHealth = playerInitialHealth = 200
    playerAttackPower = 180
elif level < 100:
    playerHealth = playerInitialHealth = 210
    playerAttackPower = 200
else:
    playerHealth = playerInitialHealth = 220
    playerAttackPower = 230