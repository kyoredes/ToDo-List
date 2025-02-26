import hashlib
from nanoid import generate

alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
unique_id = generate(alphabet, 21)


def create_id(*args):
    if args:
        data_string = "".join(args)
        return hashlib.sha256(data_string.encode("utf-8")).hexdigest()
    return unique_id
