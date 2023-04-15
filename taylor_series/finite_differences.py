"""
"""

import decimal
from decimal import Decimal
from numbers import Number
import typing


OneVarFunction = typing.Callable[[Number], Number]


class FiniteDifference:
    """

    :param func:
    """
    def __init__(self, func: OneVarFunction):
        self.func = func

    @staticmethod
    def forward(func: OneVarFunction, x: Decimal, h: Decimal) -> Decimal:
        r"""
        .. math::

            {\Delta}_{h}[f](x) = f(x + h) - f(x)

        :param x:
        :param h:
        :return:
        """
        return func(x + h) - func(x)
    
    @staticmethod
    def backward(func: OneVarFunction, x: Decimal, h: Decimal) -> Decimal:
        r"""
        .. math::

            {\nabla}_{h}[f](x) = f(x) - f(x - h)

        :param x:
        :param h:
        :return:
        """
        return func(x) - func(x - h)
    
    @staticmethod
    def central(func: OneVarFunction, x: Decimal, h: Decimal) -> Decimal:
        r"""
        .. math::

            {\delta}_{h}[f](x) = f(x + \frac{h}{2}) - f(x - \frac{h}{2})

        :param x:
        :param h:
        :return:
        """
        return func(x + h / 2) - func(x - h / 2)
    

@typing.runtime_checkable
class FDiffType(typing.Protocol):
    """
    """
    def __call__(self, func: OneVarFunction, x: Decimal, h: Decimal) -> Decimal: ...


class DifferenceQuotient:
    """
    """
    def __init__(self, func: OneVarFunction):
        self.func = func

    def __call__(self, fdiff: FDiffType, x: Number, *, prec: int = 100) -> OneVarFunction:
        """
        :param fdiff:
        :param x:
        :param prec:
        :return:
        """
        with decimal.localcontext() as ctx:
            ctx.prec = prec + 2

            p, res = 1, Decimal(0)
            while True:
                h = Decimal(f"1E-{p}")

                if h == 0 or fdiff(self.func, x, h) == 0:
                    break

                res = fdiff(self.func, x, h) / h

                p *= 2

            return res.quantize(Decimal(f"1E-{prec}"))