def do_turn(pw):
	if len(pw.my_fleets()) >= 1:
		return

	if len(pw.my_planets()) == 0:
		return

	if len(pw.enemy_planets()) == 0:
		return

	if len(pw.neutral_planets()) >= 1:
		dest = pw.get_planet(findSmallestPlanet(pw.neutral_planets()))
	else:
		if len(pw.enemy_planets()) >= 1:
			dest = pw.get_planet(findSmallestPlanet(pw.enemy_planets()))

	if len(pw.my_planets()) < 7:		
		source = pw.get_planet(findBiggestPlanet(pw.my_planets()))
	else:
		source = findClosestPlanetToDest(dest, findBiggestPlanets(pw.my_planets), pw)
	
	num_ships = source.num_ships() / 2
	pw.debug('Num Ships: ' + str(num_ships))

	pw.issue_order(source, dest, num_ships)

def findSmallestPlanet(planets):
	smallestPlanetId = 0
	smallestPlanetSize = 999999999999
	for planet in planets:
		if planet.num_ships() < smallestPlanetSize:
			smallestPlanetId = planet.planet_id()
			smallestPlanetSize = planet.num_ships()

	return smallestPlanetId

def findBiggestPlanet(planets):
	biggestPlanetId = 0
	biggestPlanetSize = 0
	for planet in planets:
		if planet.num_ships() > biggestPlanetSize:
			biggestPlanetId = planet.planet_id()
			biggestPlanetSize = planet.num_ships()

	return biggestPlanetId

def findSmallestPlanets(planets):
	planet_dict = {}

	for planet in planets:
		planet_dict[planet.planet_id()] = planet.num_ships()

	sorted_dict = sorted(planet_dict.items(), key=lambda x: x[1])

	return sorted_dict.keys()[:3]

def findBiggestPlanets(planets):
	planet_dict = {}

	for planet in planets:
		planet_dict[planet.planet_id()] = planet.num_ships()

	sorted_dict = sorted(planet_dict.items(), key=lambda x: x[1], reverse=True)

	return sorted_dict.keys()[:3]

def findClosestPlanetToDest(dest, planets, pw)
	closestPlanetDistance = 999999999999
	closestPlanet = dest
	for planet in planets:
		if closestPlanetDistance > pw.distance(pw.get_planet(planet), dest):
			closestPlanetDistance = pw.distance(pw.get_planet(planet), dest)
			closestPlanet = pw.get_planet(planet)
	
	return closestPlanet
