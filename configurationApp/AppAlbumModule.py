from injector import singleton, Module, provider

from app.application.handlers.IAlbumHandler import IAlbumHandler
from app.application.handlers.AlbumHandlerIMplementation import AlbumHandlerImplementation
from app.application.mappers.IAlbumResponseMapper import IAlbumResponseMapper
from app.domain.apis.IAlbumServicePort import IAlbumServicePort
from app.domain.spi.IAlbumPersistencePort import IAlbumPersistencePort
from app.domain.useCases.AlbumUseCases import AlbumUseCase
from app.infrastructure.outputs.sqlites.adapters.AlbumAdapter import AlbumAdapter
from app.infrastructure.outputs.sqlites.mappers.IAlbumEntityMapper import IAlbumEntityMapper
from app.infrastructure.outputs.sqlites.repository.AlbumRepositoryImplementation import AlbumRepositoryImplementation
from app.infrastructure.outputs.sqlites.repository.IAlbumRepository import IAlbumRepository
from app.application.mappers.IAlbumRequestMapper import IAlbumRequestMapper


class AppAlbumModule(Module):

    @singleton
    @provider
    def providerIAlbumRepository(self) -> IAlbumRepository:
        return AlbumRepositoryImplementation()

    @singleton
    @provider
    def providerIAlbumPersistencePort(self) -> IAlbumPersistencePort:
        return AlbumAdapter(iAlbumRepository=self.providerIAlbumRepository(), iAlbumEntityMapper=IAlbumEntityMapper())

    @singleton
    @provider
    def providerIAlbumServicePort(self) -> IAlbumServicePort:
        return AlbumUseCase(iAlbumPersistencePort=self.providerIAlbumPersistencePort())

    @singleton
    @provider
    def providerIAlbumHandler(self) -> IAlbumHandler:
        return AlbumHandlerImplementation(
            iAlbumServicePort=self.providerIAlbumServicePort(),
            iAlbumResponseMapper=IAlbumResponseMapper(),
            iAlbumRequestMapper=IAlbumRequestMapper()
        )