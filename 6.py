a = '''
Leonardo da Vinci was an Italian Renaissance artist, architect, engineer
and scientist. He is renowned for his ability to observe and capture nature,
scientific phenomena, and human emotions in all media. Leonardo’s innovative
masterpieces demonstrate a mastery of light, perspective, and overall effect.
His most-loved works include the Mona Lisa portrait and The Last Supper mural.
Considered one of the greatest minds in history, Leonardo's approach to
acquiring knowledge on everything from anatomy to mechanics involved
understanding both the theory and practice of any given subject. In short,
by combining the skills of the artisan with those of the scholar, Leonardo's
vision demonstrated the benefits of a completely new approach to understanding
the present world and just how to best create new and marvellous things for
a future one.
'''

a = a.replace(' ', '')

symbol = ''
result = ''

for _ in range(3):
    counter = 0
    for i in range(2000):
        q = a.count(chr(i))
        if q >= counter:
            counter = q
            symbol = chr(i)
    result += '{} - {}, '.format(symbol, counter)
    a = a.replace(symbol, '')
    
print(result[:-2])

        
        
