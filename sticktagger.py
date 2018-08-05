#!/usr/bin/env python
#
# Crudely retags a music collection based on 
# the directory structure

import sys
import os
import re # regular expressions
import shutil
import mutagen
#import logging

# glbl_ = global
# fxx_ = function XX
#

glbl_musicRoot = '/Users/matt/Stickshaker/music_test/music_dirs'
glbl_dataRoot = '/Users/matt/Stickshaker/data'

