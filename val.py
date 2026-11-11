def int_val(text):
    legal_choice = False
    while not legal_choice:
        try:
            client_choice = int(input(text))
            legal_choice = True
        except ValueError:
            "int only "
    return client_choice