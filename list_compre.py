# squares = []
# for i in range(10):
#     squares.append(i*i)
# print(squares)

# squares = [i*i for i in range(10)]
# print(squares)

VAT_RATE = 0.23
prices_net = [1.09, 23.56, 57.84, 4.56]
def get_gross_price(price):
    return price * (1 + VAT_RATE)

# gross_price = map(get_gross_price, prices_net)
# print(list(gross_price))

# gross_price = [get_gross_price(i) for i in prices_net]
# print(gross_price)

# gross_price = [lambda a: a+4 for i in range(4)]
# print(gross_price[-2])



# sentence = 'The rocket, who was named Ted, came back \
# from Mars because he missed his friends.'
# def is_consonant(letter):
#     vowels = 'aeiou'
#     return letter.isalpha() and letter.lower() not in vowels
# consonants = [i for i in sentence if is_consonant(i)]
# print(consonants)

# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# prices = [i if i > 0 else 0 for i in original_prices]
# print(prices)

# quote = "life, uh, finds a way"
# unique_vowels = {i for i in quote if i in 'aeiou'}
# print(unique_vowels)

# squares = {i: i * i for i in range(10)}
# print(squares)
#
# sample = {"a": 1, "b": 2, "c": 3}
# sample_rev = {v: k for k, v in sample.items()}
# print(sample_rev)

# elem = [lambda x: x + a for a in range(100)][0]
# print(elem(1))

