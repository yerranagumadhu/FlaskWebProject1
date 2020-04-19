"""
The flask application package.
"""

from flask import Flask,request, render_template
app = Flask(__name__)

"""
Movie recomendation code 

"""


import FlaskWebProject1.views
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#credits = pd.read_csv(r"C:\Users\Yerra\Desktop\spark\movie_recommendation_system\data\tmdb_5000_credits.csv")
movies = pd.read_csv(r"C:\Users\Yerra\Desktop\spark\movie_recommendation_system\data\new_data\movie_dataset.csv")
features = ['keywords','cast','genres','director']

# We are considering the 4 features i.e. keywords, cast, genres and director for the movie reocomedation 
def combine_features(row):
    return row['keywords']+' '+row['cast']+' '+row['genres']+' '+row['director']

# Helper function to get the title from the index
def get_title_from_index(index):
    return movies[movies.index == index]['title'].values[0]

# Helper function to get the index from the Title
def  get_index_from_title(title):
    return movies[movies.title == title]['index'].values[0]

def movie_predict(movie_user_like):
    for feature in features:
        movies[feature] = movies[feature].fillna('')

    movies['combined_features'] = movies.apply(combine_features, axis = 1)

    # Convert a collection of text into a  matrix of token counts
    count_matrix = CountVectorizer().fit_transform(movies['combined_features'])

    # Get the cosine similarity matrix from the count matrix
    cosine_sim = cosine_similarity(count_matrix)

    #Get the Movie name from the user and fetch the index from the movie
    movie_index = get_index_from_title(movie_user_like)

    ## Enumerate all the simillarty score for the movie to make a tuple of movie index and similarity scores 
    # Note : we will return a list of tuples in the form 

    similar_movies = list(enumerate(cosine_sim[movie_index]))

    # Now sort the similar movies based on the similarity score  in descinding order and fetch only the top 5 matching movies and remove the 1st record since it matches with it's own record

    recomended_movies =  []

    for i in sorted(similar_movies, key = lambda x: x[1], reverse= True)[1:6]:
        recomended_movies.append(get_title_from_index(i[0]))


    return recomended_movies


# End of the Movie recomendation system

@app.route("/movie", methods=["GET", "POST"])
def movie():
    feedback = 'outside of the Post method'
    if request.method == "POST":

        req = request.form['movie']
        movie_predicted =  movie_predict(req)    
              
        return render_template("recommended.html",  movie_predicted = movie_predicted)

    return render_template("recommended.html")