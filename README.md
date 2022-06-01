# week_5_project

Spending tracker using python with flask, html, css, and sqlite. 
CRUD app using restful routes.
A user is can enter transactions with a date, tag and merchant. A list of the transactions is displayed in date order and the user can filter the transactions by month, tag and merchant.
Tags and merchants can by made inactive and reactivated by the user. 

# Database set_up
sqlite3 spending_manager.db < spending_manager.sql

# Populate database 
python3 console.py

# Run app
flask run
