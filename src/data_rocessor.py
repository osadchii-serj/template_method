from abc import ABC, abstractmethod


class DataProcessor(ABC):

    def process_data(self):
        self.read_data()
        self.clean_data()
        self.analyze_data()
        self.save_results()

    @abstractmethod
    def read_data(self):
        raise NotImplementedError()

    @abstractmethod
    def clean_data(self):
        raise NotImplementedError()

    @abstractmethod
    def analyze_data(self):
        raise NotImplementedError()

    @abstractmethod
    def save_results(self):
        raise NotImplementedError()
