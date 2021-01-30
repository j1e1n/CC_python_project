from flask import Flask, render_template, request, redirect
from flask import Blueprint

places_blueprint = Blueprint("places", __name__)

from repositories import place_repository
from repositories import country_repository
from models.place import Place