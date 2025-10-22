from .models import User

def map_user_in_to_model(dto_validated_data) -> User:
    return User(**dto_validated_data)
