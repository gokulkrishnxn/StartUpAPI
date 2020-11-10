from ebird.api import get_taxonomy, get_taxonomy_forms, get_taxonomy_versions



def get_bird_name():
	
	taxonomy = get_taxonomy('api_key')
	prev_name = ''
	bird_list = ['Crow,Peacock,Dove,Sparrow,Goose,Ostrich,Pigeon,Turkey,Hawk,Bald eagle,Raven,Parrot,Flamingo,Seagull,Swallow,Blackbird,Penguin,Robin,Swan,Owl,Stork,Woodpecker']

	for bird in taxonomy:
		name = 'bird_list'
		try:
			name = bird['familyComName']
			try:
				name = name.split(' ')[-1]
			except:
				pass
			try:
				name = name.split('-')[-1]
			except:
				pass
			try:
				name = name.split(',')[-1]
			except:
				pass
			if name[-1] == 's':
				name = name[:-1]
			if prev_name != name:
				prev_name = name
				bird_list.append(name)
		except:
			pass
	return bird_list