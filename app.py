"""
Simple Flask web application for ShopFront.
Returns contacts page on any GET request.
Handles POST requests from contact form.
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
@app.route("/<path:subpath>", methods=["GET"])
def contacts_page(subpath=None):
    """Обрабатывает любой GET-запрос и возвращает страницу контактов"""
    return render_template("contacts.html")


@app.route("/submit-form", methods=["POST"])
def handle_form_submission():
    """Обрабатывает POST-запрос из формы обратной связи"""
    # Получаем данные из формы
    form_data = {
        "name": request.form.get("name"),
        "email": request.form.get("email"),
        "message": request.form.get("message"),
    }

    # Печатаем в консоль сервера
    print("\n" + "=" * 50)
    print("НОВАЯ ЗАЯВКА С ФОРМЫ:")
    print(f"Имя: {form_data['name']}")
    print(f"Email: {form_data['email']}")
    print(f"Сообщение: {form_data['message']}")
    print("=" * 50 + "\n")

    # Можно вернуть успешный ответ или перенаправить
    return "Форма успешно отправлена! Данные выведены в консоль.", 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
