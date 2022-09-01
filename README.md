Travail d'implémentation dans le cadre du Projet Détecteur de Fake News décrit dans la publication suivante : https://hal.archives-ouvertes.fr/hal-03697974/document


POCs sur la mise en place de deux blocs du détecteur de Fake News
POCs réalisés sur le Dataset suivant : https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

AnalyseSemantiqueBayesLime :
Classification des News par l'algorithme Bayésien Naïf basée sur la fréquence d'apparition des mots dans les news.
Mise en place de Lime pour expliquer les résultats : pour chaque News classée, on sait quels mots ont eu le plus d'importance dans la classification.
On utilise l'algorithme Bayésien Naïf, désigné comme modèle le plus efficace pour ce genre de classification (voir Khan, Junaed Younus, Md Tawkat Islam Khondaker, Sadia Afroz, Gias Uddin, et Anindya Iqbal. « A benchmark study of machine learning models for online fake news detection ». Machine Learning with Applications 4 (2021))

SentimentAnalysis :
Classification des News en Fake/True basée sur le Sentiment Analysis : la bibliothèque nltk : vaderSentiment, SentimentIntensityAnalyser, qui retourne un score de sentiment positif, neutre et négatif.
L'utilisation de Lime permet de comprendre quel type de sentiment (positif, neutre ou négatif) influe le plus sur la classification des news.

LIME est modèle-agnostique, ce qui signifie qu'il peut être appliqué à n'importe quel modèle d'apprentissage automatique. La technique tente de comprendre le modèle en perturbant l'entrée des échantillons de données et en comprenant comment les prédictions changent.

Les résultats de ces algorithmes et plus particulièrement l'explicabilité permettent ensuite d'adapter l'utilisation faite du modèle conceptuel : on détecte les paramètres ayant le plus d'influence dans la discrimination des News.

Suite des opérations : 
- appliquer la structure présente pour tester les précisions des classifications avec d'autres types de classificateurs ;
- appliquer d'autres outils d'explicabilité tels que SHAP pour obtenir plus d'éléments d'explicabilité ;
- mettre en place les autres blocs de la détection de Fake News (Analyse de structure, de l'auteur etc.) ;
- entrainer le modèle avec des datasets plus adaptés (diversité des thèmes abordés).

Difficultés rencontrées :
- utilisation de l'outil Lime : bien veiller à donner à LimeTabularExplainer des données du bon type et de la bonne taille (type Matrice + type dans les cellules de la matrice) ;
- trouver l'équilibre dans la préparation des données entre simplification trop importante (qui permet une durée d'execution moindre pour le programme mais qui fait perdre en performance de classification) et un manque de simplification (plus de précision mais temps d'execution très importants) ;
- comprendre quelle est l'ampleur de l'overfitting dans notre solution (les scores des classificateur paraissent élevés alors que les modèles utilisés sont assez simples) ;
- il semblerait que notre programme ne soit pas suffisement optimisé : les durées d'entrainement avec des corpus de quelques news (5 vraies 5 fausses) sont déja longs (entre 3 et 5 minutes) : voir pour la mise à l'échelle ;
- l'entrainement du modèle nécéssite une machine disposant d'une taille de mémoire importante.