from collections import OrderedDict


class GenderChoice:
    MALE = 'hr'
    FEMALE = 'female'
    OTHER = 'other'

    FieldStr = OrderedDict({
        MALE: 'Male',
        FEMALE: 'Female',
        OTHER: 'Other',
    })

    @classmethod
    def choices(cls):
        return cls.FieldStr.items()


class UserRole:
    HR = 'hr'
    LEADER = 'leader'
    EMPLOYEE = 'employee'

    FieldStr = OrderedDict({
        HR: 'HR',
        LEADER: 'Leader',
        EMPLOYEE: 'Employee',
    })

    @classmethod
    def choices(cls):
        return cls.FieldStr.items()
