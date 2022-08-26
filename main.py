# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
Goal_1="Gullit"
Goal_2="Van Basten"
GoalMin_1="32"
GoalMin_2="54"
Scorers=(Goal_1+" "+GoalMin_1)+", "+(Goal_2+" "+GoalMin_2)
print(Scorers)
print(f"{Goal_1} scored in the {GoalMin_1}nd minute\n{Goal_2} scored in the {GoalMin_2}th minute")
player="Marco van Basten"
last_name="van Basten"
first_name=player[player.find("Marco"):5]
print(first_name)
z=len(first_name)
Last_name_len=len(player[player.find("van Basten"):])
print(Last_name_len)
name_short=player[0:1]+". "+last_name
print(name_short)
chant_0=(first_name+"! ")*z
chant=chant_0[0:len(chant_0)-1]
print(chant)
