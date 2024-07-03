
from to_roman_funcs import to_roman, to_arabigo

def test_to_roman_simples():
    assert to_roman(1)=="I"
    assert to_roman(5)=="V"
    assert to_roman(10)=="X"
    assert to_roman(50)=="L"
    assert to_roman(100)=="C"
    assert to_roman(500)=="D"
    assert to_roman(1000)=="M"

def test_to_roman_complex():
    assert to_roman(3)=="III"
    assert to_roman(6)=="VI"
    assert to_roman(12)=="XII"
    assert to_roman(102)=="CII"
    assert to_roman(1153)=="MCLIII"
    assert to_roman(432)=="CDXXXII"
    assert to_roman(1994)=="MCMXCIV"

def test_to_arabigo_simple():
    assert to_arabigo("I")==1
    assert to_arabigo("V")==5
    assert to_arabigo("X")==10
    assert to_arabigo("L")==50
    assert to_arabigo("C")==100
    assert to_arabigo("D")==500
    assert to_arabigo("M")==1000

def test_to_arabigo_complex():
    assert to_arabigo("III")==3

    assert to_arabigo("IV")==4
    assert to_arabigo("VL")==45
    assert to_arabigo("CVXX")==115
    assert to_arabigo("VD")==495
    assert to_arabigo("CCXC")==290
    assert to_arabigo("MCM")==1900

def test_compare():
    for n in range(1,4001):
        assert to_arabigo(to_roman(n))==n
