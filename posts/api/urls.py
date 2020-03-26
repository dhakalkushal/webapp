from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import User
from posts.models import Post
from posts.api.serializers import PostSerializer
