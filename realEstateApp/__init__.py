from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from realEstateApp.models import initialize_base
from pyramid.session import UnencryptedCookieSessionFactoryConfig


def get_db(request):
    maker = request.registry.settings['db.sessionmaker']
    return maker()


def main(global_config, **settings):
    '''Main config function'''

    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_base(engine)
    maker = sessionmaker(bind=engine)
    settings['db.sessionmaker'] = maker

    my_session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    config = Configurator(settings=settings,
                          session_factory=my_session_factory)

    config.set_request_property(get_db, 'db', reify=True)

    #Static routes, use style sheets with /style/folder/file
    config.add_static_view('style', 'realEstateApp:dependencies/')

    # Routes
    # General
    config.add_route('index', '/')
    config.add_route('contact-info', '/contact-info')
    config.add_route('info', '/info')
    # Home 1
    config.add_route('home1', '/home1')
    config.add_route('home1-exterior', '/home1/exterior')
    config.add_route('home1-living-room', '/home1/living-room')
    config.add_route('home1-kitchen', '/home1/kitchen')
    config.add_route('home1-dining-room', '/home1/dining-room')
    config.add_route('home1-stairs', '/home1/stairs')
    config.add_route('home1-bedrooms', '/home1/bedrooms')
    config.add_route('home1-baths', '/home1/baths')
    config.add_route('home1-more', '/home1/more')
    # Home 2
    config.add_route('home2', '/home2')
    config.add_route('home2-exterior', '/home2/exterior')
    config.add_route('home2-living-room', '/home2/living-room')
    config.add_route('home2-kitchen', '/home2/kitchen')
    config.add_route('home2-dining-room', '/home2/dining-room')
    config.add_route('home2-stairs', '/home2/stairs')
    config.add_route('home2-bedrooms', '/home2/bedrooms')
    config.add_route('home2-baths', '/home2/baths')
    config.add_route('home2-lower-level', '/home2/lower-level')
    config.add_route('home2-more', '/home2/more')

    config.scan('realEstateApp')
    return config.make_wsgi_app()
