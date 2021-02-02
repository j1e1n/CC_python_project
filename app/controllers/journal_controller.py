from flask import Flask, render_template, request, redirect
from flask import Blueprint

journal_blueprint = Blueprint("journal", __name__)

from repositories import place_repository
from repositories import journal_repository
from models.journal import Journal
from models.place import Place

@journal_blueprint.route('/journal')
def journal():
    entries = journal_repository.select_all()
    return render_template("journal/index.html", all_entries = entries)


@journal_blueprint.route('/journal/new', methods = ['GET'])
def new_journal_entry():
    places = place_repository.select_all()
    visited_places = []
    for place in places:
        if place.visited == True:
            visited_places.append(place)

    return render_template("journal/new.html", visited_places = visited_places)


@journal_blueprint.route('/journal', methods=['POST'])
def create_journal_entry():
    place_id = request.form['place_id']
    journal_entry = request.form['entry']
   
    place = place_repository.select(place_id)
    entry = Journal(place, journal_entry)
    journal_repository.save(entry)
    return redirect('/journal')
