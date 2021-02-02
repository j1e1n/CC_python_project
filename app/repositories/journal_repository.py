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
