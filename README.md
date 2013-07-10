Councilmatic for Your City!
===========================

An instance of [Councilmatic](https://github.com/codeforamerica/councilmatic), a subscription service for city council legislative information, started in Philadelphia.  Based on code for the [Philly instance](https://github.com/mjumbewu/philly-councilmatic).

Install
-------

1.  (optional) Create a Virtualenv
2.  `pip install -r requirements.txt`
3.  Create a PostGIS database called 'councilmatic'. Refer to the 
    [GeoDjango documentation](https://docs.djangoproject.com/en/dev/ref/contrib/gis/install/postgis/) 
    or other PostGIS documentation for instructions.
4.  Create log directory: `mkdir website/logs`


### Configure

1.  `cp website/local_settings.py.template website/local_settings.py`
2.  Configure `local_settings.py` with your database settings and with 
    information about the legislative management site for your city.


### Setup

	python website/manage.py syncdb
	python website/manage.py migrate

If you chose to create a superuser during the `syncdb` command, you should now create a subscriber for that superuser. A subscriber could not be created until the subscriptions app's database tables were set up, and that didn't happen until the `migrate` command. Now that the subscription app is ready, sync the subscriber objects:

	python website/manage.py syncsubscribers

Now you should be able to run the site:

	python website/manage.py runserver


### Load data

1.  `python website/manage.py updatelegfiles`. For your development instance,
    let this run for a few minutes just to get some data to see in the site.
    For a live site, you'll want to let this run to completion at least once.
2.  `python website/manage.py update_index`