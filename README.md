# ISA-2019
Rashid L, Andrew W, Alex H

## App Description
Our app, Rebu, is a marketplace where people can buy/sell homemade meals. 

## Run Instructions
Rebu can be run by using the run script provided.
Commands for the dev environment inclue `./run start`, `./run restart`, and `./run stop`
Commands for the production environment inlude `./run start-prod`, `./run restart-prod`, and `./run stop-prod`
Other commands include `./run help` and `./run mysql` to access the help menu and create the database respectively

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
