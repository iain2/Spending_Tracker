from flask import Flask, redirect, render_template, Blueprint, request
from models.merchant import Merchant
from models.transaction import *
from models.tag import Tag
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

tag_blueprint = Blueprint("Tags", __name__)


@tag_blueprint.route("/tags")
def tags():

    tags = tag_repository.select_all()

    return render_template("tags/index.html", tags=tags, total=total)


@tag_blueprint.route("/tags", methods=["POST"])
def create_tag():
    tag_name = request.form["tag"]
    tag = Tag(tag_name)
    tag_repository.save(tag)
    return redirect("/tags")


@tag_blueprint.route("/tags/<id>/edit", methods=["GET"])
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template("tags/edit.html", tag=tag)


@tag_blueprint.route("/tags/<id>", methods=["POST"])
def update_merchant(id):
    name = request.form["tag"]
    active = request.form["active"]
    tag = Tag(name, active, id)
    tag_repository.update(tag)

    return redirect("/tags")


@tag_blueprint.route("/tags/<id>")
def show(id):
    tag = tag_repository.select(id)
    transactions = transaction_repository.tags(tag)
    total = total_spent(transactions)
    return render_template(
        "tags/show.html", transactions=transactions, total=total, tag=tag
    )
