# Copyright (C) 2026 GitHub Copilot
#
# SPDX-License-Identifier: MIT
"""Shared configuration for flood data source selection."""

import os

# Switch between live data and mock data.
# Set this value to False in any task or script to use the mock JSON file.
USE_LIVE_DATA = False

PACKAGE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.abspath(os.path.join(PACKAGE_ROOT, 'collected_data'))
LIVE_DATA_FILE = os.path.join(DATA_DIR, 'live_data_28days.json')
MOCK_DATA_FILE = os.path.join(DATA_DIR, 'mock_data_28days.json')