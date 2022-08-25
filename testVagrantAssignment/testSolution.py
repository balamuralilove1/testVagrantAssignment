# balamurali chellaboina
# V.S.M college of engineering , ramachandrapuram
# 2021
# 9581773166
# balamuralilove1@gmail.com


class Planets:
    def __init__(self, planets_list):
        self.planets_list = []

    def adding_planet(self, name, surface_gasses, no_of_moons, has_rings):
        self.planets_list.extend(
            [[name, surface_gasses, no_of_moons, has_rings]])

    def count_of_having_rings(self):
        planets = self.planets_list
        count_of_moons = 0
        for each_planet in planets:
            if(each_planet[3] == "Yes"):
                count_of_moons += each_planet[2]
        print(count_of_moons)

    def maximum_gases(self):
        planets = self.planets_list
        gases_list = []
        unique_gases = []
        gas = ""
        count = 0
        for each_planet in planets:
            if(len(each_planet[1]) != 0):
                for gas in each_planet[1]:
                    gases_list.append(gas)
                    if(gas not in unique_gases):
                        unique_gases.append(gas)
        for each_gas in unique_gases:
            gas_count = gases_list.count(each_gas)
            if(gas_count > count):
                gas = each_gas
                count = gas_count
            elif(gas_count == count):
                gas = gas + " " + each_gas
        print(gas)


planet_list = Planets("")
planet_list.adding_planet("Mercury", [], 0, "No")
planet_list.adding_planet("Venus", ["Carbon Dioxide", "Nitrogen"], 0, "No")
planet_list.adding_planet("Earth", ["Nitrogen", "Oxygen"], 1, "No")
planet_list.adding_planet("Jupitor", ["Hydrogen", "Helium"], 79, "Yes")
planet_list.adding_planet("Saturn", ["Hydrogen", "Helium"], 83, "Yes")
planet_list.adding_planet(
    "Uranus", ["Hydrogen", "Helium", "Methane"], 27, "Yes")
planet_list.count_of_having_rings()
planet_list.maximum_gases()
