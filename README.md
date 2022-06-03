# Proyecto - Modelo de Recuperación de Información (SI)

## Modelo del Sistema

Para la realización de este proyecto se utilizó un Modelo de Recuperación de Información Vectorial.

Este modelo, para la recuperación de los documentos, puede dar un ranking de los documentos de acuerdo con el grado de similaridad que este tenga con la consulta, algo deseado para la realización del proyecto. También, puede establecerse un umbral de similitud y recuperar los documentos cuyo grado de similitud sean mayores que este umbral, lo que puede ser de utilidad para obtener los valores de Precisión y Recobrado deseados.

El modelo booleano, a pesar de ser un modelo simple y fácil de implementar, no fue considerado el más adecuado para este proyecto porque este solo considera si los términos indexados están presentes, o no, en un documento. Esta estrategia de recuperación binaria no tiene noción de ranking, solo recupera los documentos donde la coincidencia es exacta, por lo que no hay correspondencia parcial. También, el lenguaje utilizado para realizar las consultas puede ser considerado complejo para usuarios inexpertos. Este modelo tiende a recuperar muchos o muy pocos documentos, y todos los términos tienen la misma importancia cuando se quiere encontrar los documentos relevantes para una determinada consulta.

En el caso del Modelo de Recuperación de Información Probabilístico, a pesar de que este si permite obtener un ranking entre los documentos recuperados. El peso de los términos es binario, por lo que no se tiene en cuenta la frecuencia de ocurrencia de los términos. Se asume independencia entre los términos. Y lo más importante, se hace necesario encontrar un primer conjunto de documentos relevantes, lo que hace un poco más difícil el trabajo con este tipo de modelo para este proyecto en específico.

El modelo vectorial fue considerado el más ideal para la realización del proyecto, ya que con su esquema de ponderación y su estrategia de coincidencia parcial permite recuperar los documentos más relevantes para una consulta siguiendo un ranking y no hay necesidad de tener un conocimiento previo sobre los documentos que sean considerados relevantes. Además, un documento no tiene que coincidir exactamente con la consulta para ser considerado relevante, algo que es bueno, ya que un documento relevante puede no cumplir con todos los requerimientos de la consulta, sino con un subconjunto de ellos. Este sistema no está sin limitaciones, pues asume que los términos indexados son mutuamente independientes, algo que no refleja el comportamiento del lenguaje natural.

## Código del Sistema

En el código del proyecto, lo primero que se realiza es la lectura de toda la información relacionada con el corpus de los documentos. En el caso específico de este proyecto, los datos de los documentos se encuentran en un archivo JSON. Una vez que se ha cargado toda la información de los documentos, se procede a indexar cada uno de estos.

En el proceso de indexación de los documentos, primero se realiza la toquenización de toda su información, donde se eliminan todos los signos de puntuación que tengan la información asociada al documento, y también se eliminan los Stops Words. Luego, se analizan cada uno de los tokens restantes para indicar que parte gramatical representan (sustantivos, verbos, etc.) para llevarlos a su raíz gramatical y así facilitar el proceso de comparación de dos términos semejantes. Una vez finalizado este proceso, se calcula la frecuencia normalizada de los términos del documento.

Una vez que todos los documentos han sido indexados, se pasa a recorrer todos los términos de todos los documentos para encontrar y guardar todos los términos presentes en el corpus. Luego, se calcula la frecuencia de ocurrencia de los términos dentro de todos los documentos. Dado que ya se tienen los valores de las frecuencias normalizadas para los términos en todos los documentos y se calcularon los valores de la frecuencia de ocurrencia en el corpus, se comienza a calcular los vectores para cada documento, calculando los pesos de cada termino para todos los documentos. Una vez terminado, se guardan los valores de los vectores esperando a que el usuario realice alguna consulta.

Cuando un usuario realiza una consulta, el texto y toda la información asociada a la consulta (en caso de que exista) se indexa de forma similar a la información de los documentos. Luego, se calculan los valores de las frecuencias normalizadas y suavizadas (dependiendo del valor de a) de los términos dentro de la consulta, ya con estos valores se pasa a calcular el vector de la consulta, calculando el peso de cada uno de sus términos.

Para determinar los documentos más relevantes, el vector de la consulta se multiplica con el vector de cada documento del corpus, de esta operación se obtiene una lista con todos los documentos del corpus y el valor de su similitud con la consulta. Todos los documentos que tengan una similitud menor que un margen determinado, son eliminados. Los documentos restantes son ordenados por el valor de su similitud, comenzando con los documentos que tengan la mayor similitud con la consulta. Una vez ordenados los documentos, se reportan al usuario los primeros 'n' documentos de esta lista, siendo '' un número determinado para obtener los valores de precisión y recobrado deseados.

### Utilización de NLTK

NLTK, o Natural Language Toolkit, es un paquete de Python que puede ser utilizado para el procesamiento del lenguaje natural. Con este paquete se puede facilitar el preprocesamiento de un texto y brinda herramientas para el análisis de este.

En este proyecto, NLTK se utiliza para la realización de la tokenización de los textos de los documentos, la eliminación de las Stop Words, determinar que parte de la oración representa cada palabra y la obtención de la raíz gramatical de estas. Una vez que se tiene la tokenización final de los textos, se utiliza la FreqDist de esta librería para obtener las frecuencias de los términos en el texto.

## Evaluación del Sistema

Para la evaluación del sistema de recuperación de información, se utilizaron las colecciones de pruebas CISI, perteneciente a la Universidad de Glasgow, y Cranfield, de la Universidad de Cranfield.

Los resultados obtenidos con estas colecciones de pruebas no fueron muy alentadores, especialmente con la colección Cranfield. Estos son los mejores resultados obtenidos con diferentes valores de similitud mínima y cantidad máxima de documentos relevantes que se podían retornar para cada colección de prueba.

### CISI

```
Max Documents: 100 & Min Similarity: 0.03
Average Recuperated Documents: 100.0
Maximum Precision - 0.56
Minimum Precision - 0.01
Average Precision - 0.1456578947368421
Maximum Recall - 1.0
Minimum Recall - 0.07692307692307693
Average Recall - 0.4299928300595881
Precision + Recall: 0.5756507247964302

Max Documents: 75 & Min Similarity: 0.03
Average Recuperated Documents: 75.0
Maximum Precision - 0.5733333333333334
Minimum Precision - 0.013333333333333334
Average Precision - 0.1647368421052632
Maximum Recall - 1.0
Minimum Recall - 0.05555555555555555
Average Recall - 0.384999388673894
Precision + Recall: 0.5497362307791572

Max Documents: 100 & Min Similarity: 0.08
Average Recuperated Documents: 44.10526315789474
Maximum Precision - 0.7317073170731707
Minimum Precision - 0.0
Average Precision - 0.2225188251433321
Maximum Recall - 1.0
Minimum Recall - 0.0
Average Recall - 0.30425823054519313
Precision + Recall: 0.5267770556885252

Max Documents: 100 & Min Similarity: 0.03
Maximum Precision - 0.68
Minimum Precision - 0.0
Average Precision - 0.19253322946589416
Maximum Recall - 1.0
Minimum Recall - 0.0
Average Recall - 0.3186669408729217
Precision + Recall: 0.5112001703388158
```

### CRANFIELD

```
Max Documents: 100 & Min Similarity: 0.03
Average Recuperated Documents: 244.38815789473685
Maximum Precision - 0.08
Minimum Precision - 0.0
Average Precision - 0.007775911763820797
Maximum Recall - 1.0
Minimum Recall - 0.0
Average Recall - 0.1791893398372242
Precision + Recall: 0.18696525160104502

Max Documents: 100 & Min Similarity: 0.03
Average Recuperated Documents: 197.7434210526316
Maximum Precision - 0.095
Minimum Precision - 0.0
Average Precision - 0.008091379439637952
Maximum Recall - 1.0
Minimum Recall - 0.0
Average Recall - 0.1489367022344145
Precision + Recall: 0.15702808167405244

Max Documents: 100 & Min Similarity: 0.03
Average Recuperated Documents: 183.25
Maximum Precision - 0.10309278350515463
Minimum Precision - 0.0
Average Precision - 0.008371925816315278
Maximum Recall - 1.0
Minimum Recall - 0.0
Average Recall - 0.1402699121531507
Precision + Recall: 0.14864183796946598

Max Documents: 100 & Min Similarity: 0.03
Average Recuperated Documents: 99.20394736842105
Maximum Precision - 0.15
Minimum Precision - 0.0
Average Precision - 0.009591581379684551
Maximum Recall - 1.0
Minimum Recall - 0.0
Average Recall - 0.08751826578845634
Precision + Recall: 0.09710984716814089
```

# Análisis del Sistema

En el sistema desarrollado, cuando las consultas contienen términos, donde estos o su raíz gramatical, se corresponden con los términos presentes en los documentos, entonces el sistema va a considerar estos documentos como relevantes. Esto puede ser beneficioso en casos donde la información que se dan en las consultas es explicita, pero cuando el usuario no indica de forma directa los términos del contenido que desea encontrar, los resultados del sistema desarrollado no son muy buenos. Quizás, por esto es que el sistema no tiene un buen rendimiento en la colección de prueba Cranfield.

# Recomendaciones

Para mejorar el proyecto realizado, como propuesta se puede realizar un análisis más avanzado de los textos de los documentos, donde se pueden incluir en los términos de las consultas palabras que tengan un significado similar, entre otras técnicas, para obtener resultados más relevantes cuando se realizan consultas. El proyecto debe incluir retroalimentación y la posibilidad de expandir la consultar para facilitar al usuario la obtención de documentos que sean relevantes. También, para facilitar la interacción del usuario con nuestro sistema, se debe agregar una interfaz visual para que el usuario se sienta más cómodo y pueda tener una mejor interacción con el programa en el momento de realizar una consulta.
