# GenerateMe
Generate a random identity with python/django and some js.

The true reason behind this project is that I got tired of making up an identity when placing orders in my local KFC.

## Get started
Start by getting some first and last names. You will need those with assigned genders. The structure of FirstNameModel and LastNameModel is first/last_name and gender. Once you have it, make migrations and store it in default django sqlite database.

If you got the data needed in a csv file you can use a method from app.utils -  populate_db. You don’t need column headers. To populate FirstNameModel filename should start with “first”, “last” for  LastNameModel.

#### Caution
Use populate_db for small datasets. Let’s say a few hundred rows. It’s slow and will take forever for thousands and more rows.

## Run server
After populating the database you are ready to go. Just run the server, go to index page and click “Generate”. Form will be filled out with random first name, last name, date of birth (any date between 1970 and 2010 details in app.utils draw_dob) and nickname (details in app.utils generate_nickname). Copy form content by clicking clipboard icon placed by form input fields.
