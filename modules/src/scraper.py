import re

import numpy as np
import requests
import bs4
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):

        # self.__base_url = 'https://rozetka.com.ua/knigi/c4326572'
        # self.__base_link = link

        self.__pages_container_class = "pagination__item ng-star-inserted"
        self.__content_class = "content content_type_catalog"
        self.__price_class = "goods-tile__price-value"
        self.__characteristics_class = "characteristics-full__item ng-star-inserted"

    def _send_request(self, url: str) -> BeautifulSoup:
        return BeautifulSoup(requests.get(url).text, "lxml")

    def extract_last_page_number(self, pagination_items: bs4.element.ResultSet) -> int:

        pagination_items_str_last = str(pagination_items[-1].a)
        split_page_numbers = re.search("=\d{1,4}", pagination_items_str_last)

        return int(split_page_numbers[0][1:])

    def _extract_href(self, item) -> str:
        return item.parent.parent.get("href")

    def _extract_price(self, item) -> str:
        return (
            item.parent.parent.parent.find(class_=self.__price_class)
                .string.replace('\xa0', '')
                .strip()
        )

    def _extract_data(self, item, info_filter) -> dict:

        request_result = {}

        try:
            last_minus_index = item.rfind('-')

            title = item[:last_minus_index]

            href = self._extract_href(item)
            price = self._extract_price(item)

            request_result['Название'] = title
            request_result['Ссылка'] = href
            request_result['Цена'] = price

            additional_info_list = self._send_request(href)
            info_list = additional_info_list.find_all(
                class_=self.__characteristics_class
            )

            for info in info_list:

                name_value = info.get_text(separator=": ").split(':')

                if name_value[0] in info_filter:
                    request_result[name_value[0]] = name_value[1]

            return request_result

        except Exception as e:
            print(f'ERROR IN <<_extract_data>> METHOD\n{repr(e)}')

    def perform_search(self, link: str, search_for: str, info_filter: np.ndarray) -> list[dict]:

        search_result: list[dict] = []

        doc = self._send_request(link)
        page_numbers_list = doc.find_all(class_=self.__pages_container_class)
        pages_count = self.extract_last_page_number(page_numbers_list)

        for i in range(1, pages_count + 1):

            url = link + f"page={i}"
            doc = self._send_request(url)
            div = doc.find(class_=self.__content_class)

            try:

                items = div.find_all(text=re.compile(search_for, re.IGNORECASE))
                print(f"PAGE {i} | {pages_count}")

                for item in items:

                    search_result.append(self._extract_data(item, info_filter))

            except Exception as e:
                print("\n\nERROR:\n\n", repr(e))

        return search_result
