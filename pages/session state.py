import streamlit as st
st.set_page_config(
    page_title="session_state Example"),

# إنشاء القائمة في session_state إذا لم تكن موجودة
if "tex_list" not in st.session_state:
    st.session_state.tex_list = []

user_input = st.text_input("Enter text to add to the list:")

if st.button("Add to list"):
    if user_input:
        st.session_state.tex_list.append(user_input)

if st.button("Clear list"):
    st.session_state.tex_list.clear()

st.write("Display list:", st.session_state.tex_list)
#st.write('session state:', st.session_state)
