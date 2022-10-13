from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__)

description = """
                <!DOCTYPE html>
                <head>
                <title>API Landing</title>
                </head>
                <body>  
                    <h3>Apagando</h3>
                    <a href="http://localhost:5000/api?value=2">sample request</a>
                </body>
                """


@app.route("/", methods=["GET"])
def home():
    return description


@app.route("/api", methods=["GET"])
def square():
    if not all(k in request.args for k in (["value"])):
        # we can also print dynamically
        # using python f strings and with
        # html elements such as line breaks (<br>)
        error_message = f"\
                            Required paremeters : 'value'<br>\
                            Supplied paremeters : {[k for k in request.args]}\
                            "
        return error_message
    else:
        # assign and cast variable to int
        value = int(request.args["value"])
        # or use the built in get method and assign a type
        # http://werkzeug.palletsprojects.com/en/0.15.x/datastructures/#werkzeug.datastructures.MultiDict.get
        value = request.args.get("value", type=int)
        return json.dumps({"Value Squared": value**2})


@app.route("/about")
def about():

    # return index.html page
    return render_template("examples/index.html")


@app.route("/test")
def test():
    return [{"hello": "world", "hi": "world2"}, {"hello": "there", "hi": "there2"}]


@app.route("/test2")
def test2():

    list = []
    url = "https://docs.google.com/spreadsheets/d/1lTZpSuPc0hgY5xglxDV5K92Bzd97ta6OiBWuW79mkJk/export?format=csv"
    r = requests.get(url, allow_redirects=True)
    open("test.csv", "wb").write(r.content)

    # read csv file and append to list
    with open("test.csv", "r") as f:
        for line in f:
            list.append(line)
    return list
