russian_vowels = 'аAeЕёЁиИоОуУыЫэЭюЮяЯ'
russian_consonants = 'бБвВгГдДжЖзЗкКлЛмМнНпПрРсСтТфФхХцЦчЧшШщЩ'
english_vowels = 'aeiouyAEIOUY'
english_consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

russian_vowels_result = []
russian_consonants_result = []
english_vowels_result = []
english_consonants_result = []

letters = (x for x in input("Введите буквы через пробел: "))
for i in letters:
    if i in russian_vowels:
        russian_vowels_result.append(i)
    elif i in russian_consonants:
        russian_consonants_result.append(i)
    elif i in english_vowels:
        english_vowels_result.append(i)       
    elif i in english_consonants:
        english_consonants_result.append(i)
    else:
        continue

print("Русские гласные:", ' '.join(russian_vowels_result))
print("Русские согласные:", ' '.join(russian_consonants_result))
print("Английские гласные:", ' '.join(english_vowels_result))
print("Английские согласные:", ' '.join(english_consonants_result))
