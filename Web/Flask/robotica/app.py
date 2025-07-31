from flask import Flask, render_template

app = Flask(__name__)
# Rotas (paginas)
@app.route('/')
def index():
    return render_template('index.html')
#fim rotas
if __name__ == '__main__':
    app.run(debug=True)