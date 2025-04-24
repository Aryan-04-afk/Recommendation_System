def recommend_movies(user_id, data, P_like, P_dislike, feature_probs, top_n=5):
    user_data = data[data['userId'] == user_id]
    seen_movies = set(user_data['movieId'])

    all_movies = data[['movieId', 'title'] + genre_cols + ['occupation']].drop_duplicates('movieId')
    user_occ = user_data['occupation'].iloc[0]
    all_movies['occupation'] = user_occ  

    recs = []
    for _, row in all_movies.iterrows():
        if row['movieId'] in seen_movies:
            continue

        features = {col: row[col] for col in genre_cols + ['occupation']}
        pred = predict(features, P_like, P_dislike, feature_probs)
        if pred == 1:
            recs.append(row['title'])

    return recs[:top_n]
