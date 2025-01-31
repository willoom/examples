#!/bin/bash

: '
Script de backup de directorio de configuración del sistema /etc

Crea un script llamado etcbackup.sh que en el directorio /root/backup guarde un fichero con nombre 
YYYYMMDD_HHmm_etc.tar.bz2, que sea compilación comprimida con algoritmo Bzip2 del directorio de 
configuración general del sistema /etc.

Asume que lo ejecutará root.

Si el directorio /root/backup no existiese, informará que de que se creará (y lo creará).

Para hacer este script hay que extrar los datos necesarios de date.

Recuerda usar la cabecera adecuada de los scripts de bash y darle los permisos oportunos de ejecución al 
script.

Extrema las medidas de seguridad a la hora de invocar comandos que no pertenezcan a bash.
'

TAR=/usr/bin/tar
MKDIR=/usr/bin/mkdir
DATE=/usr/bin/date
ECHO=/usr/bin/echo

# Mejora: comprobar que los comandos existen y tenemos permisos de ejecución.

ETC_DIR=/etc
BACKUP_DIR=/root/backup

PREFIJO=`${DATE} +%Y%m%d_%H%m`
ARCHIVO="${BACKUP_DIR}/${PREFIJO}_etc.tar.bz2"


if [ ! -d $BACKUP_DIR ]; then
  $ECHO "El directorio $BACKUP_DIR no existe. Se procede a su creación..."
  $MKDIR -p $BACKUP_DIR || exit 1
  # Si no se realiza con éxito la orden mkdir, se habrá de evaluar el or.
  # y se ejecutará la orden exit 1, que hará que salgamos del script con un estado de error.
fi

echo "Listos para generar el archivo $ARCHIVO..."
$TAR cvjf $ARCHIVO $ETC_DIR

