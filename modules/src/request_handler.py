import time
import sys
import numpy as np
import pandas as pd

from tabulate import tabulate
from PyQt5.QtWidgets import QApplication, QTableView

from ..src.data import BookTypes
from ..src.scraper import Scraper
from ..src.dataframe_in_qt import BuildTable
from ..ui.fancy_prints import FancyPrints


class UserRequestHandler:
    def __init__(
        self,
        selected_types: list[int],
        selected_characteristics: list[int],
        search_term: str,
    ):
        self.types = selected_types
        self.characteristics = selected_characteristics
        self.search_term = search_term

    def process_request(self) -> None:

        scraper: Scraper = Scraper()
        req_results: list[dict] = []

        start: float = 0
        section_time: float = 0
        total_time: float = 0
        time_measurements: dict = {}

        for type_number in self.types:
            try:

                FancyPrints.current_search_place(
                    BookTypes.TYPES[type_number],
                    BookTypes.LINKS[type_number],
                    BookTypes.CHARACTERISTICS[self.characteristics]
                                                 )

                start = time.time()

                req_results = scraper.perform_search(
                    BookTypes.LINKS[type_number],
                    self.search_term,
                    BookTypes.CHARACTERISTICS[self.characteristics]
                    )

                section_time = round(time.time() - start, 2)
                time_measurements[BookTypes.TYPES[type_number]] = section_time
                total_time += section_time

            except Exception as e:
                raise ValueError(f"\nERROR in <<process_request>>: {repr(e)}")

        time_measurements['Total time'] = round(total_time, 2)
        self.represent_request_data(req_results, time_measurements)

    @staticmethod
    def represent_request_data(req_results: list[dict], time_measurements: dict):

        df = pd.DataFrame.from_dict(req_results, orient='columns')
        overall_time = pd.DataFrame.from_dict(time_measurements, orient='index')
        overall_time.rename(columns={0: 'Time, sec'}, inplace=True)

        overall_time['Time, min'] = np.round_(overall_time['Time, sec'].values / 60, 2)

        print(tabulate(overall_time, tablefmt='pretty',
                       headers=['Section', 'Time, sec', 'Time, min']))

        model = BuildTable(df)
        app = QApplication(sys.argv)

        view = QTableView()
        view.setModel(model)
        view.resizeColumnsToContents()
        view.resize(1000, 900)
        view.show()

        sys.exit(app.exec_())
