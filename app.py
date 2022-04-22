from flask import Flask, url_for, request, render_template, abort, redirect
from markupsafe import escape
from api import API
import db
import datetime as dt

app = Flask(__name__)


@app.route("/")
def home():
    data = db.allData()
    return render_template('index.html', title="Index", hdata=data)


@app.route("/alert/<message>")
def alert(message):
    return f"<a href='/'>Geri Dön</a>\n<h1>{escape(message)}</h1>"


@app.route("/getData", methods=["GET"])
def getData():
    if request.args:
        if request.method == 'GET':
            if request.args["startTime"] and request.args["coin"] and request.args["parite"] and request.args["interval"]:
                symbol = escape(request.args["coin"] + request.args["parite"])
                interval = escape(request.args["interval"])
                startTime = escape(request.args["startTime"]).replace("T", " ")
                startTime = dt.datetime.strptime(startTime, "%Y-%m-%d %H:%M")

                res = API().getData(
                    1000,
                    symbol=symbol,
                    interval=interval,
                    startTime=startTime
                )

                data = db.allData()
                return render_template('index.html', title="Index", data=res,hdata=data)


            else:
                return redirect(url_for('alert', message="Gerekli Alanları Doldurunuz"))
        else:
            return redirect(url_for('home'))

    else:
        return redirect(url_for('home'))
