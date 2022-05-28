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
    merchant = Merchant(name, id)
    print(merchant.name)
    merchant_repository.update(merchant)
    return redirect("/merchants")
