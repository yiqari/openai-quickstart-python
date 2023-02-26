import os

import openai
import socket
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        print("************TEST********")
        print("************TEST********")
        print("************TEST********")
        print("************TEST********")
        print("************TEST********")
        print("************TEST********")

        input = request.json["input"]
        print(input)
        print("************TEST********")
        hostname = socket.gethostname()
        PAddr = request.remote_addr
        print("hostname: " + hostname + " IP Address: " + PAddr)
        print(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
        response = openai.Completion.create(
            model="text-davinci-003",
            max_tokens = 256,
            stop=None,
            prompt=input,
            temperature=0.6,
        )
        print(response)

        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")

    return result

    # return render_template("index.html", result="test123")


def generate_prompt(input):
    return """Suggest three names for an animal that is a superhero.

input: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
input: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
input: {}
Names:""".format(
        input.capitalize()
    )
