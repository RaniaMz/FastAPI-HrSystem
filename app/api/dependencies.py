# app/api/dependencies.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """
    Get the current user based on the provided OAuth2 token.

    Args:
        token (str): OAuth2 token from the request.

    Returns:
        User: Current user.
    """
    # Example logic to verify the token and retrieve the user
    # You might want to implement your own authentication logic here
    # This is just a placeholder example

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Example logic to verify the token and retrieve the user
    # Replace this with your authentication logic
    # For example, you might use a token decoding library like PyJWT
    # or query a database to verify the token and get user details
    if token != "fake_access_token":
        raise credentials_exception

    # Assuming you have a User model with appropriate attributes
    # Replace this with your own logic to get the user based on the token
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", uuid="fake_user_id")

    return user
