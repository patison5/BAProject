SERVER_URL = "";
GET_ORG_URL = SERVER_URL + "loadOrg?org_name=";


window.onload = function() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    let org = urlParams.get('org')
    show_org(org);
}

function show_org(org_name) {
    let get_org = new XMLHttpRequest();
    get_org.open("GET", GET_ORG_URL + org_name, true);
    get_org.onload = function() {
        let org_info = JSON.parse(get_org.responseText);

        let org_field = document.getElementById("field");

        let title_text = document.getElementsByClassName("tit-text")[0];
        title_text.innerHTML = "Организация";

        console.log(document.getElementsByTagName("a"));

        if (org_info.page_type == "organization") {
            title_text.innerHTML = "Организация";
        }
        if (org_info.page_type == "service") {
            title_text.innerHTML = "Услуга";
        }
        if (org_info.page_type == "cinema") {
            title_text.innerHTML = "Концертный зал";

            document.getElementsByTagName("p")[2].innerHTML = "БАНКИ";
            console.log(document.getElementsByTagName("object")[2].data);
            document.getElementsByTagName("img")[2].src = "static/imgs/SVG/img-11.svg";
            document.getElementsByTagName("a")[2].href = "banks";
        }
        if (org_info.page_type == "cafe") {
            title_text.innerHTML = "Кафе";

            document.getElementsByTagName("p")[3].innerHTML = "БАНКИ";
            document.getElementsByTagName("img")[3].src = "static/imgs/SVG/img-11.svg";
            document.getElementsByTagName("a")[3].href = "banks";
        }
        if (org_info.page_type == "tourist_agency") {
            title_text.innerHTML = "Туристическое агентство";

            document.getElementsByTagName("p")[4].innerHTML = "БАНКИ";
            document.getElementsByTagName("img")[4].src = "static/imgs/SVG/img-11.svg";
            document.getElementsByTagName("a")[4].href = "banks";
        }
        if (org_info.page_type == "photo") {
            title_text.innerHTML = "Фото и полиграфия";

            document.getElementsByTagName("p")[5].innerHTML = "БАНКИ";
            document.getElementsByTagName("img")[5].src = "static/imgs/SVG/img-11.svg";
            document.getElementsByTagName("a")[5].href = "banks";
        }
        if (org_info.page_type == "market") {
            title_text.innerHTML = "Минемаркет";

            document.getElementsByTagName("p")[6].innerHTML = "БАНКИ";
            document.getElementsByTagName("img")[6].src = "static/imgs/SVG/img-11.svg";
            document.getElementsByTagName("a")[6].href = "banks";
        }
        if (org_info.page_type == "pharmacy") {
            title_text.innerHTML = "Аптечный пункт";

            document.getElementsByTagName("p")[7].innerHTML = "БАНКИ";
            document.getElementsByTagName("img")[7].src = "static/imgs/SVG/img-11.svg";
            document.getElementsByTagName("a")[7].href = "banks";
        }

        let header_text = document.getElementsByClassName("header-text-p")[0];
        let main_text = document.getElementsByClassName("main-info-text-p")[0];

        let address = document.getElementsByClassName("address-p")[0];
        let phone = document.getElementsByClassName("phone-p")[0];
        let email = document.getElementsByClassName("email-p")[0];
        let url = document.getElementsByClassName("url-p")[0];
        let time = document.getElementsByClassName("time-p")[0];

        let second_description = document.getElementsByClassName("second-description")[0];

        let under_description = document.getElementsByClassName("under-description")[0];

        let under_block_1 = document.getElementsByClassName("under-block-1")[0];
        let under_block_2 = document.getElementsByClassName("under-block-2")[0];
        let under_block_3 = document.getElementsByClassName("under-block-3")[0];
        let under_block_4 = document.getElementsByClassName("under-block-4")[0];

        let additional_img_1 = document.getElementsByClassName("block block-img-1")[0];
        let additional_img_2 = document.getElementsByClassName("block block-img-2")[0];
        let additional_img_3 = document.getElementsByClassName("block block-img-3")[0];
        let additional_img_4 = document.getElementsByClassName("block block-img-4")[0];

        additional_img_1.style.backgroundImage = "url(" + org_info.additional_photos[0] + ")";
        additional_img_2.style.backgroundImage = "url(" + org_info.additional_photos[1] + ")";
        additional_img_3.style.backgroundImage = "url(" + org_info.additional_photos[2] + ")";
        additional_img_4.style.backgroundImage = "url(" + org_info.additional_photos[3] + ")";

        let main_img = document.getElementsByClassName('main_img')[0];
        let logo_img = document.getElementsByClassName('logo_img')[0];

        main_img.src = org_info.main_photo;
        logo_img.src = org_info.logo;

        header_text.innerHTML = org_info.name;
        main_text.innerHTML = org_info.description;

        address.innerHTML = org_info.address;
        phone.innerHTML = org_info.phone;
        email.innerHTML = org_info.mail;
        url.innerHTML = org_info.url;
        time.innerHTML = org_info.time;

        second_description.innerHTML = org_info.main_photo_description;
        under_description.innerHTML = org_info.additional_title;

        under_block_1.innerHTML = org_info.additional_photos_text[0];
        under_block_2.innerHTML = org_info.additional_photos_text[1];
        under_block_3.innerHTML = org_info.additional_photos_text[2];
        under_block_4.innerHTML = org_info.additional_photos_text[3];

        if ((org_info.additional_photos[0] == '') || (org_info.additional_photos[1] == '') ||
            (org_info.additional_photos[2] == '') || (org_info.additional_photos[3] == '')) {
            let under = document.getElementsByClassName('under')[0];
            under.innerHTML = '';
        }
        org_field.style.visibility = "visible";
    }
    get_org.send(null);
}