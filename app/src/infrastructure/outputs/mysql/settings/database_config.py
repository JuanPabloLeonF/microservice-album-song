from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
from app.configuration.enviroments_config import DATABASE_URL
from app.configuration.exceptions_personalities import ErrorSessionDatabase

class DatabaseConfiguration:
    BaseModels = declarative_base()
    _engine = None
    _SessionLocal = None

    @classmethod
    async def configDatabase(cls):
        try:
            cls._engine = create_async_engine(DATABASE_URL, echo=True, future=True)
            cls._SessionLocal = sessionmaker(
                bind=cls._engine,
                class_=AsyncSession,
                expire_on_commit=False
            )
            async with cls._engine.begin() as conn:
                await conn.run_sync(cls.BaseModels.metadata.create_all)
        except OperationalError as error:
            cls._engine = None
            cls._SessionLocal = None
            raise ErrorSessionDatabase(str(error))
        except Exception as error:
            cls._engine = None
            cls._SessionLocal = None
            raise ErrorSessionDatabase(str(error))

    @classmethod
    def getSession(cls) -> AsyncSession:
        if cls._SessionLocal is None:
            raise ErrorSessionDatabase("❌ La base de datos no ha sido inicializada. Verifica la conexión.")

        return cls._SessionLocal()

    @staticmethod
    async def runDatabase():
        await DatabaseConfiguration.configDatabase()
