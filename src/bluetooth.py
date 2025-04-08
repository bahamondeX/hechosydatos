import json
from bleak import BleakScanner
from .utils import get_logger, println

logger = get_logger(__name__)


async def get_devices():
    while True:
        logger.info("Scanning for devices...")
        devices = await BleakScanner.discover(timeout=15)  # type: ignore
        logger.info("Found %d devices", len(devices))
        for device in devices:
            logger.info("Device: %s", device)
            yield println(json.dumps({"address": device.address, "name": device.name}))
