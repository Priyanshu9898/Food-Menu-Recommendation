from flask import Flask, jsonify
import os
from dotenv import load_dotenv
import openai
import json

load_dotenv()


app = Flask(__name__)

# print(os.getenv("OPENAI_SECRET_KEY"))
# print(os.getenv("OPENAI_ORG_KEY"))
openai.api_key = os.getenv("OPENAI_SECRET_KEY")


@app.route("/")
def hello():
    return "Hello, World!"


@app.route('/predict', methods=['GET'])
def predict():
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt="""Create me a today's vegetarian menu of Indian Household in Below JSON format and do not include any extra spaces as well as new line in response.\n{"Breakfast": `MenuItems`, "Lunch": `MenuItems`, "High-Tea": `MenuItems`, "Dinner": `MenuItems`}""",
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # print(response['choices'][0]["text"])

    return response['choices'][0]["text"]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
