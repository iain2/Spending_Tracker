from gettext import translation
from flask import Flask, redirect, render_template, Blueprint
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

transaction_blueprint = Blueprint("Transactions", __name__)


@transaction_blueprint.route("/transactions")
def books():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", transactions=transactions)


# 'POST' form for add new transactions
# drop down list for tags and merchants

# form for new tags

# form for new merchants

# total spent
# select_all loop through add translation.amount to total return total
