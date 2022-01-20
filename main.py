from modules.src.request_handler import *
from modules.ui.fancy_prints import *


def main() -> None:

    search_term: str = input("KEYWORD: ")

    FancyPrints.scrape_menu()
    selected_types: list[int] = [
        int(type_num) - 1 for type_num in input("SELECT TYPES: ").split()
    ]
    print("-------------------------------------------------------------------------")

    FancyPrints.characteristics_menu()
    selected_characteristics: list[int] = [
        int(characteristics_num) - 1 for characteristics_num in input("SELECT CHARACTERISTICS: ").split()
    ]
    print("-------------------------------------------------------------------------")

    req_hndlr: UserRequestHandler = UserRequestHandler(
        selected_types, selected_characteristics, search_term
    )
    req_hndlr.process_request()


if __name__ == "__main__":
    main()
