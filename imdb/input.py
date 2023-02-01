actors_list = [
    {
        "actor_id": "actor_1",
        "name": "Actor 1"
    }, {
        "actor_id": "actor_2",
        "name": "Actor 2"
    }, {
        "actor_id": "actor_3",
        "name": "Actor 3"
    }, {
        "actor_id": "actor_4",
        "name": "Actor 4"
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
                "role": "Father",
                "is_debut_movie": False
            }
        ],
        "box_office_collection_in_crores": "120.3",
        "release_date": "2022-3-3",
        "director_name": "Director 3"
    },
    {
        "movie_id": "movie_2",
        "name": "Movie 2",
        "actors": [
            {
                "actor_id": "actor_1",
                "role": "hero",
                "is_debut_movie": False
            }, {
                "actor_id": "actor_2",
                "role": "Father",
                "is_debut_movie": False
            }, {
                "actor_id": "actor_4",
                "role": "Comedian",
                "is_debut_movie": False
            }
        ],
        "box_office_collection_in_crores": "220.3",
        "release_date": "2019-3-3",
        "director_name": "Director 2"
    },
    {
        "movie_id": "movie_3",
        "name": "Movie 3",
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
                "actor_id": "actor_3",
                "role": "Heroine",
                "is_debut_movie": False
            }
        ],
        "box_office_collection_in_crores": "250.3",
        "release_date": "2022-6-3",
        "director_name": "Director 3"
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
    },
    {
        "movie_id": "movie_2",
        "rating_one_count": 4,
        "rating_two_count": 5,
        "rating_three_count": 9,
        "rating_four_count": 4,
        "rating_five_count": 4
    },
    {
        "movie_id": "movie_3",
        "rating_one_count": 4,
        "rating_two_count": 4,
        "rating_three_count": 41,
        "rating_four_count": 4,
        "rating_five_count": 4
    }
]
