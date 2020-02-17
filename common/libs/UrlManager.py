import time
#from application import  app
import application
class UrlManager(object):
    def __init__(self):
        pass

    @staticmethod
    def buildUrl( path ):
        return path

    @staticmethod
    def buildStaticUrl(path):
        release_version = application.app.config.get( 'RELEASE_VERSION' )
        ver = "%s"%( int( time.time() ) ) if not release_version else release_version
        path =  "/static" + path + "?ver=" + ver
        return UrlManager.buildUrl( path )

    @staticmethod
    def buildImageUrl( path ):
        app_config = application.app.config['APP']
        url = app_config['domain'] + application.app.config['UPLOAD']['prefix_url'] + path
        return url