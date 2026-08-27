from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from redirect_service.redirect_schemas import Rules


class RedirectDbHandler:   # pylint: disable=too-few-public-methods
    def __init__(self):
        self.engine = create_async_engine("postgresql+asyncpg://yulia:yulia@localhost:5438/rules", future=True, echo=False)
        self.async_session = sessionmaker(self.engine, class_=AsyncSession)

    async def fetch_all(self) -> list[Rules]:
        result = await self.async_session().scalars(select(Rules).order_by(Rules.priority))
        return result.all()
