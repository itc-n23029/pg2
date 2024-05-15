def comma(lst):
    if len(lst) == 0:
        return 'You gave me nothing.'
    elif len(lst) == 1:
        return lst[0]
    else:
        return ', '.join(lst[:-1]) + ', and ' + lst[-1]

spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma(spam))

