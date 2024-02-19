import pandas as pd
import os

from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import train_test_split

PATH_SEPARATOR = os.sep


def training_modello(dataset):
    if dataset is None or not isinstance(dataset, pd.DataFrame):
        print("Errore: il dataset non è stato inizializzato correttamente o non è un DataFrame.")
        return None

    x = dataset.drop('Class', axis=1)
    y = dataset['Class']

    #Suddivisione del dataset in training e test (80%-20%)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    """#Salvataggio del dataset di addestramento
    trainingData = pd.concat([X_train, y_train], axis=1)
    trainingData.to_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetTraining.xlsx", index=False)"""

    #Salvataggio del dataset di test
    testData = pd.concat([x_test, y_test], axis=1)
    testData.to_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetTest.xlsx", index=False)

    #Oversampling&Undersampling per bilanciare la classe
    x_new_train, y_new_train = bilanciamento_classe(x_train, y_train)

    model = RandomForestClassifier(random_state=42)
    #Addestramento del modello
    model.fit(x_new_train, y_new_train)
    #Esecuzione delle predizioni sul set di dati
    y_pred = model.predict(x_test)

    return y_test, y_pred


def valutazione_modello(y_test, y_pred):
    #Valutazione dei risultati
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)

    return accuracy, precision


def bilanciamento_classe(x_train, y_train):

    #Sovracampionamento
    x_resampled, y_resampled = oversampling(x_train, y_train)

    #Sottocampionamento
    x, y = undersampling(x_resampled, y_resampled)

    return x, y


def oversampling(x_train, y_train):

    rapporto_attuale = 0.6

    # Bilanciamento delle classi con SMOTE (tecninca di sovracampionamento)
    smote = SMOTE(sampling_strategy=rapporto_attuale, random_state=42)
    x_resampled, y_resampled = smote.fit_resample(x_train, y_train)

    return x_resampled, y_resampled


def undersampling(x_resampled, y_resampled):

    rapporto_attuale = 0.8

    # Bilanciamento delle classi con RandomUnderSampler (tecninca di sottocampionamento)
    undersamplingData = RandomUnderSampler(sampling_strategy=rapporto_attuale, random_state=42)
    x, y = undersamplingData.fit_resample(x_resampled, y_resampled)

    trainingData2 = pd.concat([x, y], axis=1)
    trainingData2.to_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetTraining.xlsx", index=False)

    return x, y
