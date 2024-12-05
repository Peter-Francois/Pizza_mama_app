import json

from kivy.network.urlrequest import UrlRequest


class HttpClient:
    def get_pizzas(self, on_complete, on_error):
        url = "https://peterfrancois.pythonanywhere.com/api/getPizzas/"

        def data_received(req, result):
            data = json.loads(result)
            pizzas_dict = []
            for i in data:
                pizzas_dict.append(i['fields'])
            print("data received")
            # important de testé si on_complete n'est pas = a None avant d'utiliser la fonction
            if on_complete:
                on_complete(pizzas_dict)

        # pour les erreur de connection réseau, par exemple espace dans l'url
        def data_error(req, error):
            if on_error:
                on_error(str(error))

        # pour les erreur qui vienne du serveur, par exemple une létre de trop a la fin de l'url
        def data_failure(req, result):
            if on_error:
                on_error("server: code(" + str(req.resp_status) + ")")

        req = UrlRequest(url, on_success=data_received, on_error=data_error, on_failure=data_failure)
