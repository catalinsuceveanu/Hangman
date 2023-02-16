# side-note on words.txt
# every word is expected to have a newline character (\n) at the end. even the last word. (a plain enter on most keyboards)
# words should be lower-case and no characters/spaces

def retrieve_words():
    input_list = []
    with open ('words.txt', 'r') as input:
        for line in input:
            input_list.append(line[0:-1]) # [0:-1] removes the newline character (\n)
    return input_list

word_list = retrieve_words()
