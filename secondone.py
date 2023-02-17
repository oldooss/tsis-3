

movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# #1
#
def imdbOfMovies(movies):
    for i in range(0, len(movies)):
        current_mov = movies[7]
        if current_mov['imdb'] > 5.5:
            return True
        else:
            return False

print(imdbOfMovies(movies))

#2
#
def sublistMoviesHighScore(movies):
    out_list=[];
    for i in range(0,len(movies)):
        curren_mov=movies[i];
        if curren_mov['imdb']>5.5:
            out_list.append(curren_mov)
    return out_list

print(sublistMoviesHighScore(movies))
#
# #3

def returnMovieCategory(movies, cate_name):
    out_list=[]
    for i in movies:
        current_cat = i['category']
        if cate_name.lower() == current_cat.lower():
            out_list.append(i)
    return out_list


cat_name = input("name of category movie: ")

print(returnMovieCategory(movies, cat_name))
#
# #4
#
def avgImdbcore(movies):
    avg_score = 0
    total_movies = len(movies)
    for i in movies:
        avg_score = avg_score+i['imdb']
    avg_score = avg_score/total_movies
    return avg_score

print(avgImdbcore(movies))

#5

def avgImdbToCat(movies,cat_name):
    cat_movies = returnMovieCategory(movies,cat_name)
    avg_score = avgImdbcore(cat_movies)
    return avg_score

category_name = input("name of category movie: ")
print(avgImdbToCat(movies, category_name))
