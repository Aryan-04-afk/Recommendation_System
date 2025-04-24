import pandas as pd

ratings = pd.read_csv('u.data', sep='\t', names=['userId', 'movieId', 'rating', 'timestamp'])

movies = pd.read_csv('u.item', sep='|', encoding='latin-1', header=None,
                     names=['movieId', 'title', 'release_date', 'video_release_date',
                            'IMDb_URL'] + [f'genre_{i}' for i in range(19)])

users = pd.read_csv('u.user', sep='|', names=['userId', 'age', 'gender', 'occupation', 'zip_code'])


ratings['label'] = ratings['rating'].apply(lambda x: 1 if x >= 4 else 0)
data = ratings.merge(users, on='userId').merge(movies, on='movieId')






