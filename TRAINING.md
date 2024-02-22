#                                   TRAINING E SELEZIONE DEL MODELLO

###         Multinominal NB
--------------PRECISION------------
0.9148936170212766
--------------ACCURACY------------
0.72
--------------RECALL------------
0.7166666666666667
--------------F1-SCORE------------
0.8037383177570093

##########################################

###         Bernoulli NB

--------------PRECISION------------
0.8
--------------ACCURACY------------
0.8
--------------RECALL------------
1.0
--------------F1-SCORE------------
0.8888888888888888

DALLA MATRICE DI CONFUSIONE RISULTA CORRETTA LA CLASSIFICAZIONE
PER LA CLASSE 'DONATING', MA TUTTE LE ISTANZE DELLA CLASSE
'NOT DONATING' SONO STATE CLASSIFICATE COME 'DONATING'

##########################################

###          Random Forest

--------------PRECISION------------
0.8275862068965517
--------------ACCURACY------------
0.7066666666666667
--------------RECALL------------
0.8
--------------F1-SCORE------------
0.8135593220338984

DALLA MATRICE DI CONFUSIONE RISULTA CHE QUASI TUTTE LE ISTANZE
DELLA CLASSE 'DONATING' SONO STATE CLASSIFICATE CORRETTAMENTE (+5 RISPETTO AL MULTINOMIAL),
MA 10 ISTANZE DELLA CLASSE 'NOT DONATING' SONO STATE CLASSIFICATE COME 'DONATING' RISPETTO
ALLE 4 DEL MULTINOMIAL
