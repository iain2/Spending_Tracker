from flask import Flask, redirect, render_template, Blueprint, request
from models.merchant import Merchant
from models.transaction import *
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

merchant_blueprint = Blueprint("Merchants", __name__)


@merchant_blueprint.route("/merchants")
def transaction():

    merchants = merchant_repository.select_all()

    return render_template(
        "merchants/index.html",
        merchants=merchants,
    )


@merchant_blueprint.route("/merchants", methods=["POST"])
def create_transaction():
    merchant_name = request.form["merchant"]
    merchant = Merchant(merchant_name)
    merchant_repository.save(merchant)
    return redirect("/merchants")


@merchant_blueprint.route("/merchants/<id>/edit", methods=["GET"])
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template("merchants/edit.html", merchant=merchant)


@merchant_blueprint.route("/merchants/<id>", methods=["POST"])
def update_merchant(id):
    name = request.form["merchant"]
    active = request.form["active"]
    merchant = Merchant(name, active, id)
    merchant_repository.update(merchant)
    return redirect("/merchants")


@merchant_blueprint.route("/merchants/<id>")
def show_merchant(id):
    merchant = merchant_repository.select(id)
    transactions = transaction_repository.merchants(merchant)
    total = total_spent(transactions)
    return render_template(
        "merchants/show.html", transactions=transactions, merchant=merchant, total=total
    )
