def processImageUpload(file, user_id):
    # verificar tipo de archivo
    if not file.name.endswith((".jpg", ".png")):
        raise ValueError("Unsupported file type")

    # cambiamos el tamaño
    image = Image.open(file)
    image = image.resize((200, 200))

    # guardamos
    file_path = f"/images/{user_id}.png"
    image.save(file_path)

    # cambiamos la imagen del usuario
    db.update("users", user_id, {"avatar_path": file_path})