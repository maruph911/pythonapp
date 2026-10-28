
import streamlit as st

st.set_page_config(page_title="Pizza Order", page_icon="🍕")

st.title("🍕 Pizza Order Calculator")

size = st.selectbox(
    "Choose pizza size",
    ["Small", "Medium", "Large"]
)

pepperoni = st.checkbox("Add pepperoni (+$3)")
extra_cheese = st.checkbox("Add extra cheese (+$1)")

prices = {"Small": 15, "Medium": 20, "Large": 25}
bill = prices[size]

if pepperoni:
    bill += 3

if extra_cheese:
    bill += 1

st.write(f"Pizza size: {size}")
st.write(f"Pepperoni: {'Yes' if pepperoni else 'No'}")
st.write(f"Extra cheese: {'Yes' if extra_cheese else 'No'}")

st.subheader(f"Your final bill is: ${bill}")
