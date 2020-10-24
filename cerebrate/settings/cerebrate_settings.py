import configparser
import os
from typing import Final, Optional, Any


class CerebrateSettings:
    _SETTINGS_FILE_NAME: Final[str] = "settings.ini"
    _SCELIGHT_PATH_KEY: Final[str] = "scelight_path"

    def __init__(self, settings_path: str):
        self.settings_file_path: Final[str] = os.path.join(
            settings_path, CerebrateSettings._SETTINGS_FILE_NAME
        )
        self.config: Final[configparser.ConfigParser] = configparser.ConfigParser()
        self._reload()

    @property
    def scelight_path(self) -> Optional[str]:
        return self._get_str(CerebrateSettings._SCELIGHT_PATH_KEY)

    @scelight_path.setter
    def scelight_path(self, value: Optional[str]):
        self._set_str(CerebrateSettings._SCELIGHT_PATH_KEY, value)

    def _get_str(self, option: str) -> Optional[str]:
        self._reload()
        return self.config.get(configparser.DEFAULTSECT, option, fallback=None)

    def _set_str(self, option: str, value: Optional[str]):
        self.config.set(configparser.DEFAULTSECT, option, value)
        self._save()

    def _reload(self):
        self.config.read(self.settings_file_path)

    def _save(self):
        with open(self.settings_file_path, "w") as file:
            self.config.write(file)
