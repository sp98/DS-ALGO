"""
Hashtable implementation in python
"""


def hash_function_str(key, table_size):
    """ Hash function to generate index using string type key """
    ov = 0
    for i in range(len(key)):
        ov = ov + i + ord(key[i])

    print(ov)


if __name__ == '__main__':
    hash_function_str('santosh', 11)
    hash_function_str('oshsant', 11)
