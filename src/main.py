import pandas as pd
import os

from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

import data_understanding as du
import data_cleaning as dc
import data_modelling as dm

PATH_SEPARATOR = os.sep


dataset = pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetFinale.xlsx")
#datasetTrue = pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetTrue.xlsx")


#dc.dropColumn(dataset)
#dc.createOnlyTrue(dataset)
#dc.showIntersectionAgeAndFrequency(datasetTrue)
#dc.showIntersectionAgeAndFrequency(datasetFalse)

#dc.changeAgeGroup(dataset)
#dc.changeCat(dataset)

y_test, y_pred = dm.trainingModello(dataset)

accuracy, precision = dm.valutazioneModello(y_test, y_pred)

print(f"Accuracy del modello sul test set: {accuracy:.2f}")
print(f"Precison del modello sul test set: {precision:.2f}")