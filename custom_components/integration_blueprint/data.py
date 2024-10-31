"""Custom types for olarm-hass."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import OlarmHassApiClient
    from .coordinator import OlarmDataUpdateCoordinator


type OlarmHassConfigEntry = ConfigEntry[OlarmHassData]


@dataclass
class OlarmHassData:
    """Data for the Blueprint integration."""

    client: OlarmHassApiClient
    coordinator: OlarmDataUpdateCoordinator
    integration: Integration
