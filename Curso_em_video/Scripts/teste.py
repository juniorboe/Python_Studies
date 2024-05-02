def teste(c):
    return help(c)


while True:
    prompt = str(input('Digite algo: ')).strip()
    if prompt == 'FIM':
        break
    help(prompt)
    
