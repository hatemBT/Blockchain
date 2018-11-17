from hashlib import sha256
import json



def hash_string_256(string):

    return sha256(string).hexdigest()



def hash_block(block):

    #must include sort keys because cannot garantie the order of the dict.
    hachebal_block= block.__dict__.copy()
    return sha256(json.dumps(hachebal_block, sort_keys=True).encode()).hexdigest()

