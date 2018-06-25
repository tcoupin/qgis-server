# -*- coding: utf-8 -*-

def serverClassFactory(serverIface):
    from .MapTipAsGetFeatureInfo import MapTipAsGetFeatureInfo
    return MapTipAsGetFeatureInfo(serverIface)

