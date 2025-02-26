import hashlib
from nanoid import generate

alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def create_id(*args):
    if args:
        data_string = "".join(args)
        return hashlib.sha256(data_string.encode("utf-8")).hexdigest()
    unique_id = generate(alphabet, 21)
    return unique_id
