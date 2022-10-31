from init_db import initialize_db
from users import *
import random


def main():
    initialize_db()

    def generate_users():
        """Generate random users for database
        """
        min_user_id = 1
        max_user_id = 400000000
        min_lvl = 1
        max_lvl = 6
        number_of_users = 200

        [add_new_user(random.randint(min_user_id,max_user_id),\
            random.randint(min_lvl, max_lvl))\
                for x in range(number_of_users)]

    generate_users()

if __name__ == '__main__':
    main()
    