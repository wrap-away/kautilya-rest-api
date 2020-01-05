import hashlib
import random
import string

JITSI_ROOT = 'https://meet.jit.si/'
POPULATION = string.ascii_letters
RANDOM_STRING_LEN = 32

get_random_string = lambda n: ''.join(random.sample(POPULATION, n))
hashing_function = lambda x: hashlib.sha1(x).hexdigest()

"""  
    get_random_hash returns a SHA1 hash of 32 random ASCII characters.

    @return str: SHA1 Hex Digest.
"""
get_random_hash = lambda : hashing_function(bytes(get_random_string(RANDOM_STRING_LEN), encoding='utf-8')) 

""" 
    get_jitsi_link creates a new jitsi meet link in the format
    https://meet.jit.si/<meeting_url>
    
    meeting_room_name: Jitsi Meeting Room name Computed using SHA1 of 32 randomly selected ASCII Characters.
    @return str: meeting_room_name
"""
def generate_room_name():
    return get_random_hash()
