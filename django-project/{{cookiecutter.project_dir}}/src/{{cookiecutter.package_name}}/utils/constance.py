import logging
from typing import TYPE_CHECKING, Any, Mapping

from constance import config
from django.forms import TextInput, Textarea, Widget


if TYPE_CHECKING:
    from django.utils.datastructures import MultiValueDict
    from django.core.files.uploadedfile import UploadedFile

    _DataT = Mapping[str, Any]  # noqa: PYI047
    _FilesT = MultiValueDict[str, UploadedFile]  # noqa: PYI047


logger = logging.getLogger(__name__)


class WriteOnlyWidget(Widget):
    def format_value(self, value: Any) -> str:
        return str(super().format_value("***"))

    def value_from_datadict(self, data: "_DataT", files: "_FilesT", name: str) -> Any:
        value = data.get(name)
        if value == "***":
            return getattr(config, name)
        return value


class WriteOnlyTextarea(WriteOnlyWidget, Textarea):
    pass


class WriteOnlyInput(WriteOnlyWidget, TextInput):
    pass
