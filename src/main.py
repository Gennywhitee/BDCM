import pandas as pd
import os

from sklearn.metrics import accuracy_score, precision_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

import data_understanding as du
import data_cleaning as dc

PATH_SEPARATOR = os.sep


dataset = pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetAgeChange.xlsx")
#datasetTrue = pd.read_excel(f"..{PATH_SEPARATOR}dataset{PATH_SEPARATOR}DatasetTrue.xlsx")


#dc.dropColumn(dataset)
#dc.createOnlyTrue(dataset)
#dc.showIntersectionAgeAndFrequency(datasetTrue)
#dc.showIntersectionAgeAndFrequency(datasetFalse)

#dc.changeAgeGroup(dataset)
#dc.changeCat(dataset)
