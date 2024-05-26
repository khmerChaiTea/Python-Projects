# Pokémon Training Game

def catch_pokemon(powers):
    if not powers:
        return
    
    min_power = max_power = powers[0]
    
    for power in powers[1:]:
        if power < min_power:
            min_power = power
        elif power > max_power:
            max_power = power
        
        
        print(min_power,max_power)

# Example usage:
powers = [3, 8, 9, 7]
catch_pokemon(powers)
print('\n')

# python code to train pokemon 
powers = [3, 8, 9, 7] 

mini, maxi = 0, 0

for power in powers: 
	if mini == 0 and maxi == 0: 
		mini, maxi = powers[0], powers[0] 
		print(mini, maxi) 
	else: 
		mini = min(mini, power) 
		maxi = max(maxi, power) 
		print(mini, maxi) 
		
# Time Complexity is O(N) with Space Complexity O(1) 
