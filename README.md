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
| first_name 	| user_id*	| signature_dish 	| calories*         	| meal_id* 	| rating*       	| rating*     	|
| last_name  	|         	| user_id*       	| description       	| eater_id*	| description   	| description 	|
| street     	|         	|                	| spice*            	|          	| cook_id*      	| eater_id*   	|
| zip_code   	|         	|                	| price**           	|          	| eater_id*     	| cook_id*    	|
| state      	|         	|                	| tags              	|          	|               	| meal_id*    	|
| country    	|         	|                	| takeout_available†	|          	|               	|             	|
| bio        	|         	|                	| num_plates        	|          	|               	|             	|
| links      	|         	|                	| start‡            	|          	|               	|             	|
| language   	|         	|                	| end‡              	|          	|               	|             	|
| gender     	|         	|                	| cook_id*          	|          	|               	|             	|

\* denotes integer field

\** denotes float field

† denotes boolean field

‡ denotes datetime field

### Sample Usage
To create a new user, send this request:

`curl -d "first_name=Jon&last_name=Esteva&street=Piedmont&zip_code=22904&state=VA&country=USA&bio=bio&links=links&language=English&gender=male" -X POST http://localhost:8000/api/v1/users/create/`

To view user 1, send this request:

`curl -X GET http://localhost:8000/api/v1/users/1/`

To update user 1, send this request:

`curl -d "first_name=Hello&last_name=World&street=JPA&zip_code=22904&state=VA&country=USA&bio=bio&links=links&language=English&gender=male" -X POST http://localhost:8000/api/v1/users/1/`

To delete user 1, send this request:

`curl -X DELETE http://localhost:8000/api/v1/users/1/`

## Contributing

 1. Create a new **Branch** on your own machine in the following format: `your-name/what-you-added`
 2. **Commit** changes to your own branch
 3. **Push** your work back up to your branch upstream
 4. Submit a **Pull request** so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull request!

## Useful Commands:
Dump database cleanly:
`python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > project_dump.json`
