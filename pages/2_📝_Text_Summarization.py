import streamlit as st
import func as f
from PIL import Image

logo = Image.open("image/logo.png")
# example = Image.open("image/example2.gif")
st.set_page_config(
    page_title="Text Summarization",
    page_icon=logo,
)

st.write("# Text Summarization Page")

st.markdown(
    """
    *This endpoint is not stable yet.*
    
    Text summarization is a technique that can help you extract the main points from a long article. It can save you time and effort by providing you with a concise summary of the content. Our website offers a text summarization service that can help you create summaries of electronic waste articles in minutes. You just need to paste the article you want to summarize, and our website will generate a summary for you. 
    
    Our website uses advanced natural language processing techniques to ensure that the summaries are accurate and coherent. Try our text summarization and discover how it can help you learn more about electronic waste.
    """
)

with st.expander("Example Usage"):
    st.markdown(
        "<h6 style='text-align: center;'>Below is the illustration on how to use this page</h6>\n"
        + "<p style='text-align: center; font-size:80%; '><i>you can use the expander icon to zoom the image (hover the image)</i></p>",
        unsafe_allow_html=True,
    )
    # st.image(example)
    st.markdown(
        "![hiyahiya](https://cdn.discordapp.com/attachments/1106222232834945084/1110884327451000972/example2.gif)"
    )

st.write("---")

st.markdown(
    "<h6 style='text-align: center;'>Summarize your paragraph!</h6>",
    unsafe_allow_html=True,
)

text_input = st.text_area(
    "Your Paragraph",
    placeholder="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Viverra maecenas accumsan lacus vel facilisis volutpat. Dignissim diam quis enim lobortis scelerisque fermentum dui faucibus. Lorem donec massa sapien faucibus et molestie ac feugiat. Sed faucibus turpis in eu mi. At augue eget arcu dictum varius duis at consectetur lorem. Non curabitur gravida arcu ac tortor dignissim. Ridiculus mus mauris vitae ultricies leo integer malesuada. Etiam tempor orci eu lobortis elementum nibh. Suspendisse in est ante in nibh mauris cursus mattis molestie. Neque vitae tempus quam pellentesque. Egestas egestas fringilla phasellus faucibus. Diam maecenas sed enim ut.",
    height=300,
    max_chars=1600,
    label_visibility="collapsed",
)

# BUTTON HANDLER
st.session_state.disabled = True
if text_input != "":
    st.session_state.disabled = False

response = ""
time = ""

# CENTER BUTTON
_, _, _, mid, _, _, _ = st.columns(7)

with mid:
    solve_button = st.button(
        "Predict!", key="but_solve", disabled=st.session_state.get("disabled")
    )

if solve_button:
    time = f.timer(None)
    response = f.summarize_api(text_input)
    time = f.timer(time)

st.write("---")

st.markdown(
    "<h6 style='text-align: center;'>Result &nbsp;&nbsp;&nbsp;</h6>",
    unsafe_allow_html=True,
)

result = st.text_area(
    "The summarization results",
    placeholder="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    height=200,
    value=str(response) + "\n\nTime taken: " + time if response != "" else "",
    label_visibility="collapsed",
)
