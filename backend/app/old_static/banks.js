SERVER_URL = "";
GET_BANK_URL = SERVER_URL + "getBank?bank_index=";
GET_BANK_LEN = SERVER_URL + "getBankLen";


window.onload = function() {
    show_bank_len();
}

function show_bank_len(template) {
    let get_bank_len = new XMLHttpRequest();
    get_bank_len.open("GET", GET_BANK_LEN, true);
    get_bank_len.onload = function() {
        let bank_field = document.getElementById("bank_field");
        let bank_container = document.getElementsByClassName("container")[0].cloneNode(true);
        bank_container.style.visibility = "visible";
        bank_field.innerHTML = "";

        for (var i = 0; i < parseInt(get_bank_len.responseText); i++) {
            show_bank(bank_container, i);
        }

    }
    get_bank_len.send(null);
}

function show_bank(template, index) {
    let get_bank = new XMLHttpRequest();
    get_bank.open("GET", GET_BANK_URL + index, true);
    get_bank.onload = function() {
        let bank_info = JSON.parse(get_bank.responseText);

        let bank_container_tmp = template.cloneNode(true);

        let logo = bank_container_tmp.getElementsByTagName('img')[0];
        let name = bank_container_tmp.getElementsByClassName('bank-name')[0];

        let time = bank_container_tmp.getElementsByClassName('bank-time')[0];
        let floors = bank_container_tmp.getElementsByClassName('bank-place')[0];
        let description = bank_container_tmp.getElementsByClassName('bank-action')[0];

        logo.src = bank_info.logo;
        name.innerHTML = bank_info.name;
        time.innerHTML = bank_info.time;
        floors.innerHTML = bank_info.floors;
        description.innerHTML = bank_info.description;

        bank_field.appendChild(bank_container_tmp);

    }
    get_bank.send(null);
}