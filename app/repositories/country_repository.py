from db.run_sql import run_sql
from models.country import Country
from models.place import Place


def save(country):
    sql = "INSERT INTO countries (name) VALUES (%s) RETURNING *"
    values = [country.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['id'])
        countries.append(country)
    return countries


def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result != None:
        country = Country(result['name'], result['id'])
    return country


def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)


def places(country):
    places = []

    sql = "SELECT * FROM places WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        place = Place(row['name'], row['country_id'], row['description'], row['visited'], row['id'] )
        places.append(place)
    return places


def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(country):
    sql = "UPDATE countries SET name = %s WHERE id = %s"
    values = [country.name, country.id]
    run_sql(sql, values)
