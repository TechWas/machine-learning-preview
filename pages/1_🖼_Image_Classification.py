import streamlit as st

st.set_page_config(
    page_title="Image Classification",
    page_icon="🖼",
)

st.write("# Image Classification Page")

st.write("this is a description")

with st.expander("Example Usage"):
    st.write(
        """
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
        """
    )
    st.image("https://static.streamlit.io/examples/dice.jpg")

with st.expander("Class list for predictions"):
    st.write(
        """
        Below is the class list for predictions
        """
    )
    st.image("https://static.streamlit.io/examples/dice.jpg")

st.write("---")

st.markdown(
    "<h6 style='text-align: center;'>Predict your own image!</h6>",
    unsafe_allow_html=True,
)

st.write("---")

left_layout, right_layout = st.columns(2)

st.session_state.disabled = False

with left_layout:
    st.write(
        "<h6 style='text-align: center;'>Prediction</h6>",
        unsafe_allow_html=True,
    )
    uploaded_file = st.file_uploader(
        "", type=["jpg", "jpeg"], label_visibility="collapsed"
    )
    if uploaded_file:
        img_val = uploaded_file.getvalue()


with right_layout:
    st.write(
        "<h6 style='text-align: center;'>Result</h6>",
        unsafe_allow_html=True,
    )

    # contains response
    st.code(
        """
        result{
            
            
            
        }
        """
    )

# wtf is this code
_, _, _, mid, _, _, _ = st.columns(7)

with mid:
    solve_button = st.button(
        "Predict!", key="but_solve", disabled=st.session_state.get("disabled")
    )
    if solve_button:
        # req to api
        # response = ...
        pass
