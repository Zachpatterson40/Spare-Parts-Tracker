import streamlit as st
import pandas as pd

# Load Excel Data
@st.cache_data
def load_data():
    return pd.read_excel("spare_parts.xlsx")

df = load_data()

# App Layout
st.title("🔧 Spare Parts Manager")

# Page Navigation
page = st.selectbox("Select an option:", ["Home", "Search Spares", "Request Spares", "Consume Spares"])

if page == "Home":
    st.header("Welcome!")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔍 Search Spares"):
            st.session_state.page = "Search Spares"
    with col2:
        if st.button("📝 Request Spares"):
            st.session_state.page = "Request Spares"
    with col3:
        if st.button("➖ Consume Spares"):
            st.session_state.page = "Consume Spares"

elif page == "Search Spares":
    st.header("🔍 Search Spare Parts")
    search = st.text_input("Enter manufacturer, part number, or name")
    if search:
        filtered = df[df.apply(lambda row: search.lower() in str(row).lower(), axis=1)]
        st.dataframe(filtered)
    else:
        st.dataframe(df)

elif page == "Request Spares":
    st.header("📝 Request New Spare Part")
    name = st.text_input("Your name")
    part_name = st.text_input("Part name")
    part_number = st.text_input("Part number")
    manufacturer = st.text_input("Manufacturer")
    reason = st.text_area("Why is this needed?")
    
    if st.button("Submit Request"):
        # Save to CSV or database (to be added)
        st.success("Request submitted!")

elif page == "Consume Spares":
    st.header("➖ Consume Spare Part")
    search = st.text_input("Search by part number, name, or manufacturer")
    quantity_used = st.number_input("Quantity used", min_value=1, step=1)

    if st.button("Consume"):
        # Logic to reduce quantity (to be added)
        st.success(f"Recorded usage of {quantity_used} units.")