export IMAGE_TAG=$(cat VERSION)

docker manifest create --amend cachengo/vspgwu-synchronizer:$IMAGE_TAG cachengo/vspgwu-synchronizer-x86_64:$IMAGE_TAG cachengo/vspgwu-synchronizer-aarch64:$IMAGE_TAG
docker manifest push cachengo/vspgwu-synchronizer:$IMAGE_TAG
