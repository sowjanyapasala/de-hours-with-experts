#!/usr/bin/python3
import pydoc
import sys
import os

# Caesar encoding, for use with decoding below
ENCODING = {
    'y': 'a',
    'h': 'b',
    'v': 'c',
    'x': 'd',
    'k': 'e',
    'p': 'f',
    'z': 'g',
    's': 'h',
    'a': 'i',
    'b': 'j',
    'e': 'k',
    'w': 'l',
    'u': 'm',
    'q': 'n',
    'n': 'o',
    'l': 'p',
    'm': 'q',
    'f': 'r',
    'o': 's',
    'i': 't',
    'g': 'u',
    'j': 'v',
    't': 'w',
    'd': 'x',
    'r': 'y',
    'c': 'z',
    '3': '0',
    '8': '1',
    '4': '2',
    '0': '3',
    '2': '4',
    '7': '5',
    '5': '6',
    '9': '7',
    '1': '8',
    '6': '9'
 }

"""An ingredient has an amount and a description.
For example: an Ingredient could have "1 cup" as the amount and "butter" as the description."""
class Ingredient():
    def __init__(self, amount, description) -> None:
        self.amount = amount
        self.description = description


def decode_string(str):
    """Given a string named str, use the Caesar encoding above to return the decoded string."""
    # Loop through each letter in string, then replaces using the encoding provided
    # Still getting some funny outputs with this, honestly struggled with this and tried to limit how much help I had
    for letter in str:
        if letter in ENCODING:
            str = str.replace(letter, ENCODING[letter])
        else:
            pass
    return str


def decode_ingredient(line):
    """Given an ingredient, decode the amount and description, and return a new Ingredient"""
    # Split line and assign to variable, in this case, we can assume before split is amount, after split is description
    amount_split, description_split = line.split('#')
    ingredient = Ingredient(decode_string(amount_split), decode_string(description_split))
    return ingredient.amount, ingredient.description


def main():
    """A program that decodes a secret recipe"""
    # Opens recipe, decodes lines then writes to new file
    with open("secret_recipe.txt", "r") as recipe:
        lines = [line.rstrip() for line in recipe]
        for line in lines:
            with open('decoded_recipe.txt', 'a') as write_file:
                write_file.write(f'{decode_ingredient(line)}\n')

if __name__ == "__main__":
    main()
