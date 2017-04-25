import SymbolMap

class RomanToDecimalConverter:

    def convert(self, input):

        chars = list(input)

        newList = self.convert_seq(chars)
        print(newList)

        newList = self.remove_subtractive_notation(newList)
        print(newList)

        conversion = sum(newList)
        print(conversion)

    def remove_subtractive_notation(self, list):

        cleanedList = []
        i = 0;
        while i  < len(list):
            print(i)
            if i == len(list) - 1:
                cleanedList.append(list[i])
            elif list[i] < list[i+1]:
                cleanedList.append(list[i+1] - list[i])
                i += 1
            else:
                cleanedList.append(list[i])
            i += 1

        return cleanedList

    def convert_seq(self, list):

        newList = []

        index = 0
        while(index < len(list)):
            symbol = list[index]
            symbolCount, seqValue = self.compress(list, symbol, index)
            index += symbolCount
            newList.append(seqValue)

        return newList


    def compress(self, list, symbol, start):

        symbolCount = 0
        for i in range(start, len(list)): #or a while loop
            if symbol == list[i]:
                symbolCount += 1
            else:
                break

        seqValue = symbolCount * SymbolMap.symbolValues[symbol]

        return symbolCount, seqValue




converter = RomanToDecimalConverter()
converter.convert("mmmcmxxiv")

# print(converter.compress(["m","m","m","c", "m"], "m", 0))
# print(converter.compress(["m","m","m","c"], "c", 4))