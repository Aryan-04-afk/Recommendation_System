from collections import defaultdict

# Choose features (e.g., genres and occupation)
genre_cols = [f'genre_{i}' for i in range(19)]

def train_naive_bayes(data):
    # Prior probabilities
    like_data = data[data['like'] == 1]
    dislike_data = data[data['like'] == 0]
    total = len(data)
    
    P_like = len(like_data) / total
    P_dislike = len(dislike_data) / total

    feature_probs = {'like': defaultdict(dict), 'dislike': defaultdict(dict)}

    for col in genre_cols + ['occupation']:
        for value in data[col].unique():
            
            num_like = len(like_data[like_data[col] == value])
            feature_probs['like'][col][value] = laplace_smoothing(num_like, len(like_data))
            
            
            num_dislike = len(dislike_data[dislike_data[col] == value])
            feature_probs['dislike'][col][value] = laplace_smoothing(num_dislike, len(dislike_data))

    return P_like, P_dislike, feature_probs
