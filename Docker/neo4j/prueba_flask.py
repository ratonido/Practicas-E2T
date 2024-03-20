from flask import Flask, render_template


app=Flask("EEAE")



@app.route("/")
def principal():
    return "Hola Mundo"

@app.route("/hola/<nombre>")
def saludo(nombre):
    return "Hola otra vez" + nombre

@app.route('/codigo')
def python():
    return render_template ('pyton.html')

@app.route('/codigo/<variable>')
def cuantas(variable):
    return render_template ('pyton.html',veces=int(variable))






app.run(port=8080, debug=True)
