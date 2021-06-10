# Gelin Eguinosa Rosique
# C-511

from nltk.probability import FreqDist
from tokenizer import tokenize


class Query:
    """
    Clase encargada de representar la informacion relacionada con una consulta,
    sus terminos, las frecuencias de sus terminos y el vector de pesos de la
    consulta.
    """

    def __init__(self, text, corpus_idf, a=0.5):
        """
        Inicializa la clase, realiza la tokenizacion del texto de la consulta,
        calcula el peso de los terminos y guarda estos valores en un vector.
        :param text: El texto de la consulta (string).
        :param corpus_idf: Diccionario que contiene la frecuencia de ocurrencia
        de los terminos en el corpus (idf).
        :param a: Variable de suavizado, para amortiguar la contribucion de la
        frecuencia del termino.
        """

        # Guardar el texto de la consulta
        self.text = text

        # Realiza la tokenizacion del texto de la consulta
        self.tokens = tokenize(text)

        # Guarda los terminos de la consulta en un set, para facilitar la
        # verificacion de los terminos que contiene la consulta
        self.terms = set(self.tokens)

        # Calcula la frecuencia de los terminos en la consulta
        freq_dist = FreqDist(self.tokens)
        # Guarda la frecuencia Maxima
        self.max_freq = freq_dist[freq_dist.max()]
        # Calcula la frequencia normalizada y amortiguada de los terminos
        self.norm_freq = self.__calc_norm_frequencies(freq_dist, a)

        # Calcula el vector de pesos de la consulta
        self.weight_vector = self.__calc_weight_vector(corpus_idf)

    def __calc_norm_frequencies(self, freq_dist, a):
        """
        Calcula la frecuencia normalizada y amortiguada de los terminos de la
        consulta.
        :param freq_dist: Una 'FreqDist' del Modulo 'Natural Language Toolkit'
        que representa una Distribucion de frecuencias creada con los tokens de
        la consulta.
        :param a: Variable de suavizado, para amortiguar las frecuencias de los
        terminos.
        :return: Un diccionario conteniendo la frecuencia normalizada para cada
        termino dentro de la consulta.
        """

        norm_frequencies = {}
        for term in self.terms:
            value = a + (1 - a) * (freq_dist[term] / self.max_freq)
            norm_frequencies[term] = value

        return norm_frequencies

    def __calc_weight_vector(self, corpus_idf):
        """
        Calcula el vector de pesos de los terminos de la consulta.
        :param corpus_idf: Diccionario que contiene la frecuencia de ocurrencia
        de los terminos en el corpus (idf).
        corpus.
        :return: Un diccionario que contiene el peso de cada termino dentro del
        corpus con respecto a la consulta.
        """

        vector = {}
        # Itera por los terminos de la consulta y sus frequencias normalizadas
        for term, term_freq in self.norm_freq.items():
            # Valor de la frecuencia de ocurrencia del termino en el corpus
            # 0 por defecto, en caso de que no este en el corpus
            idf_freq = corpus_idf.get(term, 0)
            # Calcula el peso del termino en la consulta
            weight = term_freq * idf_freq
            vector[term] = weight

        return vector
