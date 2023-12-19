import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")

best_movies_with_tags = soup.findAll(name="h3", class_="listicleItem_listicle-item__title__BfenH")
best_movies = [movie.getText() for movie in best_movies_with_tags]
best_movies.reverse()
print(best_movies)
print(len(best_movies))

with open("movies.txt", mode="w") as file:
    for i in range(len(best_movies)):
        file.write(f"{best_movies[i]}\n")



