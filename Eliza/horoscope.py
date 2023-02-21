import pyaztro


class HoroscopeGenerator:
    def __init__(self):
        self.day = None
        self.month = None

    def get_horoscope_daily(self):
        self.get_birth_info()
        zodiac_sign = self.get_zodiac_sign()
        prediction = pyaztro.Aztro(sign=zodiac_sign)
        horoscope = f'Mood:\t\t {prediction.mood},' \
                    f' \nLucky number:\t {prediction.lucky_number} ' \
                    f'\nLucky time:\t {prediction.lucky_time} ' \
                    f'\nLucky color:\t {prediction.color} ' \
                    f'\nCompatibility:\t {prediction.compatibility} ' \
                    f'\nPrediction:\t {prediction.description}'
        return horoscope

    def get_birth_info(self):
        while True:
            try:
                self.day = int(input('What is your birthday day number ? : '))
                break
            except ValueError:
                print("Unable to process the entered data, please try again")
        while True:
            try:
                self.month = int(input('What is your birthday month number ? : '))
                break
            except ValueError:
                print("Unable to process the entered data, please try again")

    def get_zodiac_sign(self):
        if (self.day >= 21 and self.day <= 18 and self.month == 1) or (self.month == 4 and self.day >= 1 and self.day <= 19):
            return "aries"
        elif (self.day >= 20 and self.day <= 30 and self.month == 4) or (self.month == 5 and self.day >= 1 and self.day <= 20):
            return "taurus"
        elif (self.day >= 21 and self.day <= 31 and self.month == 5) or (self.month == 6 and self.day >= 1 and self.day <= 21):
            return "gemini"
        elif (self.day >= 22 and self.day <= 30 and self.month == 6) or (self.month == 7 and self.day >= 1 and self.day <= 22):
            return "crayfish"
        elif (self.day >= 23 and self.day <= 31 and self.month == 7) or (self.month == 8 and self.day >= 1 and self.day <= 22):
            return "leo"
        elif (self.day >= 23 and self.day <= 31 and self.month == 8) or (self.month == 9 and self.day >= 1 and self.day <= 22):
            return "virgo"
        elif (self.day >= 23 and self.day <= 30 and self.month == 9) or (self.month == 10 and self.day >= 1 and self.day <= 23):
            return "libra"
        elif (self.day >= 24 and self.day <= 31 and self.month == 10) or (self.month == 11 and self.day >= 1 and self.day <= 22):
            return "scorpio"
        elif (self.day >= 23 and self.day <= 30 and self.month == 11) or (self.month == 12 and self.day >= 1 and self.day <= 21):
            return "sagittarius"
        elif (self.day >= 22 and self.day <= 31 and self.month == 12) or (self.month == 1 and self.day >= 1 and self.day <= 20):
            return "capricorn"
        elif (self.day >= 21 and self.day <= 31 and self.month == 1) or (self.month == 2 and self.day >= 1 and self.day <= 18):
            return "aquarius"
        elif (self.day >= 19 and self.day <= 29 and self.month == 2) or (self.month == 3 and self.day >= 1 and self.day <= 20):
            return "pisces"

