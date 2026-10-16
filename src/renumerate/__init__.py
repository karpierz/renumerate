# flake8-in-file-ignores: noqa: F401,F403,F821

# Copyright (c) 2016 Adam Karpierz
# SPDX-License-Identifier: Zlib

from __future__ import annotations

from .__about__ import * ; del __about__  # type: ignore[name-defined]

from ._renumerate import * ; del _renumerate  # type: ignore[name-defined]
