import Lab2.bmi as bmi

def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.73, 57)
    print(result)
    assert (result == 0)

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.6, 90)
    assert (result == 1)

def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.8, 45)
    assert (result == -1)

