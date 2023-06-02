import argparse

def check_for_boolean_value(val):
    if val == "True":
        return True
    else:
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--age", help="Enter your age (int)", type=int, required=True
    )

    # --age: -- fuer ausgeschriebenen var namen (flag fuer user input)
    # -a: - fuer gekuerzt 
    # help: Hilfe, aufrufbar uber die flag --help
    # type: erlaubter datentyp
    # required: True/False, pflichtwert oder nicht

    parser.add_argument(
        "--name", help="Enter your name (str)", type=str, required=True
    )

    parser.add_argument(
        "--is_admin",
        help="Are you an admin? (bool)",
        type=check_for_boolean_value,
        required=False,
        default=False, # kann entsprechend dem datentyp angegeben werden
    )
    args = parser.parse_args()

    age = args.age
    name = args.name
    is_admin = args.is_admin

    print(age, type(age))
    print(name, type(name))
    print(is_admin, type(is_admin))


if __name__ == "__main__":
    main()


# python .\AdvancedPython_CommandlineArguments.py --help
# python .\AdvancedPython_CommandlineArguments.py --age=33 --name=Nils --is_admin=True