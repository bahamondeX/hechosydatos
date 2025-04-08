import asyncio
import pyaudio
from .utils import get_logger, println

logger = get_logger(__name__)


async def stream_generator(
    format: int = pyaudio.paInt16,
    channels: int = 1,
    rate: int = 16000,
    chunk_size: int = 1024,
):
    """Generate audio chunks from microphone."""
    p = pyaudio.PyAudio()
    stream = p.open(
        format=format,
        channels=channels,
        rate=rate,
        input=True,
        frames_per_buffer=chunk_size,
    )
    devices = p.get_device_count()
    for i in range(devices):
        device_info = p.get_device_info_by_index(i)
        println(str(device_info))

    try:
        while True:
            yield stream.read(chunk_size * rate * 30)
    except asyncio.CancelledError:
        logger.info("Stream cancelled")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
