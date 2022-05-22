from typing import Union


def atmospeheres_to_bars(atm: float, unit: str) -> Union[float, str]:
    """
    This function converts atm to bar
    Wikipedia reference: https://en.wikipedia.org/wiki/Standard_atmosphere_(unit)
    Wikipedia reference: https://en.wikipedia.org/wiki/Bar_(unit)

    >>> atmospeheres_to_bars(2.5, "atm")
    2.533125
    >>> atmospeheres_to_bars("12", "atm")
    12.158999999999999
    >>> atmospeheres_to_bars(0, "atm")
    0.0
    >>> atmospeheres_to_bars(35, "mmHg")
    'Invalid unit'
    >>> atmospeheres_to_bars("atmospheres", "atm")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'atmospheres'
    """
    return atm * 1.01325 if unit == "atm" else "Invalid unit"


def bars_to_atmospheres(bar: float, unit: str) -> Union[float, str]:
    """
    This function converts bar to atm
    Wikipedia reference: https://en.wikipedia.org/wiki/Standard_atmosphere_(unit)
    Wikipedia reference: https://en.wikipedia.org/wiki/Bar_(unit)

    >>> bars_to_atmospheres(36, "bar")
    35.529237601776465
    >>> bars_to_atmospheres("57.6", "bar")
    56.84678016284234
    >>> bars_to_atmospheres(0, "bar")
    0.0
    >>> bars_to_atmospheres(35, "Pa")
    'Invalid unit'
    >>> bars_to_atmospheres("barrs", "bar")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'barrs'

    """
    return bar / 1.01325 if unit == "bar" else "Invalid unit"


def atmospheres_to_milimeter_mercury(atm: float, unit: str) -> Union[float, str]:
    """
    This function converts atm to mmHg
    Wikipedia reference: https://en.wikipedia.org/wiki/Standard_atmosphere_(unit)
    Wikipedia reference: https://en.wikipedia.org/wiki/Millimetre_of_mercury

    >>> atmospheres_to_milimeter_mercury(2, "atm")
    1520.0
    >>> atmospheres_to_milimeter_mercury("6.9", "atm")
    5244.0
    >>> atmospheres_to_milimeter_mercury(0, "atm")
    0.0
    >>> atmospheres_to_milimeter_mercury(35, "torr")
    'Invalid unit'
    >>> atmospheres_to_milimeter_mercury("atmos", "atm")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'atmos'
    """
    return atm * 760 if unit == "atm" else "Invalid unit"


def milimeter_mercury_to_atmospheres(mm_hg: float, unit: str) -> Union[float, str]:
    """
    This function converts mmHg to atm
    Wikipedia reference: https://en.wikipedia.org/wiki/Standard_atmosphere_(unit)
    Wikipedia reference: https://en.wikipedia.org/wiki/Millimetre_of_mercury

    >>> milimeter_mercury_to_atmospheres(23506.92, "mmHg")
    30.93015789473684
    >>> milimeter_mercury_to_atmospheres("304000", "mmHg")
    400.0
    >>> milimeter_mercury_to_atmospheres(0, "mmHg")
    0.0
    >>> milimeter_mercury_to_atmospheres(35, "bar")
    'Invalid unit'
    >>> milimeter_mercury_to_atmospheres("merc", "mmHg")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'merc'
    """
    return mm_hg / 760 if unit == "mmHg" else "Invalid unit"


def atmospheres_to_pascals(atm: float, unit: str) -> Union[float, str]:
    """
    This function converts atm to Pa
    Wikipedia reference: https://en.wikipedia.org/wiki/Standard_atmosphere_(unit)
    Wikipedia reference: https://en.wikipedia.org/wiki/Pascal_(unit)

    >>> atmospheres_to_pascals(5.4, "atm")
    547155.0
    >>> atmospheres_to_pascals("7.098", "atm")
    719204.85
    >>> atmospheres_to_pascals(0, "atm")
    0.0
    >>> atmospheres_to_pascals(35, "Pa")
    'Invalid unit'
    >>> atmospheres_to_pascals("ats", "atm")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'ats'
    """
    return atm * 101325 if unit == "atm" else "Invalid unit"


def pascals_to_atmospheres(pa: float, unit: str) -> Union[float, str]:
    """
    This function converts Pa to atm
    Wikipedia reference: https://en.wikipedia.org/wiki/Standard_atmosphere_(unit)
    Wikipedia reference: https://en.wikipedia.org/wiki/Pascal_(unit)

    >>> pascals_to_atmospheres(202650, "Pa")
    2.0
    >>> pascals_to_atmospheres("1013250", "Pa")
    10.0
    >>> pascals_to_atmospheres(0, "Pa")
    0.0
    >>> pascals_to_atmospheres(35, "mmhg")
    'Invalid unit'
    >>> pascals_to_atmospheres("Pas", "Pa")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'Pas'
    """

    return pa / 101325 if unit == "Pa" else "Invalid unit"


def bars_to_milimeter_mercury(bar: float, unit: str) -> Union[float, str]:
    """
    This function converts bar to mmHg
    Wikipedia reference: https://en.wikipedia.org/wiki/Bar_(unit)
    Wikipedia reference: https://en.wikipedia.org/wiki/Millimetre_of_mercury

    >>> bars_to_milimeter_mercury(3.75, "bar")
    2812.725
    >>> bars_to_milimeter_mercury("0.82", "bar")
    615.0491999999999
    >>> bars_to_milimeter_mercury(0, "bar")
    0.0
    >>> bars_to_milimeter_mercury(3, "atm")
    'Invalid unit'
    >>> bars_to_milimeter_mercury("brs", "bar")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'brs'
    """
    return bar * round(760 / 1.01325, 2) if unit == "bar" else "Invalid unit"


def milimeter_mercury_to_bars(mm_hg: float, unit: str) -> Union[float, str]:
    """
    This function converts mmHg to bar
    Wikipedia reference: https://en.wikipedia.org/wiki/Bar_(unit)
    Wikipedia reference: https://en.wikipedia.org/wiki/Millimetre_of_mercury

    >>> milimeter_mercury_to_bars(4970.5, "mmHg")
    6.626803189078208
    >>> milimeter_mercury_to_bars("378", "mmHg")
    0.503959683225342
    >>> milimeter_mercury_to_bars(0, "mmHg")
    0.0
    >>> milimeter_mercury_to_bars(3, "bar")
    'Invalid unit'
    >>> milimeter_mercury_to_bars("brs", "mmHg")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'brs'
    """
    return mm_hg / round(760 / 1.01325, 2) if unit == "mmHg" else "Invalid unit"


def bars_to_pascals(bar: float, unit: str) -> Union[float, str]:
    """
    This function converts bar to Pa
    Wikipedia reference: https://en.wikipedia.org/wiki/Bar_(unit)
    Wikipedia reference: https://en.wikipedia.org/wiki/Pascal_(unit)

    >>> bars_to_pascals(0.653, "bar")
    65300.0
    >>> bars_to_pascals("1.2", "bar")
    120000.0
    >>> bars_to_pascals(0, "bar")
    0.0
    >>> bars_to_pascals(3.1, "Pa")
    'Invalid unit'
    >>> bars_to_pascals("bP", "bar")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'bP'
    """
    return bar * 100000 if unit == "bar" else "Invalid unit"


def pascals_to_bars(pa: float, unit: str) -> Union[float, str]:
    """
    This function converts Pa to bar
    Wikipedia reference: https://en.wikipedia.org/wiki/Bar_(unit)
    Wikipedia reference: https://en.wikipedia.org/wiki/Pascal_(unit)

    >>> pascals_to_bars(45000, "Pa")
    0.45
    >>> pascals_to_bars("1200000", "Pa")
    12.0
    >>> pascals_to_bars(0, "Pa")
    0.0
    >>> pascals_to_bars(3.1, "mmHg")
    'Invalid unit'
    >>> pascals_to_bars("pass", "Pa")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'pass'
    """
    return pa / 100000 if unit == "Pa" else "Invalid unit"


def milimeter_mercury_to_pascals(mm_hg: float, unit: str) -> Union[float, str]:
    """
    This function converts mmHg to Pa
    Wikipedia reference: https://en.wikipedia.org/wiki/Millimetre_of_mercury
    Wikipedia reference: https://en.wikipedia.org/wiki/Pascal_(unit)

    >>> milimeter_mercury_to_pascals(25, "mmHg")
    3333.0
    >>> milimeter_mercury_to_pascals("652", "mmHg")
    86924.64
    >>> milimeter_mercury_to_pascals(0, "mmHg")
    0.0
    >>> milimeter_mercury_to_pascals(342.1, "bar")
    'Invalid unit'
    >>> milimeter_mercury_to_pascals("mercurium", "mmHg")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'mercurium'
    """
    return mm_hg * round(101325 / 760, 2) if unit == "mmHg" else "Invalid unit"


def pascals_to_milimeter_mercury(pa: float, unit: str) -> Union[float, str]:
    """
    This function converts Pa to mmHg
    Wikipedia reference: https://en.wikipedia.org/wiki/Millimetre_of_mercury
    Wikipedia reference: https://en.wikipedia.org/wiki/Pascal_(unit)

    >>> pascals_to_milimeter_mercury(153000, "Pa")
    1147.6147614761476
    >>> pascals_to_milimeter_mercury("97650.8", "Pa")
    732.4542454245425
    >>> pascals_to_milimeter_mercury(0, "Pa")
    0.0
    >>> pascals_to_milimeter_mercury(342.1, "mmhg")
    'Invalid unit'
    >>> pascals_to_milimeter_mercury("merc", "Pa")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'merc'
    """
    return pa / round(101325 / 760, 2) if unit == "Pa" else "Invalid unit"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
