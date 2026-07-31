from flask import Flask, render_template
from flask import request, jsonify
from flask import make_response
from dotenv import load_dotenv
from functools import wraps
from datetime import datetime

import os
import sys
import atexit
import random
import sqlite3
import logging
import equation_ast
import equation_levels

from werkzeug.exceptions import BadRequest
from pyfiglet import Figlet

load_dotenv()
app = Flask(__name__)
equation_levels.init()
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

set_equations: set[str] = set()
set_equations_input: set[str] = set()
full_path_db: str = 'db/feedback.db'
parser = equation_ast.EquationParser()
logger = logging.getLogger(__name__)


"""
+----------------------------+
//====== 11.09.2025 ========//
|""symbols"" -> "symbols" ===|
+----------------------------+
"""
def non_symbol(str_non_symbol: str) -> str:
    temp_str: str = ''
    for symbol in str_non_symbol:
        if symbol != "\"":
            temp_str += symbol
    return temp_str


"""
+----------------------------+
//====== 11.09.2025 ========//
|STOP WHILE TRUE. ===========|
|EXIT FLASK. ================|
+----------------------------+
"""
def stop_app() -> None: sys.exit(0)


atexit.register(stop_app)


"""
+----------------------------+
//====== 13.09.2025 ========//
|======= DEBUG INPUT ========|
+----------------------------+
"""
def log_request_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.debug(f"Запити до {request.path}")
        logging.debug(f"Метод: {request.method}")

        try:
            logging.debug(f"JSON: {request.get_json()}")
        except BadRequest:
            logging.info("Не вдалось отримати JSON")

        response = func(*args, **kwargs)
        logging.debug(f"Відповідь: {response.get_data(as_text=True)}")

        return response
    return wrapper


@app.route('/home')
@app.route("/")
def home():
    return render_template("index.html")


"""
+---------------------------------+
//=========== 11.09.2025 ========//
|Робота з базою даних. ===========|
|Запис в базу даних FEEDBACK. ====|
|Читання відгуків для розробника. |
+---------------------------------+
"""
@app.route('/feedback_read', methods=['POST'])
@log_request_response
def feedback_read() -> dict[str, bool | list[tuple[str, str]]]:
    contents_sql: list[tuple[str, str]]
    usernames: list[str] = os.getenv('ALLOWED_USERNAMES', '').split(',')
    passwords: list[str] = os.getenv('ALLOWED_PASSWORDS', '').split(',')

    data: dict[str, str] = request.get_json()
    data_username: str = data.get('username')
    data_password: str = data.get('password')

    if data_username in usernames and data_password in passwords:
        with sqlite3.connect('db/feedback.db') as db:
            c = db.cursor()
            c.execute("SELECT title, data FROM feedback")
            contents_sql = c.fetchall()

        response = make_response(jsonify({'status': True, 'contents': contents_sql}))
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        return response
    else:
        return jsonify({'status': False})


@app.route('/feedback_input', methods=['POST'])
@log_request_response
def feedback_input() -> dict[str, bool]:
    global full_path_db
    data: dict[str, str] = request.get_json()
    data_text: str = data.get('text', '')

    with sqlite3.connect(full_path_db) as db:
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS feedback (
                             id INTEGER PRIMARY KEY AUTOINCREMENT,
                             title TEXT NOT NULL,
                             data  TEXT NOT NULL
                     )""")
        timestamp: str = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        c.execute("INSERT INTO feedback (title, data) VALUES(?, ?)", (data_text, timestamp))
        db.commit()

    response = make_response(jsonify({'status': True}))
    return response


"""
+-------------------------------------------------+
//================== 11.09.2025 =================//
|Перевірка введених рівностей. ===================|
|1. Якщо рівність правильна і нова -> flag: TRUE. |
|2. Якщо рівність не правильна -> flag: FALSE. ===|
|3. Якщо рівність не правильна -> flag: `ERROR`. =|
+-------------------------------------------------+
"""
@app.route('/equation_input_in_equations', methods=['POST'])
@log_request_response
def equation_input_in_equations() -> dict[str, bool | str]:


    def logging_print(marker=True):
        if marker: logging.info("input equation YES")
        else: logging.info("input equation NO")


    data: dict[str, str] = request.get_json()
    equation_data: str = data.get('input_equation')
    equation: str = non_symbol(equation_data)
    dict_response: dict[str, bool | str] = {}

    # DEBUG INPUT
    logging.debug(f"input equation: {equation}")

    if equation not in set_equations_input:
        if parser.is_valid_equation_cpp(equation):
            logging_print()
            dict_response['flag'] = True
            set_equations_input.add(equation)
        else:
            logging_print(False)
            dict_response['flag'] = 'ERROR'
    else:
        logging_print(False)
        dict_response['flag'] = False

    response = make_response(jsonify(dict_response))
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    return response


"""
+--------------------------------------------+
//=============== 14.09.2025 ===============//
|Функції для доступу згенерованих рівностей. |
|1. ================ EQ_4 ===================|
|2. ================ EQ_5 ===================|
|3. ================ EQ_6 ===================|
|4. ================ EQ_7 ===================|
|5. ================ EQ_8 ===================|
+--------------------------------------------+
"""
@app.route('/eq_4', methods=['GET'])
@log_request_response
def eq_4():
    global set_equations

    random_digit: int = random.randint(0, 10)
    digit: str = equation_levels.get_digit_4(random_digit)
    eq: list[str] = equation_levels.get_equations_4(random_digit)
    set_equations = set(eq)

    res_dict: dict[str, list[str]] = {
        'digit': digit,
        'eq': eq
    }
    response = make_response(jsonify(res_dict))
    response.headers["Cache-Control"] = "no-store, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/eq_5', methods=['GET'])
@log_request_response
def eq_5():
    global set_equations

    random_digit: int = random.randint(0, 10)
    digit: str = equation_levels.get_digit_5(random_digit)
    eq: list[str] = equation_levels.get_equations_5(random_digit)
    set_equations = set(eq)

    res_dict: dict[str, list[str]] = {
        'digit': digit,
        'eq': eq
    }
    response = make_response(jsonify(res_dict))
    response.headers["Cache-Control"] = "no-store, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/eq_6', methods=['GET'])
@log_request_response
def eq_6():
    global set_equations

    random_digit: int = random.randint(0, 10)
    digit: str = equation_levels.get_digit_6(random_digit)
    eq: list[str] = equation_levels.get_equations_6(random_digit)
    set_equations = set(eq)

    res_dict: dict[str, list[str]] = {
        'digit': digit,
        'eq': eq
    }
    response = make_response(jsonify(res_dict))
    response.headers["Cache-Control"] = "no-store, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/eq_7', methods=['GET'])
@log_request_response
def eq_7():
    global set_equations

    random_digit: int = random.randint(0, 10)
    digit: str = equation_levels.get_digit_7(random_digit)
    eq: list[str] = equation_levels.get_equations_7(random_digit)
    set_equations = set(eq)

    res_dict: dict[str, list[str]] = {
        'digit': digit,
        'eq': eq
    }
    response = make_response(jsonify(res_dict))
    response.headers["Cache-Control"] = "no-store, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/eq_8', methods=['GET'])
@log_request_response
def eq_8():
    global set_equations

    random_digit: int = random.randint(0, 10)
    digit: str = equation_levels.get_digit_8(random_digit)
    eq: list[str] = equation_levels.get_equations_8(random_digit)
    set_equations = set(eq)

    res_dict: dict[str, list[str]] = {
        'digit': digit,
        'eq': eq
    }
    response = make_response(jsonify(res_dict))
    response.headers["Cache-Control"] = "no-store, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    return response


"""
+-------------------------------------------------------------------+
//=========================== 20.09.2025 ==========================//
|Запуск сервера. ===================================================|
|1. Відправлення index.html. =======================================|
|2. index.html -> index.js, preloader.js, confetti.js. =============|
|3. JS & HTML -> CSS (ChartDiagram.css, dialogFeedback.css, ========|
|dialogBox.main.css, documentDeveloper.css, home.main.css, =========|
|preloader.css, slider.css, stop_timer.main.css, windowModeGame.css |
|CSS -> DYNAMIC ADAPTION -> ASYNC_JS -> PYTHON(flask_app.py)-> C,CPP|
+-------------------------------------------------------------------+
"""


def logo() -> None:
    if os.getenv("WERKZEUG_RUN_MAIN") == "true":
        return None

    f = Figlet(font='slant')
    print(f.renderText('Gusak'))
    print(f.renderText('Tatarchuk'))
    print(f.renderText('Lysenko'))


if __name__ == "__main__":
    logo()
    app.run(host='127.0.0.1', port=7850, debug=True)
