from links_gen import get_rand_links

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return empty

    elif '/wg' in lowered:
        return get_rand_links()