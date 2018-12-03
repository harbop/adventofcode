from data import Data

class Adventofcode:
    # december 1st
    def data_sum(self, data):
        return sum(data)

    # december 2nd
    def first_repeat(self, data):
        already_seen_frequencies = dict()

        frequency = 0
        already_seen_frequencies[frequency] = 1

        while 1:
            for index, value in enumerate(data):
                frequency+=value

                if frequency in already_seen_frequencies:
                    return frequency
                else:
                    already_seen_frequencies[frequency] = 1

if __name__ == '__main__':
    advent = Adventofcode()
    print("Dec 1st: sum is ", advent.data_sum(Data.prod))
    print("Dec 1st: first repeat is ", advent.first_repeat(Data.prod))
