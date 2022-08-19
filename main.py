from flask import Flask
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return "My sentiment analysis app."

@app.route('/sentiment/<phase>')
def sentiment(phase):
    tb = TextBlob(phase)
    tb_en = tb.translate(from_lang='pt_br', to='en')
    polarity = tb_en.sentiment.polarity
    return "Polarity: {}".format(polarity)

app.run(debug=True)