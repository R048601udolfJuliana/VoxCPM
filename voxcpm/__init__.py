"""VoxCPM: A speech recognition package based on OpenBMB/MiniCPM."""

__version__ = "1.5.0"
__author__ = "VoxCPM Contributors"

# Personal fork: expose __author__ in __all__ and add convenience alias
from voxcpm.model import VoxCPM
from voxcpm.inference import transcribe

# Convenience alias for shorter import usage
transcribe_audio = transcribe

__all__ = ["VoxCPM", "transcribe", "transcribe_audio", "__version__", "__author__"]
