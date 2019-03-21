import bottle
@bottle.route("/api/test")
def api_test():
    return {"testik": True}

bottle.run(host="localhost", port=8080, debug=True)
