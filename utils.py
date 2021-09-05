def log(type: str, string_to_log: str):
    type = type.lower()
    accepted_types = {
        'error',
        'info'
    }
    if type not in accepted_types:
        raise ValueError("Type must be one of {}".format(
            accepted_types
        ))

    #listens for error log
    elif type == 'error':
        with open('logging\\errors.txt', 'w+') as f:
            f.write(string_to_log)
            return True

    #listens for info log
    elif type == 'info':
        with open('logging\\info.txt', 'w+') as f:
            f.write(string_to_log)
            return True


def floor_elo(elo_input: int) -> int:
    elo_ratings = [2800, 2600, 2400, 2200, 2000, 1800, 1600, 800, 400, 100]
    elo_counter = 0
    for elo_rating in elo_ratings[::-1]:
        if elo_input >= elo_rating:
            elo_counter = elo_rating
    return elo_counter
    