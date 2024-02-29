from random import choice, randint



def get_responses(user_input: str) -> str:
    lowered = user_input.lower()

    if lowered == '':
        return "You're silent"
    else:
        return 'Hello'
