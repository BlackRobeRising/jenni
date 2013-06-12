"""roll

TODO: 
	second  d = drop
	re-roll r = re-roll based on next #
	exploding e = roll a second die of the same size if it is that # or above

	automatically sort dice from lowest to highest die	
"""

from random import randint


def roll_dice(dice = 1, sides = 20):
	try: return [randint(1, sides) for i in range(dice)]
	except: return []

def roll(jenni, input):

	roll_string = input.group(2)

	if(roll_string == None):
		result = roll_dice()
	        jenni.reply("Rolled: 1d20 - "+str(result)+" == "+str(sum(result)) )
	else:
		phase = "dice"	
		dice = ""
		sides = ""
		modifier = []	
	
		for c in roll_string:
			if (c.isdigit() or c == '.'):
				if(phase == "dice"):
					dice = str(dice) + str(c)
				elif(phase == "sides"):
					sides = str(sides) + str(c)
				elif(phase == "new_modifier"):
					modifier.append(str(c))
					phase = "modifier"
				elif(phase == "modifier"):
					modifier[-1] = modifier[-1] + str(c)
			else:
				if(phase == "modifier"):
					phase = "new_modifier"
				elif(phase == "sides"):
					if( int(sides) > 100 ):
						sides = 100

				if(phase == "dice"):
					phase = "sides"
					if( int(dice) > 50):
						dice = 50
				elif(phase == "sides"):
					phase = "new_modifier"
                                        if(c == "+"):
                                                modifier.append(c)
                                        elif(c == "-"):
                                                modifier.append(c)
                                        elif(c == "*"):
                                                modifier.append(c)
                                        elif(c == "/"):
                                                modifier.append(c)
                                        elif(c =="\\"):
                                                modifier.append(c)
                                        else:
                                                phase = "done"
				elif(phase == "new_modifier"):
					if(c == "+"):
						modifier.append(c)
					elif(c == "-"):
						modifier.append(c)
					elif(c == "*"):
						modifier.append(c)
					elif(c == "/"):
						modifier.append(c)
					elif(c =="\\"):
						modifier.append(c)
					else:
						phase = "done"
				else:
					phase = "done"		
		
		operator = ""	

		result_list = roll_dice( int(dice), int(sides) )
		result = sum(result_list)
		result_r = result
		mod_string = ""

		for mod in modifier:
			mod_string = mod_string+str(mod)
			if(operator == ""):
				operator = mod
			else:
				if(operator == "+"):
					result = result + float(mod)			
					operator = ""
				elif(operator == "-"):
					result = result - float(mod)
					operator = ""
				elif(operator == "*"):
					result = result * float(mod)
					operator = ""
				elif(operator == "/"):
					result = result / float(mod)
					operator = ""
				elif(operator =="\\"):
					result = result / float(mod)
					operator = ""

		roll_string_r = str(dice)+"d"+str(sides)+str(mod_string) 	
		jenni.reply("Rolled: "+roll_string_r+" - "+str(result_list)+"="+str(result_r)+" "+str(mod_string)+" == "+str(int(result)))

			
roll.commands = ['roll']
roll.priority = 'medium'
