import math
from player import playerInitialHealth
from beast import *
from engine import *

# The Enemy AI
def enemyAI(enemyHealth, playerHealth, enemyEnergy, playerEnergy, enemyAttackDamage, playerAttackDamage, isPlayerDefended, isEnemyDefended, experience):
    enemyHealthPercent = math.ceil((enemyHealth/enemy.health)*100)
    playerHealthPercent = math.ceil((playerHealth/playerInitialHealth)*100)

    if enemyHealthPercent < 20 and playerHealthPercent > 10:
        if enemyEnergy >= 20:
            enemyAttackDamage, playerHealth, enemyEnergy, experience, isPlayerDefended = enemyPowerAttack(playerHealth, enemyEnergy, experience, isPlayerDefended)
        else:
            enemyAttackDamage, playerHealth, experience, isPlayerDefended = enemyNormalAttack(playerHealth, experience, isPlayerDefended)
    elif enemyHealthPercent > 90:
        enemyAttackDamage, playerHealth, experience, isPlayerDefended = enemyNormalAttack(playerHealth, experience, isPlayerDefended)
    elif enemyHealthPercent > 60:
        if playerEnergy < 100:
            if enemyEnergy >= 50:
                playerEnergy, enemyEnergy = enemyFreeze(playerEnergy, enemyEnergy)
                enemyAttackDamage, playerHealth, enemyEnergy, experience, isPlayerDefended = enemyPowerAttack(playerHealth, enemyEnergy, experience, isPlayerDefended)
                if playerHealth > 0:
                    enemyAttackDamage, playerHealth, experience, isPlayerDefended = enemyNormalAttack(playerHealth, experience, isPlayerDefended)
            elif enemyEnergy >= 30:
                playerEnergy, enemyEnergy = enemyFreeze(playerEnergy, enemyEnergy)
                enemyAttackDamage, playerHealth, experience, isPlayerDefended = enemyNormalAttack(playerHealth, experience, isPlayerDefended)
                enemyAttackDamage, playerHealth, experience, isPlayerDefended = enemyNormalAttack(playerHealth, experience, isPlayerDefended)
        else:
            if enemyEnergy >= 20:
                enemyAttackDamage, playerHealth, enemyEnergy, experience, isPlayerDefended = enemyPowerAttack(playerHealth, enemyEnergy, experience, isPlayerDefended)
    elif enemyHealthPercent > 40:
        if enemyEnergy > 50:
            enemyAttackDamage, playerHealth, enemyEnergy, experience, isPlayerDefended = enemyPowerAttack(playerHealth, enemyEnergy, experience, isPlayerDefended)
        else:
            enemyAttackDamage, playerHealth, experience, isPlayerDefended = enemyNormalAttack(playerHealth, experience, isPlayerDefended)
    elif enemyHealthPercent > 20:
        if enemyEnergy > 20:
            enemyAttackDamage, playerHealth, enemyEnergy, experience, isPlayerDefended = enemyPowerAttack(playerHealth, enemyEnergy, experience, isPlayerDefended)
        else:
            enemyAttackDamage, playerHealth, experience, isPlayerDefended = enemyNormalAttack(playerHealth, experience, isPlayerDefended)
    elif enemyHealthPercent <=20:
        if enemyEnergy >= 20:
            playerAttackDamage, enemyEnergy, isEnemyDefended = enemyDefense(playerAttackDamage, enemyEnergy, isEnemyDefended)
        else:
            enemyAttackDamage, playerHealth, experience, isPlayerDefended = enemyNormalAttack(playerHealth, experience, isPlayerDefended)
    else:
        enemyAttackDamage, playerHealth, experience, isPlayerDefended = enemyNormalAttack(playerHealth, experience, isPlayerDefended)
    
    return enemyAttackDamage, playerHealth, enemyEnergy, isPlayerDefended, isEnemyDefended, experience