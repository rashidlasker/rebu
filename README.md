# ISA-2019
Rashid L, Andrew W, Alex H

## App Description
Our app, Rebu, is a marketplace where people can buy/sell homemade meals. 

## Note for Project 6
Our homepage can be found at http://localhost:8000/. You can either login with Username: `rel3en` and Password: `password` or create your own account. Once you're logged in, you can create a meal. The Create Meal page currently does not support date-time pickers for the start and end time of the meal, so you will need to input a string like `2019-02-04 06:00:00`. You can also log out after logging in. 

For this project we completed continuous integration, integration testing, and load balancing.  For continuous integration, we used Travis to run our existing unit  and integration tests.  We made sure to insert sleep statements in order to make sure the build waits for everything to come up first.  For integration testing, we used selenium to simulate a browser and several user flows for our app.  For load balancing, we created a Dockerfile that inherits from HAProxy and defines the config file that we wrote.  In the config file, we connected the logs to Papertrail and set up two web servers, "web" and "webb", that we balance between in a roundrobin method.  We also enabled stats on localhost:1936 in order to see how well the load balancer is doing.  For the optional topic, we chose performance testing, but instead of using JMeter, we used locust, which is similar, but uses python, so it fits better into the project.  Within the locustfile, we defined several methods for the testing to use including login/logout, searching, creating things, and accessing pages.  In order to start our  application, you just need to run start.sh, which will start mysql, build, and docker-compose up all in one.  If you need to restart, you can use restart.sh, which docker-compose downs before calling start.sh and down.sh can be used to clean up at the end.  All of these files are in the outermost folder of our repository.  To use locust, you can access localhost:8089 and specify how many users you want for the performance testing. Additionally, there are stats for HAProxy on localhost:1936 so you can see how the load balancer is working.  

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
