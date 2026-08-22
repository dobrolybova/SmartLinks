from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from rule_service.rule_schemas import Rules


class RuleDbHandler:
    def __init__(self):
        self.engine = create_async_engine("postgresql+asyncpg://yulia:yulia@localhost:5438/rules", future=True, echo=False)
        self.async_session = sessionmaker(self.engine, class_=AsyncSession)

    async def add(self, data: Rules) -> None:
        async with self.async_session() as session, session.begin():
            session.add(data)
            await session.commit()

    async def delete(self, rule: str) -> None:
        async with self.async_session() as session, session.begin():
            stmt = delete(Rules).where(Rules.rule == rule)
            await session.execute(stmt)
            await session.commit()
