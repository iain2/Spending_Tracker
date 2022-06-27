# week_5_project

Spending tracker using python with flask, html, css, and sqlite. 
CRUD app using restful routes.
A user can enter transactions with a date, tag and merchant. A list of the transactions is displayed in date order and the user can filter the transactions by month, tag and merchant.
Tags and merchants can by made inactive and reactivated by the user. 
New tags and merchants can be added and edited by the user. 
A budget can be set and is displayed next to the transactions showing how much of the budget is remaining.  


# Database set_up
sqlite3 db/spending_manager.db < db/spending_manager.sql

# Populate database 
python3 console.py

# Run app
flask run
