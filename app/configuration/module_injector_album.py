from injector import singleton, provider, Module

from app.src.application.handlers.i_handler_album import IAlbumHandler
from app.src.application.handlers.implementation_handler_album import ImplementationAlbumHandler
from app.src.application.mappers.i_mapper_album_application import IMapperAlbumApplication
from app.src.domain.persistence.i_persistence_album import IAlbumPersistence
from app.src.domain.services.i_service_album import IAlbumService
from app.src.domain.useCases.use_case_album import UseCaseAlbum
from app.src.infrastructure.outputs.mysql.adapters.adapter_album import AdapterAlbum
from app.src.infrastructure.outputs.mysql.mappers.i_mapper_album_entity import IMapperAlbumEntity
from app.src.infrastructure.outputs.mysql.repositories.i_album_repository import IAlbumRepository
from app.src.infrastructure.outputs.mysql.repositories.implementation_album_repository import \
    ImplementationAlbumRepository


class ModuleInjectorAlbum(Module):

    @singleton
    @provider
    def providerIAlbumRepository(self) -> IAlbumRepository:
        return ImplementationAlbumRepository()

    @singleton
    @provider
    def providerIPersistencePortAlbum(self) -> IAlbumPersistence:
        return AdapterAlbum(
            iAlbumRepository=self.providerIAlbumRepository(),
            iMapperAlbumEntity=IMapperAlbumEntity()
        )

    @singleton
    @provider
    def providerIServicePortAlbum(self) -> IAlbumService:
        return UseCaseAlbum(iAlbumPersistence=self.providerIPersistencePortAlbum())

    @singleton
    @provider
    def providerIHandlerSong(self) -> IAlbumHandler:
        return ImplementationAlbumHandler(
            iAlbumService=self.providerIServicePortAlbum(),
            iMapperAlbumApplication=IMapperAlbumApplication()
        )