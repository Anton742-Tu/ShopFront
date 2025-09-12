"""
Simple Flask web application for ShopFront.
Returns contacts page on any GET request.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
@app.route("/<path:subpath>", methods=["GET"])
def contacts_page(_subpath=None):
    """Обрабатывает любой GET-запрос и возвращает страницу контактов"""
    return render_template("contacts.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
