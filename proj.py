import streamlit as st
import pandas as pd
import pickle
import warnings
warnings.filterwarnings('ignore')

st.title('Computational analysis of stand-up comedy')
st.image('giphy.gif', width = 400)

#read in comedian dataset
df_comedians = pd.read_csv('comedians.csv')

#read in SCRIPTS dataset
df_scripts = pd.read_csv('SCRIPTS.csv')
df_scripts['Name'] = df_scripts['Script_ID'].str.split('-').str[0:2].apply(' '.join)

with st.form('comedian_name'): 
  comedian = st.selectbox('Comedian', options=df_scripts['Name'].unique())
  filtered_df = df_comedians[df_comedians['Comedian'].str.startswith(comedian)]
  st.write('Sociological information of {}'.format(comedian)) 
  st.dataframe(filtered_df)
  st.form_submit_button()

with st.form('script'):
  df_scripts_filtered = df_scripts[df_scripts['Name'] == comedian]
  st.write('List of scripts performed by {}'.format(comedian)) 
  script = st.selectbox('Script',options=df_scripts_filtered['Script_ID'].unique())
  st.form_submit_button()

