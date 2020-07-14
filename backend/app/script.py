from flask import Flask, flash, request, redirect, url_for, render_template, current_app, g

import json
from jinja2 import Environment, PackageLoader, select_autoescape

from initdb import init_db


env = Environment(
    loader=PackageLoader('script', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

UPLOAD_FOLDER = 'app/static/uploads'
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


if __name__ == '__main__':
    images, organizations, services, posters, travels, misc = init_db()

    @app.route('/')
    def index():
        template = env.get_template('page1.html')
        return template.render(
            # title = 'Организации'
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
            print("HERE IS MY JSON :::::::")
            print(titles)
            return json.dumps(titles)


    @app.route('/organizations/<int:id>')
    def show_single_organizations(id):
        single_org = organizations.get_single_organization(id)
        template = env.get_template('single_white_post.html')
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
        allAfisha = afisha.get_all_afisha()
        template = env.get_template('posts_black.html')
        return template.render(
            title='Афиша концертного зала',
            menuElement="concert_zal-inactive",
            data=convert_to_slide_array(allAfisha)
        )


    @app.route('/afisha/<int:id>')
    def page_single_afisha(id):
        afisha_single = afisha.get_single_afisha(id)

        template = env.get_template('page7.html')
        return template.render(
            title='Афиша концертного зала',
            menuElement="concert_zal-inactive",
            data=afisha_single
        )


    @app.route('/kafe')
    def page_kafe():
        cafe_info = cafe.get_cafe_info()
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
        photo_info = photo.get_photo_info()
        template = env.get_template('single_white_post.html')
        return template.render(
            title='Фото и полиграфия',
            menuElement="photo-inactive",
            data=photo_info
        )


    @app.route('/minimarket')
    def page_minimarket():
        minimarket_info = minimarket.get_minimarket_info()
        template = env.get_template('single_white_post.html')
        return template.render(
            title='Фото и полиграфия',
            menuElement="minimarket-inactive",
            data=minimarket_info
        )


    @app.route('/pharmacy')
    def page_pharmacy():
        pharmacy_info = pharmacy.get_pharmacy_info()
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


    @app.route('/admin/organizations/add')
    def admin_organizations_add():
        template = env.get_template('admin/Admin-add-organization.html')
        return template.render(
            title1="Организация",
            title2="Организации"
        )


    @app.route('/admin/organizations/update/<int:id>')
    def admin_organizations_update(id):
        template = env.get_template('admin/admin-update-organization.html')
        return template.render(
            title1="Организация",
            title2="Организации",
            data=pharmacy.get_pharmacy_info()
        )


    @app.route('/admin/afisha')
    def admin_afisha():
        afisha_info = afisha.get_all_afisha()
        template = env.get_template('admin/Admin-index.html')
        return template.render(
            data=afisha_info,
            title1="Афиша",
            title2="Афиши"
        )


    @app.route('/admin/afisha/add')
    def admin_afisha_add():
        afisha_info = afisha.get_all_afisha()
        template = env.get_template('admin/Admin-add-afisha.html')
        return template.render(
            data=afisha_info,
            title1="Афиша",
            title2="Афиши"
        )


    @app.route('/admin/banks')
    def admin_banks():
        all_banks = banks.get_banks()
        template = env.get_template('admin/admin-watch-banks.html')
        return template.render(
            data=all_banks,
            title1="Банк",
            title2="Банки"
        )


    @app.route('/admin/banks/add')
    def admin_banks_add():
        template = env.get_template('admin/admin-add-banks.html')
        return template.render(
            title1="Банк",
            title2="Банки"
        )


    @app.route('/admin/banks/update/<int:id>')
    def admin_banks_update(id):
        template = env.get_template('admin/admin-update-banks.html')
        return template.render(
            title1="Банк",
            title2="Банки"
        )


    @app.route('/admin/cafe', methods=['GET', 'PUT'])
    def admin_cafe():
        if request.method == 'GET':
            all_cafe = cafe.get_cafe_info()
            template = env.get_template('admin/Admin-update-cafe.html')
            return template.render(
                data=all_cafe,
                title1="кафе",
                title2="Кафе"
            )

        if request.method == 'PUT':
            k = request.form
            k = k.to_dict()

            link = k['link']
            timetable = k['timetable']
            title = k['title']

            return json.dumps(k)


    @app.route('/admin/pharmacy', methods=['GET', 'PUT'])
    def admin_pharmacy():
        if request.method == 'GET':
            all_pharmacy = pharmacy.get_pharmacy_info()
            template = env.get_template('admin/Admin-update-pharmacy.html')
            return template.render(
                data=all_pharmacy,
                title1="Аптечный пункт",
                title2="Аптечного пункта"
            )

        if request.method == 'PUT':
            k = request.form
            k = k.to_dict()

            link = k['link']
            timetable = k['timetable']
            title = k['title']

            return pharmacy.update_pharmacy_info(k)


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
            all_photo = pharmacy.get_pharmacy_info()
            template = env.get_template('admin/Admin-update-photo.html')
            return template.render(
                data=all_photo,
                title1="Фото и полиграфия",
                title2="Фото и полиграфии"
            )


    @app.route('/admin/minimarket', methods=['GET', 'PUT'])
    def admin_minimarket():
        if request.method == 'GET':
            all_minimarket = pharmacy.get_pharmacy_info()
            template = env.get_template('admin/Admin-update-minimarket.html')
            return template.render(
                data=all_minimarket,
                title1="Минимаркет",
                title2="Минимаркета"
            )


    @app.route('/admin/services', methods=['GET', 'PUT'])
    def admin_services():
        if request.method == 'GET':
            all_services = pharmacy.get_pharmacy_info()
            template = env.get_template('admin/Admin-watch-services.html')
            return template.render(
                data=all_services,
                title1="Сервис",
                title2="Сервиса"
            )


    @app.route('/admin/services/update/<int:id>', methods=['GET', 'PUT'])
    def admin_services_update(id):
        if request.method == 'GET':
            all_services = pharmacy.get_pharmacy_info()
            template = env.get_template('admin/Admin-update-services.html')
            return template.render(
                data=all_services,
                title1="Сервис",
                title2="Сервиса"
            )


    @app.route('/admin/tour_agent', methods=['GET', 'PUT'])
    def admin_tour_agent():
        if request.method == 'GET':
            all_tour_agent = pharmacy.get_pharmacy_info()
            template = env.get_template('admin/admin-watch-tour_agent.html')
            return template.render(
                data=all_tour_agent,
                title1="Туристическое агенство",
                title2="Туристического агенства"
            )


    @app.route('/admin/tour_agent/update', methods=['GET', 'PUT'])
    def admin_tour_agent_update():
        if request.method == 'GET':
            all_tour_agent = pharmacy.get_pharmacy_info()
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
