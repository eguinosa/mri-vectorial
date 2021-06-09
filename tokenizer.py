# Gelin Eguinosa Rosique
# C-511

from nltk import pos_tag
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer


def tokenize(text):
    """
    Realiza la tokenizacion de un texto (string).
    :param text: String que representa un texto.
    :return: Devuelve una lista conteniendo los tokens del texto.
    """
    # Realiza la tokenizacion tomando solo las palabras que contengan
    # letras y numeros.
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)

    # Elimina los Stop Words, poniendo primero todas las letras de los
    # tokens en minusculas.
    stop_words = set(stopwords.words("english"))
    lower_tokens = [word.lower() for word in tokens]
    filter_tokens = [word for word in lower_tokens if word not in stop_words]

    # Identifica que parte de la oracion son las palabras para luego
    # convertirlas en su raiz gramatical
    tagged_tokens = pos_tag(filter_tokens)
    lemmatizer = WordNetLemmatizer()
    lemma_tokens = []
    for word, tag in tagged_tokens:
        if tag.startswith('N'):
            lemma_word = lemmatizer.lemmatize(word, pos=wordnet.NOUN)
        elif tag.startswith('V'):
            lemma_word = lemmatizer.lemmatize(word, pos=wordnet.VERB)
        elif tag.startswith('J'):
            lemma_word = lemmatizer.lemmatize(word, pos=wordnet.ADJ)
        elif tag.startswith('R'):
            lemma_word = lemmatizer.lemmatize(word, pos=wordnet.ADV)
        else:
            lemma_word = word
        # Agrega la palabra transformada en su raiz a la nueva lista de
        # tokens
        lemma_tokens.append(lemma_word)

    # Devuelve la lista de tokens final.
    return lemma_tokens
