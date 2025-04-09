import streamlit as st

st.title("🔧 Spare Parts Tracker")

part = st.text_input("Enter part name")
qty = st.number_input("Enter quantity", min_value=0)
if st.button("Save Part"):
    st.success(f"Saved {qty} of {part}")