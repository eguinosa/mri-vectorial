# Gelin Eguinosa Rosique
# C-511

from math import log10, sqrt
from document import Document
from query import Query


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
        self.terms_freq = self.__calc_frequencies()

        # Calcula las frecuencas de ocurrencia de los terminos
        self.terms_idf = self.__calc_idf_frequencies()

        # Calcula los vectores de cada documento.
        for document in self.documents.values():
            document.calc_weight_vector(self.terms_idf)

    def __calc_frequencies(self):
        """
        Calcula en cuantos documentos aparece cada termino. Esta informacion se
        guarda en 'self.terms_freq'.
        :return: Un diccionario que contiene la frecuencia de cada termino
        dentro del corpus.
        """

        frequencies = {}
        # Iterando por los documentos del corpus
        for document in self.documents:
            # Iterando por los terminos del documento
            for term in document.terms:
                # Se ha encontrado el termino en al menos un documento.
                if term in frequencies:
                    frequencies[term] += 1
                # Es la primera vez que se encuentra el termino en el corpus.
                else:
                    frequencies[term] = 1

        return frequencies

    def __calc_idf_frequencies(self):
        """
        Calcula la frecuencia de ocurrencia de los terminos en el corpus.
        :return: Un diccionario que contiene la frecuencia de ocurrencia (idf)
        para cada termino dentro del corpus.
        """

        # Cantidad total de Documentos
        total_docs = self.doc_count

        idf_frequencies = {}
        for term in self.terms_freq:
            # Cantidad de documentos en los que aparece el termino 'term'
            term_docs = self.terms_freq[term]
            idf_frequencies[term] = log10(total_docs/term_docs)

        return idf_frequencies

    def process_query(self, text, number=10):
        """
        Procesa un query, y devuelve los 10 articulos mas relevantes.
        :param text: El texto del query.
        :return: Devuelve una lista conteniendo los 10 (or number) documentos
        mas relevantes con respecto al texto del query.
        """

        # Creando una instancia de query con el texto
        new_query = Query(text)
        
        # Encontrando los documentos mas relevantes
        documentos = self.top_documents(new_query, number)
        return documentos

    def top_documents(self, query, number):
        """
        Encuentra los documentos que tengan la mayor similaridad con la
        consulta.
        :param query: Query - la consulta realizada para determinar los
        documentos mas similares
        :param number: El numero de documentos que se debe retornar. Se
        retornan 10 documentos por defecto.
        :return: Una lista conteniendo los 'number' documentos mas similares
        a la consulta realizada.
        """

        # Lista conteniendo las tuplas de documentos y su similaridad con la
        # consulta
        docs_sim = []

        # Iterando por los documentos del corpus
        for document in self.documents.values():
            similarity = self.calc_similarity(query, document)
            docs_sim.append((document, similarity))

        # Ordenando la lista por el valor de similaridad
        docs_sim.sort(key=lambda x: x[1])

        # Returnando los documentos mas relevantes ('number' documentos)
        docs = [doc_tuple[0] for doc_tuple in docs_sim[:number]]
        return docs

    def calc_similarity(self, query, document):
        """
        Calcula la similitud entre la consulta y los documentos del corpus,
        utilizando el coseno del angulo entre los vectores de cada uno.
        :param query: Query - consulta que contiene un vector de pesos para los
        terminos del corpus.
        :param document: Document - Documento que contiene un vector de pesos
        para los terminos del corpus.
        :return: El valor que representa la similaridad entre el documento y la
        consulta.
        """

        # La suma de las multiplicaciones de los pesos
        sum_mult_weight = 0
        # La suma de los cuadrados de los pesos del documentos
        doc_sum_squares = 0
        # La suma de los cuadrados de los pesos de la consulta
        query_sum_squares = 0

        # Iterando por todos los terminos en el corpus
        for term in self.terms_freq.keys():
            doc_weight = document.weight_vector[term]
            query_weight = query.weight_vector[term]

            # Sumando los pesos del termino actual
            sum_mult_weight += doc_weight * query_weight
            doc_sum_squares += doc_weight * doc_weight
            query_sum_squares += query_weight * query_weight

        similarity = sum_mult_weight / (sqrt(doc_sum_squares) * sqrt(query_sum_squares))
        return similarity
