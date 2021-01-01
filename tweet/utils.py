from enum import IntEnum


class TweetStatus(IntEnum):
    ACTIVE = 1
    PASSIVE = 0

    @classmethod
    def statuses(cls):
        return [(key.value, key.name) for key in cls]
