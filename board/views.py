import jwt
from rest_framework import generics, mixins
from .serializers import PostSerializer, CommentSerializer
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from .models import Post, Comment
from users.models import CustomUser


def is_authenticated(request, *args, **kwargs):
    token = request.COOKIES.get('jwt')
    if not token:
        return False
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        user = CustomUser.objects.filter(id=payload.get('id')).first()
        request.user = user

    except jwt.ExpiredSignatureError:
        return False

    return True


def is_permission_allowed(request, obj, *args, **kwargs):
    return obj.author == request.user


class PostsView(mixins.ListModelMixin, mixins.CreateModelMixin,
                generics.GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        if not is_authenticated(request):
            raise AuthenticationFailed('Unauthenticated')

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not is_authenticated(request):
            raise AuthenticationFailed('Unauthenticated')

        request.data['author'] = request.user.id
        return self.create(request, *args, **kwargs)


class PostView(mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               generics.GenericAPIView):

    """ get,delete and update a post """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        if not is_authenticated(request):
            raise AuthenticationFailed('Unauthenticated')
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if not is_authenticated(request):
            raise AuthenticationFailed('Unauthenticated')

        obj_id = kwargs.pop('pk')
        obj = self.queryset.filter(id=obj_id).first()

        if obj and not is_permission_allowed(request, obj):
            raise PermissionDenied()

        request.data['author'] = request.user.id
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if not is_authenticated(request):
            raise AuthenticationFailed('Unauthenticated')

        obj_id = kwargs.pop('pk')
        obj = self.queryset.filter(id=obj_id).first()

        if obj and not is_permission_allowed(request, obj):
            raise PermissionDenied()

        return self.destroy(request, *args, **kwargs)


# comments

class CommentsView(mixins.ListModelMixin, mixins.CreateModelMixin,
                   generics.GenericAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        if not is_authenticated(request):
            raise AuthenticationFailed('Unauthenticated')

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not is_authenticated(request):
            raise AuthenticationFailed('Unauthenticated')

        request.data['author'] = request.user.id
        return self.create(request, *args, **kwargs)


class CommentView(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        if not is_authenticated(request):
            raise AuthenticationFailed('Unauthenticated')
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        if not is_authenticated(request):
            raise AuthenticationFailed('Unauthenticated')

        obj_id = kwargs.pop('pk')
        obj = self.queryset.filter(id=obj_id).first()

        if obj and not is_permission_allowed(request, obj):
            raise PermissionDenied()

        request.data['author'] = request.user.id
        request.data['post'] = obj.post.id if obj else None
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if not is_authenticated(request):
            raise AuthenticationFailed('Unauthenticated')

        obj_id = kwargs.pop('pk')
        obj = self.queryset.filter(id=obj_id).first()

        if obj and not is_permission_allowed(request, obj):
            raise PermissionDenied()

        return self.destroy(request, *args, **kwargs)
