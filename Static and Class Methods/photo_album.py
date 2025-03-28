import math


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(math.ceil(photos_count / 4))

    def add_photo(self, label: str):
        for i, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(page)}"
        return f"No more free slots"

    def display(self):
        separator = "-" * 11 + "\n"
        result = separator
        for page in self.photos:
            result += " ".join(["[]" for _ in page]) + "\n"
            result += separator
        return result.strip()
