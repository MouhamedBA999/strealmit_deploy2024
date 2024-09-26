import streamlit as st
import numpy as np


## Affichage de text
st.title('My Title ABC ')
st.header('My header')
st.subheader('My sub')
st.text('Fixed width text')

st.write('Most object')
st.write(['st',  'is <', 10])


#Ecriture de latex
st.subheader('Ecriture de Latex')
st.text('''
Exemple 1 : Identite d'Euler
''')
st.latex(r'''
e^{i\pi} + 1 = 0
''')

st.text('''
Exemple 2 : définition de fonction convexe
''')
st.latex(r'''
\forall (x,y) \in dom(f)^2, \forall \lambda \in [0,1], \hspace{0.30cm} f(\lambda x + (1- \lambda)y) \leq \lambda f(x) + (1- \lambda)f(y)
''')

##Mettre un code 
st.subheader('Mettre un code')
st.code('''
for i in range(10):
    print(i)
''')

###Utilisation des donénes
st.subheader('Affichage des données')
st.text('''
Données Pandas
''')

import pandas as pd

customers= pd.read_csv('Churn_Modelling.csv')
#st.dataframe(customers)
#st.dataframe(customers.head(10))
st.dataframe(customers.iloc[10:15])
#st.dataframe(customers[["Geography", "Exited"]])

pip install scikit-learn
from sklearn import datasets
#iris=datasets.load_iris()
#st.dataframe(iris)




#### Affichage en Grille 
### Exemple 1 : Unique Choix
st.sidebar.radio('''
Nombre d'élèves en M1 DSIA''', [5, 8, 10, 15]) #sidebar permet l'affichage en gauche 
nom_ue = st.sidebar.radio('Quelle est votre UE préféée ?',
('Machine learning', 'Probablité' ,'Analyse de données')
)


##if nom_ue=='Machine learning':
 ##   st.sidebar.write('Vous acez choisi Machine learning')
##elif nom_ue== 'Probablité':
##    st.sidebar.write('Vous acez choisi  Probablité')
##else :
##    st.sidebar.write('Vous acez choisi  Analyse de données')
##'''

st.sidebar.write('Vous avez choisi', nom_ue)

### Exemple 2 : Multiple choix 

with st.sidebar:
    st.checkbox('Je suis un Fan de Foot')
    st.checkbox('Je suis un Fan de Tenis')


##value=st.sidebar.checkbox('Afficher donne')
##st.sidebar.write(value)

##if value:
###    st.dataframe(customers.iloc[10:15])
##else :
 ##   st.dataframe(customers.iloc[0:10])


### Exemple 3 : Liste déroulante
st.sidebar.selectbox('Sexe', ['Masculin', 'Feminin'])
etudiants=['Amedé', 'Sow', 'Nohoum', 'Robert', 'Aliou']
st.sidebar.selectbox('Liste Etudiant', etudiants, index=etudiants.index('Sow'))

#Exemple 4 : Sliders
st.sidebar.slider('''
Vous avez combien d'heures de cours par semaine ?
''', 0, 30, 0, 5)

## Exemple 5 : Multiselect
st.sidebar.multiselect('Quels sont vos cours du Lundi', ['Streamlit', 'Anglais', 'Proba', 'Stats', 'Python'])

## Exemple 6 : Choix du nombre
st.sidebar.number_input('Quel est votre chiffre préféré', 0,9)


## Ecemple 7 : Ecrire une grille de text

st.subheader('Ecrire une grille de text')
st.text_input('Presentez-vous')
st.text_area('Quel est votre projet pro ?')

##Exemple 8 : les dates
import  datetime 
from datetime import time 
st.subheader('Dates')
st.date_input('Date de naissance', datetime.date(2020, 3, 6))
st.time_input('Activer une alarme à', value=time(8,45),step=120)

## Exercice à faire  : 
##Exo 1 : 
#Créé une liste de choix possible avec mutliselect qui donne à l'utilisateur de choisir
## ses colonnes du dataframe Churn_modeling qu'il souhaite afficher 

## Exo 2 :
nbre_de_ligne=customers.shape[0]
ligne= st.sidebar.number_input('Quel est votre chiffre préféré', 0,nbre_de_ligne-1)
st.dataframe(customers.iloc[ligne])
##Exo : Afficher en ligne au lieu de colonne


## Exemple 8 : Affichage d'image et vidéos
#st.subheader('Affichage image')
#st.text(''' Image paysage''')
#st.image('paysage1.jpg', caption='Image de paysage', width=500)
#st.text(''' Vidéo ''')
#st.video('can_senegal.mp4', start_time=4)

##Exemple 9 : Graphiques
data1=pd.DataFrame(
    np.random.randn(20,3),
    columns=['a', 'b', 'c']
)
st.dataframe(data1)


#st.line_chart(data1)
#st.line_chart(data1['a']) ## Trace le graphique de la colonne a
st.line_chart(data1[['a', 'b', 'c']])

##Diagramme en barre
import matplotlib.pyplot as plt

fig, ax=plt.subplots()
ax.hist(customers['Geography'])
st.pyplot(fig)

fig, (ax1, ax2)=plt.subplots(1,2)
ax1.hist(customers['IsActiveMember'], color='green')
ax2.hist(customers['Exited'], color='red')
st.pyplot(fig)









