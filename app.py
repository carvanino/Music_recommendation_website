#!/usr/bin/python3
from flask import Flask, request, render_template, jsonify
import requests
import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# MySQL connection configuration
mysql_host = 'localhost'
mysql_user = 'root'
mysql_password = 'akinola1'
mysql_database = 'music_app'

connection = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)

token = 'BQCNi4odHW2gYoCl7x_46cqqoj5Kj82vx7149BsN5frLKxSjT7fDm4wHBr9Gz0LTuyuW64aTT5XteZVpa62wxwURePSjV93XpeNUaFVNAHeau-YVyhV3Y6aRocEuN36Rl4Os6l5fr5gH3d4XcjT-oVDBhZyqopuOavkxdwFzR_-y68JthgeMU5qvHG-Q97qt2qX2rlO6iaw9PrWtUl0'
user_headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json"
}
BASE_URL = 'https://api.spotify.com/'
user_params = {
    "limit": 50
}


@app.route("/")
def home():
    return '''
    <h1>Welcome to Play Suits!</h1>
    <form action="/search" method="post">
        <input type="text" name="query" placeholder="Enter a song or artist">
        <input type="submit" value="Search">
    </form>
    '''


@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("query")
    print(query)  # Get the query from the form

    # Perform recommendation based on the query
    results = perform_recommendation(query)
    return render_template("results.html", results=results)


@app.route("/recommend", methods=["GET"])
def recommend():
    # Get the query parameter from the request
    query = request.args.get("query")

    # Perform recommendation based on the query and get the results
    results = perform_recommendation(query)

    return jsonify(results)


def perform_recommendation(query):
    preprocessed_data = [
        ("Rihanna", "Love on the Brain", "Pop")
    ]
    data = {        'q': query,
        'type': 'track'
    }
    return_search = requests.get(
        BASE_URL + 'v1/search',
        params=data,
        headers=user_headers)
    print(return_search)
    return_searchs = return_search.json()
    print(type(return_searchs))
    if hasattr(return_searchs, 'tracks'):
        print('yes')
    print('why?')
    print(return_searchs.keys())
    # print(return_searchs['tracks'])
    track_id = return_searchs['tracks']['items'][0]['id']
    print(track_id)
    # track_id = return_searchs.get('tracks').get('items')[0].get('id')
    # track_id = return_searchs.tracks.items[0].id
    search_recommendations = requests.get(
        BASE_URL + 'v1/recommendations/',
        params={
            'seed_tracks': track_id
            },
        headers=user_headers)
    search_recommendation = search_recommendations.json()
    list_of_recommendaton = search_recommendation['tracks']
    recommended_song = []
    for recommendation in list_of_recommendaton:
        # print(recommendation)
        song = recommendation['name'] + ' By ' + recommendation['artists'][0]['name']
        print(song)
        recommended_song.append(song)

    # Perform content-based filtering using TF-IDF vectorization
    # vectorizer = TfidfVectorizer()
    # tfidf_matrix = vectorizer.fit_transform(
    #     [entry[1] for entry in preprocessed_data])

    # # Get the user input's TF-IDF vector
    # user_input_tfidf = vectorizer.transform([query])

    # # Calculate the cosine similarity between user input and preprocessed data
    # similarity_scores = cosine_similarity(user_input_tfidf, tfidf_matrix)

    # # Get the indices of top similar songs
    # top_similar_indices = similarity_scores.argsort()[0][-5:][::-1]

    # Get the recommended songs based on the indices
    # recommended_songs = [preprocessed_data[index]
    #                      for index in top_similar_indices]

    return recommended_song


if __name__ == "__main__":
    app.run()
