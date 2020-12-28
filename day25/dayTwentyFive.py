with open('dayTwentyFiveInput.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

publicKeyOne = content[0]
publicKeyTwo = content[1]


def find_secret_loop_number(number):
    subject = 7
    val = 1
    loops = 0
    while val != number:
        loops += 1
        val *= subject
        val = val % 20201227
    return loops


def find_encryption_key(public_key, loop_size):
    subject = public_key
    val = 1
    while loop_size > 0:
        loop_size -= 1
        val *= subject
        val = val % 20201227
    return val


loopsOne = find_secret_loop_number(publicKeyOne)
loopsTwo = find_secret_loop_number(publicKeyTwo)

print(find_encryption_key(publicKeyOne, loopsTwo))
print(find_encryption_key(publicKeyTwo, loopsOne))


