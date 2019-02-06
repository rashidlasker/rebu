# ISA-2019
Rashid L, Andrew W, Alex H

## App Description
Our app, Rebu, is a marketplace where people can buy/sell homemade meals. 

## API documentation
For each model, our API follows the same schema:

For read, update, and delete operations, we send GET, POST, and DELETE requests to the following url.

`api/v1/<model_name>/<id>/`

For create operations, we send a POST request to the following url.

`api/v1/<model_name>/create/`

### Models

#### Users

Fields:

- `first_name`
- `last_name`
- `street`
- `zip-code`
- `state`
- `country`
- `bio`
- `links`
- `language`
- `gender`

(maybe replace this with a data model diagram)

## Contributing

 1. Create a new **Branch** on your own machine in the following format: `your-name/what-you-added`
 2. **Commit** changes to your own branch
 3. **Push** your work back up to your branch upstream
 4. Submit a **Pull request** so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull request!

## Useful Commands:
Dump database cleanly:
`python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > project_dump.json`
