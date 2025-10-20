==========================
cookiecutter-djangopackage
==========================

A cookiecutter_ template for creating reusable Django packages (installable apps) quickly.

This is a fork of PyDanny's `cookiecutter-djangopackage`_

**Why?** I am used to my personal structure to

.. _cookiecutter-djangopackage: https://github.com/pydanny/cookiecutter-djangopackage

Features
--------

from original package

* Sane setup.py for easy PyPI registration/distribution
* Travis-CI configuration
* Codecov configuration
* Tox configuration
* Sphinx Documentation
* BSD licensed by default

Extras
~~~~~~

* `py.test`_ configuration
* `django-webtest`_ configuration
*

.. _py.test: https://pytest.org/latest/contents.html
.. _django-webtest: https://github.com/django-webtest/django-webtest


Usage
------

First, get cookiecutter. Trust me, it's awesome::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/saxix/cookiecutter-djangopackage.git

You'll be prompted for some questions, answer them, then it will create a cookiecutter-dj-package with
your new package.

Let's pretend you want to create a reusable Django app called "Blogging-for-Humans", with an app that can be placed
in INSTALLED_APPS as "blogging_humans". Rather than have to copy/paste from other people's projects and
then fight enthusiasm destroying app layout issues like `setup.py` configuration and creating test
harnesses, you get cookiecutter_ to do all the work.

**Warning**: After this point, change 'Daniel Greenfeld', 'pydanny', etc to your own information.

It prompts you for questions. Answer them::

    Cloning into 'cookiecutter-dj-package'...
    remote: Counting objects: 49, done.
    remote: Compressing objects: 100% (33/33), done.
    remote: Total 49 (delta 6), reused 48 (delta 5)
    Unpacking objects: 100% (49/49), done.
    full_name (default is "Your full name here")? Daniel Greenfeld
    email (default is "you@example.com")? pydanny@gmail.com
    github_username (default is "yourname")? pydanny
    project_name (default is "dj-package")? Blogging-for-Humans
    repo_name (default is "dj-package")? blogging-for-humans
    app_name (default is "djpackage")? blogging_humans
    project_short_description (default is "Your project description goes here")? A blog that's easy for humans to use!
    release_date (default is "2013-08-15")? 2013-08-15
    year (default is "2013")? 2013
    version (default is "0.1.0")? 0.3.0

Enter the project and take a look around::

    $ cd blogging-for-humans/
    $ ls

Create a GitHub repo and push it there::

    $ git init
    $ git add .
    $ git commit -m "first awesome commit!"
    $ git remote add origin git@github.com:pydanny/blogging-for-humans.git
    $ git push -u origin master

Now take a look at your repo. Awesome, right?

It's time to write the code!!!

Register on PyPI
~~~~~~~~~~~~~~~~~

Once you've got at least a prototype working and tests running, it's time to register the app on PyPI::

    python setup.py register


Releasing on PyPI
~~~~~~~~~~~~~~~~~~~~~~~~

Time to release a new version? Easy! Just run::

    $ python setup.py publish

It will answer with something like::

    You probably want to also tag the version now:
          git tag -a 0.1.0 -m 'version 0.1.0'
          git push --tags

Go ahead and follow those instructions.

Add to Django Packages
~~~~~~~~~~~~~~~~~~~~~~~

Once you have a release, and assuming you have an account there, just go to https://www.djangopackages.com/packages/add/ and add it there.


Follows Best Practices
~~~~~~~~~~~~~~~~~~~~~~~

.. image:: http://twoscoops.smugmug.com/Two-Scoops-Press-Media-Kit/i-C8s5jkn/0/O/favicon-152.png
   :name: Two Scoops Logo
   :align: center
   :alt: Two Scoops of Django
   :target: http://twoscoopspress.org/products/two-scoops-of-django-1-8

This project follows best practices as espoused in `Two Scoops of Django: Best Practices for Django 1.8`_.

.. _`Two Scoops of Django: Best Practices for Django 1.8`: http://twoscoopspress.org/products/two-scoops-of-django-1-8
