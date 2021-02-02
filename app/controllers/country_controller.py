from flask import Flask, render_template, request, redirect
from flask import Blueprint

countries_blueprint = Blueprint("countries", __name__)

from repositories import place_repository
from repositories import country_repository
from models.country import Country


