# Gelin Eguinosa Rosique
# C-511

import json
import time
from corpus import Corpus


def dataset_test(docs_path, querys_path, answers_path, max_docs=100, min_sim=0.07):
    """
    Realiza la evalucacion del MRI implementado en la Coleccion de Prueba CISI.
    Calcula la precision y el recobrado para cada consulta, y los promedios
    para todas las consultas en general.
    :param docs_path: La ubicacion del .json de los documentos
    :param querys_path: La ubicacion del .json de las consultas
    :param answers_path: La ubicacion del .json de las respuestas.
    :param max_docs: Numero maximo de documentos que se pueden devolver por
    cada consulta.
    :param min_sim: La similitud minima para que un documento pueda considerarse
    relevante.
    """

    # Duracion total del test
    test_start = time.time()

    # Carga los documentos del corpus
    print("Loading Corpus...")
    start_time = time.time()
    f = open(docs_path)
    data = json.load(f)
    f.close()
    corpus = Corpus(data)
    finish_time = time.time()
    interval = finish_time - start_time
    print(f"{corpus.doc_count} documents loaded ({interval} seconds)")
    print(f"{max_docs} maximum number of documents per query.")
    print(f"{min_sim} minimum similarity.")

    # Carga las consultas de la coleccion de prueba
    print("\nLoading Queries...")
    start_time = time.time()
    queries = load_queries(querys_path)
    finish_time = time.time()
    interval = finish_time - start_time
    print(f"{len(queries)} queries loaded ({interval} seconds)")

    # Carga las respuestas a las consultas en la coleccion de prueba
    print("\nLoading Answers...")
    start_time = time.time()
    collection_answers = load_answers(answers_path)
    finish_time = time.time()
    interval = finish_time - start_time
    print(f"{len(collection_answers)} answers loaded ({interval} seconds)")

    # Verifica la Precision y Recobrado para cada consulta
    precisions = []
    recalls = []
    number_results = []
    for query_id, text in queries.items():
        # Chequea si esta consulta este dentro de las respuestas dadas
        if query_id not in collection_answers:
            continue

        # Obtiene los resultados de la consulta usando mi MRI
        print(f"\nVerifying Results - Query {query_id}...")
        start_time = time.time()
        relevant_docs = corpus.query_process(text, max_docs, min_sim)
        finish_time = time.time()
        interval = finish_time - start_time
        print(f"{len(relevant_docs)} results ({interval} seconds)")
        similarities = [similarity for doc, similarity in relevant_docs]
        max_similarity = max(similarities)
        min_similarity = min(similarities)
        print(f"Max Similarity - {max_similarity}")
        print(f"Min Similarity - {min_similarity}")

        # Guardando la cantidad de resultados dados en la consulta.
        number_results.append(len(relevant_docs))

        # Comparando los resultados con los de la coleccion de prueba
        ids_answers = {int(doc.id) for doc, similarity in relevant_docs}
        ids_collection = collection_answers[query_id]
        recup_relev = ids_answers & ids_collection
        precision = len(recup_relev) / len(ids_answers)
        recall = len(recup_relev) / len(ids_collection)
        precisions.append(precision)
        recalls.append(recall)

        # Dar los resultados para esta consulta:
        print(f"Precision: {precision}")
        print(f"Recall: {recall}")

    # Dar los resultados generales para todas las consultas en la coleccion de
    # prueba
    max_precision = max(precisions)
    min_precision = min(precisions)
    average_precision = sum(precisions) / len(precisions)
    max_recall = max(recalls)
    min_recall = min(recalls)
    average_recall = sum(recalls) / len(recalls)
    average_results = sum(number_results) / len(number_results)

    print("\nCorpus final results:")
    print(f"  Average Recuperated Documents: {average_results}\n")
    print(f"  Maximum Precision - {max_precision}")
    print(f"  Minimum Precision - {min_precision}")
    print(f"  Average Precision - {average_precision}\n")
    print(f"  Maximum Recall - {max_recall}")
    print(f"  Minimum Recall - {min_recall}")
    print(f"  Average Recall - {average_recall}\n")
    print(f"  Precision + Recall: {average_precision + average_recall}\n")

    # Duracion del Test
    test_duration = time.time() - test_start
    print(f"\nTest duration: {test_duration} seconds.")


def load_queries(queries_path):
    """
    Carga todas las consultas dadas en la coleccion de prueba.
    :param queries_path: La ubicacion del .JSON de las consultas.
    :return: Un diccionario conteniendo un int representando el id de las
    consultas como llave, y como valor, un string representado el texto de la
    consulta.
    """

    # Abre el .JSON y guarda la informacion en un diccionario
    f = open(queries_path)
    data_queries = json.load(f)
    f.close()

    # Convierte los id de los querys a int, para facilitar la comparacion y
    # guarda el id y el texto de las consultas
    dict_queries = {}
    for query_id, query_info in data_queries.items():
        number_id = int(query_id)
        text_query = ""
        for key, info in query_info.items():
            if key == 'id':
                continue
            text_query += info + ". "

        dict_queries[number_id] = text_query

    return dict_queries


def load_answers(answers_path):
    """
    Lee y salva la informacion relacionada con las respuestas de las consultas
    del corpus dado.
    :param answers_path: .json donde se encuentran las respuestas de las
    consultas
    :return: Un diccionario conteniendo el conjunto de las respuestas correctas
    para cada consulta.
    """

    # Abre el JSON y guarda la informacion en un diccionario
    f = open(answers_path)
    data_answers = json.load(f)
    f.close()

    # Convierte los valores de los id del diccionario a 'int' para facilitar sus
    # comparaciones, guarda los ids de las respuestas en un 'set'
    dict_answers = {}
    for query_id, answers in data_answers.items():
        # Convierte en 'int' el id de la consulta
        number_id = int(query_id)
        # Convierte en 'int' la lista de keys de la respuestas a la consulta
        answers_num_id = {int(answer_id) for answer_id in answers}
        dict_answers[number_id] = answers_num_id

    return dict_answers
