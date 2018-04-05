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
            max_def = randint(0, monster_def)                    
            final_dam = max_dam - max_def
            #######################################
            # this equation uses randint(0, x) so that you get a random damage amount

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

                else:
                    print('BLOCK')
                    # removing any old damage scores for average damage
                    final_damage = 0
                    crit_dam = 0

            # if the dice rolls a 19 or 20 it's a critical attack        
            elif monster_hp > 0 and d_20 > 18:

                # # # # # # # # # # # # # # # # # # # # # #
                # This is the critical damage calculation #
                # # # # # # # # # # # # # # # # # # # # # #
                crit_dam = final_dam * 2 + randint(0, 1)                
                ###########################################
                # the randint(0, 1) is because any number * 2 ends up even, this is so you                
                # can have an odd number as your critical damage value

                # for display purposes
                print('crit damage\n d20 roll =',d_20,', dam =', max_dam,', def =', max_def,
                      ',final damage =', final_dam, ' crit damage =', crit_dam)

                # this is a critical hit            
                if final_dam > 0:
                    remaining_hp = monster_hp - crit_dam
                    print('Monster Hp =', (remaining_hp), '/ ', total_hp, '\n')
                    monster_hp = remaining_hp
                    final_dam = 0

                # if you hit a crit but no damage is done because of defense
                else:
                    print('CRIT BLOCK')
                    print('')
                    
                    # removing any old damage scores for average damage
                    final_damage = 0
                    crit_dam = 0

            # when the monster loses all it's HP, you get a taly with average damage and total attacks            
            elif monster_hp < 0:
                average_dam = total_damage / total_attack

                print('Monster dead, congratulations\nTotal Attacks =', total_attack, '; and Average Damage = %.1f' % average_dam)
                print('Total damage done = ', total_damage)
                break


        else:
            print('error')
strike() 
