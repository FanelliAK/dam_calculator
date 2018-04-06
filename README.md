
# dam_calculator
damage_calculator for a roguelite

this damage calculator sometimes get's stuck on the dice roll miss, it's very random and 99% of the time works just fine.  if you get this buggy loops just stop run.  I use this program with Thonny so I'm able to edit and then run to get output.

it has 3 variables, hp, player attack, monster defense
locations for damage calulator and critical
d_20 dice roll for hit chance and critical/miss
if damage is less than block with the calculator a block happens.


edit: I realize I suck at explaining things so I copied what can be changed and if everything is left alone the program will work. this way it's more useable to everyone cause I imagine people will want to put in their own from their rogue game. 

        # # # # # # # # # # # # # # # # # # # #
        # Damage Equation # # Damage Equation #
        # # # # # # # # # # # # # # # # # # # #            
        max_dam = player_atk + randint(0, player_atk)            
        max_def = randint(0, monster_def) + randint(0, monster_def)                    
        final_dam = max_dam - max_def

            # # # # # # # # # # # # # # # # # # # # # #
            # This is the critical damage calculation #
            # # # # # # # # # # # # # # # # # # # # # #
            max_crit = max_dam * 2 + randint(0, 1)
            crit_dam = max_crit - max_def                
            ###########################################

this spot can be changed if you want your own chance to hit mechanic.
    # Rolls the 20 sided Dice
    d_20 = randint(1, 20)


  and at top we have
  # player attack, adjust as needed!
  player_atk = 10
  
  # monster defense, adjust as needed!
  monster_def = 10
  
  def strike():
      # Set Monster Total hitpoints, will be deducted as calculator rolls
      monster_hp = 100
