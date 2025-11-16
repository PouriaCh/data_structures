from typing import List, Optional


class HashTable:
    def __init__(self, size: int = 7) -> None:
        self.data_map = [None] * size
    
    def __hash(self, key: str) -> int:
        my_hash: int = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self) -> None:
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key: str, value: int) -> None:
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key: str) -> Optional[int]:
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for item in self.data_map[index]:
                if item[0] == key:
                    return item[1]
        return
        
    def keys(self) -> List[str]:
        keys_list: List[str] = []
        for items_list in self.data_map:
            if items_list is not None:
                for item in items_list:
                    keys_list.append(item[0])
        return keys_list


if __name__ == "__main__":
    my_hash_table = HashTable()

    my_hash_table.set_item("bolts", 1400)
    my_hash_table.set_item("washers", 50)
    my_hash_table.set_item("lumber", 70)

    my_hash_table.print_table()
    print(my_hash_table.keys())
