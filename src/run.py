from json_data_processor import JSONDataProcessor
from csv_data_processor import CSVDataProcessor

if __name__ == "__main__":

    csv_processor = CSVDataProcessor()
    csv_processor.process_data()

    print()

    json_processor = JSONDataProcessor()
    json_processor.process_data()
