"""
Simple Flask web application for ShopFront.
Separate templates for home and contacts pages.
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home_page():
    """Домашняя страница"""
    return render_template("index.html")


@app.route("/contacts", methods=["GET"])
def contacts_page():
    """Страница контактов"""
    return render_template("contacts.html")


@app.route("/<path:subpath>", methods=["GET"])
def any_other_page(subpath):
    """Все остальные GET-запросы перенаправляем на главную"""
    return render_template("index.html")


@app.route("/submit-form", methods=["POST"])
def handle_form_submission():
    """Обрабатывает POST-запрос из формы обратной связи"""
    form_data = {
        "name": request.form.get("name"),
        "email": request.form.get("email"),
        "message": request.form.get("message"),
    }

    print("\n" + "=" * 50)
    print("НОВАЯ ЗАЯВКА С ФОРМЫ:")
    print(f"Имя: {form_data['name']}")
    print(f"Email: {form_data['email']}")
    print(f"Сообщение: {form_data['message']}")
    print("=" * 50 + "\n")

    return "Форма успешно отправлена! Данные выведены в консоль.", 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
