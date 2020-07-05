import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
# from banks import BanksController
# from organizations import OrganizationsController, ToursController
# from adv import AdvController

from string import Template

from organizations import OrganizationsController
from pharmacy import PharmacyController
from minimarket import MinimarketController
from cafe import CafeController
from services import ServicesController



import json
from jinja2 import Environment, PackageLoader, select_autoescape
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

def convert_to_slide_array (array):
    li2 = []
    for i in range(0, len(array), 4):
        li2.append(array[i:i+4])
    return li2


data_set = {
    "title": "Комитет общественных связей и молодежной политики города Москвы", 
    "logo": "http://127.0.0.1:5000/static/images/icons/img-10.svg",
    "text": "kv ipsum dolor sit amet, consectetur adipisicing elit. Maxime iure adipisci fuga tenetur repudiandae explicabo ad voluptas unde distinctio? Sint laudantium quae minus nesciunt repellendus doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
    "address": [
        "121099, Г. Москва",
        "ул. Новый Арбат, д.36",
        "19 этаж, кабинет 1928"
    ], 
    "phones": [
        "+7 (495) 633-60-02",
        "+7 (495) 633-60-02 - Офис",
        "+7 (495) 633-60-02 - Пресс-служба"
    ],
    "email": "kow@mos.ru",
    "link": "https://www.mos.ru/kos",
    "barcode": "http://127.0.0.1:5000/static/images/icons/img-1.svg",
    "images": [
        {
            "src": "http://127.0.0.1:5000/static/images/icons/Resurs_1.png",
            "desc": "Фото на документы"
        },
        {
            "src": "http://127.0.0.1:5000/static/images/icons/Resurs_1.png",
            "desc": "Поликлиника медицинского центра"
        },
        {
            "src": "http://127.0.0.1:5000/static/images/icons/Resurs_1.png",
            "desc": "Фото на документы"
        },
    ] 
}


black_post_set = [
    {
        "title": "Комитет общественных связей и молодежной политики города Москвы", 
        "logo": "http://127.0.0.1:5000/static/images/woman.png",
        "text": "kv ipsum dolor sit amet, consectetur adipisicing elit. Maxime iure adipisci fuga tenetur repudiandae explicabo ad voluptas unde distinctio? Sint laudantium quae minus nesciunt repellendus doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
        "date": "22.02.12",
        "time": "13:00",
        "address": "Большой концертный зал",
    },
    {
        "title": "Комитет общественных связей и молодежной политики города Москвы", 
        "logo": "http://127.0.0.1:5000/static/images/woman.png",
        "text": "kv ipsum dolor sit amet, consectetur adipisicing elit. Maxime iure adipisci fuga tenetur repudiandae explicabo ad voluptas unde distinctio? Sint laudantium quae minus nesciunt repellendus doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
        "date": "22.02.12",
        "time": "13:00",
        "address": "Большой концертный зал",
    },
    {
        "title": "Комитет общественных связей и молодежной политики города Москвы", 
        "logo": "http://127.0.0.1:5000/static/images/woman.png",
        "text": "kv ipsum dolor sit amet, consectetur adipisicing elit. Maxime iure adipisci fuga tenetur repudiandae explicabo ad voluptas unde distinctio? Sint laudantium quae minus nesciunt repellendus doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
        "date": "22.02.12",
        "time": "13:00",
        "address": "Большой концертный зал",
    },
    {
        "title": "Комитет общественных связей и молодежной политики города Москвы", 
        "logo": "http://127.0.0.1:5000/static/images/woman.png",
        "text": "kv ipsum dolor sit amet, consectetur adipisicing elit. Maxime iure adipisci fuga tenetur repudiandae explicabo ad voluptas unde distinctio? Sint laudantium quae minus nesciunt repellendus doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
        "date": "22.02.12",
        "time": "13:00",
        "address": "Большой концертный зал",
    },
    {
        "title": "Комитет общественных связей и молодежной политики города Москвы", 
        "logo": "http://127.0.0.1:5000/static/images/woman.png",
        "text": "kv ipsum dolor sit amet, consectetur adipisicing elit. Maxime iure adipisci fuga tenetur repudiandae explicabo ad voluptas unde distinctio? Sint laudantium quae minus nesciunt repellendus doloribus! Eos necessitatibus molestias sint reprehenderit cupiditate praesentium beatae fugit autem tempore iure aliquam culpa, suscipit inventore eaque. Et pariatur earum nam numquam soluta doloremque, repellat sapiente.", 
        "date": "22.02.12",
        "time": "13:00",
        "address": "Большой концертный зал",
    },
]

afisha_single = {
    "title": "Концерт для ложечников баяна",
    "date": "22.02.12",
    "time": "13:00",
    "stage": "Большой концертный зал",
    "text": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Tempore odit at impedit corporis, deserunt, totam velit architecto exercitationem enim similique quia expedita, fugit quam praesentium accusantium! Earum velit mollitia fuga minus quae quaerat at cumque nobis adipisci commodi est aliquid quis reprehenderit animi veniam, architecto nemo doloribus illo harum! Distinctio sit iure mollitia consequuntur libero! Ex, minus ducimus. Temporibus obcaecati quibusdam cupiditate, quasi impedit nostrum dolores ab laborum odit excepturi, recusandae voluptas, quisquam tenetur blanditiis est nesciunt tempora ipsa inventore necessitatibus. Earum suscipit sapiente, velit cum quis, ratione maxime minus dignissimos alias unde! Quae excepturi, sapiente ipsum vitae voluptatibus vero?",
    "img": "http://127.0.0.1:5000/static/images/afisha.png"
}


black_post_set = convert_to_slide_array(black_post_set)
# data_set =  json.loads(data_set)


if __name__ == '__main__':
    # banks = BanksController()
    organizations = OrganizationsController()
    pharmacy = PharmacyController()
    minimarket = MinimarketController()
    cafe = CafeController()
    services = ServicesController()
    # tours = ToursController()
    # adv = AdvController()

    @app.route('/')
    def page_index():
        template = env.get_template('page1.html')
        return template.render(
            # title = 'Организации'
            search = 'true'
        )

    @app.route('/organizations', methods=['GET'])
    def page_organizations():
        template = env.get_template('organizations.html')
        return template.render(
            title = 'Организации',
            menuElement = "organizations-inactive",
            search = 'true'
        )

    @app.route('/organizations', methods=['POST'])
    def organizations_post():
        titles = organizations.get_organization_titles()
        return json.dumps(titles)

    @app.route('/organizations/<int:id>')
    def show_single_organizations(id):
        single_org  = organizations.get_single_organization(id)

        template = env.get_template('single_white_post.html')
        return template.render(
            title = 'Фото и полиграфия',
            menuElement = "minimarket-inactive",
            data = single_org
        )

    @app.route('/services')
    def page_services():
        single_service = ServicesController.get_single_service()
        template = env.get_template('organizations.html')
        return template.render(
            title = 'Услуги',
            menuElement = "organizations-inactive",
            data = single_service
        )

    @app.route('/afisha')
    def page_afisha():
        template = env.get_template('posts_black.html')
        return template.render(
            title = 'Афиша концертного зала',
            menuElement = "concert_zal-inactive",
            data = black_post_set
        )

    @app.route('/afisha/<int:id>')
    def page_single_afisha(id):
        template = env.get_template('page7.html')
        return template.render(
            title = 'Афиша концертного зала',
            menuElement = "concert_zal-inactive",
            data = afisha_single
        )

    @app.route('/kafe')
    def page_kafe():
        cafe_info = cafe.get_cafe_info()
        template = env.get_template('single_white_post.html')
        return template.render(
            title = 'Кафе',
            menuElement = "kafe-inactive",
            data = cafe_info
        )

    @app.route('/banks')
    def page_banks():
        template = env.get_template('posts_black.html')
        return template.render(
            title = 'Банкоматы',
            menuElement = "banks-inactive",
            data = black_post_set
        )


    @app.route('/tour_agent')
    def page_tour_agent():
        template = env.get_template('posts_black.html')
        return template.render(
            title = 'Банкоматы',
            menuElement = "tour_agent-inactive",
            data = black_post_set
        )


    @app.route('/photo')
    def page_photo():
        template = env.get_template('single_white_post.html')
        return template.render(
            title = 'Фото и полиграфия',
            menuElement = "photo-inactive",
            data = data_set
        )


    @app.route('/minimarket')
    def page_minimarket():
        minimarket_info = minimarket.get_minimarket_info()
        template = env.get_template('single_white_post.html')
        return template.render(
            title = 'Фото и полиграфия',
            menuElement = "minimarket-inactive",
            data = minimarket_info
        )

    @app.route('/pharmacy')
    def page_pharmacy():
        pharmacy_info = pharmacy.get_pharmacy_info()
        template = env.get_template('single_white_post.html')
        return template.render(
            title = 'Фото и полиграфия',
            menuElement = "pharmacy-inactive",
            data = pharmacy_info
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