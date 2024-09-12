from dataclasses import dataclass


@dataclass
class Text:
    """{"text": xyz, "rot_type": rot13/rot47, "status": encrypted/decrypted}"""
    text: str
    rot_type: str
    status: str
