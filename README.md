# ISA-2019
Rashid L, Andrew W, Alex H

## App Description
Our app, Rebu, is a marketplace where people can buy/sell homemade meals. 

## API Documentation
For each model, our API follows the same schema:

For read, update, and delete operations, we send GET, POST, and DELETE requests to the following url.

`api/v1/<model_name>/<id>/`

For create operations, we send a POST request to the following url.

`api/v1/<model_name>/create/`

### Models
Here are the models and their respective fields (excluding the primary key).

| users      	| eaters  	| cooks          	| meals             	| plates   	| eater_ratings 	| reviews     	|
|------------	|---------	|----------------	|-------------------	|----------	|---------------	|-------------	|
| first_name 	| user*	| signature_dish 	| calories*         	| meal* 	| rating*       	| rating*     	|
| last_name  	|         	| user*       	| description       	| eater*	| description   	| description 	|
| street     	|         	|                	| spice*            	|          	| cook*      	| eater*   	|
| zip_code   	|         	|                	| price**           	|          	| eater*     	| cook*    	|
| state      	|         	|                	| tags              	|          	|               	| meal*    	|
| country    	|         	|                	| takeout_available†	|          	|               	|             	|
| bio        	|         	|                	| num_plates        	|          	|               	|             	|
| links      	|         	|                	| start‡            	|          	|               	|             	|
| language   	|         	|                	| end‡              	|          	|               	|             	|
| gender     	|         	|                	| cook*          	|          	|               	|             	|

\* denotes integer field

\** denotes float field

† denotes boolean field

‡ denotes datetime field

### Sample Usage
#### User
To create a new user, send this request:

`curl -d "first_name=Jon&last_name=Esteva&street=Piedmont&zip_code=22904&state=VA&country=USA&bio=bio&links=links&language=English&gender=male" -X POST http://localhost:8000/api/v1/users/create/`

To view user 1, send this request:

`curl -X GET http://localhost:8000/api/v1/users/1/`

To update user 1, send this request:

`curl -d "first_name=Hello&last_name=World&street=JPA&zip_code=22904&state=VA&country=USA&bio=bio&links=links&language=English&gender=male" -X POST http://localhost:8000/api/v1/users/1/`

To delete user 1, send this request:

`curl -X DELETE http://localhost:8000/api/v1/users/1/`

#### Meal
To create a new meal, send this request:

`curl -d "calories=120&description=cheeseburger&spice=0&price=8.00&tags=american&takeout_available=False&num_plates=2&start=2019-02-04 06:00:00&end=2019-02-04 10:00:00&cook=1" -X POST http://localhost:8000/api/v1/meals/create/`

To view meal 1, send this request:

`curl -X GET http://localhost:8000/api/v1/meals/1/`

To update meal 1, send this request:

`curl -d "calories=120&description=hamburger&spice=0&price=6.00&tags=american&takeout_available=False&num_plates=2&start=2019-02-05 06:00:00&end=2019-02-05 08:00:00&cook=1" -X POST http://localhost:8000/api/v1/meals/1/`

To delete meal 1, send this request:

`curl -X DELETE http://localhost:8000/api/v1/meals/1/`

#### Review
To create a new review, send this request:

`curl -d "rating=3&description=good&eater=1&cook=1&meal=1" -X POST http://localhost:8000/api/v1/reviews/create/`

To view meal 1, send this request:

`curl -X GET http://localhost:8000/api/v1/reviews/1/`

To update meal 1, send this request:

`curl -d "rating=1&description=bad&eater=1&cook=1&meal=1" -X POST http://localhost:8000/api/v1/reviews/1/`

To delete user 1, send this request:

`curl -X DELETE http://localhost:8000/api/v1/reviews/1/`

#### Eater
To create a new eater, send this request:

`curl -d "user=4" -X POST http://localhost:8000/api/v1/eaters/create/`

To view eater 1, send this request:

`curl -X GET http://localhost:8000/api/v1/eaters/1/`

To update eater 1, send this request:

`curl -d "user=5" -X POST http://localhost:8000/api/v1/eaters/1/`

To delete eater 1, send this request:

`curl -X DELETE http://localhost:8000/api/v1/eaters/1/`

#### Cook
To create a new cook, send this request:

`curl -d "user=1&signature_dish=chicken" -X POST http://localhost:8000/api/v1/cooks/create/`

To view cook 1, send this request:

`curl -X GET http://localhost:8000/api/v1/cooks/1/`

To update cook 1, send this request:

`curl -d "user=2&signature_dish=burger" -X POST http://localhost:8000/api/v1/cooks/1/`

To delete cook 1, send this request:

`curl -X DELETE http://localhost:8000/api/v1/cooks/1/`

#### Plate
To create a new plate, send this request:

`curl -d "meal=1&eater=1" -X POST http://localhost:8000/api/v1/plates/create/`

To view plate 1, send this request:

`curl -X GET http://localhost:8000/api/v1/plates/1/`

To update plate 1, send this request:

`curl -d "meal=1&eater=2" -X POST http://localhost:8000/api/v1/plates/1/`

To delete plate 1, send this request:

`curl -X DELETE http://localhost:8000/api/v1/plates/1/`

#### Eater Rating
To create a new eater rating, send this request:

`curl -d "rating=1&description=good&cook=1&eater=1" -X POST http://localhost:8000/api/v1/eater_ratings/create/`

To view eater rating 1, send this request:

`curl -X GET http://localhost:8000/api/v1/eater_ratings/1/`

To update eater rating 1, send this request:

`curl -d "rating=3&description=great&cook=1&eater=1" -X POST http://localhost:8000/api/v1/eater_ratings/1/`

To delete eater rating 1, send this request:

`curl -X DELETE http://localhost:8000/api/v1/eater_ratings/1/`

## Contributing

 1. Create a new **Branch** on your own machine in the following format: `your-name/what-you-added`
 2. **Commit** changes to your own branch
 3. **Push** your work back up to your branch upstream
 4. Submit a **Pull request** so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull request!

## Useful Commands:
Dump database cleanly:
`python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > project_dump.json`
