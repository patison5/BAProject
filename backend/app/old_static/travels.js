console.log("Start");

SERVER_URL = "";
GET_ORG_URL = SERVER_URL + "getTours";


function show_org(org_name) {
    let get_org = new XMLHttpRequest();
    get_org.open("GET", GET_ORG_URL, true);
    get_org.onload = function() {
        let tour_info = JSON.parse(get_org.responseText);
        console.log(tour_info);

        let slider_1 = document.getElementsByClassName("swiper-slide")[1];
        let concert_container = slider_1.getElementsByClassName("content")[0].cloneNode(true);

        slider_1.innerHTML = '';

        // console.log(slider_1)
        for (var prop in tour_info) {
            if (tour_info[prop].type == "tour") {
                let concert_container_tmp = concert_container.cloneNode(true);
                // console.log(concert_container_tmp.getElementsByClassName("content__title"));
                concert_container_tmp.getElementsByClassName("content__title")[0].innerHTML = tour_info[prop].name;
                concert_container_tmp.getElementsByClassName("date_1")[0].innerHTML = tour_info[prop].description;
                concert_container_tmp.getElementsByClassName("content__text")[0].innerHTML = tour_info[prop].address;
                imgs = concert_container_tmp.getElementsByTagName("img");
                imgs[0].src = tour_info[prop].additional_photo[0];
                imgs[1].src = tour_info[prop].additional_photo[1];
                // console.log(tour_info[prop].additional_photo[0]);

                slider_1.appendChild(concert_container_tmp);
            }
        }

        let slider_2 = document.getElementsByClassName("swiper-slide")[2];
        let concert_container_2 = slider_2.getElementsByClassName("content")[0].cloneNode(true);

        slider_2.innerHTML = '';

        console.log(slider_2)
        for (var prop in tour_info) {
            if (tour_info[prop].type == "adv") {
                let concert_container_tmp = concert_container_2.cloneNode(true);
                imgs = concert_container_tmp.getElementsByTagName("img");
                imgs[0].src = tour_info[prop].imgs[0];
                imgs[1].src = tour_info[prop].imgs[1];
                imgs[2].src = tour_info[prop].imgs[2];
                imgs[3].src = tour_info[prop].imgs[3];
                imgs[4].src = tour_info[prop].imgs[4];
                imgs[5].src = tour_info[prop].imgs[5];
                concert_container_tmp.getElementsByClassName("content__inner-text")[0].innerHTML = tour_info[prop].text1;
                concert_container_tmp.getElementsByClassName("content__inner-text")[1].innerHTML = tour_info[prop].text2;
                concert_container_tmp.getElementsByClassName("content__inner-text")[2].innerHTML = tour_info[prop].text3;
                concert_container_tmp.getElementsByClassName("content__inner-text")[3].innerHTML = tour_info[prop].text4;

                slider_1.appendChild(concert_container_tmp);
            }
        }



    }
    get_org.send(null);
}

window.onload = function() {
    show_org();
}