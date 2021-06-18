from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    nome_mascote = 'Canarinho the Legend'
    pistola = True
    return render_template(
        'index.html',
        nome_mascote = nome_mascote,
        pistola = pistola
    )

if __name__ == "__main__":
    app.run(debug = True)