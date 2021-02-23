import numpy as np

# 各定价销售成功的概率
leisure = {
    5: 31/31, 7: 25/31, 9: 20/31, 11: 15/31,
    13: 10/31, 15: 6/31, 17: 3/31, 20: 1/31, 999: 0
}

business = {
    9: 31/31, 11: 30/31, 13: 28/31,
    15: 26/31, 17: 24/31, 20: 10/31, 999: 0
}

p = np.zeros((10, 30))
ev = np.zeros((10, 30))

def propagate(rem_seat, rem_cus):
    _dct = business if rem_cus < 10 else leisure
    _max_value, _max_price = 0, 0
    for key in _dct:
        _tmp_value = _dct[key] * key  # 销售成功的期望收益
        if rem_cus > 0:
            _tmp_value += (1 - _dct[key]) * ev[rem_seat, rem_cus - 1]  # 销售失败后的期望收益
            if rem_seat > 0: _tmp_value += _dct[key] * ev[rem_seat - 1, rem_cus - 1]  # 销售成功后的期望收益
        if _tmp_value > _max_value: _max_value, _max_price = _tmp_value, key
    ev[rem_seat, rem_cus] = _max_value
    p[rem_seat, rem_cus] = _max_price

for rem_customer in range(30):
    for rem_seat in range(10):
        if rem_seat >= rem_customer - 20: propagate(rem_seat, rem_customer)

print(p)
print(ev)

np.savetxt('001_pricing_strategy.csv', p, fmt='%.2f', delimiter=',')
np.savetxt('002_expected_value.csv', ev, fmt='%.2f', delimiter=',')