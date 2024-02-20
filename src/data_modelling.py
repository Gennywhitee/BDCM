import random

import pandas as pd
import os

from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

PATH_SEPARATOR = os.sep


def data_partitioning(dataset):
    x = dataset.drop('Class', axis=1)
    y = dataset['Class']

    # Suddivisione del dataset in training e test (90%-10%)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)

    # Salvataggio Training dataset
    trainingData = pd.concat([x_train, y_train], axis=1)
    trainingData.to_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetTraining.xlsx", index=False)

    # Salvataggio del dataset di test
    testData = pd.concat([x_test, y_test], axis=1)
    testData.to_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetTest.xlsx", index=False)


def training_modello(dataset_train, dataset_test):
    x_train = dataset_train.drop('Class', axis=1)
    y_train = dataset_train['Class']

    x_test = dataset_test.drop('Class', axis=1)
    y_test = dataset_test['Class']

    model = RandomForestClassifier(random_state=42)
    # Addestramento del modello
    model.fit(x_train, y_train)
    # Esecuzione delle predizioni sul set di dati
    y_pred = model.predict(x_test)

    valutazione_modello(y_test, y_pred)

    return y_test, y_pred


def valutazione_modello(y_test, y_pred):
    # Valutazione dei risultati
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)

    print("--------------PRECISION------------")
    print(precision)
    print("--------------ACCURACY------------")
    print(accuracy)


"""def bilanciamento_classe(dataset):
    # Sovracampionamento
    datasetOver = oversampling_data(dataset, 200)

    # Sottocampionamento
    datasetUnder = undersampling(dataset)
    return x, y"""


"""def oversampling(x_train, y_train):
    rapporto_attuale = 0.6

    # Bilanciamento delle classi con SMOTE (tecninca di sovracampionamento)
    smote = SMOTE(sampling_strategy=rapporto_attuale, random_state=42)
    x_resampled, y_resampled = smote.fit_resample(x_train, y_train)

    return x_resampled, y_resampled
"""


def undersampling(dataset):
    x_resampled = dataset.drop('Class', axis=1)
    y_resampled = dataset['Class']

    rapporto_attuale = 0.8

    # Bilanciamento delle classi con RandomUnderSampler (tecninca di sottocampionamento)
    undersamplingData = RandomUnderSampler(sampling_strategy=rapporto_attuale, random_state=42)
    x, y = undersamplingData.fit_resample(x_resampled, y_resampled)

    trainingData2 = pd.concat([x, y], axis=1)
    trainingData2.to_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetTraining.xlsx", index=False)

    print("Finito Undersampling")


def average(dataset):
    avgFrequency = int(dataset['Frequency'].mean())
    avgMonetary = int(dataset['Monetary'].mean())
    avgRecency = int(dataset['Recency'].mean())
    avgTime = int(dataset['Time'].mean())

    print("MEDIA FREQUENZA: " + str(avgFrequency))
    print("MEDIA MONETARY: " + str(avgMonetary))
    print("MEDIA RECENCY: " + str(avgRecency))
    print("MEDIA TIME: " + str(avgTime))

    avg = [avgFrequency, avgMonetary, avgRecency, avgTime]

    return avg


def return_random(x):
    delta = x // 2  # divisione intera
    return random.randint(x - delta, x + delta)


def oversampling_data(dataset, x):
    avg = average(dataset)
    newData = []

    for i in range(x):  # Usa un ciclo for per semplificare il codice
        new_row = [
            random.randint(0, 1),  # Sex
            random.randint(1, 4),  # AgeGroup
            return_random(avg[0]),  # Frequency
            return_random(avg[1]),  # Monetary
            return_random(avg[2]),  # Recency
            return_random(avg[3]),  # Time
            0  # Class
        ]
        newData.append(new_row)

    # Crea un DataFrame utilizzando i nuovi dati
    columns = ['Sex', 'AgeGroup', 'Frequency', 'Monetary', 'Recency', 'Time', 'Class']
    new_data_frame = pd.DataFrame(newData, columns=columns)

    # Salva il DataFrame in un file Excel
    merge_datasets(dataset, new_data_frame)
    print("Finito agiunte "+str(x))


def merge_datasets(dataset1, dataset2):
    merged_dataset = pd.concat([dataset1, dataset2], axis=0)
    merged_dataset.to_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetTraining.xlsx", index=False)
