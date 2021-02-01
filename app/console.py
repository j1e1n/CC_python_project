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




pdb.set_trace()