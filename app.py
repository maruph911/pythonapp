
import streamlit as st

st.set_page_config(
    page_title="Maruf's Pizza House",
    page_icon="🍕",
    layout="wide"
)

st.title("🍕 Maruf's Pizza House")
st.subheader("Fresh pizza. Your favourite toppings.")
st.write("Build your perfect pizza and review your order below.")

st.divider()

# Pizza menu
st.header("Our Pizza Menu")

col1, col2, col3 = st.columns(3)

with col1:
    st.image(
        "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=500",
        caption="Classic Pizza"
    )
    st.markdown("### Small")
    st.write("$15")

with col2:
    st.image(
        "https://images.unsplash.com/photo-1571407970349-bc81e7e96d47?w=500",
        caption="Cheese Pizza"
    )
    st.markdown("### Medium")
    st.write("$20")

with col3:
    st.image(
        "https://images.unsplash.com/photo-1579751626657-72bc17010498?w=500",
        caption="Large Pizza"
    )
    st.markdown("### Large")
    st.write("$25")

st.divider()

# Customer order
st.header("Build Your Order")

with st.form("pizza_order"):
    customer_name = st.text_input("Customer name")

    size = st.selectbox(
        "Choose pizza size",
        ["Small", "Medium", "Large"]
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        max_value=20,
        value=1
    )

    pepperoni = st.checkbox("Add pepperoni (+$3 per pizza)")
    extra_cheese = st.checkbox("Add extra cheese (+$1 per pizza)")

    order_type = st.radio(
        "Order type",
        ["Pickup", "Delivery"]
    )

    submitted = st.form_submit_button("Calculate My Order")

if submitted:
    if not customer_name.strip():
        st.warning("Please enter your name.")
    else:
        prices = {
            "Small": 15,
            "Medium": 20,
            "Large": 25
        }

        per_pizza = prices[size]

        if pepperoni:
            per_pizza += 3

        if extra_cheese:
            per_pizza += 1

        total = per_pizza * quantity

        st.divider()
        st.header("Your Order Summary")

        st.write(f"**Customer:** {customer_name}")
        st.write(f"**Pizza size:** {size}")
        st.write(f"**Quantity:** {quantity}")
        st.write(f"**Order type:** {order_type}")
        st.write(f"**Price per pizza:** ${per_pizza}")
        st.subheader(f"Total bill: ${total}")

        st.success("Your order total is ready!")
        st.info(
            "Demo only: this app calculates the order "
            "but does not send it to a restaurant."
        )
