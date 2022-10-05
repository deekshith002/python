# use map to convert all string to upper case
def convert_upper(chars: str):
    return (ord(chars) - 32) if chars.isalpha() else -1


ls = ['a', 'b', 'c', 'e', 'f','z']
for i in map(convert_upper, ls):
    print(chr(i)) #chr is used to return charcter for the ascii value
