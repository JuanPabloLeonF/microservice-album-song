from injector import singleton, provider, Module

from app.src.application.handlers.i_handler_song import ISongHandler
from app.src.application.handlers.implementation_handler_song import ImplementationSongHandler
from app.src.application.mappers.i_mapper_song_application import IMapperSongApplication
from app.src.domain.persistence.i_persistence_song import ISongPersistence
from app.src.domain.services.i_service_song import ISongService
from app.src.domain.useCases.use_case_song import UseCaseSong
from app.src.infrastructure.inputs.rest.mappers.i_mapper_song_controller import IMapperSongController
from app.src.infrastructure.outputs.mysql.adapters.adatper_song import AdapterSong
from app.src.infrastructure.outputs.mysql.mappers.i_mapper_song_entity import IMapperSongEntity
from app.src.infrastructure.outputs.mysql.repositories.i_song_repository import ISongRepository
from app.src.infrastructure.outputs.mysql.repositories.implementation_song_repository import \
    ImplementationSongRepository


class ModuleInjectorSong(Module):

    @singleton
    @provider
    def providerISongRepository(self) -> ISongRepository:
        return ImplementationSongRepository()

    @singleton
    @provider
    def providerIPersistencePortSong(self) -> ISongPersistence:
        return AdapterSong(
            iSongRepository=self.providerISongRepository(),
            iMapperSongEntity=IMapperSongEntity()
        )

    @singleton
    @provider
    def providerIServicePortSong(self) -> ISongService:
        return UseCaseSong(iSongPersistence=self.providerIPersistencePortSong())

    @singleton
    @provider
    def providerIHandlerSong(self) -> ISongHandler:
        return ImplementationSongHandler(
            iSongService=self.providerIServicePortSong(),
            iMapperSongApplication=IMapperSongApplication()
        )