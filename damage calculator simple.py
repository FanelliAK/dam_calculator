from random import randint

# player attack, adjust as needed!
player_atk = 10

# monster defense, adjust as needed!
monster_def = 10

def strike():
    # Set Monster Total hitpoints, will be deducted as calculator rolls
    monster_hp = 100
    
    # Just variables set to make things work
    total_hp = monster_hp
    total_attack = 0
    total_damage = 0
    final_dam = 0
    crit_dam = 0
    
    # loop while monster health is remaining    
    while True:
        
        # Adds total count to give an average at the end
        total_attack += 1
        total_damage += final_dam
        total_damage += crit_dam

        # Rolls the 20 sided Dice
        d_20 = randint(1, 20)

        # this is a missed attack with the dice roll        
        if d_20 < 2:

            print('miss your d_20 roll =', d_20)
            print(' ')
            
            # this is so the average damage doesn't increase on a miss attack
            final_dam = 0
            crit_dam = 0
            
            continue
        # dice rolled a hit!    
        elif d_20 >= 2:

            # # # # # # # # # # # # # # # # # # # #
            # Damage Equation # # Damage Equation #
            # # # # # # # # # # # # # # # # # # # #            
            max_dam = player_atk + randint(0, player_atk)            
            max_def = randint(0, monster_def) + randint(0, monster_def)                    
            final_dam = max_dam - max_def
            #######################################
            # this equation uses randint(0, x) so that you get a random damage amount
            # player has full attack + random 0 to attack #
            # monster defense rolls twice, I don't use * 2 so I can get odd numbers

            # if the dice rolls between 2 - 18 it's a standard hit
            if monster_hp > 0 and d_20 <= 18:
                
                # this print is to give display info                       
                print('d20 roll =',d_20,', dam =', max_dam,', def =', max_def,', final damage =', final_dam)

                if final_dam > 0:
                    # basic attack that rolled and did damage
                    remaining_hp = monster_hp - final_dam
                    print('Monster Hp =', (remaining_hp), '/ ', total_hp)
                    monster_hp = remaining_hp
                    print('')
                    crit_dam = 0
                    
                # if dice rolled a hit, but no damage is done then it's blocked
                else:
                    print('BLOCK!\n')
                    # removing any old damage scores for average damage
                    final_damage = 0
                    crit_dam = 0

            # if the dice rolls a 19 or 20 it's a critical attack        
            elif monster_hp > 0 and d_20 > 18:

                # # # # # # # # # # # # # # # # # # # # # #
                # This is the critical damage calculation #
                # # # # # # # # # # # # # # # # # # # # # #
                max_crit = max_dam * 2 + randint(0, 1)
                crit_dam = max_crit - max_def                
                ###########################################
                # the randint(0, 1) is because any number * 2 ends up even, this is so you                
                # can have an odd number as your critical damage value

                # for display purposes
                print('Crit Damage!\n d20 roll =',d_20,', dam =', max_dam,', def =', max_def,
                      ',final damage =', final_dam, ' max_crit/crit damage =', max_crit, '/', crit_dam)

                # this is a critical hit            
                if crit_dam > 0:
                    remaining_hp = monster_hp - crit_dam
                    print('Monster Hp =', (remaining_hp), '/ ', total_hp, '\n')
                    monster_hp = remaining_hp
                    final_dam = 0

                # if you hit a crit but no damage is done because of defense
                else:
                    print('CRIT BLOCK!!')
                    print('')
                    
                    # removing any old damage scores for average damage
                    final_damage = 0
                    crit_dam = 0

            # when the monster loses all it's HP, you get a taly with average damage and total attacks            
            elif monster_hp < 0:
                # this talies your total attacks, because it loops one more time after monster dies I
                # remove - 1
                
                total_attack2 = total_attack - 1
                
                # this get's the average damage
                average_dam = total_damage / total_attack2

                print('Monster dead, congratulations\nTotal Attacks =', total_attack2, '; and Average Damage = %.1f' % average_dam)
                print('Total damage done = ', total_damage)
                break


        else:
            print('error')
strike() 
