from passlib.hash import bcrypt

async def check_password(hashed_password, password) -> bool:
    return bcrypt.verify(password,hashed_password)