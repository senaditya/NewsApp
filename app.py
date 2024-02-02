from flask import Flask, render_template
import requests

# from dotenv import load_dotenv
# import os

# import json

# load_dotenv()
# apikey = os.getenv("NEWS_API")

apikey = "1038c4e42381ce597f16ce3dd1d21039"

app = Flask(__name__)


@app.route("/")
def index():
    query = "latest"
    max = "12"
    fixed = f"&lang=en&country=in&max={max}&apikey={apikey}"
    url = f"https://gnews.io/api/v4/search?q={query}{fixed}"
    response = requests.get(url)
    # News data (replace this with your actual data)
    news_data = response.json()  # this is after combining the news.property
    # with open("./sample.json", "r") as openfile:
    #     # Reading from json file
    #     json_object = json.load(openfile)
    # news_data = json_object["articles"]
    # print(news_data)
    return render_template("index.html", news_data=news_data["articles"])


# if __name__ == "__main__":
#     app.run()
