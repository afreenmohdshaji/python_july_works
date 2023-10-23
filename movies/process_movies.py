from json import load

path="C:\\Users\\afisr\\Desktop\\july_pythonworks\\movies\\db.json"

with open(path) as f:
    data=load(f)

# print(len(movie))


all_names=[name.get("Title") for name in data]
# print(all_names)


# printing the name of all directors
all_directors={d.get("Director") for d in data}
all_directors.discard("N\A")
# print(all_directors)


# finding highest imdb rating

filtered_data=[m for m in data if m.get("imdbRating")!="N/A"]
# print(filtered_data)

top_movie=max(filtered_data,key=lambda m:float(m.get("imdbRating")))
# print(top_movie.get("Title"))


# printing all genre of movie

all_genre=set()

for m in data:
    for gn in m.get("Genre").split():
        all_genre.add(gn.rstrip(","))


# print(all_genre)


# for mv in data:
#     if mv.get("Genre").count("Horror")>0:
#         print(mv.get("Title"))

for mv in data:
    R_year=mv.get("Released")
    year=R_year.split(" ")[-1]

    if year.isdigit():
        if int(year)>2014:
            print(mv.get("Title"),mv.get("Released"))

