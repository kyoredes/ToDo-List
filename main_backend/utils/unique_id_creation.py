from nanoid import generate

data = "0123456789"


def create_id(*args):
    unique_id = generate(data, 10)
    return unique_id
