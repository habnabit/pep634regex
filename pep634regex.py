import dataclasses
import re


@dataclasses.dataclass
class _ConsiderMatch:
    c: considering

    def __eq__(self, other):
        if self.c._current is None:
            raise RuntimeError('`considering` unprepared', self.c)
        self.c.match = self.c._current._matches(other, self.c.input_str)
        return self.c.match is not None


@dataclasses.dataclass
class considering:
    input_str: str
    match: re.Match | None = None
    _current: _PatternMeta | None = None

    @property
    def pattern(self):
        return _ConsiderMatch(self)


class _PatternMeta(type):
    def __instancecheck__(cls, inst):
        if not isinstance(inst, considering):
            return False
        inst._current = cls
        return True


@dataclasses.dataclass
class fullmatch(metaclass=_PatternMeta):
    __match_args__ = ('pattern',)

    def __init__(self):
        raise RuntimeError('non-instantiable class')

    @classmethod
    def _matches(cls, pattern, s):
        return re.fullmatch(pattern, s)
