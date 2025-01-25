from injector import singleton, Module, provider
from app.application.handlers.ISongHandler import ISongHandler
from app.application.handlers.SongHandlerImplementation import SongHandlerImplementation
from app.application.mappers.ISongRequestMapper import ISongRequestMapper
from app.application.mappers.ISongResponseMapper import ISongResponseMapper
from app.domain.apis.ISongServicePort import ISongServicePort
from app.domain.spi.IAlbumPersistencePort import IAlbumPersistencePort
from app.domain.useCases.SongUseCases import SongUseCase
from app.infrastructure.outputs.mysql.adapters.AlbumAdapter import AlbumAdapter
from app.infrastructure.outputs.mysql.adapters.SongAdapter import SongAdapter
from app.infrastructure.outputs.mysql.mappers.IAlbumEntityMapper import IAlbumEntityMapper
from app.infrastructure.outputs.mysql.mappers.ISongEntityMapper import ISongEntityMapper
from app.infrastructure.outputs.mysql.repository.ISongRepository import ISongRepository
from app.infrastructure.outputs.mysql.repository.SongRepositoryImplementation import \
    SongRepositoryImplementation
from app.domain.spi.ISongPersistencePort import ISongPersistencePort
from configurationApp.AppAlbumModule import AppAlbumModule


class AppSongModule(Module):
    @singleton
    @provider
    def providerISongRepository(self) -> ISongRepository:
        return SongRepositoryImplementation()

    @singleton
    @provider
    def providerISongPersistencePort(self) -> ISongPersistencePort:
        return SongAdapter(iSongRepository=self.providerISongRepository(), iSongEntityMapper=ISongEntityMapper())

    @singleton
    @provider
    def providerIAlbumPersistencePort(self) -> IAlbumPersistencePort:
        appAlbumModule: AppAlbumModule= AppAlbumModule()
        return AlbumAdapter(iAlbumRepository=appAlbumModule.providerIAlbumRepository(), iAlbumEntityMapper=IAlbumEntityMapper())

    @singleton
    @provider
    def providerISongServicePort(self) -> ISongServicePort:
        return SongUseCase(iSongPersistencePort=self.providerISongPersistencePort(), iAlbumPersistencePort=self.providerIAlbumPersistencePort())

    @singleton
    @provider
    def providerISongHandler(self) -> ISongHandler:
        return SongHandlerImplementation(
            iSongServicePort=self.providerISongServicePort(),
            iSongResponseMapper=ISongResponseMapper(),
            iSongRequestMapper=ISongRequestMapper()
        )