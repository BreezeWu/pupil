'''
(*)~---------------------------------------------------------------------------
Pupil - eye tracking platform
Copyright (C) 2012-2017  Pupil Labs

Distributed under the terms of the GNU
Lesser General Public License (LGPL v3.0).
See COPYING and COPYING.LESSER for license details.
---------------------------------------------------------------------------~(*)
'''

from .setup import extensions

import logging
logger = logging.getLogger(__name__)


def build_cpp_extension():
    import subprocess as sp
    import os, sys
    src_loc = os.path.dirname(os.path.realpath(__file__))
    install_loc = os.path.split(src_loc)[0]
    cwd = os.getcwd()
    os.chdir(src_loc)
    logger.info('Building extention modules... {}'.format([ext.name for ext in extensions]))
    build_cmd = "{} setup.py install --install-lib={}"
    ret = sp.check_output(build_cmd.format(sys.executable, install_loc), shell=True).decode()
    logger.debug('Build log:\n{}'.format(ret))
    os.chdir(cwd)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    build_cpp_extension()
