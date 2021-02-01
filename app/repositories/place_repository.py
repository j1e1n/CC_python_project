from db.run_sql import run_sql
from models.place import Place 
from models.country import Country
import repositories.country_repository as country_repository

def save(place):
    sql = "INSERT INTO places (name, country_id, description, visited) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [place.name, place.country.id, place.description, place.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    place.id = id
    return place


def select_all():
    places = []
    sql = "SELECT * FROM places"
    results = run_sql(sql)

    for row in results:
        country  = country_repository.select(row['country_id'])
        place = Place(row['name'], country, row['description'], row['visited'], row['id'])
        places.append(place)
    return places


def delete_all():
    sql = "DELETE FROM places"
    run_sql(sql)