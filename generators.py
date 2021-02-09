# def csv_reader(file_name):
#     for row in open(file_name, "r"):
#         yield row
#
# file_name = 'shops.csv'
# csv_gen = (row for row in open(file_name))
# # print(next(csv_gen))
# for elem in csv_gen:
#     print(elem)
# print(next(csv_gen))


# import sys
# nums_squared_lc = [i * 2 for i in range(10000)]
# print(sys.getsizeof(nums_squared_lc))
#
# nums_squared_gc = (i ** 2 for i in range(10000))
# print(sys.getsizeof(nums_squared_gc))

# import cProfile
# cProfile.run('sum([i * 2 for i in range(1000000)])')
# cProfile.run('sum((i * 2 for i in range(1000000)))')

# file_name = "tech.csv"
# lines = (line for line in open(file_name))
# list_line = (s.rstrip().split(",") for s in lines)
# cols = next(list_line)
# company_dicts = (dict(zip(cols, data)) for data in list_line)
# funding = (
#     int(company_dict["raisedAmt"])
#     for company_dict in company_dicts
#     if company_dict["round"] == "a"
# )
# total_series_a = sum(funding)
# print(f"Total series A fundraising: ${total_series_a}")

class Numbers:
    def __init__(self, max, n=5):
        self.n = n
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = self.n
        self.n += 1
        return result


for i in Numbers(15):
    print(i)
