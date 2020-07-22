from flask import Flask, flash, request, redirect, url_for, render_template, current_app, g, send_from_directory
from werkzeug.utils import secure_filename
import json
import os
from jinja2 import Environment, PackageLoader, select_autoescape

from initdb import init_db
from tour_agent import TourAgentController
from banks import BanksController
from pathlib import Path


env = Environment(
    loader=PackageLoader('script', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

UPLOAD_FOLDER = './static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'svg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def convert_to_slide_array(array):
    li2 = []
    for i in range(0, len(array), 4):
        li2.append(array[i:i + 4])
    return li2


def convert_to_slide_array_eight(array):
    li2 = []
    for i in range(0, len(array), 8):
        li2.append(array[i:i + 8])
    return li2

def upload_file_on_server(file, desc="", title=""):
    if file.filename == '':
        flash('No selected file')
        return "no selected file"
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        ext = filename.rsplit('.', 1)[1].lower()
        id = images.insert_image(title, desc, ext, app.config['UPLOAD_FOLDER'])
        filename = str(id) + '.' + ext

        Path(UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return str(id)


if __name__ == '__main__':
    images, organizations, services, posters, travels, misc = init_db()


    @app.route('/upload', methods=['GET','POST'])
    def upload_file():
        if request.method == 'POST':
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                ext = filename.rsplit('.', 1)[1].lower()
                id = images.insert_image('test description', ext, app.config['UPLOAD_FOLDER'])
                filename = str(id) + '.' + ext
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('uploaded_file',
                                        filename=filename))
        return render_template('upload.html')


    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


    tour_agent = TourAgentController()
    banks = BanksController()

    @app.route('/')
    def index():
        template = env.get_template('page1.html')
        return template.render(
            title = 'Организации',
            search='true'
        )


    # использую
    @app.route('/organizations', methods=['GET', 'POST'])
    def page_organizations():
        if request.method == 'GET':
            template = env.get_template('organizations.html')
            return template.render(
                title='Организации',
                menuElement="organizations-inactive",
                search='true'
            )

        if request.method == 'POST':
            titles = organizations.get_organization_titles()
            return json.dumps(titles)


    # использую
    @app.route('/organizations/<int:id>')
    def show_single_organizations(id):
        single_org = organizations.get_single_organization(id)
        template = env.get_template('single_white_post_inside.html')
        return template.render(
            title='Организации',
            menuElement="minimarket-inactive",
            data=single_org
        )


    # использую
    @app.route('/organization-service/<int:id>')
    def show_single_organization_service(id):
        single_org = services.get_single_service(id)
        template = env.get_template('single_white_post_inside.html')
        return template.render(
            title='Фото и полиграфия',
            menuElement="minimarket-inactive",
            data=single_org
        )


    # использую
    @app.route('/services')
    def page_services():
        single_service = services.get_titles_of_services()
        template = env.get_template('services.html')
        return template.render(
            title='Услуги',
            menuElement="services-inactive",
            data = convert_to_slide_array_eight(organizations.get_all_organizations(2))
        )


    @app.route('/afisha')
    def page_afisha():
        allAfisha = posters.get_all_afisha()
        template = env.get_template('posts_black.html')
        return template.render(
            title='Афиша концертного зала',
            menuElement="concert_zal-inactive",
            data=convert_to_slide_array(allAfisha)
        )


    @app.route('/afisha/<int:id>')
    def page_single_afisha(id):
        afisha_single = posters.get_single_afisha(id)

        template = env.get_template('page7.html')
        return template.render(
            title='Афиша концертного зала',
            menuElement="concert_zal-inactive",
            data=afisha_single
        )


    # используется
    @app.route('/kafe')
    def page_kafe():
        template = env.get_template('cafe-all.html')
        return template.render(
            title='Кафе',
            menuElement="kafe-inactive",
            data = convert_to_slide_array(organizations.get_all_organizations_full(1))
        )

    @app.route('/kafe/single')
    def page_kafe_single():
        cafe_info = misc.get_misc_info('cafe')
        template = env.get_template('single_white_post.html')
        return template.render(
            title='Кафе',
            menuElement="kafe-inactive",
            data=cafe_info
        )


    @app.route('/banks')
    def page_banks():
        banks_info = banks.get_banks()
        template = env.get_template('banks.html')

        # banks = convert_to_slide_array(organizations.get_all_organizations_full(3))

        print(organizations.get_all_organizations_full(3))
        return template.render(
            title='Банкоматы',
            menuElement="banks-inactive",
            data = convert_to_slide_array(organizations.get_all_organizations_full(3))
        )


    @app.route('/tour_agent')
    def page_tour_agent():
        tours_list = tour_agent.get_all_tour_agent()
        template = env.get_template('posts_white.html')
        return template.render(
            title='Туристические агенства',
            menuElement="tour_agent-inactive",
            data=convert_to_slide_array(tours_list)
        )


    @app.route('/tour_single_info')
    def tour_single_info():
        tours_list = tour_agent.get_all_tour_agent()
        template = env.get_template('page9.html')
        return template.render(
            title='Туристические агенства',
            menuElement="tour_agent-inactive",
            data=convert_to_slide_array(tours_list)
        )

    


    @app.route('/tour_agent/<int:id>')
    def page_single_tour_agent(id):
        tours_list = tour_agent.get_single_tour_agent(id)
        template = env.get_template('single_white_post.html')
        return template.render(
            title='Туристические агенства',
            menuElement="tour_agent-inactive",
            data=tours_list
        )


    @app.route('/photo')
    def page_photo():
        template = env.get_template('single_white_post.html')
        return template.render(
            title='Фото и полиграфия',
            menuElement="photo-inactive",
            data = organizations.get_single_organization_by_type(4)
        )


    @app.route('/minimarket')
    def page_minimarket():
        template = env.get_template('single_white_post.html')
        return template.render(
            title = 'Фото и полиграфия',
            menuElement = "minimarket-inactive",
            data = organizations.get_single_organization_by_type(5)
        )


    @app.route('/pharmacy')
    def page_pharmacy():
        template = env.get_template('single_white_post.html')
        return template.render(
            title='Фото и полиграфия',
            menuElement="pharmacy-inactive",
            data = organizations.get_single_organization_by_type(6)
        )


    @app.route('/admin')
    def admin_index():
        template = env.get_template('admin/Admin-index.html')
        return template.render()


    @app.route('/admin/organizations')
    def admin_organizations():
        all_organizations = organizations.get_all_organizations()
        template = env.get_template('admin/admin-watch-organization.html')
        return template.render(
            data=all_organizations,
            title1="Организация",
            title2="Организации"
        )


    @app.route('/admin/organizations/add', methods=['GET', 'POST'])
    def admin_organizations_add():
        if request.method == 'GET':
            template = env.get_template('admin/Admin-add-organization.html')
            return template.render(
                title1="Организация",
                title2="Организации",
                page_type="0",
            )

        if request.method == 'POST':
            data = request.form
            data = data.to_dict()
            return json.dumps(organizations.create_new_organization(data))


    @app.route('/admin/organizations/update/<int:id>')
    def admin_organizations_update_watch(id):
        template = env.get_template('admin/admin-update-organization.html')
        return template.render(
            title1="",
            title2="",
            data=organizations.get_single_organization(id)
        )


    @app.route('/admin/organizations/update', methods=['PUT'])
    def admin_organizations_update():
        if request.method == 'PUT':
            data = request.form
            data = data.to_dict()

            files = request.files.to_dict()

            r_data = {}

            if 'logo' in request.files:
                logo = files['logo']
                filename = secure_filename(logo.filename)
                up_img_id = upload_file_on_server(logo)
                r_data["logo"] = organizations.update_organization_logo(data["id"], up_img_id)

            if 'image' in request.files:
                logo = files['image']
                filename = secure_filename(logo.filename)
                up_img_id = upload_file_on_server(logo, data["img_desc"], data["img_title"])
                r_data["image"] = organizations.update_organization_main_image(data["id"], up_img_id)

            if 'barcode' in request.files:
                logo = files['barcode']
                filename = secure_filename(logo.filename)
                up_img_id = upload_file_on_server(logo)
                r_data["barcode"] = organizations.update_organization_barcode(data["id"], up_img_id)

            r_data["poster"] = organizations.update_organization(data)

            return r_data

    
    @app.route('/admin/organizations/delete/<int:id>')
    def delete_single_organizations(id):
        return organizations.delete_organization(id)



    @app.route('/admin/organizations/add-service', methods=['POST'])
    def admin_organizations_add_service_post():
        data = request.form
        data = data.to_dict()
        return services.create_service(data)

    @app.route('/admin/organizations/add-service/<int:id>')
    def admin_organizations_add_service_show(id):
        template = env.get_template('admin/admin-add-organization-service.html')
        return template.render(
            title1="Сервис Организации",
            title2="Сервиса Организации",
            data=organizations.get_single_organization(id),
        )

    @app.route('/admin/organizations/clear-image', methods=['POST'])
    def admin_organization_clear_images():
        data = request.form
        data = data.to_dict()

        image_type = data["image_type"]

        if (image_type == "logo"):
            organizations.update_organization_logo(data["id"], None)

        if (image_type == "main"):
            organizations.update_organization_main_image(data["id"], None)

        if (image_type == "barcode"):
            organizations.update_organization_barcode(data["id"], None)
    
        return json.dumps({
            "message": "alles gut"
        })

    @app.route('/admin/organizations/update-service/<int:id>', methods=['GET'])
    def admin_organizations_update_service_get(id):
        template = env.get_template('admin/admin-update-organization-service.html')
        print(services.get_single_service(id))
        return template.render(
            title1="Сервис Организации",
            title2="Сервиса Организации",
            data=services.get_single_service(id)
        )

    @app.route('/admin/organizations/update-service', methods=['PUT'])
    def admin_organizations_update_service_put():
        if request.method == 'PUT':
            data = request.form
            data = data.to_dict()

            files = request.files.to_dict()

            r_data = {}

            if 'logo' in request.files:
                logo = files['logo']
                filename = secure_filename(logo.filename)
                up_img_id = upload_file_on_server(logo)
                r_data["logo"] = services.update_logo(data["id"], up_img_id)

            if 'image' in request.files:
                logo = files['image']
                filename = secure_filename(logo.filename)
                up_img_id = upload_file_on_server(logo, data["img_desc"], data["img_title"])
                r_data["image"] = services.update_main_image(data["id"], up_img_id)

            if 'barcode' in request.files:
                logo = files['barcode']
                filename = secure_filename(logo.filename)
                up_img_id = upload_file_on_server(logo)
                r_data["barcode"] = services.update_barcode(data["id"], up_img_id)

            r_data["poster"] = services.update_services_info(data)

            return r_data

    @app.route('/admin/organizations/services/clear-image', methods=['POST'])
    def admin_org_serv_clear_images():
        data = request.form
        data = data.to_dict()

        image_type = data["image_type"]

        if (image_type == "logo"):
            services.update_logo(data["id"], None)
        if (image_type == "main"):
            services.update_main_image(data["id"], None)
        if (image_type == "barcode"):
            services.update_barcode(data["id"], None)

        return json.dumps({
            "message": "alles gut"
        })


    @app.route('/admin/organizations/delete-service/', methods=['POST'])
    def admin_organizations_delete_service():
        data = request.form
        data = data.to_dict()
        # return json.dumps(data)
        return services.delete_service_by_id(data["srv_id"]);

    @app.route('/admin/afisha')
    def admin_afisha():
        afisha_info = posters.get_all_afisha()
        template = env.get_template('admin/admin-watch-afisha.html')
        return template.render(
            data=afisha_info,
            title1="Афиша",
            title2="Афиши"
        )

    @app.route('/admin/afisha/update/<int:id>')
    def admin_afisha_update_watch(id):
        afisha_info = posters.get_single_afisha(id)
        template = env.get_template('admin/admin-update-afisha.html')
        return template.render(
            data=afisha_info,
            title1="Афиша",
            title2="Афиши"
        )

    @app.route('/admin/afisha/update', methods=['PUT'])
    def admin_afisha_update():
        if request.method == 'PUT':
            data = request.form
            data = data.to_dict()

            files = request.files.to_dict()
            print(files)
            print(request.files)

            r_data = {}

            if 'logo' in request.files:
                logo = files['logo']
                filename = secure_filename(logo.filename)
                logo_id = upload_file_on_server(logo)
                r_data["logo"] = posters.update_poster_logo(data["id"], logo_id)

            if 'image' in request.files:
                logo = files['image']
                filename = secure_filename(logo.filename)
                logo_id = upload_file_on_server(logo)
                r_data["image"] = posters.update_poster_main_image(data["id"], logo_id)

            r_data["poster"] = posters.update_afisha(data)

            return r_data

    @app.route('/admin/afisha/clear-image', methods=['POST'])
    def admin_afisha_clear_logo():
        data = request.form
        data = data.to_dict()

        image_type = data["image_type"]

        if (image_type == "logo"):
            posters.update_poster_logo(data["id"], None)
        else:
            posters.update_poster_main_image(data["id"], None)

        return json.dumps({
            "message": "alles gut"
        })

    @app.route('/admin/afisha/add', methods=['GET', 'POST'])
    def admin_afisha_add():
        if request.method == 'GET':
            afisha_info = posters.get_all_afisha()
            template = env.get_template('admin/Admin-add-afisha.html')
            return template.render(
                data=afisha_info,
                title1="Афиша",
                title2="Афиши"
            )

        if request.method == 'POST':
            data = request.form
            data = data.to_dict()

            # пока так...
            poster_creation =  posters.create_new_poster(data)

            files = request.files.to_dict()
            if 'logo' in request.files:
                logo = files['logo']
                filename = secure_filename(logo.filename)
                logo_id = upload_file_on_server(logo)
                # logo_id = posters.update_poster_logo(logo_id)

            return poster_creation

    @app.route('/admin/afisha/delete/<int:id>')
    def admin_afisha_update_delete(id):
        return json.dumps(posters.delete_poster(id))


    @app.route('/admin/banks')
    def admin_banks():
        template = env.get_template('admin/admin-watch-banks.html')
        return template.render(
            title1="Банк",
            title2="Банки",
            data = organizations.get_all_organizations(3)
        )


    @app.route('/admin/banks/add', methods=['GET', 'POST'])
    def admin_banks_add():
        if request.method == 'GET':
            template = env.get_template('admin/admin-add-banks.html')
            return template.render(
                title1="Банк",
                title2="Банки",
            )


        if request.method == 'POST':
            data = request.form
            data = data.to_dict()
            return json.dumps(organizations.create_new_organization_bank(data))



    @app.route('/admin/banks/update/<int:id>')
    def admin_banks_update(id):
        template = env.get_template('admin/admin-update-banks.html')
        return template.render(
            title1="Банка",
            title2="Банки",
            data = organizations.get_single_organization(id)
        )

    @app.route('/admin/banks/update', methods=['PUT'])
    def admin_organizations_banks_update():
        if request.method == 'PUT':
            data = request.form
            data = data.to_dict()

            files = request.files.to_dict()

            r_data = {}

            if 'logo' in request.files:
                logo = files['logo']
                filename = secure_filename(logo.filename)
                up_img_id = upload_file_on_server(logo)

                print("some data:")
                print(data["id"])
                print(up_img_id)
                print(logo)
                r_data["logo"] = organizations.update_organization_logo(data["id"], up_img_id)

            r_data["poster"] = organizations.update_organization_bank(data)

            return r_data

    @app.route('/admin/cafe', methods=['GET', 'PUT'])
    def admin_cafe():
        if request.method == 'GET':
            all_cafe = organizations.get_all_organizations(1) #type = 1 -> кафе
            template = env.get_template('admin/admin-watch-organization.html')
            return template.render(
                data=all_cafe,
                title1="кафе",
                title2="Кафе"
            )

        if request.method == 'PUT':
            k = request.form
            k = k.to_dict()
            return json.dumps(k)


    @app.route('/admin/cafe/add', methods=['GET', 'POST'])
    def admin_cafe_add():
        if request.method == 'GET':
            template = env.get_template('admin/Admin-add-organization.html')
            return template.render(
                title1="Кафе",
                title2="Кафе",
                page_type="1",
            )

        if request.method == 'POST':
            data = request.form
            data = data.to_dict()
            return json.dumps(organizations.create_new_organization(data))



    @app.route('/admin/pharmacy', methods=['GET', 'PUT'])
    def admin_pharmacy():
        if request.method == 'GET':
            template = env.get_template('admin/admin-update-organization.html')
            return template.render(
                data = organizations.get_single_organization_by_type(6),
                title1="Аптечный пункт",
                title2="Аптечного пункта"
            )

        if request.method == 'PUT':
            k = request.form
            k = k.to_dict()
            return misc.update_misc_info("pharmacy", k)


    @app.route('/admin/pharmacy/update-image', methods=['POST'])
    def ph_update_image():
        files = request.files.to_dict()

        print(files)
        if 'logo' in request.files:
            logo = files['logo']
            print(logo)
            print(logo.filename)
            return logo.filename

        return "updated"


    @app.route('/admin/photo', methods=['GET', 'PUT'])
    def admin_photo():
        if request.method == 'GET':
            template = env.get_template('admin/admin-update-organization.html')
            return template.render(
                data = organizations.get_single_organization_by_type(4),
                title1 = "Фото и полиграфия",
                title2 = "Фото и полиграфии"
            )


    @app.route('/admin/minimarket', methods=['GET', 'PUT'])
    def admin_minimarket():
        if request.method == 'GET':
            all_minimarket = organizations.get_single_organization_by_type(5)
            template = env.get_template('admin/admin-update-organization.html')
            return template.render(
                data=all_minimarket,
                title1="Минимаркет",
                title2="Минимаркета"
            )


    @app.route('/admin/services', methods=['GET'])
    def admin_services():
        if request.method == 'GET':
            template = env.get_template('admin/admin-watch-organization.html')
            return template.render(
                data = organizations.get_all_organizations(2),
                title1="Сервис",
                title2="Сервиса"
            )


    @app.route('/admin/services/add', methods=['GET', 'PUT'])
    def admin_services_add():
        if request.method == 'GET':
            template = env.get_template('admin/admin-add-organization.html')
            return template.render(
                title1="Сервис",
                title2="Сервиса",
                page_type="2",
            )


    @app.route('/admin/services/update/<int:id>', methods=['GET', 'PUT'])
    def admin_services_update(id):
        if request.method == 'GET':
            all_services = misc.get_misc_info('pharmacy')
            template = env.get_template('admin/Admin-update-services.html')
            return template.render(
                data=all_services,
                title1="Сервис",
                title2="Сервиса"
            )


    @app.route('/admin/tour_agent', methods=['GET', 'PUT'])
    def admin_tour_agent():
        if request.method == 'GET':
            all_tour_agent = organizations.get_single_organization_by_type(7)
            template = env.get_template('admin/admin-watch-tour_agent.html')
            return template.render(
                data=all_tour_agent,
                title1="Туристическое агенство",
                title2="Туристического агенства"
            )


    @app.route('/admin/tour_agent/update', methods=['GET', 'PUT'])
    def admin_tour_agent_update():
        if request.method == 'GET':
            all_tour_agent = misc.get_misc_info('pharmacy')
            template = env.get_template('admin/admin-watch-tour_agent.html')
            return template.render(
                data=all_tour_agent,
                title1="Туристическое агенство",
                title2="Туристического агенства"
            )


    @app.route('/admin/travels/rubrics', methods=['GET', 'PUT'])
    def admin_tour_agent_agents():
        if request.method == 'GET':
            all_tour_agent = travels.get_all_rubrics()
            template = env.get_template('admin/admin-watch-tour_agent-agents.html')
            return template.render(
                data=all_tour_agent,
                title1="Туристическое агенство",
                title2="Туристического агенства"
            )


    @app.route('/admin/tour_agent/agents-add')
    def admin_tour_agent_agents_add():
        if request.method == 'GET':
            all_tour_agent = banks.get_banks()
            template = env.get_template('admin/admin-add-tour_agent-agents.html')
            return template.render(
                data=all_tour_agent,
                title1="Агенства",
                title2="Агенства"
            )


    @app.route('/admin/travels/agents/update/<int:id>', methods=['GET'])
    def admin_travels_agents_watch(id):
        if request.method == 'GET':
            all_tour_agent = travels.get_single_rubric(id)
            template = env.get_template('admin/admin-update-travels-agents.html')
            return template.render(
                data=all_tour_agent,
                title1="Агенства",
                title2="Агенства"
            )



    app.run(debug=True, host="127.0.0.1", port=5000)
