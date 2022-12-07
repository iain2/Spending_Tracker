# Spending Tracker 

## Description

Spending tracker using python with flask, html, css, and sqlite. 
CRUD app using restful routes.
A user can enter transactions with a date, tag and merchant. A list of the transactions is displayed in date order and the user can filter the transactions by month, tag and merchant.
Tags and merchants can by made inactive and reactivated by the user. 
New tags and merchants can be added and edited by the user. 
A budget can be set and is displayed next to the transactions showing how much of the budget is remaining. 

## Instructions 

From the home page you can select which page to navigate to. 

![image](https://user-images.githubusercontent.com/102697747/206193380-c492d7d3-5466-4557-b82c-e726de709b42.png)

#

The transactions are listed in the transaction page in chronological order. New transactions can be added using the form on the right hand side. A transaction has a amount, merchant, category tag and date attached to it.  

![image](https://user-images.githubusercontent.com/102697747/206193977-146ddb33-7484-49c8-a5ac-a8adfd5b14da.png)

#

Transactions can be filtered by month on the sort by month page to allow the user to see all the transactions from a given month 

![image](https://user-images.githubusercontent.com/102697747/206194234-3b490f2a-bdc4-4547-9082-532e6366507d.png)

#

![image](https://user-images.githubusercontent.com/102697747/206195156-f0664b03-4f2b-4258-841f-3b9aa29d560b.png)


#

Tags and Merchants can be added using the tags and merchant pages, disused tags and merchants can be deactivated and will not apear in the in the transaction form 

![image](https://user-images.githubusercontent.com/102697747/206194617-f715c99a-4a09-4699-b468-5dff291deef4.png)

#

The budget can be set in the budget panel, this is shown in the transaction page showing how much of the given budget is left after the listed transactions 

![image](https://user-images.githubusercontent.com/102697747/206194882-c225b3e9-d500-44b1-a895-67edad589701.png)


## Set-up

### Database set_up
```
sqlite3 db/spending_manager.db < db/spending_manager.sql
```

### Populate database 
```
python3 console.py
```
### Run app
```
flask run
```
## Built with

-[Python]

-[Flask]

-[SQLite]

