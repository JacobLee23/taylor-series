"""
"""

import typing


class FiniteDifference:
    """
    """
    @staticmethod
    def forward(f: typing.Callable[[float], float], h: float) -> typing.Callable[[float], float]:
        """
        :param f:
        :param h:
        :return:
        """
        return lambda x: f(x + h) - f(x)

    @staticmethod
    def backward(f: typing.Callable[[float], float], h: float) -> typing.Callable[[float], float]:
        """
        :param f:
        :param h:
        :return:
        """
        return lambda x: f(x) - f(x - h)

    @staticmethod
    def central(f: typing.Callable[[float], float], h: float) -> typing.Callable[[float], float]:
        """
        :param f:
        :param h:
        :return:
        """
        return lambda x: f(x + h / 2) - f(x - h / 2)
