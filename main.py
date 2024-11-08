


#dictionary containing letters as keys and morsse code as values

morse_dictionary = {'A': '.---', 'B':'---...', 'C':'--- . --- .', 'D':'--- . .', 'E':'.','F':'. . --- .','G':'--- --- .','H':'. . . .',
'I':'. .', 'J':'. --- --- ---', 'K':'--- . ---', 'L':'. --- . .', 'M':'--- ---', 'N':'--- .', 'O': '--- --- ---', 'P':'. --- --- .', 
'Q':'--- --- . ---', 'R':'. --- .', 'S':'. . .', 'T':'---', 'U':'. . ---',
'V':'. . . ---', 'W':'. --- ---', 'X': '--- . . ---', 'Y':'--- . --- ---',
'Z': '--- --- . .',
1:'. --- --- --- ---', 2:'. . --- --- ---', 3:'... --- ---', 4:'. . . . ---',
5:'. . . . . ', 6:'--- . . . .', 7:'--- --- . . .', 8:'--- --- --- . .',
9: '--- --- --- --- .', 0:'--- --- --- --- ---'

}

user_input = input("Type text to convert to Morse code\n")

user_input = user_input.upper()

converted_word = []

for word in user_input:
    if word in morse_dictionary:
        add_letter = morse_dictionary[word]
        converted_word.append(add_letter)

conversion = "".join(converted_word)


print (conversion)
