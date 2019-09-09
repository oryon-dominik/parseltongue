import hashids
import string

""" 

Luhn mod n

Append a number to your hash, that validates if the hash is a valid hash
derived from: https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/luhn.py

"""

class Luhn():
    def __init__(self, hash):
        self.hash = hash
        self.alphabet = string.ascii_letters + string.digits

    def checksum(self, hash):
        """Calculate the Luhn checksum over the provided hash. The checksum
        is returned as an int. Valid numbers should have a checksum of 0."""
        n = len(self.alphabet)
        number = tuple(self.alphabet.index(i)
                    for i in reversed(str(hash)))
        return (sum(number[::2]) +
                sum(sum(divmod(i * 2, n))
                    for i in number[1::2])) % n

    def is_valid(self):
        """Check if the instanced hash passes the Luhn checksum."""
        return self.checksum(self.hash) == 0

    def calc_check_digit(self):
        """Calculate the extra digit that should be appended to the provided hash to
        make it a valid hash."""
        ck = self.checksum(str(self.hash) + self.alphabet[0])
        return self.alphabet[-ck]


# generate hash-ids from integer-ids that are 'valid hashes'
Hash = hashids.Hashids(salt='yoursalt')
ids = [1, 1337, 1_000_000, 11_234_567_891_234]

for _int in ids:
    hash_id = Hash.encode(_int)
    luhn = Luhn(hash_id)
    full_id = f"{hash_id}{luhn.calc_check_digit()}"
    # Luhn(full_id).is_valid()
