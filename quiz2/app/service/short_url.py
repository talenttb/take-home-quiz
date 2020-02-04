import random


def gen_rdm_base_str():
    prefix_ch = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    available_ch = '023456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    result = ''
    for i in range(2):
        result += prefix_ch[random.randrange(len(prefix_ch))]
    for i in range(6):
        result += available_ch[random.randrange(len(available_ch))]

    return result
