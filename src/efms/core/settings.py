from efms.core.constants import CONFIG_DIRECTORY

from efms.core.config_loader import ConfigLoader


loader = ConfigLoader(

    CONFIG_DIRECTORY / "config.json"

)

settings = loader.config