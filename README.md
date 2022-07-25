POCs sur la mise en place de deux blocs du détecteur de Fake News
POCs réalisés sur le Dataset suivant : https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

AnalyseSemantiqueBayesLime :
Classification des News par l'algorithme Bayésien Naïf basée sur la fréquence d'apparition des mots dans les news.
Mise en place de Lime pour expliquer les résultats : pour chaque News classée, on sait quels mots ont eu le plus d'importance dans la classification.
On utilise l'algorithme Bayésien Naïf, désigné comme modèle le plus efficace pour ce genre de classification (voir Khan, Junaed Younus, Md Tawkat Islam Khondaker, Sadia Afroz, Gias Uddin, et Anindya Iqbal. « A benchmark study of machine learning models for online fake news detection ». Machine Learning with Applications 4 (2021))

SentimentAnalysis :
Classification des News en Fake/True basée sur le Sentiment Analysis : la bibliothèque nltk : vaderSentiment, SentimentIntensityAnalyser, qui retourne un score de sentiment positif, neutre et négatif.
L'utilisation de Lime permet de comprendre quel type de sentiment (positif, neutre ou négatif) influe le plus sur la classification des news.


Les résultats de ces algorithmes et plus particulièrement l'explicabilité permettent ensuite d'adapter l'utilisation faite du modèle conceptuel : on détecte les paramètres ayant le plus d'influence dans la discrimination des News.

Suite des opérations : 
Appliquer d'autres 

