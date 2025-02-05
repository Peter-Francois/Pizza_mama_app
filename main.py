from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import CoverBehavior

from http_client import HttpClient
from models import Pizza
from storage_manager import StorageManager
from navigation_screen_manager import NavigationScreenManager

class Menu(BoxLayout):
    pass

class MyScreenManager(NavigationScreenManager):
    pass

class PizzaWidget(BoxLayout):
    # pour affiché le nom de la pizza dans le widget on créé une StringProperty
    nom = StringProperty()
    ingredients = StringProperty()
    prix = NumericProperty()
    vegetarienne = BooleanProperty()


class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)
    str_error = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        HttpClient().get_pizzas(self.on_server_data, self.on_server_error)
        """self.pizzas = [
            Pizza("4 fromages", "Chèvre, emmental, brie, conté", 9.5, True),
            Pizza("Calzone", "fromage, jambon, champignons", 10, False),
            Pizza("Chorizo", "Tomate, chorizo, jambon, parmesan", 11.2, False)
        ]"""

    # on vient créé une fonction on_parent qui est la fonction qui assure que le fichier kv a été
    # rajouté au parent et on charge les datas dans la recycleView
    # ici les data vienne du fichier pizzas.json qui sauvgarde a chaque ouverture les données du serveur
    def on_parent(self, widget, parent):
        pizzas_dict = StorageManager().load_data("pizzas")
        if pizzas_dict:
            self.recycleView.data = pizzas_dict

    def on_server_data(self, pizzas_dict):
        self.recycleView.data = pizzas_dict
        StorageManager().save_data("pizzas", pizzas_dict)

    def on_server_error(self, error):
        self.str_error = "Error: " + str(error)


class PizzaApp(App):
    pass

PizzaApp().run()

