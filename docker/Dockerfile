FROM ubuntu:18.04

ARG QGIS_VERSION=3.4.1

ENV DEBIAN_FRONTEND noninteractive


RUN apt-get update && \
	apt-get upgrade -y && \
	apt-get install --no-install-recommends -y apt-utils apt-transport-https lsb-release ca-certificates gnupg apache2 libapache2-mod-fcgid && \
	mkdir -p /var/run/apache2 && chown www-data:www-data /var/run/apache2 && \
	mkdir -p /var/lock/apache2 && chown www-data:www-data /var/lock/apache2 && \
	a2enmod headers && \
	a2enmod rewrite && \
	rm -r /var/lib/apt/lists/*


RUN	bash -c "echo 'deb https://qgis.org/debian bionic main' > /etc/apt/sources.list.d/qgis.list" && \
	apt-key adv --keyserver keyserver.ubuntu.com --recv-key CAEB3DC3BDF7FB45 && \
	apt-get update && \
	apt-get install -y --no-install-recommends qgis-server=1:${QGIS_VERSION}\* python-qgis=1:${QGIS_VERSION}\* && \
	mkdir -p /qgis/plugins && \
	mkdir -p /qgis/options && \
	mkdir -p /qgis/cache && \
	rm -r /var/lib/apt/lists/*


ADD 000-default.conf /etc/apache2/sites-available/000-default.conf

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_LOG_DIR ''
ENV LANG C

ENV QGIS_DEBUG 5
ENV QGIS_SERVER_LOG_FILE /dev/stdout
ENV QGIS_SERVER_LOG_LEVEL 5
ENV PGSERVICEFILE ''
ENV QGIS_PROJECT_FILE /project/project.qgz
ENV QGIS_PLUGINPATH /qgis/plugins
ENV QGIS_OPTIONS_PATH /qgis/options
ENV QGIS_SERVER_PARALLEL_RENDERING 1
ENV QGIS_SERVER_MAX_THREADS -1
ENV QGIS_SERVER_CACHE_DIRECTORY /qgis/cache
ENV QGIS_SERVER_CACHE_SIZE 50
ENV MAX_CACHE_LAYERS 100
ENV QGIS_PREFIX_PATH /usr

CMD /usr/sbin/apache2 -DFOREGROUND
