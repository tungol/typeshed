from collections.abc import Mapping, Sequence
from types import ModuleType
from typing import Any, Final

__all__ = [
    "_main",
    "freeze_support",
    "set_executable",
    "get_executable",
    "get_preparation_data",
    "get_command_line",
    "import_main_path",
]

WINEXE: Final[bool]
WINSERVICE: Final[bool]

def set_executable(exe: str) -> None: ...
def get_executable() -> str: ...
def is_forking(argv: Sequence[str]) -> bool: ...
def freeze_support() -> None: ...
def get_command_line(**kwds: Any) -> list[str]: ...
def spawn_main(pipe_handle: int, parent_pid: int | None = None, tracker_fd: int | None = None) -> None: ...

# undocumented
def _main(fd: int, parent_sentinel: int) -> int: ...
def get_preparation_data(name: str) -> dict[str, Any]: ...

old_main_modules: list[ModuleType]

def prepare(data: Mapping[str, Any]) -> None: ...
def import_main_path(main_path: str) -> None: ...
