# Gelin Eguinosa Rosique
# C-511

import math
from document import Document


class Corpus:
    """
    Esta clase es la encargada de guardar toda la informacion relacionada con
    los documentos del corpus: los documentos, todos los terminos que aperecen,
    etc...
    Ademas, es la clase con la que interactua el 'query' para determinar con que
    documentos del corpus tiene la mayor similitud.
    """

    def __init__(self, corpus):
        """
        Inicializa la clase, y todos los documentos que contiene el corpus.
        :param corpus:
            Un diccionario que contiene todos los documentos, identificados por
            un 'id', el titulo, el autor, el texto del documento y otros campos
            para alguna informacion addicional que se tenga sobre el documento.
        """
        # Itera por todos los documentos del corpus para inicializarlos.
        self.doc_count = len(corpus)
        self.documents = {}
        for id_doc, document in corpus.items():
            new_document = Document(document)
            self.documents[id_doc] = new_document

        # Calcula la frecuencia de los terminos dentro de los documentos.
        self.terms_freq = {}
        self.__calc_frequencies()

        # Calcula las frecuencas de ocurrencia de los terminos
        self.terms_idf = {}
        self.__calc_idf_frequencies()

        # Calcula los vectores de cada documento.
        for document in self.documents.values():
            document.calc_weight_vector(self.terms_idf)

    def __calc_frequencies(self):
        """
        Calcula en cuantos documentos aparece cada termino. Esta informacion se
        guarda en 'self.terms_freq'.
        """
        # Iterando por los documentos del corpus
        for document in self.documents:
            # Iterando por los terminos del documento
            for term in document.terms:
                # Se ha encontrado el termino en al menos un documento.
                if term in self.terms_freq:
                    self.terms_freq[term] += 1
                # Es la primera vez que se encuentra el termino en el corpus.
                else:
                    self.terms_freq[term] = 1

    def __calc_idf_frequencies(self):
        """
        Calcula la frecuencia de ocurrencia de los terminos en el corpus
        """
        for term in self.terms_freq:
            # Cantidad total de Documentos
            total_docs = self.doc_count
            # Cantidad de documentos en los que aparece el termino 'term'
            term_docs = self.terms_freq[term]
            self.terms_idf[term] = math.log10(total_docs/term_docs)
