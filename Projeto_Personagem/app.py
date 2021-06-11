from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    nome = 'Aatrox'
    hp = 1500
    exibir_imagem = True
    imagem = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/25c93289-0576-4645-bc48-e828abec9740/dcyj4w4-bcc6eb71-43f9-474c-8c57-57095a7259de.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzI1YzkzMjg5LTA1NzYtNDY0NS1iYzQ4LWU4MjhhYmVjOTc0MFwvZGN5ajR3NC1iY2M2ZWI3MS00M2Y5LTQ3NGMtOGM1Ny01NzA5NWE3MjU5ZGUuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.2fz4bKNq_sl5RFZ8sgisXG6JiDiTO6cTvmw23sCNyik"
    
    return render_template(
        'index.html',
        nome = nome, 
        hp = hp, 
        exibir_imagem = 
        exibir_imagem, 
        imagem = imagem
        )
    
if __name__ == "__main__":
    app.run(debug=True)