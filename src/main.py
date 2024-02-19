import pandas as pd
import os

from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

import data_understanding as du
import data_cleaning as dc

PATH_SEPARATOR = os.sep


dataset = pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetFinale.xlsx")
#datasetTrue = pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetTrue.xlsx")


#dc.dropColumn(dataset)
#dc.createOnlyTrue(dataset)
#dc.showIntersectionAgeAndFrequency(datasetTrue)
#dc.showIntersectionAgeAndFrequency(datasetFalse)

#dc.changeAgeGroup(dataset)
#dc.changeCat(dataset)

"""Codifica delle variabili categoriche
categoricalFeatures = ['Sex', 'AgeGroup']

# Esegui la codifica one-hot per le colonne categoriche
df_encoded = pd.get_dummies(dataset, columns=categoricalFeatures)
"""

X = dataset.drop('Class', axis=1)
y = dataset['Class']

#Suddivisione del dataset in training e test (80%-20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
#Addestramento del modello
model.fit(X_train, y_train)
#Esecuzione delle predizioni sul set di dati
y_pred= model.predict(X_test)

#Valutazione dei risultati
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)

print(f"Accuracy del modello sul test set: {accuracy:.2f}")
print(f"Precison del modello sul test set: {precision:.2f}")
