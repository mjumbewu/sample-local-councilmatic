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


Customizations
--------------

### Templates

You can overwrite any Councilmatic template in your local instance. To overwrite a template, reconstruct the location of that file in your project folder. For example, to change the way that the home page (dashboard) is layed out, copy the file https://github.com/codeforamerica/councilmatic/blob/master/councilmatic/templates/councilmatic/dashboard.html to websites/councilmatic_customizations/templates/councilmatic/dashboard.html and modify it to your liking. Notice that both files have the path "templates/councilmatic/dashboard.html". Any of the templates in the https://github.com/codeforamerica/councilmatic/blob/master/councilmatic/templates/ folder can be overridden in a similar way, by placing the corresponding copy into the websites/councilmatic_customizations/templates/ folder.

### Styles and Images

You can overwrite any Councilmatic static files much in the same way that you can templates. The css and images for Councilmatic are at https://github.com/codeforamerica/councilmatic/tree/master/councilmatic/static and would be overwritted in the website/councilmatic_customizations/static/ folder.

### Views and Advanced Functionality

Most of the views for Councilmatic are implemented in https://github.com/codeforamerica/councilmatic/blob/master/councilmatic/views.py. If you need to extend the functionality of a view, use the appropriate Councilmatic view as a base class for a new class in website/councilmatic_customizations/views.py. 