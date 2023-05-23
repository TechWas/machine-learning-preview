import streamlit as st

st.set_page_config(
    page_title="Text Summarization",
    page_icon="📝",
)

st.write("# Text Summarization Page")

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

st.write("---")

st.markdown(
    "<h6 style='text-align: center;'>Summarize your paragraph!</h6>",
    unsafe_allow_html=True,
)

text = st.text_area(
    "",
    placeholder="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Viverra maecenas accumsan lacus vel facilisis volutpat. Dignissim diam quis enim lobortis scelerisque fermentum dui faucibus. Lorem donec massa sapien faucibus et molestie ac feugiat. Sed faucibus turpis in eu mi. At augue eget arcu dictum varius duis at consectetur lorem. Non curabitur gravida arcu ac tortor dignissim. Ridiculus mus mauris vitae ultricies leo integer malesuada. Etiam tempor orci eu lobortis elementum nibh. Suspendisse in est ante in nibh mauris cursus mattis molestie. Neque vitae tempus quam pellentesque. Egestas egestas fringilla phasellus faucibus. Diam maecenas sed enim ut.",
    height=300,
    label_visibility="collapsed",
)


st.session_state.disabled = False

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

st.write("---")

st.markdown(
    "<h6 style='text-align: center;'>Result</h6>",
    unsafe_allow_html=True,
)

result = st.text_area(
    "",
    placeholder="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    height=200,
    label_visibility="collapsed",
)
