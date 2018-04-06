from typing import Dict


class UrdObject(object):
    def __init__(self):
        self.__map = dict()  # type: Dict[int, bool]
        self.__frequency = 0
        self.__max_count = -1

    def add(self, address):
        self.__map[address] = True

    def get_count(self):
        return self.__max_count

    def get_frequency(self):
        return self.__frequency

    def initialize_next(self):
        if len(self.__map) == 0:
            return
        if self.__max_count < len(self.__map):
            self.__max_count = len(self.__map)
            self.__frequency = 1
        elif self.__max_count == len(self.__map):
            self.__frequency += 1
        self.__map.clear()

    def reset_urd(self):
        self.__map.clear()