from flask import Flask, jsonify

varStore = {}
app = Flask(__name__)

# setting debug to true allows code updates without restart
app.config["DEBUG"] = True

@app.route("/set/<k>/<v>")
def setValue(k, v):
    """Adds or updates a new k, v pair"""
    varStore[k] = v
    return jsonify(message=f"Created new key: '{k}' with value: {v}")


@app.route("/get/<k>")
def getValue(k):
    """retrieves a value with the given key"""
    keys = varStore.keys()
    if k not in keys:
        return jsonify(message="That key does not exist")
    else:
        return jsonify(value=varStore[k])

@app.route("/list")
def listKeys():
    return jsonify(keys=list(varStore.keys()))

@app.route("/")
def appMethods():
    """Simple homepage that displays available methods"""
    return jsonify(
        listKeys="/list",
        setValue="/set/k/v",
        getValue="/get/k"
    )

app.run()
