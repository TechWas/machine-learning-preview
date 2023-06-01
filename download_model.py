import gdown
import zipfile


def run_download():
    print("downloading the model ...")

    # download
    url = "https://drive.google.com/uc?id=1awYkq4kYERAuNOyAk7WCNH3XPYNa-B93"
    output = "saved_model_test.zip"
    gdown.download(url, output, quiet=False)

    print("extracting zipped model ...")

    # extract
    with zipfile.ZipFile(output, "r") as zip_ref:
        zip_ref.extractall("saved_model")

    print("success!")