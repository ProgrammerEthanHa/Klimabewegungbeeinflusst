import streamlit as st
import pandas as pd
import altair as alt

st.header("Die Klimabewegung beeinflusst das Leben junger Menschen")
st.subheader("Hat das Engagement junger Menschen für den Klimaschutz Einfluss auf Dein eigenes Leben?")

source = pd.DataFrame({
        'Anteil(%)': [36, 14, 50],
        'Meinung': ['Nein', 'Ich weiß nicht', 'Ja']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Meinung:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis: 1010 Befragte; (14 bis 22 Jahre) in Deutschland; 2021
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Umweltbundesamt")