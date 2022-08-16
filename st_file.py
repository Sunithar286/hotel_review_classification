import re
import string

import nltk
import pandas as pd
import streamlit as st
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC


def matrix_fit(X):
    X = [word for word in X if word]
    X = [word.strip() for word in X]
    X = [word for word in X if word]
    X = [re.sub('\s+', ' ', word) for word in X]
    X = [re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", word) for word in X]
    X = [re.sub('[0-9' ']+', '', word) for word in X]
    X = [re.sub('[^A-Za-z' ']+', ' ', word) for word in X]
    for i in range(len(X)):
        X[i] = X[i].translate(str.maketrans('', '', string.punctuation))
    for i in range(len(X)):
        X[i] = word_tokenize(X[i])

    my_stop_words = stopwords.words('english')
    my_stop_words.append('the')
    my_stop_words.append('hotel')
    for i in range(len(X)):
        X[i] = [word for word in X[i] if not word in my_stop_words]
    # ps = PorterStemmer()
    # for i in range(len(X)):
    #     X[i] = [ps.stem(word) for word in X[i]]
    for i in range(len(X)):
        X[i] = ' '.join([word for word in X[i]])
    return X


def Tokenize():
    reviews = st.text_area('User Input Reviews', 'type here')
    reviews = matrix_fit([reviews])
    try:
        vector = TfidfVectorizer(norm="l2", analyzer='word', ngram_range=(1, 3), max_features=500)
        matrix = vector.fit_transform(reviews)
        reviews1 = matrix.toarray()
    except Exception as e:
        print(e)
        return [e]

    return reviews1


def main():
    st.title('Model Deployment: Logistic Regression')

    st.sidebar.subheader("Choose Activity")
    page = st.sidebar.selectbox('Page Activity', ["", "sentiment classification"])
    st.sidebar.header('User Input Parameters')

    nltk.download('punkt')
    nltk.download('stopwords')

    df = Tokenize()
    st.subheader('User Input parameters')
    st.write(df)

    data = pd.read_csv(r'C:\Users\Suneetha\python files\PROJECT-2\hotel_reviews.csv',encoding="Latin1")
    data = data.head(20)
    Rating1 = []
    for i in range(len(data)):
        if data['Rating'][i] > 3:
            Rating1.append(1)
        else:
            Rating1.append(0)

    Rating1 = pd.DataFrame(Rating1, columns=['Rating1'])
    data = pd.concat([data, Rating1], axis=1)
    Y = data['Rating1']
    X = data['Review']
    X = matrix_fit(X)
    try:
        vector = TfidfVectorizer(lowercase=True, norm="l2", analyzer='word', ngram_range=(1, 3), max_features=len(df[0]))
        matrix = vector.fit_transform(X)
        X = matrix.toarray()
        model = SVC(C=1, gamma=1, kernel='rbf')
        model.fit(X, Y)
        print(df)
        prediction = model.predict(df)
        result = 'Negative' if prediction[0] == 0 else 'Positive'
        print(result)
        st.subheader('Result')
        st.write(result)
        prediction_proba = model.predict_proba(df)
    except Exception as e:
        print(e)
        return [e]

main()
