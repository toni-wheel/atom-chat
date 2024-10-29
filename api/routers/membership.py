from fastapi import APIRouter, Depends, HTTPException
from typing import List, Annotated
import crud.membership as membership_crud
import schemas.membership as membership_schemas
import schemas.user as user_schemas
import schemas.channel as channel_schemas


membership_router = APIRouter(prefix="/memberships", tags=["memberships"])


# Создание нового членства
@membership_router.post("/", response_model=membership_schemas.MembershipOut)
async def create_membership(
    membership: Annotated[membership_schemas.MembershipCreate, Depends()]
):
    return await membership_crud.create_membership(membership)


# Получение всех членств
@membership_router.get("/", response_model=List[membership_schemas.MembershipOut])
def read_memberships(limit: int = 5, offset: int = 0):
    return membership_crud.read_memberships(limit, offset)


# Обновление членства по ID
@membership_router.patch("/{membership_id}", response_model=membership_schemas.MembershipOut)
def update_membership(
    membership_id: int,
    update_data: Annotated[membership_schemas.MembershipUpdate, Depends()],
):
    updated_membership = membership_crud.update_membership(
        membership_id, update_data.dict(exclude_unset=True)
    )
    if updated_membership is None:
        raise HTTPException(status_code=404, detail="Членство не найдено")
    return updated_membership


# Удаление всех членств
@membership_router.delete("/", response_model=List[membership_schemas.MembershipOut])
def delete_memberships():
    memberships = membership_crud.delete_memberships()
    if memberships is None:
        raise HTTPException(status_code=404, detail="Членства не найдены")
    return memberships


# Удаление членства по ID
@membership_router.delete("/{membership_id}", response_model=membership_schemas.MembershipOut)
def delete_membership(membership_id: int):
    membership = membership_crud.delete_membership(membership_id)
    if membership is None:
        raise HTTPException(status_code=404, detail="Членство не найдено")
    return membership


# Получение всех пользователей по channel_id
@membership_router.get("/channel/{channel_id}/users", response_model=List[user_schemas.User])
def read_users_by_channel(channel_id: int, limit: int = 5, offset: int = 0):
    users = membership_crud.read_users_by_channel(channel_id, limit, offset)
    if not users:
        raise HTTPException(status_code=404, detail="Пользователи не найдены для данного канала")
    return users


# Получение всех каналов по user_id
@membership_router.get("/user/{user_id}/channels", response_model=List[channel_schemas.ChannelOut])
def read_channels_by_user(user_id: int, limit: int = 5, offset: int = 0):
    channels = membership_crud.read_channels_by_user(user_id, limit, offset)
    if not channels:
        raise HTTPException(status_code=404, detail="Каналы не найдены для данного пользователя")
    return channels
