import streamlit as st
import pandas as pd 
import seaborn as sns

st.title('Simple Data Analysis')
st.subheader('Data Analysis using Python and Streamlit app')

upload = st.file_uploader('upload csv format only')
if upload is not None:
    data = pd.read_csv(upload)

if st.checkbox('Preview the dataset\n'):
    if st.button('head'):
        st.write(data.head())
    if st.button('tail'):
        st.write(data.tail())

if upload is not None:
    if st.checkbox('Datatypes of each columns\n'):
        st.text('Datatypes : ')
        st.write(data.dtypes)

if upload is not None:
    radio = st.radio('What dimension do you want to check ? \n', ('Rows','Columns'))
    if radio=='Rows':
        st.text('No of Rows : \n')
        st.write(data.shape[0])
    if radio=='Columns':
        st.text('No of Columns : \n')
        st.write(data.shape[1])

if upload is not None:
    test = data.isnull().values.any()
    if test==True:
        if st.checkbox('null values in the dataset'):
            sns.heatmap(data.isnull())
            st.pyplot()
        else:
            st.success('No missing values, Congrats!!!')

if upload is not None:
    test = data.duplicated().any()
    if test==True:
        dup = st.selectbox('Want to remove duplicates',\
                        ('Yes','No'))
        if dup=='Yes':
            data.drop_duplicates()
            st.text('Duplicates are removed\n')
        else:
            st.text('No Problem\n')

if upload is not None:
    if st.checkbox('Summary of the dataset\n'):
        st.write(data.describe())

if st.button('About App\n'):
    st.text('First Streamlit App')
    st.text('I like very much')

if st.button('By'):
    st.text('Biggod')
