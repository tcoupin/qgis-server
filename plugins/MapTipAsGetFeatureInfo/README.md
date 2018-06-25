# qgis-MapTipAsGetFeatureInfo
Qgis server plugin to use maptip instead of legacy html in GetFeatureInfo

Since HTML GetFeatureInfo response is not customizable (for the moment ;) ), this plugin replace the tables by the maptip of each layer.

This plugin use a set of "replace" functions. If the HTML tables layouts change, the plugin may be unusable (see convertFeatureInfoHtml function of src/server/wms/qgswmsrenderer.cpp, https://github.com/qgis/QGIS/blob/6470aacb3397ba119b0d6c29b5c83e28ecedae31/src/server/services/wms/qgswmsrenderer.cpp#L1988).