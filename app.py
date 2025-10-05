# 🎬 Movie Recommender System (Streamlit Cloud Safe Version)
# ---------------------------------------------------------

import pickle
import streamlit as st
import requests
import os
import gdown

# TMDB API key 
API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

# ------------------- Google Drive Settings -------------------
SIMILARITY_FILE_ID = "1Bpz4Vive2zhDYKgbmdJuzigcwADcM-o-"
SIMILARITY_FILE = "similarity.pkl"

# ------------------- Download similarity.pkl from Google Drive -------------------
def download_similarity(file_id=SIMILARITY_FILE_ID, file_path=SIMILARITY_FILE):
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    if not os.path.exists(file_path):
        with st.spinner("📥 Downloading similarity.pkl from Google Drive..."):
            response = requests.get(url)
            # Check if the response is actual pickle data
            if response.status_code == 200 and b'html' not in response.content[:200].lower():
                with open(file_path, "wb") as f:
                    f.write(response.content)
                st.success("✅ similarity.pkl downloaded successfully!")
            else:
                st.error("❌ Failed to download similarity.pkl. Make sure the file is public on Google Drive and link is correct.")

download_similarity()

# ------------------- Functions -------------------
@st.cache_data(show_spinner=False)
def fetch_movie_details(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        data = requests.get(url).json()

        poster_path = data.get('poster_path', '')
        full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else ""
        title = data.get('title', 'N/A')
        rating = data.get('vote_average', 'N/A')
        overview = data.get('overview', 'N/A')
        genres = ', '.join([genre['name'] for genre in data.get('genres', [])])

        return {
            'poster': full_path,
            'title': title,
            'rating': rating,
            'overview': overview,
            'genres': genres
        }
    except:
        return {'poster': '', 'title': 'Error', 'rating': '-', 'overview': 'Could not fetch data.', 'genres': '-'}


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        details = fetch_movie_details(movie_id)
        recommended_movies.append(details)
    return recommended_movies

# ------------------- Streamlit UI -------------------
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")
st.title("🎬 Movie Recommender System")

# Load movie data and similarity matrix
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open(SIMILARITY_FILE, 'rb'))

# Movie dropdown
selected_movie = st.selectbox("🎥 Type or select a movie", movies['title'].values)

# Show recommendations
if st.button("🔍 Show Recommendation"):
    recommended_movies = recommend(selected_movie)
    st.subheader(f"🎯 Top 5 recommendations for: {selected_movie}")
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.image(recommended_movies[idx]['poster'])
            st.markdown(f"**{recommended_movies[idx]['title']}**")
            st.markdown(f"⭐ *Rating:* {recommended_movies[idx]['rating']}")
            st.markdown(f"🎬 *Genre:* {recommended_movies[idx]['genres']}")
            st.markdown(f"📝 *Overview:* {recommended_movies[idx]['overview'][:150]}...")
