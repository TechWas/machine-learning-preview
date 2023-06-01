import os
from download_model import run_download
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM

path = "saved_model"

def run_init():
    if os.path.isdir(path):
        print("Directory exists")
    else:
        print("Directory does not exist")
        print("Executing download_model.py ...")
        run_download()

model = TFAutoModelForSeq2SeqLM.from_pretrained(path)
tokenizer = AutoTokenizer.from_pretrained(path + "/tokenizer", local_files_only=True)