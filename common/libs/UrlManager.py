# -*- coding: utf-8 -*-
import time
#from application import app
class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl( path ):
        return path
        return

    @staticmethod
    def buildStaticUrl(path):
        # release_version = app.config.get( 'RELEASE_VERSION' )
        # ver = "%s"%( int( time.time() ) ) if not release_version else release_version
        # path =  "/static" + path + "?ver=" + ver
        # return UrlManager.buildUrl( path )
        ver = "%s"%( 2222222 )
        path = "/static"+path + "?ver="+ver
        return UrlManager.buildUrl(path)

    # @staticmethod
    # def buildImageUrl( path ):
    #     #app_config = app.config['APP']
    #     url = app_config['domain'] + app.config['UPLOAD']['prefix_url'] + path
    #     return url