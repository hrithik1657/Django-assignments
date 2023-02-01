from typing import Any, List, Dict

from imdb_1.models import Actor, Director, Movie, Rating, MovieCast


def profile():
    def decorator(func):
        def handler(*args, **kwargs):
            import line_profiler
            profiler = line_profiler.LineProfiler()
            profiler.enable_by_count()
            profiler.add_function(func)
            result = func(*args, **kwargs)
            profiler.print_stats()
            return result

        handler.__doc__ = func.__doc__
        return handler

    return decorator


def populate_database(actors_list: object, directors_list: object, movies_list: object, movie_rating_list: object) -> None:
    actors_object_list = []
    for actor in actors_list:
        actors_object_list.append(
            Actor(
                name=actor["name"], actor_id=actor["actor_id"], gender=actor["gender"]
            )
        )
    Actor.objects.bulk_create(actors_object_list)

    directors_object_list = []
    for director in directors_list:
        directors_object_list.append(
            Director(director)
        )
    Director.objects.bulk_create(directors_object_list)

    movies_objects_list = []
    for movie in movies_list:
        movies_objects_list.append(
            Movie(
                movie_id=movie["movie_id"], name=movie["name"],
                box_office_collection_in_crores=movie["box_office_collection_in_crores"],
                release_date=movie["release_date"],
                director_id=movie["director_name"]
            )
        )
    Movie.objects.bulk_create(movies_objects_list)

    moviecast_objects_list = []
    for movie in movies_list:
        movie_id = movie["movie_id"]
        for cast in movie["actors"]:
            moviecast_objects_list.append(
                MovieCast(
                    movie_id=movie_id, actor_id=cast["actor_id"], role=cast["role"],
                    is_debut_movie=cast["is_debut_movie"]
                )
            )
    MovieCast.objects.bulk_create(moviecast_objects_list)

    movie_rating_object_list = []
    for rating in movie_rating_list:
        movie_rating_object_list.append(
            Rating(
                movie_id=rating["movie_id"],
                rating_one_count=rating["rating_one_count"],
                rating_two_count=rating["rating_two_count"],
                rating_three_count=rating["rating_three_count"],
                rating_four_count=rating["rating_four_count"],
                rating_five_count=rating["rating_five_count"]
            )
        )
    Rating.objects.bulk_create(movie_rating_object_list)


# Task 2
@profile()
def remove_all_actors_from_given_movie(movie_object: object) -> None:
    movie = Movie.objects.prefetch_related('actors').get(movie_id=movie_object.movie_id)
    m = movie.actors
    m.clear()


# Task 3
@profile()
def get_all_rating_objects_for_given_movies(movie_objs: object) -> list[object]:
    rating = Rating.objects.filter(movie__in=movie_objs)
    return list(rating)


# Task 4

def get_total_number_of_rating_count(rating: object) -> int:
    total_sum_of_rating = sum([rating.rating_one_count,
                               rating.rating_two_count,
                               rating.rating_three_count,
                               rating.rating_four_count,
                               rating.rating_five_count])

    return total_sum_of_rating


def get_average_rating_of_movie(rating: object) -> float:
    total_sum_of_rating = sum([rating.rating_one_count,
                               rating.rating_two_count * 2,
                               rating.rating_three_count * 3,
                               rating.rating_four_count * 4,
                               rating.rating_five_count * 5])

    total_sum_of_rating_count = get_total_number_of_rating_count(rating)

    if total_sum_of_rating_count == 0:
        return 0
    average = total_sum_of_rating / total_sum_of_rating_count
    return round(average, 2)


def get_cast_list(movie: object, cast_detail_objects: object) -> list[dict[str, dict[str, Any] | Any]]:
    cast_list = []
    for cast_detail in cast_detail_objects:
        if movie == cast_detail.movie:
            actor = {'name': cast_detail.actor.name,
                     'actor_id': cast_detail.actor.actor_id,
                     'gender': cast_detail.actor.gender}
            cast_dict = {'actor': actor,
                         'role': cast_detail.role,
                         'is_debut_movie': cast_detail.is_debut_movie}
            cast_list.append(cast_dict)
    return cast_list


@profile()
def get_movies_by_given_movie_names(movie_names: object) -> list[
    dict[str, list[dict[str, dict[str, Any] | Any]] | float | int | Any]]:
    movies_object = Movie.objects.filter(name__in=movie_names).select_related('rating', 'director')

    cast_detail_objects = MovieCast.objects.filter(movie__in=list(movies_object)).select_related('actor', 'movie', )

    cast_detail_dict = {}
    for movie in list(movies_object):
        cast_list = get_cast_list(movie, cast_detail_objects)
        cast_detail_dict[movie] = cast_list

    movies_detail_list = []
    for movie in list(movies_object):
        movie_dict = {
            "movie_id": movie.movie_id,
            "name": movie.name,
            "cast": cast_detail_dict[movie],
            "box_office_collection_in_crores": movie.box_office_collection_in_crores,
            "release_date": movie.release_date,
            "director_name": movie.director,
            "average_rating": get_average_rating_of_movie(movie.rating),
            "total_number_of_rating": get_total_number_of_rating_count(movie.rating)
        }
        movies_detail_list.append(movie_dict)

    return movies_detail_list


# Task 5
@profile()
def get_all_actor_objects_acted_in_given_movies(movie_objs: object) -> list[Any]:
    movie_id_list = []
    for movie in movie_objs:
        movie_id_list.append(movie.movie_id)
    casts = MovieCast.objects.filter(movie_id__in=movie_id_list).select_related('actor')
    actor_object_list = []
    for cast in casts:
        actor_object_list.append(cast.actor)

    return list(set(actor_object_list))


# Task 6
def get_female_count(movie: object, cast_detail_objects: object) -> int:
    no_of_female_cast = 0
    for cast_detail in cast_detail_objects:
        if cast_detail.actor.gender == 'Female' and movie == cast_detail.movie:
            no_of_female_cast += 1

    return no_of_female_cast


def get_female_cast_list(movie: object, cast_detail_objects: object) -> list[dict[str, dict[str, Any] | Any]]:
    cast_list = []
    for cast_detail in cast_detail_objects:
        if movie == cast_detail.movie and cast_detail.actor.gender == 'Female':
            actor = {'name': cast_detail.actor.name,
                     'actor_id': cast_detail.actor.actor_id
                     }
            cast_dict = {'actor': actor,
                         'role': cast_detail.role,
                         'is_debut_movie': cast_detail.is_debut_movie}
            cast_list.append(cast_dict)

    return cast_list


@profile()
def get_movie_detail_list() -> list[dict[str, list[dict[str, dict[str, Any] | Any]] | int | Any]]:
    movies_object = Movie.objects.select_related('rating', 'director').all()

    cast_detail_objects = MovieCast.objects.filter(movie__in=list(movies_object)).select_related('actor', 'movie', )

    movie_female_count = {}
    cast_detail_dict = {}
    for movie in list(movies_object):
        movie_female_count[movie] = get_female_count(movie, cast_detail_objects)
        cast_detail_dict[movie] = get_female_cast_list(movie, cast_detail_objects)

    movies_detail_list = []
    for movie in list(movies_object):
        movie_dict = {
            "movie_id": movie.movie_id,
            "name": movie.name,
            "cast": cast_detail_dict[movie],
            "no_of_female_cast": movie_female_count[movie],
            "box_office_collection_in_crores": movie.box_office_collection_in_crores,
            "release_date": movie.release_date,
            "director_name": movie.director,
            "rating": movie.rating
        }
        movies_detail_list.append(movie_dict)

    return movies_detail_list


@profile()
def get_female_cast_details_from_movies_having_more_than_five_female_cast() -> list[dict[str, int | float | Any]]:
    movie_detail_list_having_more_than_five_female_cast = []

    movie_detail_list = get_movie_detail_list()
    for movie_detail in movie_detail_list:
        if movie_detail['no_of_female_cast'] >= 5:
            movie_dict_having_more_than_five_female_cast = {"movie_id": movie_detail['movie_id'],
                                                            "name": movie_detail['name'],
                                                            "cast": movie_detail['cast'],
                                                            "box_office_collection_in_crores": movie_detail[
                                                                'box_office_collection_in_crores'],
                                                            "release_date": movie_detail['release_date'],
                                                            "director_name": movie_detail['director_name'],
                                                            "average_rating": get_average_rating_of_movie(
                                                                movie_detail['rating']),
                                                            "total_number_of_rating": get_total_number_of_rating_count(
                                                                movie_detail['rating'])
                                                            }
            movie_detail_list_having_more_than_five_female_cast.append(movie_dict_having_more_than_five_female_cast)

    return movie_detail_list_having_more_than_five_female_cast


# Task 7
def get_casts_detail_list(actor: object, movie: object, casts: object) -> list[dict[str, Any]]:
    casts_detail_list = []
    for cast in casts:
        if cast.actor == actor and cast.movie == movie:
            casts_detail_list.append({"role": cast.role,
                                      "is_debut_movie": cast.is_debut_movie})

    return casts_detail_list


def get_movies_dict(movies: object, actor: object, casts: object) -> dict[Any, list[dict[str, Any]]]:
    movies_dict = {}
    for movie in movies:
        movies_dict[movie] = get_casts_detail_list(actor, movie, casts)

    return movies_dict


def get_movies_detail_list(casts: object, casts_detail_dict: object, actor: object) -> list[
    dict[str, float | int | Any]]:
    movies_detail_list = []
    for cast in casts:
        movies_detail_dict = {}
        if actor == cast.actor:
            movies_detail_dict['movie_id'] = cast.movie.movie_id
            movies_detail_dict['name'] = cast.movie.name
            movies_detail_dict['casts'] = casts_detail_dict[actor][cast.movie]
            movies_detail_dict['box_office_collection_in_crores'] = cast.movie.box_office_collection_in_crores
            movies_detail_dict['release_date'] = cast.movie.release_date
            movies_detail_dict['director'] = cast.movie.director
            movies_detail_dict['rating'] = get_average_rating_of_movie(cast.movie.rating)
            movies_detail_dict["total_number_of_ratings"] = get_total_number_of_rating_count(cast.movie.rating)

            if movies_detail_dict not in movies_detail_list:
                movies_detail_list.append(movies_detail_dict)
    return movies_detail_list


@profile()
def get_actor_movies_released_in_year_greater_than_or_equal_to_2000() -> list[
    dict[str, list[dict[str, float | int | Any]] | Any]]:
    movies = Movie.objects.filter(release_date__year__gte=2000).select_related('director', 'rating')

    casts = MovieCast.objects.filter(movie__in=movies).select_related('movie', 'actor', 'movie__director',
                                                                      'movie__rating')

    actors_list = []
    for cast in casts:
        actors_list.append(cast.actor)

    actors = list(set(actors_list))
    casts_detail_dict = {}

    for actor in actors:
        casts_detail_dict[actor] = get_movies_dict(movies, actor, casts)

    actors_detail_list = []
    for actor in actors:
        actor_detail_dict = {"name": actor.name,
                             "actor_id": actor.actor_id,
                             'movies': get_movies_detail_list(casts, casts_detail_dict, actor)}

        actors_detail_list.append(actor_detail_dict)

    return actors_detail_list


# Task 8
@profile()
def reset_ratings_for_movies_in_given_year(year: object) -> None:
    movies = Movie.objects.filter(release_date__year=year)

    for movie in list(movies):
        rating = Rating.objects.get(movie_id=movie.movie_id)
        rating.rating_one_count = 0
        rating.rating_two_count = 0
        rating.rating_three_count = 0
        rating.rating_four_count = 0
        rating.rating_five_count = 0
        rating.save()
