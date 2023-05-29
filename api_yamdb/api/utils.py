from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework.generics import get_object_or_404

from api_yamdb.settings import DEFAULT_FROM_EMAIL
from reviews.models import User
from .serializers import ConfirmationCodeSerializer


def sent_confirmation_code(request):
    """Функция отправки кода подтверждения при регистрации"""
    serializer = ConfirmationCodeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    email = serializer.validated_data.get('email')
    user = get_object_or_404(User, username=username)
    confirmation_code = default_token_generator.make_token(user)
    return send_mail(
        'Код подтверждения',
        f'Ваш код подтверждения: {confirmation_code}',
        [DEFAULT_FROM_EMAIL],
        [email],
        fail_silently=False,
    )
