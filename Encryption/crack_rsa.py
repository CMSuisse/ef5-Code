from time import time

public_e = 1
public_n = 1

MSG_CONTENTS = []
DECRYPT_CONTENTS = []

START_TIME = time()

private_p = 1

for private_p_candidate in range(2, public_n//2):
    if private_p_candidate % 2 == 0:
        continue
    for i in range(2, private_p_candidate//2):
        if private_p_candidate % i == 0:
            break
    else:
        private_p = private_p_candidate
    if not public_n % private_p_candidate == 0:
        private_p = 1
    else:
        break

private_q = public_n / private_p
PHI_VALUE = (private_p - 1)*(private_q - 1)
private_d = 2

while not public_e*private_d % PHI_VALUE == 1:
    private_d += 1

for M in MSG_CONTENTS:
    S = M**private_d
    DECRYPT_CONTENTS.append(chr(S % public_n))

END_TIME = time()

print(DECRYPT_CONTENTS)
print("That took {} seconds".format(END_TIME - START_TIME))
print(private_d, private_q, private_p)