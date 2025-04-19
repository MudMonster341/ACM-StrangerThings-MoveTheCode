''' Utility functions defined here '''

def generate_email(id: str) -> str:
    # id is 2021A7PS0116U : email is f20210116@dubai.bits-pilani.ac.in
    year = id[0:4]
    roll = id[8:12]
    return "f" + year + roll + "@dubai.bits-pilani.ac.in"

def time_in_words(time: str) -> str:
    m, s = [int(val) for val in time.split(':')]
    time_taken = ""
    if m != 0:
        time_taken += f"{m}min "
    if s != 0:
        time_taken += f"{s}s"
    return time_taken.strip()
