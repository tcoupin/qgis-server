import re
from qgis.PyQt.QtCore import *
from qgis.core import *
from qgis.server import *


class MapTipAsGetFeatureInfo:
   

    def __init__(self, serverIface):
        self.serverIface = serverIface
        serverIface.registerFilter( MapTipAsGetFeatureInfoFilter(serverIface) , 100 )

class MapTipAsGetFeatureInfoFilter(QgsServerFilter):

    def __init__(self, serverIface):
        super(MapTipAsGetFeatureInfoFilter, self).__init__(serverIface)

    def requestReady(self):
        request = self.serverInterface().requestHandler()
        params = request.parameterMap()
        if (params.get('SERVICE').upper() == 'WMS' \
                and params.get('REQUEST').upper() == 'GETFEATUREINFO' \
                and "HTML" in params.get('INFO_FORMAT').upper()):
            request.setParameter('WITH_MAPTIP','true')

    def responseComplete(self):
        request = self.serverInterface().requestHandler()
        params = request.parameterMap()
        if (params.get('SERVICE').upper() == 'WMS' \
                and params.get('REQUEST').upper() == 'GETFEATUREINFO' \
                and "HTML" in params.get('INFO_FORMAT').upper()):
            body = str(request.body().data(), encoding='utf-8')

            # Remove all newline
            body = re.sub(r'\n', '', body)
            # One line per table
            body = re.sub(r'</table>', r'</table><!--endtable-->\n', body, flags=re.IGNORECASE)
            body = re.sub(r'<table', r'\n<!--starttable--><table', body, flags=re.IGNORECASE)
            # Extract Maptip
            body = re.sub(r'<!--starttable--><table.*maptip</th><td>(.*)</td>.*/table><!--endtable-->', r'\1', body, flags=re.IGNORECASE )
            # Clear any table
            body = re.sub(r'.*<!--starttable-->.*', r'', body, flags=re.IGNORECASE)
            body = re.sub(r'.*<!--endtable-->.*', r'', body, flags=re.IGNORECASE)
            request.clearBody()
            request.appendBody(bytes(body,encoding='utf-8'))