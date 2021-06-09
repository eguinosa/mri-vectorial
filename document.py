# Gelin Eguinosa Rosique
# C-511

from nltk.probability import FreqDist
from tokenizer import tokenize


class Document:
    """
    Clase para salvar toda la informacion de un documento, realizar la
    tokenizacion del texto del documento y crear el vector del documento con
    los pesos asociados a los terminos del corpus
    """

    def __init__(self, document):
        """
        Inicializa los datos del documento.
        :param document: Un diccionario conteniendo el id del documento, el
        autor, el texto y otras informaciones relevantes.
        """
        self.id = document['id']

        # Realiza la tokenizacion de la informacion del documento
        self.tokens = []
        self.__document_tokenizing(document)

        # Guarda los terminos del documento en un 'set', para facilitar la
        # busqueda y verificacion de los tokens que estan en el documento.
        self.terms = set(self.tokens)

        # Calcula y guarda la frequencia de ocurrencia de los terminos, tambien
        # la frequencia maxima
        freq_dist = FreqDist(self.tokens)
        self.max_freq = freq_dist[freq_dist.max()]
        # Crea un diccionario para guardar la frecuencia
        # normalizada de los terminos.
        self.norm_freq = {}
        self.__save_frequencies(freq_dist)

        # Crear diccionario para guardar los pesos de los terminos en el
        # documento.
        self.weight_vector = {}

    def __document_tokenizing(self, document):
        """
        Realiza la tokenizacion de toda la informacion relevante, excepto el
        'id' del documento.
        Todos los tokens creados son guardados en la lista 'self.tokens'.
        :param document: El diccionario que contiene toda la informacion
        relacionada con el documento.
        """
        for key, value in document.items():
            if key == 'id':
                continue
            new_tokens = tokenize(value)
            self.tokens += new_tokens

    def __save_frequencies(self, freq_dist):
        """
        Guarda las frequencias y las frequencias normalizadas de los terminos
        del documento en sus respectivos diccionarios.
        :param freq_dist: Una 'FreqDist' del Modulo 'Natural Language Toolkit'
        creado con los tokens del documento.
        """
        for term in self.terms:
            # La frecuencia del termino en el documento dividida por la
            # frecuencia maxima.
            value = freq_dist[term] / self.max_freq
            self.norm_freq[term] = value

    def calc_weight_vector(self, idf_frequencies):
        """
        Calcula el peso de los terminos en el documento.
        :param idf_frequencies: Recibe las frecuencias de ocurrencia de los
        terminos dentro de los documentos del corpus.
        """
        for term, idf_freq in idf_frequencies.items():
            # La frecuencia normalizada del termino.
            tf_freq = self.norm_freq[term]
            # Calculando el peso del termino 'term'.
            value = tf_freq * idf_freq
            self.weight_vector[term] = value
