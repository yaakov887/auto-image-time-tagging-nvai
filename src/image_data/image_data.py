'''
Created on Jun 10, 2013

@author: jacoberg2
'''
#!/usr/bin/env python

import os
import shutil
import sys
import pyexiv2

from errno import ENOENT
from datetime import datetime
from datetime import time

class Image_Data:
    '''
    classdocs
    '''
    #IPTC keywords key
    _keyword_key = 'Iptc.Application2.Keywords'
    _time_key = 'Exif.Photo.DateTimeDigitized'


    def __init__(self,path):
        '''
        Constructor
        '''
        self.image_path = path
        if not os.path.exists(self.image_path) or not os.path.isfile(self.image_path):
            raise IOError(ENOENT, os.strerror(ENOENT), filename)
        
        self.image_time = time.dst()
        self.id_tags = []
        
    def tag_count (self):
        return len(self.id_tags)
    
    def move_image_file (self, to_path):
        try:
            shutil.move(self.image_path, to_path)
        except:
            raise
    
    def add_id_tag(self,id_tag):
        self.id_tags.append(id_tag)
        
    def extract_image_time(self):
        metadata = pyexiv2.ImageMetadata(self.image_path)
        metadata.read()

        time_array = (metadata[self._time_key].raw_value).split(' ')
        self.image_time = datetime.strptime(time_array[1], '%H:%M:%S')
        
    def attach_id_tags(self):
        metadata = pyexiv2.ImageMetadata(self.image_path)
        metadata[self._keyword_key] = pyexiv2.IptcTag(self.keyword_key, self.id_tags)
        metadata.write(preserve_timestamps=True)