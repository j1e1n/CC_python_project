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