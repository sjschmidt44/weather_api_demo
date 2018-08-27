from pyramid_restful.routers import ViewSetRouter
from .views.weather import WeatherLocationAPIView


def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')

    router = ViewSetRouter(config)
    router.register('api/v1/location', WeatherLocationAPIView, 'location')