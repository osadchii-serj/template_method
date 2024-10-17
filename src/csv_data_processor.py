from data_processor import DataProcessor


class CSVDataProcessor(DataProcessor):

    def read_data(self):
        print("Чтение данных из CSV файла.")

    def clean_data(self):
        print("Очистка данных из CSV.")

    def analyze_data(self):
        print("Анализ данных из CSV.")

    def save_results(self):
        print("Сохранение результатов анализа в CSV.")
