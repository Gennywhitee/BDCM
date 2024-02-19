import pandas as pd
import os

from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

PATH_SEPARATOR = os.sep

from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def trainingModello(dataset):
    X = dataset.drop('Class', axis=1)
    y = dataset['Class']

    #Suddivisione del dataset in training e test (80%-20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #Salvataggio del dataset di addestramento
    trainingData = pd.concat([X_train, y_train], axis=1)
    trainingData.to_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetTraining.xlsx", index=False)

    #Salvataggio del dataset di test
    testData = pd.concat([X_test, y_test], axis=1)
    testData.to_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetTest.xlsx", index=False)

    #Oversampling&Undersampling
    X_resampled, y_resampled = oversampling(X_train, y_train)

    #Undersampling
    X, y = undersampling(X_resampled, y_resampled)

    model = DecisionTreeClassifier(random_state=42)
    #Addestramento del modello
    model.fit(X, y)
    #Esecuzione delle predizioni sul set di dati
    y_pred= model.predict(X_test)

    return y_test, y_pred

def valutazioneModello(y_test, y_pred):
    #Valutazione dei risultati
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)

    return accuracy, precision


def oversampling(X_train, y_train):

    rapporto_attuale = 0.6

    # Bilanciamento delle classi con SMOTE (tecninca di sovracampionamento)
    smote = SMOTE(sampling_strategy=rapporto_attuale, random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

    trainingData2 = pd.concat([X_resampled, y_resampled], axis=1)
    trainingData2.to_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetTraining2.xlsx", index=False)

    return X_resampled, y_resampled

def undersampling(X_resampled, y_resampled):

    rapporto_attuale = 0.8

    # Bilanciamento delle classi con RandomUnderSampler (tecninca di sottocampionamento)
    undersamplingData = RandomUnderSampler(sampling_strategy=rapporto_attuale, random_state=42)
    X, y = undersamplingData.fit_resample(X_resampled, y_resampled)

    trainingData2 = pd.concat([X, y], axis=1)
    trainingData2.to_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetTraining3.xlsx", index=False)

    return X, y
