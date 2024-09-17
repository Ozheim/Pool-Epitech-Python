# my strings, and the order I'd like them to have
my_strings = ["how", "there", "hello", "you", "are"]
my_ordering = [2, 1, 0, 3, 4]

# sort them
sorted_strings = [x for _, x in sorted(zip(my_ordering, my_strings))]
print(sorted_strings)