from homeassistant.components.stt import SpeechToTextEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.config_entries import ConfigEntry

import requests

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    async_add_entities([WhisperSTT()])

class WhisperSTT(SpeechToTextEntity):
    @property
    def supported_languages(self):
        return ["ru"]

    @property
    def engine(self):
        return "whisper_stt"

    @property
    def name(self):
        return "Whisper STT Remote"

    async def async_process_audio_stream(self, metadata, stream):
        audio_data = b"".join([d async for d in stream])
        response = requests.post(
            "http://192.168.0.3:8000/transcribe",
            headers={"Content-Type": "audio/wav"},
            data=audio_data
        )
        response.raise_for_status()
        return {"text": response.json()["text"]}
