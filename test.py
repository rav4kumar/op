### Don't change this ###
import random
#########################

def get_damage(attack, defense):

  attack_value = get_roll(attack)

  defense_value = get_roll(defense)

  damage = None

  if defense_value > attack_value:

    damage = 0

  else:

    damage = attack_value - defense_value

  return damage

def get_roll(rollstring):
  try:

    roll_list = rollstring.split("d")

    numOfdice = int(roll_list[0])

    side = int(roll_list[1])

    sum = 0

    for i in range(numOfdice):

      sum = sum + random.randint(1, side)

  except:

    print("wrong input")

  return sum
def main_menu():
  try:

    numOfRoll = int(input("How many rolls do you want to take? "))

    attack_defense_list = []

    for num in range(numOfRoll):

      str_input = "Input attack and defense roll " + str(num+1) +": "

      attack_defense = input(str_input)

      attack_defense_list.append(attack_defense)

    for attack_defense in attack_defense_list:

      attack_and_defense = attack_defense.split(",")

      attack = attack_and_defense[0]

      defense = attack_and_defense[1]

      damage = get_damage(attack, defense)

      output_str = "Attack:"+ attack + ", Defense:" + defense + " : Damage: " + str(damage)

      print(output_str)

  except:

    print("wrong input")


### Don't change this ###
main_menu()
#########################
