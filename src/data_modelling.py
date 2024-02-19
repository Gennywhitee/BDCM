import pandas as pd

from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def trainingModello(dataset):
    X = dataset.drop('Class', axis=1)
    y = dataset['Class']

    #Suddivisione del dataset in training e test (80%-20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    #Addestramento del modello
    model.fit(X_train, y_train)
    #Esecuzione delle predizioni sul set di dati
    y_pred= model.predict(X_test)

    return y_test, y_pred

def valutazioneModello(y_test, y_pred):
    #Valutazione dei risultati
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)

    return accuracy, precision
