def validate(date_str):
    parts = date_str.split("-")
    if len(parts) != 3:
        return False
    if parts[1] < 1 or parts[1] > 12:
        return False
    return True