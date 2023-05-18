import price_info
def test_total_cost_of_shopping():
    expected_result = 46.75

    result = 0
    for key in price_info.price_list.keys():
        # print(key)
        # print(price_info.quantity_list[key])
        # print(price_info.cost_of_fruits(key, price_info.quantity_list[key]))
        result += price_info.cost_of_fruits(key, price_info.quantity_list[key])
    print(result)

    assert(expected_result==result)
