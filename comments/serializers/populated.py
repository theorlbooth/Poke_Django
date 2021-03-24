from jwt_auth.serializers.common import UserSerializer
from ..serializers.common import CommentSerializer

class PopulatedCommentSerializer(CommentSerializer):

    owner = UserSerializer()
    