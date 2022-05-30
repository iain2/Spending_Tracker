import imp
from flask import Flask, redirect, render_template, Blueprint, request
from models.merchant import Merchant
from models.transaction import *
from models.tag import Tag
from models.user import User
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository
import repositories.user_repository as user_repository

budget_blueprint = Blueprint("Budget", __name__)


@budget_blueprint.route("/budget")
def users():

    users = user_repository.select_all()
    user = users[0]

    return render_template("budget/index.html", user=user, users=users)


@budget_blueprint.route("/budget/<id>/edit", methods=["GET"])
def edit_users(id):
    users = user_repository.select_all()
    user = users[0]
    return render_template("budget/edit.html", users=users, user=user)


@budget_blueprint.route("/budget/<id>/edit", methods=["POST"])
def update_user(id):
    name = request.form["name"]
    amount = request.form["amount"]
    updated_user = User(amount, name, id)
    user_repository.update(updated_user)
    return redirect("/budget")
