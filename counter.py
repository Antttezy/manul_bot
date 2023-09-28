class PallasCounter:
    _HUNDREDS = ['сто', 'двести', 'триста', 'четыреста', 'пятьсот',
                 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']

    _TENS = ['десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
             'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']

    _TEN_TO_TWENTY = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
                      'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']

    _ONES_M = ['один', 'два', 'три', 'четыре', 'пять',
               'шесть', 'семь', 'восемь', 'девять']

    _ONES_F = ['одна', 'две', 'три', 'четыре', 'пять',
               'шесть', 'семь', 'восемь', 'девять']

    _people_min: int
    _people_hist: int
    _pallas_counter: int

    def __init__(self, people_min: int = 5, start_value=0):
        self._people_min = people_min
        self._people_hist = [0] * people_min
        self._pallas_counter = start_value

    def try_increment(self, id_: int) -> bool:
        if not self._check_user(id_):
            return False

        self._insert_id(id_)
        self._pallas_counter += 1
        return True

    def __str__(self) -> str:
        thousands_num = PallasCounter._get_thousands_num(self._pallas_counter)
        thousands = PallasCounter._get_thousands_word(self._pallas_counter)
        pallas_num = PallasCounter._get_pallas_num(self._pallas_counter)
        pallas = PallasCounter._get_pallas_word(self._pallas_counter)

        return ' '.join(
            filter(lambda x: len(x) != 0,
                   [thousands_num, thousands, pallas_num, pallas])
        )

    def _insert_id(self, id_: int):
        for i in range(self._people_min - 1, 0, -1):
            self._people_hist[i] = self._people_hist[i - 1]

        self._people_hist[0] = id_

    def _check_user(self, id_: int):
        return not (id_ in self._people_hist)

    def _get_thousands_num(count: int):
        if count < 1000:
            return ''

        count = (count % 1_000_000) // 1000

        word = ''
        counter = count // 100

        if count >= 100:
            word += PallasCounter._HUNDREDS[counter - 1] + ' '

        counter = count % 100

        if counter > 10 and counter < 20:
            word += PallasCounter._TEN_TO_TWENTY[counter - 11] + ' '
        elif counter >= 10:
            word += PallasCounter._TENS[(counter // 10) - 1] + ' '

        counter = count % 10

        if counter > 0 and (count % 100 < 10 or count % 100 > 20) and (count >= 2):
            word += PallasCounter._ONES_F[counter - 1]

        return word.strip()

    def _get_thousands_word(count: int):
        if count < 1000:
            return ''

        count = ((count % 1_000_000) // 1000) % 100
        rem = count % 10

        if rem == 0 or (rem >= 5 and rem <= 9) or (count > 10 and count < 20):
            return 'тысяч'
        elif rem == 1:
            return 'тысяча'
        elif rem > 1 and rem < 5:
            return 'тысячи'

    def _get_pallas_num(count: int):
        count = count % 1000

        word = ''
        counter = count // 100

        if count >= 100:
            word += PallasCounter._HUNDREDS[counter - 1] + ' '

        counter = count % 100

        if counter > 10 and counter < 20:
            word += PallasCounter._TEN_TO_TWENTY[counter - 11] + ' '
        elif counter >= 10:
            word += PallasCounter._TENS[(counter // 10) - 1] + ' '

        counter = count % 10

        if counter > 0 and (count % 100 < 10 or count % 100 > 20):
            word += PallasCounter._ONES_M[counter - 1]

        return word.strip()

    def _get_pallas_word(count: int):
        count = count % 100
        rem = count % 10

        if rem == 0 or (rem >= 5 and rem <= 9) or (count > 10 and count < 20):
            return 'манулов'
        elif rem == 1:
            return 'манул'
        elif rem > 1 and rem < 5:
            return 'манула'
