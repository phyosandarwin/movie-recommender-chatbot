import streamlit as st
import os
from components.data_handler import load_movie_data
from components.ui_components import display_guide_header, display_search_results, display_recommendations
from components.recommend_engine import search_movie, recommend_genre, recommend_language, recommend_similar_movie

st.set_page_config(page_title='Movie Recommendation Guide', layout='wide', page_icon="📃")
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"]{
    background-image: url("https://static.storyweaver.org.in/illustrations/58827/search/14.jpg");
    background-size: cover;
    background-color: rgba(0, 0, 0, 0.4);
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)


# load pickle files
data_folder = os.path.join(os.getcwd(), 'data', 'pkl_files')
movie_search_data = load_movie_data(os.path.join(data_folder, "movie_search_data.pkl"))
movie_genre_data = load_movie_data(os.path.join(data_folder, "movie_genre_data.pkl"))
movie_lang_data = load_movie_data(os.path.join(data_folder, "movie_lang_data.pkl"))
movie_overview_data = load_movie_data(os.path.join(data_folder, "movie_overview_data.pkl"))

# to be used for finding movies with similar plots
movie_list = sorted(movie_overview_data['title'].tolist())


def guide_page():

    display_guide_header()

    user_choice = st.selectbox("What would you like to do?", ("Search Movie Title", "Get Recommendations"))

    if user_choice == "Search Movie Title":
        with st.expander("Search Movie Title", expanded=True):
            movie_title = st.text_input("Enter the movie title:")
            if st.button("Search"):
                search_results = search_movie(movie_title)
                display_search_results(search_results)
    else:
        with st.expander("Get Recommendations",expanded=True):
            st.subheader("Movie Recommendations")
            recommendation_choice = st.radio("How do you wish to be recommended movies?", ("Genre", "Language", "Similar Plot"))

            if recommendation_choice == 'Genre':
                selected_genre = st.selectbox("Pick your genre:", genre_options)
                if st.button("Recommend"):
                    recommendation_results = recommend_genre(selected_genre)
                    display_recommendations(recommendation_results, selected_genre)

            elif recommendation_choice == 'Language':
                selected_language = st.selectbox("Pick your language:", language_list)
                if st.button("Recommend"):
                    recommendation_results = recommend_language(selected_language)
                    display_recommendations(recommendation_results, selected_language)

            elif recommendation_choice == 'Similar Plot':
                selected_movie = st.selectbox("Pick your movie (list is sorted in alphabetical order):", movie_list)
                if st.button("Recommend"):
                    recommendation_results = recommend_similar_movie(selected_movie)
                    display_recommendations(recommendation_results, "movies with similar plots")

# selection options for genre and language
genre_options = ['Action', 'Adventure','Animation', 'Comedy',  'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 
                 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War',
                 'Western']

language_list = ['English', 'French', 'Dutch', 'Spanish', 'Korean', 'Japanese',
       'Finnish', 'Ukrainian', 'Norwegian', 'Estonian', 'Cantonese',
       'Polish', 'Russian', 'German', 'Chinese', 'Italian', 'Basque',
       'Thai', 'Turkish', 'Swedish', 'Icelandic', 'Tagalog', 'Arabic',
       'Tamil', 'Telugu', 'Romanian', 'Indonesian', 'Galician', 'Danish',
       'Macedonian', 'Portuguese', 'Vietnamese', 'Catalan', 'Hindi',
       'Persian', 'Hebrew', 'Serbian', 'Malayalam', 'Greek', 'Hungarian',
       'Czech', 'Norwegian Bokmal', 'Kannada', 'Irish', 'Khmer',
       'Dzongkha', 'Panjabi']



#-----run guide page--------
if __name__ == "__main__":
    guide_page()
