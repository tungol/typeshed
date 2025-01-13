from _typeshed import Incomplete
from collections.abc import Callable, Collection, Mapping
from typing_extensions import TypeAlias

from authlib.oauth2 import JsonRequest, OAuth2Error, OAuth2Request
from authlib.oauth2.rfc6749 import BaseGrant, ClientMixin
from authlib.oauth2.rfc6750 import BearerTokenGenerator

_ServerResponse: TypeAlias = tuple[int, str, list[tuple[str, str]]]

class AuthorizationServer:
    scopes_supported: Collection[str] | None
    def __init__(self, scopes_supported: Collection[str] | None = None) -> None: ...
    def query_client(self, client_id: str) -> ClientMixin: ...
    def save_token(self, token: dict[str, str | int], request: OAuth2Request) -> None: ...
    def generate_token(
        self,
        grant_type: str,
        client: ClientMixin,
        user: Incomplete | None = None,
        scope: str | None = None,
        expires_in: int | None = None,
        include_refresh_token: bool = True,
    ) -> dict[str, str | int]: ...
    def register_token_generator(self, grant_type: str, func: BearerTokenGenerator) -> None: ...
    def authenticate_client(self, request: OAuth2Request, methods: Collection[str], endpoint: str = "token") -> ClientMixin: ...
    def register_client_auth_method(self, method, func) -> None: ...
    def get_error_uri(self, request, error) -> None: ...
    def send_signal(self, name, *args: object, **kwargs: object) -> None: ...
    def create_oauth2_request(self, request) -> OAuth2Request: ...
    def create_json_request(self, request) -> JsonRequest: ...
    def handle_response(self, status: int, body: Mapping[str, object], headers: Mapping[str, str]) -> object: ...
    def validate_requested_scope(self, scope: str, state: str | None = None) -> None: ...
    def register_grant(
        self, grant_cls: type[BaseGrant], extensions: Collection[Callable[[BaseGrant], None]] | None = None
    ) -> None: ...
    def register_endpoint(self, endpoint) -> None: ...
    def get_authorization_grant(self, request: OAuth2Request) -> BaseGrant: ...
    def get_consent_grant(self, request: Incomplete | None = None, end_user: Incomplete | None = None): ...
    def get_token_grant(self, request: OAuth2Request) -> BaseGrant: ...
    def create_endpoint_response(self, name, request: Incomplete | None = None): ...
    def create_authorization_response(
        self, request: Incomplete | None = None, grant_user: Incomplete | None = None
    ) -> object: ...
    def create_token_response(self, request: Incomplete | None = None) -> _ServerResponse: ...
    def handle_error_response(self, request: OAuth2Request, error: OAuth2Error) -> object: ...
