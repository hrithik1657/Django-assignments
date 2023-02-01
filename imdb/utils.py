from typing import Any

from imdb.models import Actor, Director, Movie, Rating, MovieCast


def populate_database(actors_list: object, directors_list: object, movies_list: object,
                      movie_rating_list: object) -> None:
    actors__list = []
    for actor in actors_list:
        actors__list.append(Actor(name=actor["name"], actor_id=actor["actor_id"]))
    Actor.objects.bulk_create(actors__list)

    director_obj_list = []
    for director in directors_list:
        director_obj_list.append(Director(name=director))

    Director.objects.bulk_create(director_obj_list)

    movies__list = []
    for movie in movies_list:
        movies__list.append(Movie(movie_id=movie["movie_id"],
                                  name=movie["name"],
                                  box_office_collection_in_crores=movie["box_office_collection_in_crores"],
                                  release_date=movie["release_date"],
                                  director_id=movie["director_name"]
                                  )
                            )
    Movie.objects.bulk_create(movies__list)

    casts__list = []
    for movie in movies_list:
        movie_id = movie['movie_id']
        for cast in movie['actors']:
            casts__list.append(MovieCast(movie_id=movie_id,
                                         role=cast['role'],
                                         is_debut_movie=cast['is_debut_movie'],
                                         actor_id=cast['actor_id'])
                               )
    MovieCast.objects.bulk_create(casts__list)

    movie_rating_object_list = []
    for rating in movie_rating_list:
        movie_rating_object_list.append(Rating(movie_id=rating["movie_id"],
                                               rating_one_count=rating["rating_one_count"],
                                               rating_two_count=rating["rating_two_count"],
                                               rating_three_count=rating["rating_three_count"],
                                               rating_four_count=rating["rating_four_count"],
                                               rating_five_count=rating["rating_five_count"]
                                               )
                                        )
    Rating.objects.bulk_create(movie_rating_object_list)


def get_no_of_distinct_movies_actor_acted(actor_id: object) -> object:
    movies = Movie.objects.filter(actors__actor_id=actor_id).distinct()
    return len(list(movies))


def get_movies_directed_by_director(director_obj: object) -> object:
    movies = Movie.objects.filter(director=director_obj.name)
    return list(movies)


def get_average_rating_of_movie(movie_obj: object) -> float | Any:
    rating = Rating.objects.get(movie_id=movie_obj.movie_id)
    avg1 = (rating.rating_one_count +
            rating.rating_two_count * 2 +
            rating.rating_three_count * 3 +
            rating.rating_four_count * 4 +
            rating.rating_five_count * 5)

    avg2 = (rating.rating_one_count +
            rating.rating_two_count +
            rating.rating_three_count +
            rating.rating_four_count +
            rating.rating_five_count)

    avg = avg1 / avg2
    return round(avg, 2)


def delete_movie_rating(movie_obj: object):
    Rating.objects.get(movie_id=movie_obj.movie_id).delete()


def get_all_actor_objects_acted_in_given_movies(movie_objs: object) -> object:
    movie_id_list = []
    for movie_obj in movie_objs:
        movie_id_list.append(movie_obj.movie_id)

    movie_cast_obj = MovieCast.objects.filter(movie_id__in=movie_id_list)
    actor_id_list = []
    for movie_cast in movie_cast_obj:
        actor_id_list.append(movie_cast.actor_id)

    actors = Actor.objects.filter(actor_id__in=actor_id_list)

    return list(actors)


def update_director_for_given_movie(movie_obj: object, director_obj: object):
    movie = Movie.objects.get(movie_id=movie_obj.movie_id)
    movie.director = director_obj
    movie.save()


def get_distinct_movies_acted_by_actor_whose_name_contains_john() -> object:
    movies = Movie.objects.filter(actors__name="john").distinct()
    return list(movies)


def remove_all_actors_from_given_movie(movie_obj: object) -> None:
    movie = Movie.objects.get(movie_id=movie_obj.movie_id)
    movie.actors.clear()


def get_all_rating_objects_for_given_movies(movie_objs: object) -> object:
    movie_id_list = []
    for movie in movie_objs:
        movie_id_list.append(movie.movie_id)
    rating = Rating.objects.filter(movie_id__in=movie_id_list)
    return list(rating)
