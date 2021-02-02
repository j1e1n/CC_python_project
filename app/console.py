import pdb
from models.place import Place
from models.country import Country
from models.journal import Journal

import repositories.place_repository as place_repository
import repositories.country_repository as country_repository
import repositories.journal_repository as journal_repository


place_repository.delete_all()
country_repository.delete_all()

country_1 = Country("United States")
country_repository.save(country_1)

country_2 = Country("England")
country_repository.save(country_2)

place_1 = Place("RMS Queen Mary", country_1, "Former war ship with a history of accidental deaths.", True)
place_repository.save(place_1)

place_2 = Place("Ancient Ram Inn", country_2, "1100s pub, said to be the most haunted hotel in the country.")
place_repository.save(place_2)

place_3 = Place("The Stanley Hotel", country_1, "The hotel that inspired Stephen King's 'The Shining'.")
place_repository.save(place_3)

place_4 = Place("Blickling Hall", country_2, "The headless ghost of Anne Boleyn is said to appear here.")
place_repository.save(place_4)

place_5 = Place("Dunster Castle", country_2, "11th century fortress with a military history", True)
place_repository.save(place_5)

place_6 = Place("Eastern State Penitentiary", country_1, "Old prison with a history of severe punishments")
place_repository.save(place_6)

journal_entry_1 = Journal(place_1, "Very eerie location, heard childrens' voices by the pool.")
journal_repository.save(journal_entry_1)

journal_entry_2 = Journal(place_1, "Went back today, visited the engine room this time, there's an overwhelming feeling of being watched.")
journal_repository.save(journal_entry_2)

journal_entry_3 = Journal(place_5, "A lot of activity here! Witnessed an apparition of a man in green and other guests dogs refused to enter the Gatehouse area...")
journal_repository.save(journal_entry_3)


pdb.set_trace()