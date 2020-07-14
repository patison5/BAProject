from organizations import OrganizationsController
from pharmacy import PharmacyController
from travels import TravelsController
from misc import MiscController
from services import ServicesController
from images import ImagesController
from posters import PostersController

def insert_data(images, organizations, services, posters, travels, misc):
    # images.init_data()
    organizations.init_data()
    # services.init_data()
    # posters.init_data()
    # travels.init_data()
    # misc.init_data()
    # images.init_additional()

def flush_db(images, organizations, services, posters, travels, misc):
    images.drop_additional()
    posters.drop_table()
    travels.drop_table()
    misc.drop_table()
    services.drop_table()
    organizations.drop_table()
    images.drop_table()

def create_tables(images, organizations, services, posters, travels, misc):
    images.create_table()
    organizations.create_table()
    services.create_table()
    posters.create_table()
    travels.create_table()
    misc.create_table()
    images.create_additional()

def init_db():
    images = ImagesController()
    organizations = OrganizationsController()
    services = ServicesController()
    posters = PostersController()
    travels = TravelsController()
    misc = MiscController()

    flush_db(images, organizations, services, posters, travels, misc)
    create_tables(images, organizations, services, posters, travels, misc)
    
    return (images, organizations, services, posters, travels, misc)
