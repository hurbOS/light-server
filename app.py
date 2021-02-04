from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/core")
def core():
    output = {}
    directory = r'core'
    for package in os.listdir(directory):
        for file in os.listdir("core/" + package):
            if file == "pkg":
                output[package] = {}
                d = output[package]
                with open("core/" + package + "/" + file) as f:
                    for line in f:
                        (key, val) = line.split(": ")
                        d[key] = val.strip("\n")
    return output

if __name__ == "__main__":
    app.run(debug=True)
