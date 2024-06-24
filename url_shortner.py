import string
import random

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
shortned_url = {}


def generate_short_url(length=6):  # set default length is six
    chars = string.ascii_letters + string.digits
    short_url = "".join(random.choice(chars) for _ in range(length))
    return short_url


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        long_url = request.form['long_url']
        short_url = generate_short_url()

        while short_url in shortned_url:
            short_url = generate_short_url()

        shortned_url[short_url] = long_url
        return f"shortned url: {request.url_root}{short_url}"

    return render_template("index.html")


@app.route("/")
def redirect_url(short_url):
    long_url = shortned_url.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "url not found ", 404


if __name__ == "__main__":
    app.run(debug=True)