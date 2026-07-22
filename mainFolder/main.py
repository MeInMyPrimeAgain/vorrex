import random, math, json
from beast import *
from engine import *
from player import *
from ai import enemyAI

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

print("             VORREX\n#------------------------------#")
    
playerEnergy = enemyEnergy = 100

enemyAttackDamage = 0
playerAttackDamage = 0

isPlayerDefended = False
isEnemyDefended = False

playerHealthPercent = math.ceil((playerHealth/playerInitialHealth)*100)
enemyHealthPercent = math.ceil((enemyHealth/enemy.health)*100)

# Introduction cards(Player and Enemy)
def start():
    print(f"              You\nHealth        : {playerHealth}\nAttack Damage : {playerAttackPower}\nLevel         : {level}\n#------------------------------#")
    print(f"           {enemy}\nHealth        : {enemyHealth}\nAttack Damage : {enemyAttackPower}\nDifficulty    : {enemy.difficulty}\n#------------------------------#")
        
try:
    if random.choice([True, False]):
        start()
        print("   You will attack first!!\n#------------------------------#")
        input("Press 'Enter' to start the game")
        while playerHealth > 0 and enemyHealth > 0:
            playerHealthPercent = math.ceil((playerHealth/playerInitialHealth)*100)
            enemyHealthPercent = math.ceil((enemyHealth/enemy.health)*100)
            if playerEnergy >= 30:
                main = input(f"[1] Normal Attack\n[2] Defense\n[3] Power Attack\n[4] Freeze Attack\nChoose by number(1/2/3/4): ")
                if main == "1" or main == "" or "normal" in main.lower():
                    playerAttackDamage, enemyHealth, experience, isEnemyDefended = playerNormalAttack(enemyHealth, experience, isEnemyDefended)
                elif main == "2" or "defense" in main.lower():
                    enemyAttackDamage, playerEnergy, isPlayerDefended = playerDefense(enemyAttackDamage, playerEnergy, isPlayerDefended)
                elif main == "3" or "power" in main.lower():
                    playerAttackDamage, enemyHealth, playerEnergy, experience, isEnemyDefended = playerPowerAttack(enemyHealth, playerEnergy, experience, isEnemyDefended)
                elif main == "4" or "freeze" in main.lower():
                    enemyEnergy, playerEnergy = playerFreeze(enemyEnergy, playerEnergy)
                    for i in range(2):
                        if enemyHealth > 0:
                            if playerEnergy >= 20:
                                main = input(f"[1] Normal Attack\n[2] Defense\n[3] Power Attack\nChoose by number(1/2/3): ")
                                if main == "1" or main == "" or "normal" in main.lower():
                                    playerAttackDamage, enemyHealth, experience, isEnemyDefended = playerNormalAttack(enemyHealth, experience, isEnemyDefended)
                                elif main == "2" or "defense" in main.lower():
                                    enemyAttackDamage, playerEnergy, isPlayerDefended = playerDefense(enemyAttackDamage, playerEnergy, isPlayerDefended)
                                elif main == "3" or "power" in main.lower():
                                    playerAttackDamage, enemyHealth, playerEnergy, experience, isEnemyDefended = playerPowerAttack(enemyHealth, playerEnergy, experience, isEnemyDefended)
                                else:
                                    print("Wrong move!! Turn skipped!!😑")
                                            
                            elif playerEnergy >= 10:
                                main = input(f"[1] Normal Attack\n[2] Defense\nChoose by number(1/2): ")
                                if main == "1" or main == "" or "normal" in main.lower():
                                    playerAttackDamage, enemyHealth, experience, isEnemyDefended = playerNormalAttack(enemyHealth, experience, isEnemyDefended)
                                elif main == "2" or "defense" in main.lower():
                                    enemyAttackDamage, playerEnergy, isPlayerDefended = playerDefense(enemyAttackDamage, playerEnergy, isPlayerDefended)
                                else:
                                    print("Wrong move!! Turn skipped!!😑")
                            else:
                                main = input(f"[1] Normal Attack or Press 'Enter' to attack normally: ")
                                if main == "1" or "normal" in main.lower() or main == "":
                                    playerAttackDamage, enemyHealth, experience, isEnemyDefended = playerNormalAttack(enemyHealth, experience, isEnemyDefended)
                                else:
                                    print("Wrong move!! Turn skipped!!😑")
                        else:
                            print(f"You defeated {enemy}!! VICTORY!! 🏆")
                            break
                            
                else:
                    print("Wrong move!! Turn skipped!!😑")

            elif playerEnergy >= 20:
                main = input(f"[1] Normal Attack\n[2] Defense\n[3] Power Attack \nChoose by number(1/2): ")
                if main == "1" or main == "" or "normal" in main.lower():
                    playerAttackDamage, enemyHealth, experience, isEnemyDefended = playerNormalAttack(enemyHealth, experience, isEnemyDefended)
                elif main == "2" or "defense" in main.lower():
                    enemyAttackDamage, playerEnergy, isPlayerDefended = playerDefense(enemyAttackDamage, playerEnergy, isPlayerDefended)
                elif main == "3" or "power" in main.lower():
                    playerAttackDamage, enemyHealth, playerEnergy, experience, isEnemyDefended = playerPowerAttack(enemyHealth, playerEnergy, experience, isEnemyDefended)
                else:
                    print("Wrong move!! Turn skipped!!😑")
            
            elif playerEnergy >= 10:
                main = input(f"[1] Normal Attack\n[2] Defense \nChoose by number(1/2): ")
                if main == "1" or main == "" or "normal" in main.lower():
                    playerAttackDamage, enemyHealth, experience, isEnemyDefended = playerNormalAttack(enemyHealth, experience, isEnemyDefended)
                elif main == "2" or "defense" in main.lower():
                    enemyAttackDamage, playerEnergy, isPlayerDefended = playerDefense(enemyAttackDamage, playerEnergy, isPlayerDefended)
                else:
                    print("Wrong move!! Turn skipped!!😑")
            
            else:
                main = input(f"[1] Normal Attack or Press 'Enter' to attack normally: ")
                if main == "1" or "normal" in main.lower() or main == "":
                    playerAttackDamage, enemyHealth, experience, isEnemyDefended = playerNormalAttack(enemyHealth, experience, isEnemyDefended)
                else:
                    print("Wrong move!! Turn skipped!!😑")
            # Enemy turn
            if enemyHealth <= 0:
                break
            else:
                enemyAttackDamage, playerHealth, enemyEnergy, isPlayerDefended, isEnemyDefended, experience = enemyAI(enemyHealth, playerHealth, enemyEnergy, playerEnergy, enemyAttackDamage, playerAttackDamage, isPlayerDefended, isEnemyDefended, experience)
                
    else:
        start()
        print(f"   {enemy} will attack first!!\n#------------------------------#")
        input("Press 'Enter' to start the game")
        while playerHealth > 0 and enemyHealth > 0:
            enemyAttackDamage, playerHealth, enemyEnergy, isPlayerDefended, isEnemyDefended, experience = enemyAI(enemyHealth, playerHealth, enemyEnergy, playerEnergy, enemyAttackDamage, playerAttackDamage, isPlayerDefended, isEnemyDefended, experience)
            # player turn
            if playerHealth <= 0:
                break
            else:
                playerHealthPercent = math.ceil((playerHealth/playerInitialHealth)*100)
                enemyHealthPercent = math.ceil((enemyHealth/enemy.health)*100)
                if playerEnergy >= 30:
                    main = input(f"[1] Normal Attack\n[2] Defense\n[3] Power Attack\n[4] Freeze Attack\nChoose by number(1/2/3/4): ")
                    if main == "1" or main == "" or "normal" in main.lower():
                        playerAttackDamage, enemyHealth, experience, isEnemyDefended = playerNormalAttack(enemyHealth, experience, isEnemyDefended)
                    elif main == "2" or "defense" in main.lower():
                        enemyAttackDamage, playerEnergy, isPlayerDefended = playerDefense(enemyAttackDamage, playerEnergy, isPlayerDefended)
                    elif main == "3" or "power" in main.lower():
                        playerAttackDamage, enemyHealth, playerEnergy, experience, isEnemyDefended = playerPowerAttack(enemyHealth, playerEnergy, experience, isEnemyDefended)
                    elif main == "4" or "freeze" in main.lower():
                        enemyEnergy, playerEnergy = playerFreeze(enemyEnergy, playerEnergy)
                        for i in range(2):
                            if enemyHealth > 0:
                                if playerEnergy >= 20:
                                    main = input(f"[1] Normal Attack\n[2] Defense\n[3] Power Attack\nChoose by number(1/2/3): ")
                                    if main == "1" or main == "" or "normal" in main.lower():
                                        playerAttackDamage, enemyHealth, experience, isEnemyDefended = playerNormalAttack(enemyHealth, experience, isEnemyDefended)
                                    elif main == "2" or "defense" in main.lower():
                                        enemyAttackDamage, playerEnergy, isPlayerDefended = playerDefense(enemyAttackDamage, playerEnergy, isPlayerDefended)
                                    elif main == "3" or "power" in main.lower():
                                        playerAttackDamage, enemyHealth, playerEnergy, experience, isEnemyDefended = playerPowerAttack(enemyHealth, playerEnergy, experience, isEnemyDefended)
                                    else:
                                        print("Wrong move!! Turn skipped!!😑")
                                                
                                elif playerEnergy >= 10:
                                    main = input(f"[1] Normal Attack\n[2] Defense\nChoose by number(1/2): ")
                                    if main == "1" or main == "" or "normal" in main.lower():
                                        playerAttackDamage, enemyHealth, experience, isEnemyDefended = playerNormalAttack(enemyHealth, experience, isEnemyDefended)
                                    elif main == "2" or "defense" in main.lower():
                                        enemyAttackDamage, playerEnergy, isPlayerDefended = playerDefense(enemyAttackDamage, playerEnergy, isPlayerDefended)
                                    else:
                                        print("Wrong move!! Turn skipped!!😑")
                            else:
                                main = input(f"[1] Normal Attack or Press 'Enter' to attack normally: ")
                                if main == "1" or "normal" in main.lower() or main == "":
                                    playerAttackDamage, enemyHealth, experience, isEnemyDefended = playerNormalAttack(enemyHealth, experience, isEnemyDefended)
                                else:
                                    print("Wrong move!! Turn skipped!!😑")
                        else:
                            print(f"You defeated {enemy}!! VICTORY!! 🏆")
                            break
                            
                    else:
                        print("Wrong move!! Turn skipped!!😑")

                elif playerEnergy >= 20:
                    main = input(f"[1] Normal Attack\n[2] Defense\n[3] Power Attack \nChoose by number(1/2): ")
                    if main == "1" or main == "" or "normal" in main.lower():
                        playerAttackDamage, enemyHealth, experience, isEnemyDefended = playerNormalAttack(enemyHealth, experience, isEnemyDefended)
                    elif main == "2" or "defense" in main.lower():
                        enemyAttackDamage, playerEnergy, isPlayerDefended = playerDefense(enemyAttackDamage, playerEnergy, isPlayerDefended)
                    elif main == "3" or "power" in main.lower():
                        playerAttackDamage, enemyHealth, playerEnergy, experience, isEnemyDefended = playerPowerAttack(enemyHealth, playerEnergy, experience, isEnemyDefended)
                    else:
                        print("Wrong move!! Turn skipped!!😑")
                
                elif playerEnergy >= 10:
                    main = input(f"[1] Normal Attack\n[2] Defense \nChoose by number(1/2): ")
                    if main == "1" or main == "" or "normal" in main.lower():
                        playerAttackDamage, enemyHealth, experience, isEnemyDefended = playerNormalAttack(enemyHealth, experience, isEnemyDefended)
                    elif main == "2" or "defense" in main.lower():
                        enemyAttackDamage, playerEnergy, isPlayerDefended = playerDefense(enemyAttackDamage, playerEnergy, isPlayerDefended)
                    else:
                        print("Wrong move!! Turn skipped!!😑")

except KeyboardInterrupt:
    print("\n⚠️  Forcefully exited the game!! ⚠️")

try:
    with open("mainFolder/save.json", "r") as f:
        data = json.load(f)
        if experience >= 100:
            experience -= 100
            level += 1
        data["experience"] = experience
        data["level"] = level
        
    with open("mainFolder/save.json", "w") as f:
        json.dump(data, f, indent=4)

except (json.JSONDecodeError, FileNotFoundError, KeyError):
    data = {"level": 1, "experience": 0}
    with open("mainFolder/save.json", "w") as f:
        json.dump(data, f, indent=4)
