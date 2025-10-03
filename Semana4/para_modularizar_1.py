def registerUser(form_data):
    # validamos...
    if not form_data.get("email") or "@" not in form_data["email"]:
        raise ValueError("Invalid email")
    if len(form_data.get("password", "")) < 8:
        raise ValueError("Password too short")
    
    # creamos un diccionario de datos 
    user = {
        "email": form_data["email"],
        "password_hash": hash_password(form_data["password"]),
        "created_at": datetime.now()
    }

    # guardamos el dato de usuario en un archivo.
    with open("users.txt", "a") as f:
        f.write(json.dumps(user) + "\n")

    return "User registered"