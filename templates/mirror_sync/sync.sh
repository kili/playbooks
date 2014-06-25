#!/bin/bash

RSYNC="/usr/bin/rsync"
ROOT_DIR="{{ mirror_sync_root_dir }}"
DATA_PATH="{{ proxy_index_path }}"

if [ -z "${1}" ]
then
  echo "no conf specified"
  exit 1
fi
source ${1}

mkdir -p ${DATA_PATH}${DIST_PREFIX}
for DIST in ${DISTS}
do
  ${RSYNC} ${RSYNC_PARAMS} -arvv rsync://${MIRROR}${DIST_PREFIX}/${DIST} ${DATA_PATH}${DIST_PREFIX} >> ${LOG_FILE} 2>&1
done
