from flask import Flask

app = Flask(__name__)
# Rotas (paginas)
@app.route('/')
def index():
    return "Olá mundo!"
#fim rotas
if __name__ == '__main__':
    app.run(debug=True)