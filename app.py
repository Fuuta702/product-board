import random

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>八幡平　産直掲示板</h1><ul>おはよう</ul><p>こんばんは</p>"


@app.route("/hello/<name>")
def hello(name):
    return f"<p>こんにちは、{name}さん</p>"


@app.route("/omikuji")
def omikuji():
    omikujis = ["大吉", "中吉", "吉", "凶"]
    unnsei = random.choice(omikujis)
    return f"<p>あなたの運勢は<strong>{unnsei}</storong></p>"
