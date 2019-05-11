from bottle import route, run

@route("/<top:int>/<bottom:int>")
def danger(top, bottom):
    res = {"result": 0, "error": None}
    try:
        res["result"] = top / bottom
    except Exception as err:
        res["error"] = f"Для входных данных {top} и {bottom} не получилось: {err}"

    return res

run(host="localhost", port="8080")s