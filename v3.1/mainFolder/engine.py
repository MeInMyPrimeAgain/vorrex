import random
import math
from beast import enemy, enemyAttackPower
from player import playerAttackPower, playerInitialHealth


# Normal Attack (player)
def playerNormalAttack(enemyHealth, experience, isEnemyDefended):
    playerAttackDamage = random.randint(0, playerAttackPower)
    if isEnemyDefended:
        enemyHealth -= (math.ceil((0.33 * playerAttackDamage)/10))
        isEnemyDefended = False
    else:
        enemyHealth -= (math.ceil((playerAttackDamage/10)))
    if enemyHealth <= 0:
        print(f"You defeated {enemy}!! VICTORY!! 🏆")
        experience += 20
    else:
        print(f"You've dealt a damage of {playerAttackDamage} --- {enemy}'s health: {math.ceil((enemyHealth/enemy.health)*100)}%\n")
    return playerAttackDamage, enemyHealth, experience, isEnemyDefended

# Normal Attack (enemy)
def enemyNormalAttack(playerHealth, experience, isPlayerDefended):
    enemyAttackDamage = random.randint(0, enemyAttackPower)
    if isPlayerDefended:
        playerHealth -= (math.ceil((0.33 * enemyAttackDamage)/10))
        isPlayerDefended = False
    else:
        playerHealth -= math.ceil(enemyAttackDamage/10)
    if playerHealth <= 0:
        print(f"{enemy} defeated you!! DEFEAT!! 😞")
        experience += 2
    else:
        print(f"{enemy} dealt a damage of {enemyAttackDamage} --- Your health: {math.ceil((playerHealth/playerInitialHealth)*100)}%\n")
    return enemyAttackDamage, playerHealth, experience, isPlayerDefended

# The Power Attack (player)
def playerPowerAttack(enemyHealth, playerEnergy, experience, isEnemyDefended):
    playerAttackDamage = random.randint(0, playerAttackPower)
    playerAttackDamage += math.ceil(2/3 * playerAttackDamage)
    playerEnergy = max(0, playerEnergy - 20)
    if isEnemyDefended:
        enemyHealth -= (math.ceil((0.33 * playerAttackDamage)/10))
        isEnemyDefended = False
    else:
        enemyHealth -= math.ceil(playerAttackDamage/10)
    if enemyHealth <= 0:
        print(f"You defeated {enemy}!! VICTORY!! 🏆")
        experience += 20
    else:
        print(f"You've dealt a power damage of {playerAttackDamage} --- {enemy}'s health: {math.ceil((enemyHealth/enemy.health)*100)}% - Your ⚡: {playerEnergy}\n")
    return playerAttackDamage, enemyHealth, playerEnergy, experience, isEnemyDefended

# The Power Attack (enemy)
def enemyPowerAttack(playerHealth, enemyEnergy, experience, isPlayerDefended):
    enemyAttackDamage = random.randint(0, enemyAttackPower)
    enemyAttackDamage += math.ceil(2/3 * enemyAttackDamage)
    enemyEnergy = max(0, enemyEnergy - 20)
    if isPlayerDefended:
        playerHealth -= (math.ceil((0.33 * enemyAttackDamage)/10))
        isPlayerDefended = False
    else:
        playerHealth -= math.ceil(enemyAttackDamage/10)
    if playerHealth <= 0:
        print(f"{enemy} defeated you!! DEFEAT!! 😞")
        experience += 2
    else:
        print(f"{enemy} dealt a power damage of {enemyAttackDamage} --- Your health: {math.ceil((playerHealth/playerInitialHealth)*100)}% - {enemy}'s ⚡: {enemyEnergy}\n")
    return enemyAttackDamage, playerHealth, enemyEnergy, experience, isPlayerDefended

# Player Defense
def playerDefense(enemyAttackDamage, playerEnergy, isPlayerDefended):
    playerEnergy = max(0, playerEnergy - 10)
    print(f"You are defending yourself!! --- Your ⚡: {playerEnergy}\n")
    isPlayerDefended = True
    return enemyAttackDamage, playerEnergy, isPlayerDefended

# Enemy Defense
def enemyDefense(playerAttackDamage, enemyEnergy, isEnemyDefended): 
    enemyEnergy = max(0, enemyEnergy - 10)
    print(f"{enemy} is defending himself!! --- {enemy}'s ⚡: {enemyEnergy}\n")
    isEnemyDefended = True
    return playerAttackDamage, enemyEnergy, isEnemyDefended

# Freeze attack (player)
def playerFreeze(enemyEnergy, playerEnergy):
    enemyEnergy = min(enemyEnergy + 20, 100)
    playerEnergy = max(0, playerEnergy - 30)
    print(f"You froze {enemy}!! --- Your⚡: {playerEnergy}")
    return enemyEnergy, playerEnergy

# Freeze attack (enemy)
def enemyFreeze(playerEnergy, enemyEnergy):
    playerEnergy = min(playerEnergy + 20, 100)
    enemyEnergy = max(0, enemyEnergy - 30)
    print(f"{enemy} froze you!! --- {enemy}'s⚡: {enemyEnergy}")
    return playerEnergy, enemyEnergy
