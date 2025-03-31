from flask import Flask, render_template, redirect, url_for, session
from MarkovModel import MarkovModel

app = Flask(__name__)
app.secret_key = "votre_cle_secrete"
pages = ["home", "page1", "page2", "page3", "page4"]
markov = MarkovModel(pages)

@app.route('/')
def home():
    session['previous_page'] = 'home'
    return render_template("index.html", page="home", pages=pages)

@app.route('/navigate/<page>')
def navigate(page):
    prev_page = session.get('previous_page', 'home')
    if page in pages:
        markov.update(prev_page, page)
        session['previous_page'] = page
        return render_template("index.html", page=page, pages=pages)
    return redirect(url_for('home'))

@app.route('/stats')
def stats():
    probabilities = markov.get_probabilities()
    transitions = markov.get_transitions()
    return render_template("stats.html", transitions=transitions, probabilities=probabilities, pages=pages)

if __name__ == '__main__':
    app.run(debug=True)
