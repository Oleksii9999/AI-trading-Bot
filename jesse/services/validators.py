from jesse import exceptions


def validate_routes(router):
    """

    :param router:
    """
    if not router.routes:
        raise exceptions.RouteNotFound(
            'No routes found. Please add at least one route at: routes.py\nMore info: https://docs.jesse-ai.com/docs/routes.html#routing')
