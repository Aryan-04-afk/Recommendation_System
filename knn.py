import pandas as pd

import math
from collections import defaultdict,Counter


ratings=pd.read_csv('ratings.csv',names=['user_id','movie_id','rating','timestamp'])

user_ratings={}

for row in ratings.itertuples(index=False):
     user=int(row.user_id)
     movie=int(row.movie_id)
     ratings=float(row.rating)
     if user not in user_ratings:
          user_ratings[user]={}
     
     user_ratings[user][movie] = rating



def euclidian_distance(user_1,user_2):
     """Compute Euclidean distance between two users based on common rated movies."""
     common_movies=set(user_ratings[user_1])& set(user_ratings[user_2])

     if not common_movies:
          return('inf')
     

     squared_sum =0

     for movie in common_movies:
          diff=user_ratings[user_1][movie]-user_ratings[user_2][movie]
          squared_sum+=diff*diff
     
     return squared_sum**0.5


def get_k():
     n_user=ratings['user_id'].nunique
     
     k=int(round(math.sqrt(n_user/2)))

     if k%2==0:
          k+=1
     if k<1:
          k=1
     

     return k


k=get_k()


def get_k_neighbours(target_userId,k):

     distances=[]

     neighbours=[]

     for other_user in user_ratings:
          if other_user==target_userId:
               continue

          dist=euclidian_distance(target_userId,other_user)

          distances.append((dist,other_user))
          
          distances.sort()

     for i in range((min(k,len(distances)))):
          neighbours.append(distances[i][1])
      
     return neighbours



def knn_recommend(target_user_id,k):

     neighbours=get_k_neighbours(target_user_id,k)

     user_seen=set(user_ratings[target_user_id])

     
     candidate_movies=set()
     for neigbour in neighbours:
          neigbour_movies=set(user_ratings[neigbour])
          candidate_movies.update(neigbour_movies-user_seen)
     
     scores=[]
     
     for movie in candidate_movies:
          ratings_list=[]
          for neighbour in neighbours:
               if movie in user_ratings[neigbour]:
                    ratings_list.append(user_ratings[neigbour][movie])
          
          if ratings_list:
               avg_rating=sum(ratings_list) / len(ratings_list)
               scores.append((avg_rating, movie))
          
               scores.sort(reverse=True)

     return scores[:10]




if __name__ == "__main__":
    user_id = int(input("Enter user ID: "))
    recs = knn_recommend(user_id, k)
    print("\nTop recommendations:")
    for avg_rating, movie_id in recs:
        print(f"Movie ID: {movie_id} - Predicted rating: {avg_rating:.2f}")









     
          









