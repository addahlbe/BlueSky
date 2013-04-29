from pyramid.view import view_config
from pyramid.security import NO_PERMISSION_REQUIRED


@view_config(route_name='index', renderer='realEstateApp:templates/index.mako', permission=NO_PERMISSION_REQUIRED)
def index(request):
    return {
    }


@view_config(route_name='contact-info', renderer='realEstateApp:templates/contact-info.mako', permission=NO_PERMISSION_REQUIRED)
def contact(request):
    return {
    }


@view_config(route_name='info', renderer='realEstateApp:templates/info.mako', permission=NO_PERMISSION_REQUIRED)
def info(request):
    return {
    }


@view_config(route_name='home1', renderer='realEstateApp:templates/home1.mako', permission=NO_PERMISSION_REQUIRED)
def home1(request):
    return {
    }


@view_config(route_name='home1-exterior', renderer='realEstateApp:templates/home1-exterior.mako', permission=NO_PERMISSION_REQUIRED)
def exterior(request):
    return {
    }


@view_config(route_name='home1-living-room', renderer='realEstateApp:templates/home1-living-room.mako', permission=NO_PERMISSION_REQUIRED)
def livingRroom1(request):
    return {
    }


@view_config(route_name='home1-kitchen', renderer='realEstateApp:templates/home1-kitchen.mako', permission=NO_PERMISSION_REQUIRED)
def kitchen1(request):
    return {
    }


@view_config(route_name='home1-dining-room', renderer='realEstateApp:templates/home1-dining-room.mako', permission=NO_PERMISSION_REQUIRED)
def diningRoom1(request):
    return {
    }


@view_config(route_name='home1-stairs', renderer='realEstateApp:templates/home1-stairs.mako', permission=NO_PERMISSION_REQUIRED)
def stairs1(request):
    return {
    }


@view_config(route_name='home1-bedrooms', renderer='realEstateApp:templates/home1-bedrooms.mako', permission=NO_PERMISSION_REQUIRED)
def bedrooms1(request):
    return {
    }


@view_config(route_name='home1-baths', renderer='realEstateApp:templates/home1-baths.mako', permission=NO_PERMISSION_REQUIRED)
def baths1(request):
    return {
    }


@view_config(route_name='home1-more', renderer='realEstateApp:templates/home1-more.mako', permission=NO_PERMISSION_REQUIRED)
def more1(request):
    return {
    }


@view_config(route_name='home2', renderer='realEstateApp:templates/home2.mako', permission=NO_PERMISSION_REQUIRED)
def home2(request):
    return {
    }


@view_config(route_name='home2-exterior', renderer='realEstateApp:templates/home2-exterior.mako', permission=NO_PERMISSION_REQUIRED)
def exterior2(request):
    return {
    }


@view_config(route_name='home2-living-room', renderer='realEstateApp:templates/home2-living-room.mako', permission=NO_PERMISSION_REQUIRED)
def livingRroom2(request):
    return {
    }


@view_config(route_name='home2-kitchen', renderer='realEstateApp:templates/home2-kitchen.mako', permission=NO_PERMISSION_REQUIRED)
def kitchen2(request):
    return {
    }


@view_config(route_name='home2-dining-room', renderer='realEstateApp:templates/home2-dining-room.mako', permission=NO_PERMISSION_REQUIRED)
def diningRoom2(request):
    return {
    }


@view_config(route_name='home2-stairs', renderer='realEstateApp:templates/home2-stairs.mako', permission=NO_PERMISSION_REQUIRED)
def stairs2(request):
    return {
    }


@view_config(route_name='home2-bedrooms', renderer='realEstateApp:templates/home2-bedrooms.mako', permission=NO_PERMISSION_REQUIRED)
def bedrooms2(request):
    return {
    }


@view_config(route_name='home2-baths', renderer='realEstateApp:templates/home2-baths.mako', permission=NO_PERMISSION_REQUIRED)
def baths2(request):
    return {
    }


@view_config(route_name='home2-lower-level', renderer='realEstateApp:templates/home2-lower-level.mako', permission=NO_PERMISSION_REQUIRED)
def lowerLevel2(request):
    return {
    }

@view_config(route_name='home2-more', renderer='realEstateApp:templates/home2-more.mako', permission=NO_PERMISSION_REQUIRED)
def more2(request):
    return {
    }
