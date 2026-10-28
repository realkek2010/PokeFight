from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
  # Lädt die index.html aus dem 'templates'-Ordner
  return render_template('index.html')


if __name__ == '__main__':
  # Startet den lokalen Server (im Debug-Modus für Live-Updates)
  app.run(debug=True, host='0.0.0.0', port=5000)