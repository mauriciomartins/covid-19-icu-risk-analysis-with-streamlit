"""Minimal imghdr shim for environments missing the stdlib module.

This provides a lightweight `what()` function that detects common image
types by header bytes: 'jpeg', 'png', 'gif', 'bmp', 'webp', 'rgb', 'pbm', 'pgm', 'pnm', 'tiff'.

It is not a full replacement for the CPython stdlib, but it satisfies
typical checks done by downstream code during deployment.
"""
from __future__ import annotations

import os
from typing import Optional

_MAX_HEADER = 32


def _read_header(fp) -> bytes:
    try:
        pos = None
        if hasattr(fp, "seek"):
            try:
                pos = fp.tell()
            except Exception:
                pos = None
        data = fp.read(_MAX_HEADER)
        if pos is not None:
            try:
                fp.seek(pos)
            except Exception:
                pass
        return data or b""
    except Exception:
        return b""


def what(file: object) -> Optional[str]:
    """Detect image type by header bytes.

    `file` may be a filename (str / os.PathLike) or a file-like object
    with a `read()` method.
    """
    header = b""

    # filename
    if isinstance(file, (str, os.PathLike)):
        try:
            with open(os.fspath(file), "rb") as f:
                header = _read_header(f)
        except Exception:
            return None
    else:
        # file-like object
        if hasattr(file, "read"):
            header = _read_header(file)
        else:
            return None

    if header.startswith(b"\xff\xd8\xff"):
        return "jpeg"
    if header.startswith(b"\x89PNG\r\n\x1a\n"):
        return "png"
    if header[:6] in (b"GIF87a", b"GIF89a"):
        return "gif"
    if header.startswith(b"BM"):
        return "bmp"
    if header.startswith(b"II\x2A\x00") or header.startswith(b"MM\x00\x2A"):
        return "tiff"
    if header.startswith(b"RIFF") and len(header) >= 12 and header[8:12] == b"WEBP":
        return "webp"
    # PBM/PGM/PPM (plain formats start with 'P')
    if header.startswith(b"P4"):
        return "pbm"
    if header.startswith(b"P5"):
        return "pgm"
    if header.startswith(b"P6"):
        return "ppm"

    # Fallback: check common textual signatures
    if header.startswith(b"RGB"):
        return "rgb"

    return None


__all__ = ["what"]
