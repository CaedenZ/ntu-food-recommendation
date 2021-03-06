# A program coded in Python that can recommend a canteen in NTU for the user to have a meal based on user’s position
# and input. The basic function of a F&B recommendation system is that the user can get a recommendation based on
# his/her inquiry such as using the following three steps:
# [i.] The user is asked to enter his/her location on NTU campus.
# [ii.] The user is asked to enter his inquiry criteria.
# [iii.] The recommendation information displayed.

# Made by Gupta Jay, Xavier Ho, Iyer Rajagopal Mahadevan
# Mini Project
# Introduction to Computational Thinking (CZ1003)
# School of Computer Science and Engineering
# Nanyang Technological University


# MASTER LIST OF ALL FOOD PREFERENCES (Xavier Ho & Gupta Jay)
def food_preferences():
    all_preferences = {'Dietary Preference': ['Vegetarian', 'Halal', 'Non-Halal'],
                       'Cuisine': ['Malay', 'Vegetarian', 'Indian', 'Chinese', 'Western', 'Italian', 'Korean',
                                   'Japanese', 'Vietnamese', 'Fast Food'],
                       'Price': ['$2-$5', '$5-$8', '$8-$12']
                    }
    return all_preferences


# MASTER CANTEEN DATABASE (Gupta Jay, Xavier Ho & Iyer Rajagopal Mahadevan)
def candict():
    canteen_dict = {1: {'Name': 'Canteen 1',
                        'x-coordinate': 429,
                        'y-coordinate': 428,
                        'Distance from user': 0.00,
                        'Dietary Preference': ['Halal', 'Vegetarian', 'Non-Halal'],
                        'Cuisine': ['Vegetarian', 'Indian', 'Chinese', 'Western', 'Fast Food'],
                        'Price': ['$2-$5', '$5-$8'],
                        'Timing': ['7', '24']},

                    2: {'Name': 'Canteen 2',
                        'x-coordinate': 463,
                        'y-coordinate': 370,
                        'Distance from user': 0.00,
                        'Dietary Preference': ['Halal', 'Non-Halal'],
                        'Cuisine': ['Malay', 'Chinese', 'Western', 'Japanese', 'Korean'],
                        'Price': ['$2-$5', '$5-$8', '$8-$12'],
                        'Timing': ['7', '24']},

                    3: {'Name': 'Canteen 9',
                        'x-coordinate': 574,
                        'y-coordinate': 260,
                        'Distance from user': 0.00,
                        'Dietary Preference': ['Vegetarian', 'Halal', 'Non-Halal'],
                        'Cuisine': ['Malay', 'Chinese', 'Western', 'Fast Food'],
                        'Price': ['$2-$5'],
                        'Timing': ['7', '24']},

                    4: {'Name': 'Canteen 11',
                        'x-coordinate': 669,
                        'y-coordinate': 220,
                        'Distance from user': 0.00,
                        'Dietary Preference': ['Vegetarian', 'Non-Halal'],
                        'Cuisine': ['Malay', 'Chinese', 'Western', 'Indian'],
                        'Price': ['$5-$8'],
                        'Timing': ['7', '21']},

                    5: {'Name': 'Canteen 13',
                        'x-coordinate': 431,
                        'y-coordinate': 160,
                        'Distance from user': 0.00,
                        'Dietary Preference': ['Vegetarian', 'Halal', 'Non-Halal'],
                        'Cuisine': ['Malay', 'Chinese', 'Western'],
                        'Price': ['$2-$5', '$5-$8'],
                        'Timing': ['7', '21']},

                    6: {'Name': 'Canteen 14',
                        'x-coordinate': 497,
                        'y-coordinate': 162,
                        'Distance from user': 0.00,
                        'Dietary Preference': ['Vegetarian', 'Non-Halal'],
                        'Cuisine': ['Malay', 'Chinese', 'Western', 'Fast Food', 'Korean'],
                        'Price': ['$5-$8'],
                        'Timing': ['7', '21']},

                    7: {'Name': 'Canteen 16',
                        'x-coordinate': 393,
                        'y-coordinate': 200,
                        'Distance from user': 0.00,
                        'Dietary Preference': ['Vegetarian', 'Halal', 'Non-Halal'],
                        'Cuisine': ['Malay', 'Chinese', 'Western', 'Indian'],
                        'Price': ['$5-$8'],
                        'Timing': ['7', '21']},

                    8: {'Name': 'Ananda Kitchen',
                        'x-coordinate': 682,
                        'y-coordinate': 277,
                        'Distance from user': 0.00,
                        'Dietary Preference': ['Non-Halal'],
                        'Cuisine': ['Indian'],
                        'Price': ['$5-$8', '$8-$12'],
                        'Timing': ['12', '22']},

                    9: {'Name': 'Foodgle Food Court',
                        'x-coordinate': 616,
                        'y-coordinate': 178,
                        'Distance from user': 0.00,
                        'Dietary Preference': ['Halal', 'Non-Halal'],
                        'Cuisine': ['Malay', 'Chinese', 'Western'],
                        'Price': ['$5-$8'],
                        'Timing': ['7', '21']},

                    10: {'Name': 'North Hill Food Court',
                         'x-coordinate': 703,
                         'y-coordinate': 298,
                         'Distance from user': 0.00,
                         'Dietary Preference': ['Vegetarian', 'Halal', 'Non-Halal'],
                         'Cuisine': ['Malay', 'Chinese', 'Western'],
                         'Price': ['$5-$8'],
                         'Timing': ['7', '21']},

                    11: {'Name': 'Pioneer Food Court',
                         'x-coordinate': 484,
                         'y-coordinate': 509,
                         'Distance from user': 0.00,
                         'Dietary Preference': ['Vegetarian', 'Halal', 'Non-Halal'],
                         'Cuisine': ['Malay', 'Chinese', 'Western'],
                         'Price': ['$5-$8'],
                         'Timing': ['7', '21']},

                    12: {'Name': 'Quad Cafe',
                         'x-coordinate': 197,
                         'y-coordinate': 306,
                         'Distance from user': 0.00,
                         'Dietary Preference': ['Halal', 'Non-Halal'],
                         'Cuisine': ['Malay', 'Chinese', 'Western', 'Korean', 'Indian'],
                         'Price': ['$5-$8'],
                         'Timing': ['7', '15']},

                    13: {'Name': 'North Spine',
                         'x-coordinate': 263,
                         'y-coordinate': 266,
                         'Distance from user': 0.00,
                         'Dietary Preference': ['Vegetarian', 'Halal', 'Non-Halal'],
                         'Cuisine': ['Malay', 'Chinese', 'Western', 'Indian', 'Italian', 'Korean', 'Fast Food',
                                     'Vietnamese'],
                         'Price': ['$5-$8'],
                         'Timing': ['7', '21']},

                    14: {'Name': 'Koufu',
                         'x-coordinate': 213,
                         'y-coordinate': 449,
                         'Distance from user': 0.00,
                         'Dietary Preference': ['Vegetarian','Halal', 'Non-Halal'],
                         'Cuisine': ['Malay', 'Chinese', 'Western', 'Japanese', 'Italian', 'Indian'],
                         'Price': ['$5-$8'],
                         'Timing': ['7', '21']},

                    15: {'Name': 'NIE Canteen',
                         'x-coordinate': 254,
                         'y-coordinate': 156,
                         'Distance from user': 0.00,
                         'Dietary Preference': ['Halal', 'Non-Halal'],
                         'Cuisine': ['Malay', 'Chinese', 'Western'],
                         'Price': ['$2-$5', '$5-$8'],
                         'Timing': ['7', '21']},

                    16: {'Name': 'Canteen 4',
                         'x-coordinate': 345,
                         'y-coordinate': 479,
                         'Distance from user': 0.00,
                         'Dietary Preference': ['Halal', 'Non-Halal'],
                         'Cuisine': ['Malay', 'Chinese', 'Western', 'Japanese', 'Korean', 'Italian'],
                         'Price': ['$2-$5', '$5-$8'],
                         'Timing': ['7', '21']}
                    }

    return canteen_dict
