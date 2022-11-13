
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open("ADN8.png")

st.image(image, use_column_width=True)

st.write("""
DNA Nucleotide Contagem Web App

essa app conta nucleotide de DNA!

***
""")
st.header("Sequência de DNA")
sequence_input = "DNA QUERY  2\n GAACATCGTGGA..."
sequence = st.text_area("ENTRADA", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.write("""
****
""")

st.header('ENTRADA(DNA QUERY)')
sequence

st.header('SAIDA(DNA QUERY)')

st.header('DICIONARIO')
def DNA_nucleotide_count(sequence):
    A = sequence.count('A')
    T = sequence.count('T')
    C = sequence.count('C')
    G = sequence.count('G')

    d = {'A': A, 'T': T, 'C': C, 'G': G}

    return d

X = DNA_nucleotide_count(sequence)




st.subheader('2. Print Text')
st.write('Possue ' + str(X['A']) + ' adenine (A)')
st.write('Possue  ' + str(X['T']) + ' thymine (T)')
st.write('Possue' + str(X['G']) + ' guanine (G)')
st.write('Possue' + str(X['C']) + ' cytosine (C)')

st.subheader('DATAFRAME')
df = pd.DataFrame.from_dict(X, orient= 'index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns= {'index':'nucleotide'})
st.write(df)

st.subheader('Grafico')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

p = p.properties(
    width=alt.Step(88)
)


st.write(p)
