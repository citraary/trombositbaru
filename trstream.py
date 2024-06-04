import pickle
import streamlit as st
import pandas as pd
import numpy as np
import math
import random

trombositmodel = pickle.load(open('trombositmodel.sav', 'rb'))

st.title('Predict Colorectal Cancer Stage')

pc = st.text_input ('Platelet count')

pdw = st.text_input ('Platelet distribution width')

mpv = st.text_input ('Mean platelet volume')

pct = st.text_input('Plateletcrit')

if st.button('Predict'):
    trprediction = trombositmodel.predict([[pc, pdw, mpv, pct]])
    
    st.text('Stage')
    st.success(trprediction)