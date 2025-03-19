from injector import singleton, provider, Module
from app.src.application.handlers.i_handler_user import IHandlerUser
from app.src.application.handlers.implementation_handler_user import ImplementationHandlerUser
from app.src.application.mappers.i_mapper_handler import IMapperHandler
from app.src.domain.persistence.i_persistence_port_user import IPersistencePortUser
from app.src.domain.services.i_services_port_user import IServicesPortUser
from app.src.domain.useCases.use_case_user import UseCaseUser
from app.src.infrastructure.outputs.mysql.adapters.adapter_user import AdapterUser
from app.src.infrastructure.outputs.mysql.mappers.i_mappers_user import IMapperUser
from app.src.infrastructure.outputs.mysql.repositories.i_repository_user import IUserRepository
from app.src.infrastructure.outputs.mysql.repositories.implementation_repository_user import ImplementationUserRepository

class ModuleInjectorUser(Module):

    @singleton
    @provider
    def providerIUserRepository(self) -> IUserRepository:
        return ImplementationUserRepository()

    @singleton
    @provider
    def providerIPersistencePortUser(self) -> IPersistencePortUser:
        return AdapterUser(
            iMapperUser=IMapperUser(),
            iUserRepository=self.providerIUserRepository()
        )

    @singleton
    @provider
    def providerIServicePortUser(self) -> IServicesPortUser:
        return UseCaseUser(iPersistencePortUser=self.providerIPersistencePortUser())

    @singleton
    @provider
    def providerIHandlerUser(self) -> IHandlerUser:
        return ImplementationHandlerUser(
            iMapperHandler=IMapperHandler(),
            iServicesPortUser=self.providerIServicePortUser()
        )