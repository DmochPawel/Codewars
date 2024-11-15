
# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    new_list = []
    
    list = text.split()
    for word in list:
        if word.isalpha() and len(word) > 1:
            new_word = word[1:] + word[0] + "ay"
            new_list.append(new_word)
        elif word.isalnum() and len(word) == 1:
            new_word = word[0] + "ay"
            new_list.append(new_word)
        else:
            new_list.append(word)
    new_text =" ".join(new_list)
    return new_text

print(pig_it('Pig latin is cool') =='igPay atinlay siay oolcay')
print(pig_it('This is my string') == 'hisTay siay ymay tringsay')
print(pig_it("O tempora o mores !") =='Oay emporatay oay oresmay !')
print(pig_it('Quis custodiet ipsos custodes ?') == 'uisQay ustodietcay psosiay ustodescay ?')