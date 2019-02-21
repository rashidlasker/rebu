# ISA-2019
Rashid L, Andrew W, Alex H

## App Description
Our app, Rebu, is a marketplace where people can buy/sell homemade meals. 

## Note for Project 3
Our homepage can be found at http://localhost:8000/ and displays the three most recently added meals.  If you click "LEARN MORE" on the leftmost (or top depending on window size) meal, it will take you to http://localhost:8000/meals/3/, which is the item page for the most recently added meal.  

All of the unit tests are separated by class in tests.py and as such can be run by `python manage.py test`

The User Stories have been added to the Wiki and can be found at https://github.com/rashidlasker/ISA-2019/wiki/User-Stories

## Contributing

 1. Create a new **Branch** on your own machine in the following format: `your-name/what-you-added`
 2. **Commit** changes to your own branch
 3. **Push** your work back up to your branch upstream
 4. Submit a **Pull request** so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull request!

## Useful Commands:
Dump database cleanly:
`python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > project_dump.json`

When editing Sass files:
`gulp` and then `docker-compose up`
