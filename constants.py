# the name of fields
KEY_FIELDS = ['A', 'B', 'C', 'D', 'E']

# Define the distribution of rules with 1, 2, 3, 4, and 5 keys
key_distribution = {
    1: 0.01,  # 1% of rules will have 1 key
    2: 0.02,  # 2% of rules will have 2 keys
    3: 0.02,  # 2% of rules will have 3 keys
    4: 0.15,  # 15% of rules will have 4 keys
    5: 0.80   # 80% of rules will have 5 keys
}

# # the name of fields
# KEY_FIELDS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
#
# # Define the distribution of rules with 1, 2, 3, 4, and 5 keys
# key_distribution = {
#     1: 0.01,  # 1% of rules will have 1 key
#     2: 0.02,  # 2% of rules will have 2 keys
#     3: 0.02,  # 2% of rules will have 3 keys
#     4: 0.05,  # 15% of rules will have 4 keys
#     5: 0.10,  # 80% of rules will have 5 keys
#     6: 0.10,  # 80% of rules will have 5 keys
#     7: 0.15,   # 80% of rules will have 5 keys
#     8: 0.15,   # 80% of rules will have 5 keys
#     9: 0.20,   # 80% of rules will have 5 keys
#     10: 0.20   # 80% of rules will have 5 keys
# }


# the max integer that can be used as value for any of the key
max_int = 100
