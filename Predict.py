import numpy as np

def predict(movie_features, P_like, P_dislike, feature_probs):
    prob_like = np.log(P_like)
    prob_dislike = np.log(P_dislike)

    for col, value in movie_features.items():
        prob_like += np.log(feature_probs['like'][col].get(value, 1e-6))
        prob_dislike += np.log(feature_probs['dislike'][col].get(value, 1e-6))

    return 1 if prob_like > prob_dislike else 0
