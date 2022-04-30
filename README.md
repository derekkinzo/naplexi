# naplexi

## Virtual Environment
Create conda virtual environment from yml file

``` conda env create -n naplexi --file envname.yml ```

Update virtual environment yml

``` conda env update --file environment.yml --prune ```

Remove virtual environment
``` conda env remove -n naplexi ```


## Heroku

Login to account

```heroku login```


Create heroku app project
```heroku create naplexi```


Push to heroku repo
```git push heroku main```

Run Heroku Locally (optionally for windows since doesn't support gunicorn)
```
heroku local
heroku local -f Procfile.windows
```
## DJANGO
Start the django live reload server in a separate terminal window and leave it running.
```python manage.py livereload```