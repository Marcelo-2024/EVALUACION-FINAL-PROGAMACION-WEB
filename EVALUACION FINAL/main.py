from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        quantity = int(request.form['quantity'])

        total_without_discount = quantity * 9000

        discount = 0
        if age >= 18 and age <= 30:
            discount = 0.15
        elif age > 30:
            discount = 0.25

        total_with_discount = total_without_discount - (total_without_discount * discount)

        return render_template('ejercicio1.html', name=name, total_without_discount=total_without_discount, total_with_discount=total_with_discount)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "juan" and password == "admin":
            message = "Bienvenido administrador juan"
        elif username == "pepe" and password == "user":
            message = "Bienvenido usuario pepe"
        else:
            message = "Usuario o contraseña incorrectos"

        return render_template('ejercicio2.html', message=message)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
