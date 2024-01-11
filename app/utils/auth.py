from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.services.user_service import UserService

security = HTTPBearer()


async def has_access(userUUID: HTTPAuthorizationCredentials = Depends(security)):
    """
        Function that is used to validate the token in the case that it requires it
    """
    uuid = userUUID.credentials
    user = await UserService().get_user(uuid)
    if user is None :
        raise HTTPException(status_code=403, detail="User not authorized to access all candidates")

