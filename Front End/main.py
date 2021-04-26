from flask import Flask, render_template, redirect, url_for
from forms import Quadraticform
import requests, json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jzdfkvgjbasd'

@app.route('/', methods=['GET', 'POST'])
def quadratic_equation():
    form = Quadraticform()
    url = 'http://127.0.0.1:8000/quadratic_equation'
    if form.validate_on_submit():
        inputObj = {
            "a": float(form.a.data),
            "b": float(form.b.data),
            "c": float(form.c.data)
        }

        postInput = requests.post(url, data=json.dumps(inputObj))
        response = json.loads(postInput.text)
        print(response)
        return render_template("quadraticTemplate.html", form=form, response=response)
    return render_template("quadraticTemplate.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)