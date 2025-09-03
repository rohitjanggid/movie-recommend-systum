# 🎬 Movie Recommender System

A powerful and visually appealing **content-based movie recommender system** that suggests similar movies based on text features like genres, overview, and title. Built using Python, Scikit-learn, and Streamlit, and enhanced with real-time movie data using the TMDB API.

---

## 🔍 Project Overview

This project demonstrates a content-based filtering recommender system that:
- Recommends 5 similar movies based on your input
- Fetches real-time posters, ratings, genres, and overviews from TMDB API
- Uses TF-IDF vectorization and cosine similarity for calculating similarity between movies
- Displays results using an interactive and responsive Streamlit interface

---

## 🚀 Features

✅ Recommend top 5 similar movies
✅ Show poster, title, rating, genre, and overview
✅ Clean UI using Streamlit columns
✅ TMDB API for real-time movie data
✅ Machine Learning pipeline built using TF-IDF + cosine similarity

---

## 💡 Machine Learning Approach

- **Model Type:** Content-Based Filtering
- **Vectorization:** CountVectorizer
- **Similarity Metric:** Cosine Similarity
- **Tools:** Scikit-learn, Pandas, NumPy
- **Data:** MovieLens (with TMDB metadata enrichment)

---

## 🧱 Project Structure

```
movies-recommender-system/
├── app.py                         # Streamlit frontend
├── model/
│   ├── movie_list.pkl            # Movie title and ID data
│   └── similarity.pkl            # Cosine similarity matrix
├── movies-recommender-system.ipynb # ML pipeline notebook
├── requirements.txt             # Required dependencies
└── README.md                    # Project documentation
```

---


## ⚙️ How to Run This Project

### 🔧 Step 1: Clone the repository
```bash
git clone https://github.com/your-username/movies-recommender-system.git
cd movies-recommender-system
```

### 📦 Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### ▶ Step 3: Run the app
```bash
streamlit run app.py
```

---

## 📎 Sample Output

When you enter a movie like `The Dark Knight`, it shows:
- 🎥 Poster of 5 similar movies
- ⭐ Their rating
- 🎬 Their genre
- 📄 Short overview (plot summary)

---

## 📚 Skills Demonstrated

- ✅ Machine Learning: TF-IDF + cosine similarity
- ✅ Python and Data Preprocessing
- ✅ Streamlit Web App Development
- ✅ API Integration (TMDB)
- ✅ Model Saving and Loading using Pickle

---

## 👨‍💻 Author

**Rohit Khati**  
BCA Student | Machine Learning Learner | Python Developer  
📫 Connect on:-\
[GitHub](https://github.com/rohitjanggid)\
[Linkedin](https://www.linkedin.com/in/rohit-jangid-a185a7372)\
[Twitter](https://x.com/rohit_janggid)

---

## ⭐ Like This Project?

Give a ⭐ on GitHub and feel free to fork and try it yourself!
