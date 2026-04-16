"""VoxCPM: A speech recognition package based on OpenBMB/MiniCPM."""

__version__ = "1.5.0"
__author__ = "VoxCPM Contributors"

from voxcpm.model import VoxCPM
from voxcpm.inference import transcribe

__all__ = ["VoxCPM", "transcribe", "__version__"]
