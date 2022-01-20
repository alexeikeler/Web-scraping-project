from ..src.data import BookTypes


class FancyPrints:

    @staticmethod
    def scrape_menu() -> None:

        print("-------------------------------------------------------------------------")

        print("SEARCH IN: ")
        print("-------------------------------------------------------------------------")
        for index, section in enumerate(BookTypes.TYPES):
            print(f"{index + 1} - {section}")
        print("-------------------------------------------------------------------------")

    @staticmethod
    def characteristics_menu() -> None:

        print("\n-------------------------------------------------------------------------")
        print("ADDITIONAL CHARACTERISTICS (BASE ARE: Название, Цена, Ссылка)")
        print("-------------------------------------------------------------------------")
        for index, chrs in enumerate(BookTypes.CHARACTERISTICS):
            print(f"{index + 1} - {chrs}")
        print("-------------------------------------------------------------------------")

    @staticmethod
    def current_search_place(section: str, link: str, info_to_search: list[str]):

        print(
            "\n-------------------------------------------------------------------------"
        )
        print(
            f"SEARCHING IN '{section}' TYPE "
            f"\nLINK: {link}"
            f"\nCHOOSEN ADDITIONAL CHARACTERISTICS: {info_to_search}"
        )
        print("-------------------------------------------------------------------------\n")
