#!/usr/bin/env python3
"""The module contains pagination exercise"""
import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page, page_size):
        """returns start and end index"""
        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get the page dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        total_rows = len(dataset)

        start_index, end_index = self.index_range(page, page_size)

        if start_index >= total_rows:
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Get the dataset per the given page and the hyperdata set"""
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)

        hyper_dataset = {}
        hyper_dataset['page_size'] = len(self.get_page(page, page_size))
        hyper_dataset['page'] = page
        hyper_dataset['data'] = self.get_page(page, page_size)
        hyper_dataset['next_page'] = page + 1 if page < total_pages else None
        hyper_dataset['prev_page'] = page - 1 if page > 1 else None
        hyper_dataset['total_pages'] = total_pages

        return hyper_dataset
