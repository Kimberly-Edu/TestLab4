import Lab2.bmi as bmi

def Test_bmi_normal_weight():
    result = bmi.calculate_bmi(57, 1.73)
    assert (result == 0)

def Test_bmi_over_weight():
    result = bmi.calculate_bmi(90, 1.6)
    assert (result == 1)

def Test_bmi_under_weight():
    result = bmi.calculate_bmi(45, 1.8)
    assert (result == -1)

