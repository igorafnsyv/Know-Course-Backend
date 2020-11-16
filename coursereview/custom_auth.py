from rest_framework.authentication import TokenAuthentication

# TODO: add to views


class BearerTokenAuthentication(TokenAuthentication):

    keyword = 'Bearer'
