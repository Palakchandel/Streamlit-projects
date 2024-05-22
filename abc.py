import streamlit as st
st.title('hello')
st.write('python')
s=st.number_input("enter any number")
if s>=50:
    st.write('you are eligible for 50% discount')
else:
    st.write('Sorry! , good luck')
a=st.radio('Are you working',options=['Yes','No'])
if a=='Yes':
    st.write('You can take weekdays classes')
else:
    st.write('you can go for weekend classes')

c=st.sidebar.checkbox('Are you intrested in programming')
if c==True:
    d=st.sidebar.radio('You can choose languages',options=['Python','Java','DA','AI'])
    if d=='Python':
        st.sidebar.write('Welcome to python classes')
    if s=='Java':
        st.sidebar.write('Welcome to java classes')
    if s=='DA':
        st.sidebar.write('Welcome to DA classes')
    if s=='AI':
        st.sidebar.write('Welcome to AI classes')
else:
    st.sidebar.write('You can go for other stream\n Good Luck')


