import pandas as pd
import warnings
warnings.filterwarnings('ignore') 

import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st

#déclaration du titre
st.title('Analyse dataset "Voiture"')
st.write("Par : TEYCHON Jaufré")

#lien DF
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"

#lecture DF
df = pd.read_csv(link)

#sous-titre
st.write("DF avec Filtrage : ")

#Filtrage par continent
continent_filter = st.sidebar.selectbox('Filtrer par continent', ['Tous'] + df['continent'].unique().tolist())
if continent_filter != 'Tous':
    df = df[df['continent'] == continent_filter]

df

#sous-titre
st.write("Analyse : ")

# Pair plot
fig = sns.pairplot(df, hue='continent')
st.pyplot(fig)
