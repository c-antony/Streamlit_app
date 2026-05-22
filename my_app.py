import streamlit as st

st.write('hello','MBA ESG')

st.header('st.button')

if st.button('say hello'):
     st.write('why hello?')
else:
     st.write('goodbye')