def custom_fuzz_buzz(_slice=None, start=None, end=None):

    fuzz_buzz_output = []
    for num in _slice[start:end]:
        if num % 3 == 0 and num % 5 == 0:
            fuzz_buzz_output.append('FuzzBuzz')
        elif num % 3 == 0:
            fuzz_buzz_output.append('Fuzz')
        elif num % 5 == 0:
            fuzz_buzz_output.append('Buzz')
        else:
            fuzz_buzz_output.append(num)
    return fuzz_buzz_output


print(custom_fuzz_buzz([3, 7, 6, 15, 20], 1, 5))


class Celsius:
    def __init__(self, temperature):
        self._temp = temperature

    @property
    def temperature(self):
        if self._temp < -273:
            raise ValueError
        return self._temp

    @temperature.setter
    def temperature(self, temp_new_value):
        self._temp = temp_new_value


# Property => getter here
c1 = Celsius(150)
print(c1.temperature)

# Here call setter
c1.temperature = -100
# Call getter again
print(c1.temperature)
