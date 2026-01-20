import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self.load_all_artists()
        self._artists_by_album = []
        self._G = nx.DiGraph()

    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()
        print(f"Artisti: {self._artists_list}")

    def load_artists_with_min_albums(self, min_albums):
        self._artists_by_album = DAO.get_artists_by_album(min_albums)

    def build_graph(self):
        self._G.clear()
        self._G.add_nodes_from(self._artists_by_album)

        for a1 in self._artists_by_album:
            for a2 in self._artists_by_album:
                peso = (DAO.get_weighted_edges_by_artists(a1, a2))
                if peso == 0:
                    continue
                else:
                    self._G.add_edge(a1, a2, weight=peso)


    def get_graph_details(self):
        return self._G.number_of_nodes(), self._G.number_of_edges()
