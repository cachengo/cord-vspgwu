export IMAGE_TAG=$(cat VERSION)
export AARCH=`uname -m`

docker build -f Dockerfile.synchronizer -t cachengo/vspgwu-synchronizer-$AARCH:$IMAGE_TAG .
docker push cachengo/vspgwu-synchronizer-$AARCH:$IMAGE_TAG
