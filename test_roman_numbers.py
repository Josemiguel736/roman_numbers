from to_roman_funcs import to_roman,  divide_miles, roman_mil

def test_romanos_simples():
    assert to_roman(1) == 'I'
    assert to_roman(5) == 'V'
    assert to_roman(10) == 'X'
    assert to_roman(50) == 'L'
    assert to_roman(100) == 'C'
    assert to_roman(500) == 'D'
    assert to_roman(1000) == 'M'

def test_romanos_1_al_9():
    assert to_roman(1) == 'I'
    assert to_roman(2) == 'II'
    assert to_roman(3) == 'III'
    assert to_roman(4) == 'IV'
    assert to_roman(5) == 'V'
    assert to_roman(6) == 'VI'
    assert to_roman(7) == 'VII'
    assert to_roman(8) == 'VIII'
    assert to_roman(9) == 'IX'

def test_romanos_10_al_90():
    assert to_roman(10) == 'X'
    assert to_roman(20) == 'XX'
    assert to_roman(30) == 'XXX'
    assert to_roman(40) == 'XL'
    assert to_roman(50) == 'L'
    assert to_roman(60) == 'LX'
    assert to_roman(70) == 'LXX'
    assert to_roman(80) == 'LXXX'
    assert to_roman(90) == 'XC'



def test_divide_en_miles():
    assert divide_miles(4568)==[4,568]
    assert divide_miles(560)==[560]

def test_divide_en_miles_con_millones():
    assert divide_miles(4444568)==[568,444,4]
    assert divide_miles(560)==[560]

def test_roman_mil():
    assert roman_mil(68993)=="LXVIII*CMXCIII"
    assert roman_mil(4000)=="IV*"
