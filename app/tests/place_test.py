import unittest
from models.place import Place

class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place = Place("Edinburgh Castle", "Scotland", "Old castle with a history of ghost sightings", False)


    def test_place_has_name(self):
        self.assertEqual("Edinburgh Castle", self.place.name)

        
    def test_place_has_country(self):
        self.assertEqual("Scotland", self.place.country)


    def test_place_has_description(self):
        self.assertEqual("Old castle with a history of ghost sightings", self.place.description)

    
    def test_can_mark_as_visited(self):
        self.place.mark_as_visited()
        self.assertEqual(True, self.place.visited)