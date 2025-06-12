import streamlit as st

## Login page ##
with st.container(
    border=True,
):
    st.title("Welcome")
    st.text("Your meal prep adventure starts here!")
    st.image(
        "./src/assets/meals.jpg",
    )
    if st.button(
        "Sign in with Google",
        icon="🌐",
        use_container_width=True,
    ):
        st.login("google")
    if st.button(
        "Sign in with Facebook (soon)",
        icon="🌐",
        use_container_width=True,
        disabled=True,
    ):
        st.login("facebook")
