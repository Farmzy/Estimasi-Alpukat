import pickle
import streamlit as st

model = pickle.load(open('estimasi_avocado.sav', 'rb'))

#['year','Small_Bags','Large_Bags','Xlarge_Bags']
st.title('Estimasi harga jual alpukat')
year = st.number_input('Input tahun alpukat sampai 2018')
Small_Bags = st.number_input('Input alpukat sekantong kecil')
Large_Bags = st.number_input('Input alpukat sekantong besar')
Xlarge_Bags = st.number_input('Input alpukat sekantong sangat besar')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year,Small_Bags,Large_Bags,Xlarge_Bags]]
        )
    st.write ('Estimasi harga alpukat USD : ', predict)
    st.write ('Estimasi harga alpukat IDR : ', predict*14880,75)