# qgis-server
Plugins and docker for qgis-server 3.*
https://gitlab.com/gred/qgis-server/

Official doc: https://docs.qgis.org/testing/en/docs/user_manual/working_with_ogc/server/index.html

Image Docker : `registry.gitlab.com/gred/qgis-server`, liste des tags 

## Mise à jour

* Modifier la ligne `ARG QGIS_VERSION=3.4.1` dans le fichier `docker/Dockerfile`
* `git add docker/Dockerfile && git commit -m "Update qgis 3.4.1"`
* ajouter un tag au repo git : `git tag 3.4.1 `
* `git push && git push --tags`
* Vérifier le statut sur https://gitlab.com/gred/qgis-server/pipelines

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