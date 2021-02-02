from flask import Flask, render_template, request, redirect
from flask import Blueprint

countries_blueprint = Blueprint("countries", __name__)

from repositories import place_repository
from repositories import country_repository
from models.country import Country


@countries_blueprint.route('/countries')
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)


@countries_blueprint.route('/countries/<id>')
def show_places(id):
    country = country_repository.select(id)
    places = country_repository.places(country)
    return render_template("countries/show.html", all_places=places)


@countries_blueprint.route('/countries/<id>/delete', methods=['GET'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/countries')


@countries_blueprint.route('/countries/<id>/edit', methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    return render_template("countries/edit.html", country=country)


@countries_blueprint.route('/countries/<id>', methods=['POST'])
def update_country(id):
    print(id)
    name = request.form['country'] 
    print(name)
    country = Country(name, id)
    print(country)
    country_repository.update(country)
    return redirect('/countries')
