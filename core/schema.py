import strawberry
from strawberry import relay
from strawberry.types import Info
from strawberry.django import type
from .models import User, DeployedApp
from enum import Enum
from django.db import models

@strawberry.enum
class PlanEnum(Enum):
    HOBBY = "HOBBY"
    PRO = "PRO"

@strawberry.django.type(User)
class UserType:
    id: relay.NodeID[str]
    username: str
    plan: PlanEnum

@strawberry.django.type(DeployedApp)
class DeployedAppType:
    id: relay.NodeID[str]
    active: bool

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def upgrade_account(self, user_id: str) -> UserType:
        user = await User.objects.aget(pk=user_id)  # type: ignore
        user.plan = "PRO"
        await user.asave()
        return user

    @strawberry.mutation
    async def downgrade_account(self, user_id: str) -> UserType:
        user = await User.objects.aget(pk=user_id)  # type: ignore
        user.plan = "HOBBY"
        await user.asave()
        return user

@strawberry.type
class Query:
    node: relay.Node = relay.node()

schema = strawberry.Schema(query=Query, mutation=Mutation, types=[UserType, DeployedAppType])
