#!/usr/bin/env python3

def return_evens(num_list):
    new_num_list = [i for i in num_list if i % 2 == 0]
    return new_num_list

def make_exclamation(sentence_list):
    return [f'{sentence}!' for sentence in sentence_list]