# Jonathan Lee
# Purpose: Pet Chooser Assignment


import pymysql.cursors
# Import mysql database credentials
from creds import *
# Import Pets class
from pet_class import Pet

print("*****Welcome to the Pet Chooser Program*****")
print()
input("Press [Enter] to begin:")

# Establish a connection to the MySQL database.
def connect_to_database():
    try:
        connection = pymysql.connect(host=hostname,
                                     user=username,
                                     password=password,
                                     db=database,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        return connection
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
        exit()


def retrieve_pet_info(connection):
# Fetch pets list from the database and return a list of Pet objects.
    query = """
    SELECT
        pets.name,
        pets.age,
        owners.name as 'owner_name',
        types.animal_type
    FROM pets
    JOIN owners
        ON pets.owner_id = owners.id
    JOIN types
        ON pets.animal_type_id = types.id;
    """

    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()

    pets = []
    for row in rows:
        pet = Pet(row['name'], row['age'], row['owner_name'], row['animal_type'])
        pets.append(pet)

    return pets

# Display the pet name list.
def display_pets(pets):

    input("\nPlease choose a pet from the list below:")
    print()
    for idx, pet in enumerate(pets, 1):
        print(f"[{idx}] {pet.name}")
    print("or type [Q] to Quit")


def get_user_choice(pets):
# Get pet selection and handle user input.
    while True:
        choice = input("\nChoice: ").strip()

        if choice.lower() == 'q': # code for quitting pet chooser.
            print("Thank you for using Pet Chooser. Have a nice day!")
            print()
            exit()

        try:
            choice = int(choice)
            if 1 <= choice <= len(pets):
                return choice - 1
            else:
                print("Invalid choice. Please choose a valid number from the pet list.")

        except ValueError:
            print("Invalid input. Please enter a number or type 'Q' to quit.")

# Main function loop
def main():
    connection = connect_to_database()

    while True:
        pets = retrieve_pet_info(connection)  # Get pets from the database
        display_pets(pets)  # Display pets

        choice = get_user_choice(pets)  # Get user choice
        chosen_pet = pets[choice]  # Get chosen pet

        print(f"\nCongratulations! You have selected {chosen_pet}.")

# Continue or quit option
        while True:
            input_prompt = input("\nPress [ENTER] to continue or [Q] to quit: ")
            if input_prompt == "":
                break  # Exit loop
            elif input_prompt.lower() == "q":
                print("Thanks for using Pet Chooser. Goodbye!")
                exit()  # Exit program
            else:
                print("")


if __name__ == "__main__":
    main()