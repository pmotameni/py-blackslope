import enum


class DescriptionEnumMeta(enum.EnumMeta):
    def __new__(mcs, name, bases, attrs):
        obj = super().__new__(mcs, name, bases, attrs)
        obj._value2member_map_ = {}
        for m in obj:
            value, description = m.value
            m._value_ = value
            m.description = description
            obj._value2member_map_[value] = m

        return obj
