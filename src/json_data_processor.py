from data_processor import DataProcessor


class JSONDataProcessor(DataProcessor):

    def read_data(self):
        print("Чтение данных из JSON файла.")

    def clean_data(self):
        print("Очистка данных из JSON.")

    def analyze_data(self):
        print("Анализ данных из JSON.")

    def save_results(self):
        print("Сохранение результатов анализа в JSON.")
