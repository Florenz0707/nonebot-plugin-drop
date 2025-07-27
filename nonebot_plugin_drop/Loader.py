import os
from pathlib import Path


class Loader:
    def __init__(self):
        self._dir = Path(__file__).parent / "resource"
        self._resource = list()
        for root, dirs, files in os.walk(str(self._dir)):
            for file in files:
                print(file)
                if ".png" in file and "-" in file:
                    self._resource.append(file.split('.')[0])
        print(self._resource)

    def get_items(self) -> None | list:
        return None if len(self._resource) == 0 else self._resource

    def get_item_path(self, item: str) -> None | str:
        return None if item not in self._resource else self._dir.joinpath(f"{item}.png")


if __name__ == "__main__":
    loader = Loader()
    for item in loader.get_items():
        print(loader.get_item_path(item))
