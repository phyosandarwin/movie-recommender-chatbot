import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.colored_header import colored_header
from streamlit_extras.switch_page_button import switch_page
import requests


def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    else:
        return r.json()

def display_lottie_animation(animation_json):
    st_lottie(animation_json, height=180, width=200)

def display_search_results(search_results):
    st.write('Search results:')
    renamed_search_results = search_results.rename(columns={
        'title': 'Movie Title',
        'release_date': 'Release Date',
        'vote_average': 'Average Vote',
        'overview': 'Overview',
        'runtime': 'Runtime (mins)'
    })
    st.table(renamed_search_results.set_index('Movie Title'))

def display_recommendations(recommendation_results, category):
    st.subheader(f"Top {len(recommendation_results)} movies in {category}")
    renamed_recommendation_results = recommendation_results.rename(columns={
        'title': 'Movie Title',
        'release_date': 'Release Date',
        'vote_average': 'Average Vote',
        'overview': 'Overview',
        'runtime': 'Runtime (mins)'
    })
    st.table(renamed_recommendation_results.set_index('Movie Title')) 


def display_guide_header():
    col1, col2 = st.columns([5,1])
    with col1:
        colored_header(label="Movie Recommendation Guide",
                   description="",
                   color_name="yellow-80" )
    with col2:
        guide_option = st.button("Use chatbot instead...")
        if (guide_option):
            switch_page("Chatbot")
    
    st.markdown('''
                Explore movies collected from 
                [The Movie Database (TMDB)](https://www.themoviedb.org/). 
                Users can search for specific movie titles 
                or choose from a selection of genres, languages or movie plots 
                to get recommendations.
                ''')
        
    


