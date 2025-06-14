import uuid


def generate_short_url():
    return str(uuid.uuid4())[:8]
