# qgis-server
Plugins and docker for qgis-server 3.*
https://github.com/tcoupin/qgis-server

Official doc: https://docs.qgis.org/testing/en/docs/user_manual/working_with_ogc/server/index.html

## Plugins

TODO...

## Docker & demo

Configuration by environment variables: see https://docs.qgis.org/testing/en/docs/user_manual/working_with_ogc/server/config.html#environment-variables

Default values:

```
ENV QGIS_DEBUG 5
ENV QGIS_LOG_FILE /dev/stdout
ENV QGIS_SERVER_LOG_FILE /dev/stdout
ENV QGIS_SERVER_LOG_LEVEL 5
ENV PGSERVICEFILE ''
ENV QGIS_PROJECT_FILE /project/project.qgs
ENV QGIS_PLUGINPATH /qgis/plugins
ENV QGIS_OPTIONS_PATH /qgis/options
ENV QGIS_SERVER_PARALLEL_RENDERING 1
ENV QGIS_SERVER_MAX_THREADS -1
ENV QGIS_SERVER_CACHE_DIRECTORY /qgis/cache
ENV QGIS_SERVER_CACHE_SIZE 50
ENV MAX_CACHE_LAYERS 100
```