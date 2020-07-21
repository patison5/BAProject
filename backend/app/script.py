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
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

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
    images, organizations, services, posters, travels, trvnotes, misc = init_db()


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


    @app.route('/organizations/<int:id>')
    def show_single_organizations(id):
        single_org = organizations.get_single_organization(id)
        template = env.get_template('single_white_post_inside.html')
        return template.render(
            title='Фото и полиграфия',
            menuElement="minimarket-inactive",
            data=single_org
        )


    @app.route('/services')
    def page_services():
        single_service = services.get_titles_of_services()
        template = env.get_template('services.html')
        return template.render(
            title='Услуги',
            menuElement="services-inactive",
            # data = single_service
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


    @app.route('/kafe')
    def page_kafe():
        cafe_info = misc.get_misc_info('cafe')
        template = env.get_template('cafe-all.html')
        return template.render(
            title='Кафе',
            menuElement="kafe-inactive",
            data=cafe_info
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
        template = env.get_template('page5.html')
        return template.render(
            title='Банкоматы',
            menuElement="banks-inactive",
            data=banks_info
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
        photo_info = misc.get_misc_info('photo')
        template = env.get_template('single_white_post.html')
        return template.render(
            title='Фото и полиграфия',
            menuElement="photo-inactive",
            data=photo_info
        )


    @app.route('/minimarket')
    def page_minimarket():
        minimarket_info = misc.get_misc_info('minimarket')
        template = env.get_template('single_white_post.html')
        return template.render(
            title='Фото и полиграфия',
            menuElement="minimarket-inactive",
            data=minimarket_info
        )


    @app.route('/pharmacy')
    def page_pharmacy():
        pharmacy_info = misc.get_misc_info('pharmacy')
        template = env.get_template('single_white_post.html')
        return template.render(
            title='Фото и полиграфия',
            menuElement="pharmacy-inactive",
            data=pharmacy_info
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


    @app.route('/admin/banks/add')
    def admin_banks_add():
        template = env.get_template('admin/admin-add-banks.html')
        return template.render(
            title1="Банк",
            title2="Банки",
        )


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
            all_tour_agent = misc.get_misc_info('pharmacy')
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


    @app.route('/admin/tour_agent/agents', methods=['GET', 'PUT'])
    def admin_tour_agent_agents():
        if request.method == 'GET':
            all_tour_agent = banks.get_banks()
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


    # @app.route('/banks')
    # def bank_page():
    #     return render_template("banks.html")

    # @app.route('/admin')
    # def admin_page():
    #     return render_template("admin.html")

    # @app.route('/test')
    # def test():
    #     return render_template("agency.html")

    # @app.route('/test2')
    # def test2():
    #     return render_template("service_find.html")

    # @app.route('/adv-admin')
    # def adv_admin():
    #     return render_template("adv-admin.html")

    # @app.route('/adv')
    # def adv_page():
    #     return render_template("adv.html")

    # @app.route('/add_adv', methods=['GET', 'POST'])
    # def add_adv():
    #     if request.method == 'POST':
    #         if 'file' not in request.files:
    #             flash('No file part')
    #         file = request.files['file']
    #         if file.filename == '':
    #             flash('No selected file')
    #         if file and allowed_file(file.filename):
    #             filename = secure_filename(file.filename)
    #             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #             path = str(os.path.join(app.config['UPLOAD_FOLDER'] + '/' + filename))
    #             path = path[4:]

    #             file2 = request.files['file2']
    #             filename = secure_filename(file2.filename)
    #             file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #             file2_src = str(os.path.join(app.config['UPLOAD_FOLDER'] + '/' + filename))[4:]

    #             adv.add_new_adv(logo=path,
    #                                name=request.form.get('name'), time=request.form.get('time'),
    #                                date_start=request.form.get('date_start'), date_finish=request.form.get('date_finish'), file2=file2_src)
    #     return "0"

    # @app.route('/delete_adv', methods=['GET', 'POST'])
    # def delete_adv():
    #     adv.delete_adv(request.form.get('name'))
    #     return "0"

    # @app.route('/organization')
    # def org_page():
    #     return render_template("org.html")

    # @app.route('/concert')
    # def concert_page():
    #     return render_template("concert.html")

    # @app.route('/loadOrg', methods=['GET'])
    # def get_org():
    #     org_name = request.args.get("org_name")
    #     return organizations.load_org(org_name)

    # @app.route('/getBank', methods=['GET'])
    # def get_bank():
    #     bank_index = request.args.get("bank_index")
    #     return banks.load_bank(int(bank_index))

    # @app.route('/getAds', methods=['GET'])
    # def get_ads():
    #     bank_index = request.args.get("bank_index")
    #     return adv.load_adv()

    # @app.route('/getBankLen', methods=['GET'])
    # def get_bank_len():
    #     return banks.banks_len()

    # @app.route('/add_org', methods=['GET', 'POST'])
    # def add_org():
    #     if request.method == 'POST':
    #         if 'file' not in request.files:
    #             flash('No file part')

    #         file = request.files['file']
    #         if file.filename == '':
    #             flash('No selected file')
    #         if file and allowed_file(file.filename):
    #             filename = secure_filename(file.filename)
    #             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #             path = str(os.path.join(app.config['UPLOAD_FOLDER'] + '/' + filename))
    #             path = path[4:]

    #             main_photo_src = request.files['main_photo_src']
    #             filename = secure_filename(main_photo_src.filename)
    #             if main_photo_src.filename != '':
    #                 main_photo_src.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #                 photo_src = str(os.path.join(app.config['UPLOAD_FOLDER'] + '/' + filename))[4:]
    #             else:
    #                 photo_src = ''

    #             additional_photos_1 = request.files['additional_photos_1']
    #             filename = secure_filename(additional_photos_1.filename)
    #             if additional_photos_1.filename != '':
    #                 additional_photos_1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #                 additional_photos_1_src = str(os.path.join(app.config['UPLOAD_FOLDER'] + '/' + filename))[4:]
    #             else:
    #                 additional_photos_1_src = ''

    #             additional_photos_2 = request.files['additional_photos_2']
    #             filename = secure_filename(additional_photos_2.filename)
    #             if additional_photos_2.filename != '':
    #                 additional_photos_2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #                 additional_photos_2_src = str(os.path.join(app.config['UPLOAD_FOLDER'] + '/' + filename))[4:]
    #             else:
    #                 additional_photos_2_src = ''

    #             additional_photos_3 = request.files['additional_photos_3']
    #             filename = secure_filename(additional_photos_3.filename)
    #             if additional_photos_3.filename != '':
    #                 additional_photos_3.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #                 additional_photos_3_src = str(os.path.join(app.config['UPLOAD_FOLDER'] + '/' + filename))[4:]
    #             else:
    #                 additional_photos_3_src = ''

    #             additional_photos_4 = request.files['additional_photos_4']
    #             filename = secure_filename(additional_photos_4.filename)
    #             if additional_photos_4.filename != '':
    #                 additional_photos_4.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #                 additional_photos_4_src = str(os.path.join(app.config['UPLOAD_FOLDER'] + '/' + filename))[4:]
    #             else:
    #                 additional_photos_4_src = ''

    #             additional_photos = [additional_photos_1_src, additional_photos_2_src,
    #                                  additional_photos_3_src, additional_photos_4_src]

    #             additional_photos_text = [request.form.get('additional_photo_text_1'),
    #                                       request.form.get('additional_photo_text_2'),
    #                                       request.form.get('additional_photo_text_3'),
    #                                       request.form.get('additional_photo_text_4')]

    #             page_type = request.form.get('org')
    #             if page_type is None:
    #                 page_type = "organization"

    #             organizations.add_new_org(path, request.form.get('name'), request.form.get('description'),
    #                                   request.form.get('address'), request.form.get('phone'), request.form.get('mail'),
    #                                   request.form.get('url'), request.form.get('time'), photo_src, request.form.get('additional_title'),
    #                                   additional_photos, additional_photos_text,
    #                                       request.form.get('main_photo_description'), page_type)
    #     return "0"

    # @app.route('/delete_bank', methods=['GET', 'POST'])
    # def delete_bank():
    #     banks.delete_bank(request.form.get('name'))
    #     return "0"

    # @app.route('/find_org', methods=['GET', 'POST'])
    # def find_org():
    #     return render_template("org_find.html")

    # @app.route('/find_org_service', methods=['GET', 'POST'])
    # def org_find_service():
    #     return render_template("org_find_service.html")

    # @app.route('/find_current_org', methods=['GET', 'POST'])
    # def find_current_org():
    #     return organizations.find_all(request.args.get('org_type'))

    # @app.route('/add_bank', methods=['GET', 'POST'])
    # def get_image():
    #     if request.method == 'POST':
    #         if 'file' not in request.files:
    #             flash('No file part')
    #         file = request.files['file']
    #         if file.filename == '':
    #             flash('No selected file')
    #         if file and allowed_file(file.filename):
    #             filename = secure_filename(file.filename)
    #             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #             path = str(os.path.join(app.config['UPLOAD_FOLDER'] + '/' + filename))
    #             path = path[4:]
    #             banks.add_new_bank(logo=path,
    #                                name=request.form.get('name'), time=request.form.get('time'),
    #                                floors=request.form.get('floors'), description=request.form.get('description'))
    #     return "0"

    # @app.route('/delete_org', methods=['GET', 'POST'])
    # def delete_org():
    #     organizations.delete_org(request.form.get('name'))
    #     return "0"

    # @app.route('/add_travel_tour', methods=['GET', 'POST'])
    # def add_travel_tour():
    #     if request.method == 'POST':

    #         additional_photos_1 = request.files['additional_photos_1']
    #         filename = secure_filename(additional_photos_1.filename)
    #         if additional_photos_1.filename != '':
    #             additional_photos_1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #             additional_photos_1_src = str(os.path.join(app.config['UPLOAD_FOLDER'] + '/' + filename))[4:]
    #         else:
    #             additional_photos_1_src = ''

    #         additional_photos_2 = request.files['additional_photos_2']
    #         filename = secure_filename(additional_photos_2.filename)
    #         if additional_photos_2.filename != '':
    #             additional_photos_2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #             additional_photos_2_src = str(os.path.join(app.config['UPLOAD_FOLDER'] + '/' + filename))[4:]
    #         else:
    #             additional_photos_2_src = ''

    #         additional_photos = [additional_photos_1_src, additional_photos_2_src]
    #         page_type = request.form.get('org')
    #         if page_type is None:
    #             page_type = "organization"

    #         tours.add_new_travel_tour("path", request.form.get('name'), request.form.get('description'),
    #                                           request.form.get('address'), additional_photos)
    #     return "0"

    # @app.route('/add_travel_adv', methods=['GET', 'POST'])
    # def add_travel_adv():
    #     if request.method == 'POST':
    #         additional_photos_1 = request.files['additional_photos_1']
    #         filename = secure_filename(additional_photos_1.filename)
    #         if additional_photos_1.filename != '':
    #             additional_photos_1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #             additional_photos_1_src = str(os.path.join(app.config['UPLOAD_FOLDER'] + '/' + filename))[4:]
    #         else:
    #             additional_photos_1_src = ''

    #         additional_photos_2 = request.files['additional_photos_2']
    #         filename = secure_filename(additional_photos_2.filename)
    #         if additional_photos_2.filename != '':
    #             additional_photos_2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #             additional_photos_2_src = str(os.path.join(app.config['UPLOAD_FOLDER'] + '/' + filename))[4:]
    #         else:
    #             additional_photos_2_src = ''

    #         additional_photos_3 = request.files['additional_photos_3']
    #         filename = secure_filename(additional_photos_3.filename)
    #         if additional_photos_3.filename != '':
    #             additional_photos_3.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #             additional_photos_3_src = str(os.path.join(app.config['UPLOAD_FOLDER'] + '/' + filename))[4:]
    #         else:
    #             additional_photos_3_src = ''

    #         additional_photos_4 = request.files['additional_photos_2']
    #         filename = secure_filename(additional_photos_4.filename)
    #         if additional_photos_4.filename != '':
    #             additional_photos_4.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #             additional_photos_4_src = str(os.path.join(app.config['UPLOAD_FOLDER'] + '/' + filename))[4:]
    #         else:
    #             additional_photos_4_src = ''

    #         additional_photos_5 = request.files['additional_photos_2']
    #         filename = secure_filename(additional_photos_5.filename)
    #         if additional_photos_5.filename != '':
    #             additional_photos_5.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #             additional_photos_5_src = str(os.path.join(app.config['UPLOAD_FOLDER'] + '/' + filename))[4:]
    #         else:
    #             additional_photos_5_src = ''

    #         additional_photos_6 = request.files['additional_photos_2']
    #         filename = secure_filename(additional_photos_6.filename)
    #         if additional_photos_6.filename != '':
    #             additional_photos_6.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #             additional_photos_6_src = str(os.path.join(app.config['UPLOAD_FOLDER'] + '/' + filename))[4:]
    #         else:
    #             additional_photos_6_src = ''

    #         additional_photos = [additional_photos_1_src, additional_photos_2_src, additional_photos_3_src,
    #                              additional_photos_4_src, additional_photos_5_src, additional_photos_6_src]

    #         tours.add_adv(additional_photos, request.form.get('text1'), request.form.get('text2'),
    #                       request.form.get('text3'), request.form.get('text4'))
    #     return "0"

    # @app.route('/getTours', methods=['GET'])
    # def get_tours():
    #     return tours.load_all()

    app.run(debug=True, host="127.0.0.1", port=5000)

# services-inactive
# concert_zal-inactive
# kafe-inactive
# bankomat-inactive
# tour_agent-inactive
# photo-inactive
# minimarket-inactive
# pharmacy-inactive
# organizations-inactive
