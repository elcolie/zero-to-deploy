from django.apps import AppConfig


# Watch out the directory name and `manage.py` if you have nested directory `apps`.
# Then do not forget to put them too for example `apps.books`
class BooksConfig(AppConfig):
    name = 'menus'
