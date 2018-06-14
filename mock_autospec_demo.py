from unittest import mock


class A:
    def x(self, y):
        return y ** 2


@mock.patch.object(A, 'x', autospec=True)
def test(mock_x):
    a = A()
    print(a.x(42))
    print(a.x(z=42))


test()
