# Movie Recommender Chatbot 🎬🍿

This is a movie recommendation and chatbot application built with Streamlit. Users can explore movies and get recommendations according to the criteria they select. Users can also navigate to the chatbot which uses the Hugging Face Model to ask related queries on movies, although, the chatbot can provide answers beyond movie knowledge.

## Features

- Search for movies to return exact or similar match
- Get recommendations by genre
- Explore movies by language
- Find similar movies
- Real time interaction with the chatbot

## Process

#### 1) Data cleaning and exploration 🔍 
Refer to [EDA Notebook](https://github.com/phyosandarwin/movie-recommender-chatbot/blob/ac63d1ffb686088c5e438fb80a1f5044efd5e469/notebooks/Movie-Recommendation%20eda.ipynb)

- removed columns irrelevant to me as a general audience
- removed rows that had not been given any votes because it is important for me to know how good a movie is before watching it 🥲
- visualising the distributions of numeric variables (though unnecessary in this project)
- clarified certain ambiguous values in categorical columns

#### 2) Building the movie recommender system and trials with Jupyter Widgets ✍
Refer to [Movie Recommendation System Development Notebook](https://github.com/phyosandarwin/movie-recommender-chatbot/blob/ac63d1ffb686088c5e438fb80a1f5044efd5e469/notebooks/Movie-Recommendation%20system.ipynb)

- Text preprocessing of movie title and overview:
  - `re`, `TfidfVectorizer`, `cosine_similarity`, `fuzz` modules used
- functions coded returns top/ best 10 search results
- used Text, Dropdown Jupyter widgets

#### 3) Exploring Hugging Chat API in Jupyter Notebook 🤗
Refer to [Hugging Chat Chatbot Notebook](https://github.com/phyosandarwin/movie-recommender-chatbot/blob/ac63d1ffb686088c5e438fb80a1f5044efd5e469/notebooks/Hugchat_Chatbot_(New_Feature).ipynb)

#### 4) Using Streamlit Frontend to build the Recommendation Guide Page and Chatbot Page 
View the webpage [here](https://movie-recommender-chatbot.streamlit.app/)!


## Getting Started

1. Clone this repository.
2. Install the required dependencies.
3. Run the Streamlit app.

## Usage

Run the Streamlit app using the following command:

```bash
streamlit run Home.py
```

## Future enhancements
- create a multi-options filtering system for recommendations section
- incorporate collaborative filtering to get movies recommended by other users who watch similar content
- use TMDB API to grab movie posters that will help users to visually reference to the recommended movies lest they want to search it up in a movie streaming website

## Acknowledgements
* Concepts of the project (including use of Jupyter widgets): [Movie Recommendation Project BY @DATAQUEST](https://youtu.be/eyEabQRBMQA)
* Use of Streamlit components and app deployment Youtube tutorials on [Sven(Coding is Fun)](https://www.youtube.com/@CodingIsFun) and [Misra Turp](https://www.youtube.com/@misraturp)
* Use of Hugging Chat API : [@Data Professor Youtube Video](https://www.youtube.com/watch?v=T_iE6TT7pS8) and his [repository](https://github.com/dataprofessor/hugchat)
