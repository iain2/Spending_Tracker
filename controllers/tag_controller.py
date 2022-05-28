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

    return render_template(
        "tags/index.html",
        tags=tags,
    )


@tag_blueprint.route("/tags", methods=["POST"])
def create_tag():
    tag_name = request.form["tag"]
    tag = Tag(tag_name)
    tag_repository.save(tag)
    return redirect("/tags")
