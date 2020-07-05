SERVER_URL = "";
GET_BANK_URL = SERVER_URL + "getAds";

window.onload = function() {
    let d = new Date();

    let month = new Array(12);

    month[0] = "ЯНВАРЯ";
    month[1] = "ФЕВРАЛЯ";
    month[2] = "МАРТА";
    month[3] = "АПРЕЛЯ";
    month[4] = "МАЯ";
    month[5] = "ИЮНЯ";
    month[6] = "ИЮЛЯ";
    month[7] = "АВГУСТА";
    month[8] = "СЕНТЯБРЯ";
    month[9] = "ОКТЯБРЯ";
    month[10] = "НОЯБРЯ";
    month[11] = "ДЕКАБРЯ";

    let time = d.getHours().toString() + ":" + d.getMinutes().toString();
    document.getElementsByClassName("time-text")[0].innerHTML = time;
    let date = d.getDate().toString() + " " + month[d.getMonth()].toString() + " " + d.getFullYear().toString();
    document.getElementsByClassName("date-text")[0].innerHTML = date;
    load_adv();
}


function load_adv() {
    let get_bank = new XMLHttpRequest();
    get_bank.open("GET", GET_BANK_URL, true);
    get_bank.onload = function() {
        let adv_info = JSON.parse(get_bank.responseText);

        let i = 0
        let delay = 0;


        let timerId = setTimeout(function request() {

            // увеличить интервал для следующего запроса
            delay = adv_info[i].time * 1000;
            show_adv(adv_info[i].logo);
            i++;
            i = i % 2;
            timerId = setTimeout(request, delay);
            console.log(delay);

        }, delay);


    }
    get_bank.send(null);
}



function show_adv(path) {
    let logo = document.getElementsByTagName('img')[1];
    logo.src = path;
    // console.log(logo);
}