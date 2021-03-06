﻿# -*- coding: utf-8 -*-

import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import os
import sys
import re
import urllib
import urllib2 
import cookielib

__addon__           = xbmcaddon.Addon()
__addon_id__        = __addon__.getAddonInfo('id')
__addonname__       = __addon__.getAddonInfo('name')
__icon__            = __addon__.getAddonInfo('icon')
__addonpath__       = xbmc.translatePath(__addon__.getAddonInfo('path'))
__lang__            = __addon__.getLocalizedString
__path__            = os.path.join(__addonpath__, 'resources', 'lib' )
__path_img__        = os.path.join(__addonpath__, 'resources', 'media' )

sys.path.append(__path__)
sys.path.append (__path_img__)

class Main:

    def start(self, selfGet):
    
        # vars
        self = selfGet
    
        list = [
            ['Rádio Depeche Mode (CZ)', 'http://mp3stream4.abradio.cz:8000/depeche128.mp3', 'https://i62.servimg.com/u/f62/19/40/01/67/radiod11.jpg'],
            ['181.fm Beatles (USA)', 'http://relay.181.fm:8062', 'https://i46.servimg.com/u/f46/19/40/01/67/c175125.png'],
            ['80s80s David Bowie (D)', 'http://streams.80s80s.de/davidbowie/mp3-128/surfmusik', 'https://i62.servimg.com/u/f62/19/40/01/67/80bowi10.jpg'],
            ['80s80s Depeche Mode (D)', 'http://streams.80s80s.de/dm/mp3-128/surfmusik', 'https://i62.servimg.com/u/f62/19/40/01/67/80mode10.jpg'],
            ['80s80s Prince (D)', 'http://streams.80s80s.de/100/mp3-128/surfmusik', 'https://i62.servimg.com/u/f62/19/40/01/67/80prin10.jpg']
                       ]

        if self.opt2 == '':
            i = 0
            for key in list:
                listItem = xbmcgui.ListItem(label=key[0], iconImage=key[2])
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sys.argv[0] + '?sp_' + str(i), listitem=listItem, isFolder=True)
                i = i + 1
            xbmcplugin.endOfDirectory(int(sys.argv[1]))
        
        else:
        
            Title = list[int(self.opt2)][0]
            Icon = list[int(self.opt2)][2]
            URL = list[int(self.opt2)][1]
        
            import radioPlayer as player
            player.Main().start(Title, Icon, URL)
            
