import SymbolMap

class DecimalToRomanConverter:
    """Need to extend to use substractive notation"""

    valuesToSymbolMap = {1000:"m", 500:"d", 100:"c", 50:"l", 10:"x", 5:"v", 1:"i"}

    def convert(self, valueToConvert):
        valueToConvert, roman = self.add_value(valueToConvert, "", "m")
        valueToConvert, roman = self.add_value(valueToConvert, roman, "c")
        valueToConvert, roman = self.add_value(valueToConvert, roman, "x")
        valueToConvert, roman = self.add_value(valueToConvert, roman, "i")
        print("Roman: " + roman)

    def get_count(self, unit, valueToConvert):
        return int(valueToConvert / unit)

    def add_value(self, valueToConvert, runningTotal, symbol):
        unit = SymbolMap.symbolValues[symbol]
        count = self.get_count(unit, valueToConvert)
        runningTotal += symbol * count
        valueToConvert -= count * unit
        return valueToConvert, runningTotal

converter = DecimalToRomanConverter()
converter.convert(3224)
