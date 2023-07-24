from operations import streebog_256_512

M1 = '323130393837363534333231303938373635343332313039383736353433323' \
     '130393837363534333231303938373635343332313039383736353433323130'

M2 = 'fbe2e5f0eee3c820fbeafaebef20fffbf0e1e0f0f520e0ed20e8ece0ebe5f0f' \
     '2f120fff0eeec20f120faf2fee5e2202ce8f6f3ede220e8e6eee1e8f0f2d1202ce8f0f2e5e220e5d1'

hash_512_1 = streebog_256_512(M1, '1')
hash_256_1 = streebog_256_512(M1, '2')

hash_512_2 = streebog_256_512(M2, '1')
hash_256_2 = streebog_256_512(M2, '2')

with open('testing.txt', 'w', encoding='utf-8') as f:
    f.write(f'{hash_512_1}\n{hash_256_1}\n\n{hash_512_2}\n{hash_256_2}')


