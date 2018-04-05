from typing import Dict


class Urd(object):
    def __init__(self):
        self.seq_number = 0
        self.map = dict()  # type: Dict[int, int]

    def access(self, address):
        try:
            urd = self.seq_number - self.map[address] - 1
            self.map[address] = self.seq_number
        except KeyError:
            urd = -1
            self.map[address] = self.seq_number
        self.seq_number += 1
        return urd
