import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):

        if self._view.txtNumAlbumMin.value.isnumeric():
           self._model.load_artists_with_min_albums(self._view.txtNumAlbumMin.value)
        else:
           self._view.alert.show_alert("Numero album minimo invalido")
           return

        self._model.build_graph()
        n_nodes, n_edges = self._model.get_graph_details()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(f"Grafo creato: {n_nodes} nodi (artisti), {n_edges} archi")
        self._view.update_page()


    def handle_connected_artists(self, e):
        pass


