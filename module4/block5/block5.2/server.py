from bottle import route, run, response
from horoscope import generate_prophecies


@route("/api/forecasts")
def api_test():
    response.headers['Access-Control-Allow-Origin'] = '*'
    return {"prophecies": generate_prophecies(total_num=6, num_sentences=2),}

run(
    host="localhost",
    port=8080,
    autoreload=True
)

