# import libraries
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz
from .data_handler import load_movie_data

# load data
movie_search_data = load_movie_data("movie_search_data.pkl")
movie_genre_data = load_movie_data("movie_genre_data.pkl")
movie_lang_data = load_movie_data("movie_lang_data.pkl")
movie_overview_data = load_movie_data("movie_overview_data.pkl")

# preprocessing title
def clean_title(title):
    title = re.sub("[^a-zA-Z0-9 ]","", title)
    title = title.lower()
    return title

#---------Operation 1: Search movie title and return exact/similar search ----------
def search_movie(title):
    # Clean the input title
    cleaned_title = clean_title(title)
    
    # Calculate cosine similarity between cleaned_title and movie titles
    vectorizer = TfidfVectorizer(ngram_range=(1,2))
    tfidf_title = vectorizer.fit_transform(movie_search_data['clean_title'])
    query_vect = vectorizer.transform([cleaned_title])
    similarity = cosine_similarity(query_vect, tfidf_title).flatten()
    
    # Fuzzy matching to account for minor title variations
    fuzzy_scores = [fuzz.ratio(cleaned_title, t) for t in movie_search_data['clean_title']]
    similarity = similarity * (0.8 + 0.2 * (pd.Series(fuzzy_scores) / 100))  # Weighted average
    
    # Get the indices of top 10 similar movies
    top_indices = similarity.argsort()[-10:][::-1]
    
    # Retrieve the top 10 search results
    search_movie_results = movie_search_data.iloc[top_indices]
    search_movie_results['release_date'] = search_movie_results['release_date'].apply(lambda x: x.strftime('%Y-%m-%d'))
    
    return search_movie_results[['title', 'release_date', 'vote_average', 'overview', 'runtime']]


#----------Operation 2: Recommendations based on dropdown criteria options-------
def recommend_genre(genre):

    # Get the movies that belong to the specified genre
    genre_movies = movie_genre_data[movie_genre_data['clean_genres'].str.contains(genre)]

    # Sort the movies by votes in descending order
    sorted_genre_movies = genre_movies.sort_values(by='vote_average', ascending=False)

    # Select the top 10 movies
    top_10_genre_movies = sorted_genre_movies.head(10)
    top_10_genre_movies['release_date'] = top_10_genre_movies['release_date'].apply(lambda x: x.strftime('%Y-%m-%d'))

    return top_10_genre_movies[['title', 'release_date', 'vote_average', 'overview', 'runtime']]

def recommend_language(language):
    # Get the movies that belong to the specified genre
    lang_movies = movie_lang_data[movie_lang_data['original_language'].str.contains(language)]

    # Sort the movies by votes in descending order
    sorted_lang_movies = lang_movies.sort_values(by='vote_average', ascending=False)

    # Select the top 10 movies
    top_10_lang_movies = sorted_lang_movies.head(10)
    top_10_lang_movies['release_date'] = top_10_lang_movies['release_date'].apply(lambda x: x.strftime('%Y-%m-%d'))

    return top_10_lang_movies[['title', 'release_date', 'vote_average', 'overview', 'runtime']]

def recommend_similar_movie(title):
    selected_title_overview = movie_overview_data.loc[movie_overview_data['title']==title, 'overview_processed'].values[0]
    
    # Calculate cosine similarity between selected title overview and all movie overviews
    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    tfidf_overview = vectorizer.fit_transform(movie_overview_data['overview_processed'])
    query_vect_overview = vectorizer.transform([selected_title_overview])
    similarity_overview = cosine_similarity(query_vect_overview, tfidf_overview).flatten()
    
    # Get the indices of top 10 similar movies based on overviews
    top_10_indices_overview = similarity_overview.argsort()[-10:][::-1]

    # Retrieve the top 10 search results based on overviews
    search_movie_results_overview = movie_overview_data.iloc[top_10_indices_overview]
    search_movie_results_overview['release_date'] = search_movie_results_overview['release_date'].apply(lambda x: x.strftime('%Y-%m-%d'))

    return search_movie_results_overview[['title', 'release_date', 'vote_average', 'overview', 'runtime']]

