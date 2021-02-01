import pdb
from models.place import Place
from models.country import Country

import repositories.place_repository as place_repository
import repositories.country_repository as country_repository


place_repository.delete_all()
country_repository.delete_all()

country_1 = Country("United States")
country_repository.save(country_1)

country_2 = Country("England")
country_repository.save(country_2)

place_1 = Place("RMS Queen Mary", country_1, "Former war ship with a history of accidental deaths.")
place_repository.save(place_1)

place_2 = Place("Ancient Ram Inn", country_2, "1100s pub, said to be the most haunted hotel in the country.")
place_repository.save(place_2)

pdb.set_trace()