# -*- coding:utf-8 -*-

import os
from .freespacebase import FreeSpaceConditionBase

class FreeSpaceCondition(FreeSpaceConditionBase):
    def __init__(self, settings):
        FreeSpaceConditionBase.__init__(self, settings)
        self._path = settings['path']

    def apply(self, client_status, torrents):
        # Calculate directory size using configured path
        total_size = 0
        if os.path.exists(self._path):
            for dirpath, dirnames, filenames in os.walk(self._path):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    try:
                        total_size += os.path.getsize(filepath)
                    except (OSError, IOError):
                        continue
        
        # Use directory size as free_space (keeping variable name unchanged)
        free_space = total_size
        FreeSpaceConditionBase.apply(self, free_space, torrents)
