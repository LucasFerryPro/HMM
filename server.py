from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "votre_cle_secrète"  # N'oubliez pas d'ajouter une clé secrète pour utiliser les sessions.

pages = ["home", "page1", "page2", "page3", "page4"]
transitions = {page: {p: 0 for p in pages} for page in pages}
hits = {page: 0 for page in pages}

def update_markov(src, dst):
    if src in pages and dst in pages:
        transitions[src][dst] += 1
        hits[src] += 1

def get_probabilities():
    probabilities = {}
    for page, trans in transitions.items():
        total = sum(trans.values())  # Le total des transitions pour la page source
        if total > 0:
            probabilities[page] = {dst: round((count / total)*100, 2)/100 for dst, count in trans.items()}  # Calcul correct des pourcentages
        else:
            probabilities[page] = {dst: 0 for dst in pages}  # Si aucune transition, mettre 0 pour tout
    return probabilities

@app.route('/')
def home():
    session['previous_page'] = 'home'  # Initialisez la page précédente pour la première fois
    return render_template("index.html", page="home", pages=pages)

@app.route('/navigate/<page>')
def navigate(page):
    prev_page = session.get('previous_page', 'home')  # Récupérez la page précédente de la session
    if page in pages:
        update_markov(prev_page, page)
        session['previous_page'] = page  # Mettez à jour la page précédente dans la session
        return render_template("index.html", page=page, pages=pages)
    return redirect(url_for('home'))

@app.route('/stats')
def stats():
    # Calcul du total des transitions pour chaque ligne (depuis chaque page)
    total_transitions_from = {page: sum(transitions[page].values()) for page in pages}
    
    # Calcul du total des transitions pour chaque colonne (vers chaque page)
    total_transitions_to = {page: sum(transitions[src][page] for src in pages) for page in pages}
    
    # Calcul du total des transitions pour chaque page (ligne et colonne)
    total_page_transitions = {page: total_transitions_from[page] + total_transitions_to[page] for page in pages}
    
    return render_template("stats.html", transitions=transitions, probabilities=get_probabilities(), pages=pages, total_transitions=total_page_transitions, total_transitions_from=total_transitions_from, total_transitions_to=total_transitions_to)

if __name__ == '__main__':
    app.run(debug=True)
