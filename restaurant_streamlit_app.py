import streamlit as st
import langchain_helper

st.title("Restaurant Name Generator")

# for a sidebar with listed selectbox options
# cuisine = st.sidebar.selectbox(
#             "Select a cuisine",("Indian", "Japanese","Russian","Italian","French")
#             )

# for user input text box
cuisine = st.text_input("Enter a cuisine (example: Indian, Japanese, etc.)")

def generate_restaurant_name_menu(cuisine):
    return {"restaurant_name": "South Delight",
            "menu_items": 'idli, dosa, sambar'
            }

if cuisine:
    response = langchain_helper.generate_restaurant_name_menu(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(', ') # values are comma separated therefore using split
    st.subheader("<<<<<  Menu Items  >>>>>")
    st.write("Here are some menu items you can consider:")
    for item in menu_items:
        st.write("-",item)