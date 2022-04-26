"""
main menu program.
"""

import parking_garage

spaceship = r"""
                        __,' __`.                _..----....____
        __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
  _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'
,'________________                          \`-._`-','
 `._              ```````````------...___   '-.._'-:
    ```--.._      ,.                     ````--...__\-.
            `.--. `-`                       ____    |  |`
              `. `.                       ,'`````.  ;  ;`
                `._`.        __________   `.      \'__/`
                   `-:._____/______/___/____`.     \  `
                               |       `._    `.    \
                               `._________`-.   `.   `.___
                                               `------'`
"""

def main_menu():
    """
    main menu
    """
    while True:
        parking_garage.clear()
        print(spaceship)
        print("Space parking system 2000")
        print("\n1. Sign in your spaceship")
        print("\n2. Sign out your spaceship")
        print("\n3. Show all available spaces")
        print("\n4. Exit application")

        choice = (input("Enter your choice..."))
        if choice == "1":
            parking_garage.add_spaceship()
        if choice == "2":
            parking_garage.remove_spaceship()
        if choice == "3":
            parking_garage.garage_status()
        if choice == "4":
            exit()


if __name__ == "__main__":
    main_menu()
