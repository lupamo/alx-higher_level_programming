#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        str_len = len(sentence)
        return (str_len, sentence[0])
