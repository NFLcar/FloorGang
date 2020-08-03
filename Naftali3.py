def do_turn(pw):
	if len(pw.my_planets()) == 0:
		return

	if len(pw.enemy_planets()) == 0:
		return

	source = pw.get_planet(findBiggestPlanet(pw.my_planets()))

	if len(pw.not_my_planets()) >= 1:
		dest = findClosestPlanetToDest(source, pw.not_my_planets(), pw)
	
	num_ships = source.num_ships() / 2
	
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

def findClosestPlanetToDest(dest, planets, pw):
	closestPlanetDistance = 999999999999
	closestPlanet = dest
	for planet in planets:
		if closestPlanetDistance > pw.distance(planet, dest):
			closestPlanetDistance = pw.distance(planet, dest)
			closestPlanet = planet
	
	return closestPlanet
