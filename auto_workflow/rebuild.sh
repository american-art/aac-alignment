ver="${1}"

FUSEKI_PATH=/opt/apache-jena-fuseki-2.4.0
source ./paths.sh

# rebuild all dev
if [ "${ver}" == "dev" ]; then
    service fuseki stop
    sleep 10s
    rm -rf ${FUSEKI_PATH}/run/databases/american-art-dev
    service fuseki start
    sleep 10s

    ./remote_auto_update_dev.sh GM
    ./remote_auto_update_dev.sh aaa
    ./remote_auto_update_dev.sh acm
    ./remote_auto_update_dev.sh autry
    ./remote_auto_update_dev.sh cbm
    ./remote_auto_update_dev.sh ccma
    ./remote_auto_update_dev.sh dma
    ./remote_auto_update_dev.sh ima
    ./remote_auto_update_dev.sh nmwa
    ./remote_auto_update_dev.sh npg
    ./remote_auto_update_dev.sh puam
    ./remote_auto_update_dev.sh saam
    ./remote_auto_update_dev.sh wam
# rebuild all pro
elif [ "${ver}" == "pro" ]; then
    service fuseki stop
    sleep 10s
    rm -rf ${FUSEKI_PATH}/run/databases/american-art
    service fuseki start
    sleep 10s

    ./remote_auto_update_pro.sh GM
    ./remote_auto_update_pro.sh aaa
    ./remote_auto_update_pro.sh acm
    ./remote_auto_update_pro.sh autry
    ./remote_auto_update_pro.sh cbm
    ./remote_auto_update_pro.sh ccma
    ./remote_auto_update_pro.sh dma
    ./remote_auto_update_pro.sh ima
    ./remote_auto_update_pro.sh nmwa
    ./remote_auto_update_pro.sh npg
    ./remote_auto_update_pro.sh puam
    ./remote_auto_update_pro.sh saam
    ./remote_auto_update_pro.sh wam
fi

# import YCBA
# ./remote_auto_update_pro.sh YCBA
