"""
"""

from numbers import Number
import typing


class FiniteDifference:
    """

    :param func:
    """
    def __init__(self, func: typing.Callable[[Number], Number]):
        self.func = func

    @classmethod
    def forward_difference(
        cls,
        func: typing.Callable[[Number], Number],
        x: Number,
        h: Number
    ) -> Number:
        r"""
        .. math::

            {\Delta}_{h}[f](x) = f(x + h) - f(x)

        :param x:
        :param h:
        :return:
        """
        return func(x + h) - func(x)
    
    @classmethod
    def backward_difference(
        cls,
        func: typing.Callable[[Number], Number],
        x: Number,
        h: Number
    ) -> Number:
        r"""
        .. math::

            {\nabla}_{h}[f](x) = f(x) - f(x - h)

        :param x:
        :param h:
        :return:
        """
        return func(x) - func(x - h)
    
    @classmethod
    def central_difference(
        cls,
        func: typing.Callable[[Number], Number],
        x: Number,
        h: Number
    ) -> Number:
        r"""
        .. math::

            {\delta}_{h}[f](x) = f(x + \frac{h}{2}) - f(x - \frac{h}{2})

        :param x:
        :param h:
        :return:
        """
        return func(x + h / 2) - func(x - h / 2)
