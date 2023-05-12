import pickle
import streamlit as st
import pandas as pd


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_lst = sorted(list(enumerate(distances)), reverse=True, key = lambda x:x[1])[1:6]
    recommended_movies = []
    for i in movies_lst:
        movie_id = movies.iloc[i[0]]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_lst = pickle.load(open('movie_list.pkl', 'rb'))
movies = pd.DataFrame(movies_lst)

st.title('Movie Recommender')

selected_movie_name = st.selectbox("What you want to watch?", movies['title'].values)


if st.button("Recommend"):
    recommended_movie_names = recommend(selected_movie_name)
    for i in recommended_movie_names:
        st.write(i)