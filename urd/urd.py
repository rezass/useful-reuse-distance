from typing import Dict
from urd_object import UrdObject
from enum import Enum


class IoType(Enum):
    read = 0
    write = 1


class Urd(object):
    def __init__(self):
        self.urd_object = dict()  # type: Dict[int, UrdObject]

    def access(self, address, io_type):
        try:
            urd_object = self.urd_object[address]
        except KeyError:
            self.urd_object[address] = UrdObject()
            return
        finally:
            for key, value in self.urd_object.iteritems():
                if key != address:
                    value.add(address)

        if io_type == IoType.write:
            urd_object.reset_urd()
            return

        self.urd_object[address].initialize_next()

    def finish(self):
        for key, value in self.urd_object.iteritems():
            value.initialize_next()

    def print_data(self):
        for key, value in sorted(self.urd_object.iteritems()):
            print("%s %s %s" % (key, value.get_count(), value.get_frequency()))