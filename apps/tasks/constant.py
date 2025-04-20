from collections import OrderedDict


class Status:
    IN_PROGRESS = 'in_progress'
    PENDING = 'pending'
    COMPLATE = 'complate'

    FieldStr = OrderedDict({
        IN_PROGRESS: 'In progress',
        PENDING: 'Pending',
        COMPLATE: 'Complate',
    })

    @classmethod
    def choices(cls):
        return cls.FieldStr.items()
