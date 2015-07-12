DEST_USER=finn
DEST_IP=10.10.10.104
DEST_FOLDER=/home/${DEST_USER}/Games/Lightning

FULL_DEST=${DEST_USER}@${DEST_IP}:${DEST_FOLDER}

scp main.py ${FULL_DEST}
scp -rp resources ${FULL_DEST}

echo Done
