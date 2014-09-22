# Copyright 2014 Xinyu, He <legendmohe@foxmail.com>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import logging.handlers

file_name = 'f_log.log'
file_logger = logging.getLogger('FileLog')
handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=50*1024*1024)
file_logger.addHandler(handler)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

DEBUG = logging.debug
INFO = logging.info
WARN = logging.warning
ERROR = logging.error
CRITICAL = logging.critical

FDEBUG = file_logger.debug
FINFO = file_logger.info
FWARN = file_logger.warning
FERROR = file_logger.error
FCRITICAL = file_logger.critical
