from db.run_sql import run_sql
from models.journal import Journal
from models.place import Place 
import repositories.place_repository as place_repository

def save(journal):
    sql = "INSERT INTO journal_entries (place_id, journal_entry) VALUES (%s, %s) RETURNING *"
    values = [journal.place.id, journal.journal_entry]
    results = run_sql(sql, values)
    id = results[0]['id']
    journal.id = id
    return journal


def select_all():
    entries = []

    sql = "SELECT * FROM journal_entries"
    results = run_sql(sql)

    for row in results:
        place = place_repository.select(row['place_id'])
        entry = Journal(place, row['journal_entry'], row['id'])
        entries.append(entry)
        print(row)
    return entries



def delete(id):
    sql = "DELETE FROM journal_entries WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(journal):
    sql = "UPDATE journal_entries SET (place_id, journal_entry) = (%s, %s) WHERE id = %s"
    values = [journal.place.id, journal.journal_entry, journal.id]
    run_sql(sql, values)


def select(id):
    journal = None
    sql = "SELECT * FROM journal_entries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result != None:
        journal = Journal(result['place_id'], result['journal_entry'], result['id'])
    return journal