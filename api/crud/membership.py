import models.membership as membership_model, models.user as user_model, models.channel as channel_model
import schemas.membership as membership_schemas


from database import db


# Создание членства
async def create_membership(membership: membership_schemas.MembershipCreate):
    new_membership = membership_model.Membership(**membership.model_dump())
    db.add(new_membership)
    db.commit()
    db.refresh(new_membership)
    return new_membership


# Получение всех членств с пагинацией
def read_memberships(limit: int, offset: int):
    return db.query(membership_model.Membership).offset(offset).limit(limit).all()


# Получение членства по ID
def read_membership(membership_id: int):
    return db.query(membership_model.Membership).filter(membership_model.Membership.id == membership_id).first()


# Обновление членства по ID
def update_membership(membership_id: int, update_data: dict):
    found_membership = read_membership(membership_id)
    if found_membership is None:
        return None
    for key, value in update_data.items():
        if hasattr(found_membership, key):
            setattr(found_membership, key, value)
    db.commit()
    db.refresh(found_membership)
    return found_membership


# Удаление всех членств
def delete_memberships():
    found_memberships = db.query(membership_model.Membership).all()
    if not found_memberships:
        return None
    for membership in found_memberships:
        db.delete(membership)
    db.commit()
    return found_memberships


# Удаление членства по ID
def delete_membership(membership_id: int):
    found_membership = read_membership(membership_id)
    if found_membership is None:
        return None
    db.delete(found_membership)
    db.commit()
    return found_membership



# Получение всех пользователей по channel_id
def read_users_by_channel(channel_id: int, limit: int = 5, offset: int = 0):
    return (
        db.query(user_model.User)
        .join(membership_model.Membership)
        .filter(membership_model.Membership.channel_id == channel_id)
        .offset(offset)
        .limit(limit)
        .all()
    )


# Получение всех каналов по user_id
def read_channels_by_user(user_id: int, limit: int = 5, offset: int = 0):
    return (
        db.query(channel_model.Channel)
        .join(membership_model.Membership)
        .filter(membership_model.Membership.user_id == user_id)
        .offset(offset)
        .limit(limit)
        .all()
    )