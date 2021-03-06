# Gelin Eguinosa Rosique
# C-511

from nltk.probability import FreqDist
from tokenizer import document_tokenizing


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

        # Guarda la informacion original del documento
        self.id = document['id']
        self.title = document['title']
        # En caso de que el documento  no especifique el autor
        self.author = document.get('author', 'Anonymous')
        self.original_document = document

        # Realiza la tokenizacion de la informacion del documento
        self.tokens = document_tokenizing(document)

        # Guarda los terminos del documento en un 'set', para facilitar la
        # busqueda y verificacion de los tokens que estan en el documento.
        self.terms = set(self.tokens)

        # Calcula y guarda la frequencia de ocurrencia de los terminos
        freq_dist = FreqDist(self.tokens)
        # Guarda la frecuencia maxima
        self.max_freq = freq_dist[freq_dist.max()]
        # Calcula la frecuencia normalizada de los terminos.
        self.norm_freq = self.__calc_norm_frequencies(freq_dist)

        # Crear diccionario para guardar los pesos de los terminos en el
        # documento cuando el corpus llame al metodo 'calc_weight_vector'
        self.weight_vector = {}

    def __calc_norm_frequencies(self, freq_dist):
        """
        Calcula las frequencias normalizadas de los terminos
        del documento y las guarda en un diccionario.
        :param freq_dist: Una 'FreqDist' del Modulo 'Natural Language Toolkit'
        creado con los tokens del documento.
        :return: Un diccionario que contiene las frecuencias normalizadas para
        todos los terminos del documento.
        """

        norm_frequencies = {}
        for term in self.terms:
            # La frecuencia del termino en el documento dividida por la
            # frecuencia maxima.
            value = freq_dist[term] / self.max_freq
            norm_frequencies[term] = value

        return norm_frequencies

    def calc_weight_vector(self, idf_frequencies):
        """
        Calcula el peso de los terminos en el documento.
        :param idf_frequencies: Recibe las frecuencias de ocurrencia de los
        terminos dentro de los documentos del corpus.
        """

        # Itera por los terminos del documento y sus respectivas frecuencias
        # normalizadas
        for term, tf_freq in self.norm_freq.items():
            # La frecuencia de ocurrencia del termino en el corpus
            idf_freq = idf_frequencies[term]
            # Calculando el peso del termino 'term'.
            weight = tf_freq * idf_freq
            self.weight_vector[term] = weight
