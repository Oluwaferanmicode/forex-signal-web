from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    signals = ['Buy', 'Sell', 'Hold']
    chosen_signal = random.choice(signals)
    return render_template('index.html', signal=chosen_signal)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)