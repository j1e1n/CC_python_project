from flask import Flask, render_template, request, redirect
from flask import Blueprint

places_blueprint = Blueprint("places", __name__)

from repositories import place_repository
from repositories import country_repository
from models.place import Place
from models.country import Country

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


@places_blueprint.route('/places/<id>/delete', methods=['GET'])
def delete_place(id):
    place_repository.delete(id)
    return redirect('/places')



@places_blueprint.route('/places/<id>/edit', methods=['GET'])
def edit_place(id):
    place = place_repository.select(id)
    countries = country_repository.select_all()
    return render_template("places/edit.html", place=place, all_countries=countries)


@places_blueprint.route('/places/<id>', methods=['POST'])
def update_place(id):
    name = request.form['name']
    country_id = request.form['country_id']
    description = request.form['description']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    place = Place(name, country, description, visited, id)
    place_repository.update(place)
    return show_place(id)


@places_blueprint.route('/places/new', methods = ['GET'])
def new_place():
    return render_template("places/new.html")


@places_blueprint.route('/places', methods=['POST'])
def create_place():
    country = Country(request.form['country'])
    country_repository.save(country)

    name = request.form['name']
    country_id = country.id
    description = request.form['description']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    place = Place(name, country, description, visited)
    place_repository.save(place)
    return redirect('/places')