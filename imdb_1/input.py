actors_list = [
    {
        "actor_id": "actor_1",
        "name": "Actor 1",
        "gender": "Male"
    }, {
        "actor_id": "actor_2",
        "name": "Actor 2",
        "gender": "Male"
    }, {
        "actor_id": "actor_3",
        "name": "Actor 3",
        "gender": "Female"
    }, {
        "actor_id": "actor_4",
        "name": "Actor 4",
        "gender": "Female"
    }
]

movies_list = [
    {
        "movie_id": "movie_1",
        "name": "Movie 1",
        "actors": [
            {
                "actor_id": "actor_1",
                "role": "hero",
                "is_debut_movie": False
            }, {
                "actor_id": "actor_2",
                "role": "Villain",
                "is_debut_movie": True
            }, {
                "actor_id": "actor_4",
                "role": "Mother",
                "is_debut_movie": False
            }
        ],
        "box_office_collection_in_crores": "120.3",
        "release_date": "2022-3-3",
        "director_name": "Director 3"
    }, {
        "movie_id": "movie_2",
        "name": "Movie 2",
        "actors": [
            {
                "actor_id": "actor_2",
                "role": "hero",
                "is_debut_movie": True
            }, {
                "actor_id": "actor_1",
                "role": "Father",
                "is_debut_movie": False
            }, {
                "actor_id": "actor_4",
                "role": "grand mother",
                "is_debut_movie": False
            }
        ],
        "box_office_collection_in_crores": "200.3",
        "release_date": "2019-3-3",
        "director_name": "Director 1"
    }, {
        "movie_id": "movie_3",
        "name": "Movie 3",
        "actors": [
            {
                "actor_id": "actor_1",
                "role": "hero",
                "is_debut_movie": False
            }, {
                "actor_id": "actor_3",
                "role": "heroine",
                "is_debut_movie": True
            }
        ],
        "box_office_collection_in_crores": "150.5",
        "release_date": "2022-9-3",
        "director_name": "Director 2"
    }
]

directors_list = [
    "Director 1", "Director 2", "Director 3"
]

movie_rating_list = [
    {
        "movie_id": "movie_1",
        "rating_one_count": 4,
        "rating_two_count": 4,
        "rating_three_count": 4,
        "rating_four_count": 4,
        "rating_five_count": 4
    }, {
        "movie_id": "movie_2",
        "rating_one_count": 4,
        "rating_two_count": 5,
        "rating_three_count": 3,
        "rating_four_count": 5,
        "rating_five_count": 4
    }, {
        "movie_id": "movie_3",
        "rating_one_count": 4,
        "rating_two_count": 2,
        "rating_three_count": 3,
        "rating_four_count": 4,
        "rating_five_count": 4
    }
]
