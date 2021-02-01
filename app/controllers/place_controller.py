from flask import Flask, render_template, request, redirect
from flask import Blueprint

places_blueprint = Blueprint("places", __name__)

from repositories import place_repository
from repositories import country_repository
from models.place import Place


@places_blueprint.route('/places')
def places():
    places = place_repository.select_all()
    visited = []
    not_visited = []
    for place in places:
        if place.visited == True:
            visited.append(place)
        else:
            not_visited.append(place)

    return render_template("places/index.html", title="Places", visited=visited, not_visited=not_visited )


@places_blueprint.route('/places/<id>', methods=['GET'])
def show_place(id):
    place = place_repository.select(id)
    visited = "Not yet."
    if place.visited == True:
        visited = "Yes."

    return render_template("places/show.html", place=place, visited =visited)