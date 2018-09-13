from unittest import mock


class A:
    def x(self, n):
        return n ** 2


m = mock.Mock(spec_set=A)
print(m.x)
m.y = 42
print(m.y)
print(m.z)
