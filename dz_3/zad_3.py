k = 'ноутбук'


k = k.upper()
sum = 0
word = {1: 'AEIOULNSTR-АВЕИНОРСТ', 2: 'DG-ДКЛМПУ', 3: 'BCMP-БГЁЬЯ', 4: 'FHVWY-ЙЫ', 5: 'K-ЖЗХЦЧ', 8: 'JX-ШЭЮ', 10: 'QZ-ФЩЪ'}
for i in k:
    for j in word:
        if i in word[j]:
            sum += j
print(sum)