from abc import ABC, abstractmethod

class DataStorage(ABC):
    @abstractmethod
    def store_data(self, data):
        pass

    @abstractmethod
    def retrieve_data(self, key):
        pass

class LocalPhoneStorage(DataStorage):
    def store_data(self, data):
        print(f"Storing data locally on phone: {data}")

    def retrieve_data(self, key):
        print(f"Retrieving data with key {key} from local phone storage")


class GoogleStorage(DataStorage):
    def store_data(self, data):
        print(f"Storing data on google cloud: {data}")

    def retrieve_data(self, key):
        print(f"Retrieving data with key {key} from google cloud storage")


phone_storage = LocalPhoneStorage()
phone_storage.store_data("User photos")
phone_storage.retrieve_data("photo_123")

google_storage = GoogleStorage()
google_storage.store_data("Project files")
google_storage.retrieve_data("file_456")