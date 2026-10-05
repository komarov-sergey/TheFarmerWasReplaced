import utils

def wood_harvest():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
				
			if can_harvest():
				harvest()
				if utils.is_even(i):
					#use_item(Items.Fertilizer)
					plant(Entities.Bush)
					use_item(Items.Fertilizer)
				else:
					#use_item(Items.Fertilizer)
					plant(Entities.Tree)
					use_item(Items.Fertilizer)
								
			move(North)
		move(East)

def sunflower_harvest():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
				
			if can_harvest():
				harvest()
				till()
				use_item(Items.Fertilizer)
				plant(Entities.Sunflower)

								
			move(North)
		move(East)
			

def carrot_harvest():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
				
			if can_harvest():
				harvest()
				till()
				plant(Entities.Carrot)
								
			move(North)
		move(East)
		
def pumpkin_harvest():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
				
			if can_harvest():
				harvest()
				
			till()
			use_item(Items.Fertilizer)
			plant(Entities.Pumpkin)
								
			move(North)
		move(East)
		
def cactus_harvest():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
				
			if can_harvest():
				harvest()
				
			till()
			plant(Entities.Cactus)
								
			move(North)
		move(East)
			
def auto_harvest(wood_count, sunflower_count, carrot_count, pumpkin_count, cactus_count):
	clear()
	change_hat(Hats.Traffic_Cone)
	while True:
		for i in range(0, wood_count):
			wood_harvest()
		for i in range(0, sunflower_count):
			sunflower_harvest()
		for i in range(0, carrot_count):
			carrot_harvest()
		for i in range(0, pumpkin_count):
			pumpkin_harvest()
		for i in range(0, cactus_count):
			cactus_harvest()