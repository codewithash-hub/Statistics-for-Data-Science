import numpy as np

# create a user preferences
user_pref = np.array([5, 1, 3])

# create a random movie matrix of 10,000 movies
movies = np.random.randint(5, size=(3,1000)) + 1

print(user_pref.shape)
print(movies.shape)
print()

rec = np.dot(user_pref, movies)
print(rec)

