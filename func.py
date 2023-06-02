import requests
import os
import io
import streamlit as st
import typing
from dotenv import load_dotenv
from datetime import datetime

# from transformers import pipeline

load_dotenv()

IMAGE_API_URL = os.getenv("IMAGE_API_URL")
SUMMARIZATION_API_URL = os.getenv("SUMMARIZATION_API_URL")
SUMMARIZATION_TOKEN = os.getenv("SUMMARIZATION_TOKEN")
# summarizer = pipeline(
#     "summarization",
#     model="sesar/BartLargeCNN-FineTuned",
#     tokenizer="sesar/BartLargeCNN-FineTuned",
#     framework="tf",
# )


@st.cache_data
def default():
    response = requests.get(IMAGE_API_URL)

    if response.status_code == 200:
        # data = response.json()
        return response.text
    else:
        data = "An error occurred:", response.status_code
        return data


@st.cache_data
def predict(image):
    url = IMAGE_API_URL + "/predict/"

    payload = {}
    files = {"file": ("image.jpg", io.BytesIO(image), "image/jpeg")}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response.text


# @st.cache_data
# def summarize(text: str) -> str:
#     """
#     Summarizes a given text.

#     This function takes in a text as input and returns a summarized version of it. Currently, the function is unfinished and simply returns the original text.

#     Args:
#         text (str): The text to be summarized.

#     Returns:
#         str: The summarized text.
#     """
#     input_ids = tokenizer.encode(text, return_tensors="tf", truncation=True)
#     generated_sequence = model.generate(input_ids=input_ids)
#     summarized_text = tokenizer.decode(
#         generated_sequence.numpy().squeeze(), skip_special_tokens=True
#     )

#     return summarized_text


@st.cache_data
def summarize_api(text: str) -> str:
    headers = {"Authorization": f"Bearer {SUMMARIZATION_TOKEN}"}

    def query(payload):
        response = requests.post(SUMMARIZATION_API_URL, headers=headers, json=payload)
        return response.json()

    output = query(
        {
            "inputs": text,
        }
    )

    return output


# @st.cache_data
# def summarize_pipeline(text: str) -> str:
#     return summarizer(text)[0]["summary_text"]


@st.cache_data
def timer(start_time: datetime = None) -> "typing.Union[datetime.datetime, str]":
    """
    Measures the time elapsed from a given start time.

    If no start time is provided, returns the current time. If a start time is provided, returns a formatted string
    representing the time elapsed from the start time to the current time.

    Args:
        start_time (datetime.datetime, optional): The start time to measure elapsed time from, or None to get the current time. Defaults to None.

    Returns:
        Union[datetime.datetime, str]: The current time if no start time is provided, or a formatted string representing the elapsed time.
    """
    if not start_time:
        start_time = datetime.now()
        return start_time
    elif start_time:
        thour, temp_sec = divmod((datetime.now() - start_time).total_seconds(), 3600)
        tmin, tsec = divmod(temp_sec, 60)
        return "%i hours %i minutes and %s seconds." % (
            thour,
            tmin,
            round(tsec, 2),
        )
