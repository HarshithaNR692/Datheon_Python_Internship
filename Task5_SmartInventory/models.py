
from abc import ABC, abstractmethod
from datetime import date


class LibraryItem(ABC):
    def __init__(self, item_id, title, price):
        self.item_id = item_id
        self.title = title
        self.price = price
        self.__borrow_date = None
        self.__is_checked_out = False

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0:
            raise ValueError("Price must be a non-negative number.")
        self.__price = value

    @property
    def borrow_date(self):
        return self.__borrow_date

    @property
    def is_checked_out(self):
        return self.__is_checked_out

    def checkout(self):
        if self.__is_checked_out:
            raise ValueError("This item is already checked out.")
        self.__borrow_date = date.today()
        self.__is_checked_out = True

    def return_item(self):
        if not self.__is_checked_out:
            raise ValueError("This item is not checked out.")
        self.__is_checked_out = False
        self.__borrow_date = None

    @abstractmethod
    def calculate_fee(self, days_late=0):
        pass

    @abstractmethod
    def display_metadata(self):
        pass

    def __str__(self):
        status = "Checked out" if self.__is_checked_out else "Available"
        return f"{self.item_id} - {self.title} ({status})"

    def __repr__(self):
        return f"{self.__class__.__name__}(item_id={self.item_id!r}, title={self.title!r})"

    def __eq__(self, other):
        if not isinstance(other, LibraryItem):
            return NotImplemented
        return self.item_id == other.item_id


class Book(LibraryItem):
    def __init__(self, item_id, title, price, author, pages):
        super().__init__(item_id, title, price)
        self.author = author
        self.pages = pages

    def calculate_fee(self, days_late=0):
        return max(0, days_late) * 2.0

    def display_metadata(self):
        return f"Book | Author: {self.author} | Pages: {self.pages}"

    def __len__(self):
        return self.pages


class Magazine(LibraryItem):
    def __init__(self, item_id, title, price, issue_number, pages):
        super().__init__(item_id, title, price)
        self.issue_number = issue_number
        self.pages = pages

    def calculate_fee(self, days_late=0):
        return max(0, days_late) * 1.0

    def display_metadata(self):
        return f"Magazine | Issue: {self.issue_number} | Pages: {self.pages}"

    def __len__(self):
        return self.pages


class DigitalMedia(LibraryItem):
    def __init__(self, item_id, title, price, file_size_mb, license_type):
        super().__init__(item_id, title, price)
        self.file_size_mb = file_size_mb
        self.license_type = license_type

    def calculate_fee(self, days_late=0):
        return 0.0

    def display_metadata(self):
        return (
            f"Digital Media | Size: {self.file_size_mb} MB "
            f"| Licence: {self.license_type}"
        )

    def __len__(self):
        return int(self.file_size_mb)
