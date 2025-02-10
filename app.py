from flask import Flask, render_template
from story_generator import generate_story

app = Flask(__name__)

@app.route('/')
def home():
    story = generate_story()
    return render_template('index.html', story=story)
if __name__ == '__main__':
    app.run(debug = True)