#!/usr/bin/python

import sys

# check if input_c is english char
def is_english(input_c):
    a_int=ord('a')
    z_int=ord('z')
    input_int=ord(input_c)
    if input_int >= a_int and input_int <= z_int:
        return True
    else:
        return False

# load dict from file
def load_dict(dict_file):
    dict={}
    f = file(dict_file, 'r')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        word=""
        pinyin=""
        # parse chinese word
        for i in range( 0, len(line)):
            if is_english(line[i]) or  line[i] == '*':
                word=line[0:i]
                line=line[i:]
                break
        # parse its pinyin
        pinyin_begin=-1
        for i in range( 0, len(line)):
            # find the beginning of pinyin
            if is_english(line[i]) and pinyin_begin == -1:
                pinyin_begin = i
            # find the ending of pinyin
            if not is_english(line[i]) and pinyin_begin != -1:
                pinyin=line[pinyin_begin:i]
                break
        dict[word] = pinyin
    # close file
    f.close()
    return dict

dict_file = 'Winpy.txt'
dict = load_dict(dict_file)

for word, pinyin in dict.items():
    line=raw_input()
    if len(line) == 0:
        break
    if line in dict:
        print dict[line]
