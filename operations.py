from constants import *

def X(k: str, a: str) -> str:

    return hex(int(k, 16) ^ int(a, 16))[2:].zfill(128)
    
    

def S(a: str) -> str:
    result = ''

    for i in range(0, len(a), 2):
        sub_block = a[i: i + 2]
        result += hex(sBox[int(sub_block, 16)])[2:].zfill(2)

    return result


def P(a: str) -> str:

    tmp = ['' for _ in range(64)]
    k = 0

    for i in range(0, len(a), 2):
        sub_block = a[i: i + 2]
        tmp[tao[i - k]] = sub_block
        k += 1

    result = ''.join(tmp)
    return result


def L(a: str) -> str:

    result = []
    
    for bits_64 in [bin(int(a[i: i + 16], 16))[2:].zfill(64) for i in range(0, len(a), 16)]:
        c = 0

        for i in range(len(bits_64)):
            
            if bits_64[i] == '1':
                c ^= int(A_matrix[i], 16)

        result.append(hex(c)[2:].zfill(16))

    return ''.join(result)




def E(K: str, m: str) -> str:
    
    for i in range(13):

        if i != 12:

            m = L(P(S(X(K, m))))

            K = L(P(S(X(K, C_Constants[i]))))


        else:
            m = X(K, m)


    result = m

    return result


def g_function(h: str, m: str, N: str = '0' * 128) -> str:
    
    return X(X(E(L(P(S(X(h, N)))), m), h), m)

def streebog_256_512(M: str, flag: str) -> str:

    
    Z_2n = 2 ** 512

    initializationVector512 = '0' * (512 // 4)

    initializationVector256 = '01' * 64


    if flag == '1':
        h = initializationVector512

    elif flag == '2':
        h = initializationVector256

    S = '0' * (512 // 4)
    N = S
    while len(M) * 4 >= 512:
        m = M[len(M) - 128:]
        h = g_function(h, m)
        N = hex((int(N, 16) + 512) % Z_2n)[2:].zfill(128)
        S = hex((int(S, 16) + int(m, 16)) % Z_2n)[2:].zfill(128)
        M = M[:len(M) - 128]


    m = hex(int('0' * (511 - len(M) * 4) + '1', 2))[2:].zfill(128 - len(M)) + M
    h = g_function(h, m, N)
    N = hex((int(N, 16) + len(M) * 4) % Z_2n)[2:].zfill(128)
    S = hex((int(S, 16) + int(m, 16)) % Z_2n)[2:].zfill(128)
    h = g_function(h, N)

    if flag == '1':
        h = g_function(h, S)

    elif flag == '2':
        h = g_function(h, S)[:64]

    return h





