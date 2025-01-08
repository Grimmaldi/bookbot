def main():
    book = 'books/frankenstein.txt'
    with open(book, 'r') as f:
        file_contents = f.read()
    print(f'--- Begin report of {book} ---')
    print(f'{count_words(file_contents)} words found in the document\n')
    for c in sorted(list(count_characters(file_contents).items()), key=lambda x: x[1], reverse=True):
        if c[0] in 'abcdefghijklmnopqrstuvwxyz':
            print(f"The '{c[0]}' character was found {c[1]} times")
    print('--- End report ---')

def count_words(text):
    return len(text.split())

def count_characters(text):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

main()