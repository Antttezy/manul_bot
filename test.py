import counter

c = counter.PallasCounter()
c._pallas_counter = 974
assert str(c) == 'девятьсот семьдесят четыре манула'

c._pallas_counter = 1000
assert str(c) == 'тысяча манулов'

c._pallas_counter = 194223
assert str(c) == 'сто девяносто четыре тысячи двести двадцать три манула'
