from unittest import mock


class A:
    def x(self, y):
        return y ** 2


m = mock.Mock(spec=A)
print(m.x)
print(m.y)
