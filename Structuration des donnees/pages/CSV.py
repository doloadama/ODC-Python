import streamlit as st

st.title("Information sur les fichiers CSV")
st.image("/home/adama/Documents/ODC-Python/Structuration des donnees/pages/csv.jpeg", caption="Source image: Bing")

("Un fichier :blue[CSV] (Comma Separated Values) est un format de fichier simple utilisé pour stocker des données tabulaires."
 " Les données dans un fichier CSV sont organisées en lignes et en colonnes,"
 " séparées par des virgules. Ce format est largement utilisé pour échanger des données"
 " entre différents logiciels et applications car il est simple, universel et indépendant de la plateforme. \n")

"Structure d'un fichier :blue[CSV] \n"

"Un fichier :blue[CSV] typique contient les éléments suivants : \n \n"

(" :red[En-tête]: La première ligne contient généralement les noms des colonnes,"
 " permettant d'identifier les différents champs de données. \n")
(" :red[Données]: Les lignes restantes contiennent les données réelles,"
 " chaque ligne représentant un enregistrement individuel. \n")
(" :red[Séparateurs]: Les virgules sont les séparateurs de champs par défaut,"
 " mais d'autres caractères comme des points-virgules ou des tabulations peuvent être utilisés. \n")

st.title("Conversion de fichier CSV")
st.file_uploader('Choisir le fichier')

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.button("CSV -> XML")

with col2:
    st.button("CSV -> JSON")

with col3:
    st.button("CSV -> YAML")

