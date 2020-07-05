SERVER_URL = "";
GET_ORG_URL = SERVER_URL + "find_current_org?org_type=";

window.onload = function() {
	const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);

    let org_type = urlParams.get('org');
    find_org(org_type);
}

function find_org(org_type) {
    const MAX_ELEMENTS = 20;

    let get_org = new XMLHttpRequest();
    get_org.open("GET", GET_ORG_URL + org_type, true);
    get_org.onload = function() {
        let slider = document.getElementsByClassName("find-content")[0];

        let first_page = document.getElementsByClassName("slider-item")[0];
        let next_page = document.getElementsByClassName("slider-item")[1];

        let another_page = first_page.cloneNode(true);
        another_page.innerHTML = "";
        another_page.style.display = 'none';

        let content = document.getElementsByClassName("content-item")[0].cloneNode(true);

        slider.innerHTML = '';

        let org_finder = JSON.parse(get_org.responseText);
        first_page.innerHTML = "";
        next_page.innerHTML = "";


        let total_el = 0;
        let current_page = another_page.cloneNode(true);

        for (key in org_finder) {
            if (org_finder[key].length != 0) {
                let e_li = org_finder[key];
                while (e_li.length != 0) {
                    if (total_el + e_li.length > MAX_ELEMENTS) {
                    	total_el_tmp = total_el;
                        total_el = create_content(slider, current_page, content, total_el, key, e_li.slice(0, MAX_ELEMENTS - total_el));

                        e_li = e_li.slice(MAX_ELEMENTS - total_el_tmp, e_li.length);
                        current_page = another_page.cloneNode(true);
                        total_el = 0;
                    } else {
                        total_el = create_content(slider, current_page, content, total_el, key, e_li);
                        e_li = []
                    }
                }

            }


        }
        function Alert() {
            alert('sdfsf');
        }

        function Sim(sldrId) {
            let id = document.getElementById(sldrId);
            if (id) {
                this.sldrRoot = id
            } else {
                this.sldrRoot = document.querySelector('.main-info')
            };

            // Carousel objects
            this.sldrList = this.sldrRoot.querySelector('.find-content');
            this.sldrElements = this.sldrList.querySelectorAll('.slider-item');
            this.sldrElemFirst = this.sldrList.querySelector('.slider-item');
            this.leftArrow = this.sldrRoot.querySelector('div.left_button');
            this.rightArrow = this.sldrRoot.querySelector('div.right_button');
            this.indicatorDots = this.sldrRoot.querySelector('div.sim-slider-dots');

            // Initialization
            this.options = Sim.defaults;
            Sim.initialize(this)
        };

        Sim.defaults = {

            // Default options for the carousel
            loop: false, // Бесконечное зацикливание слайдера
            auto: false, // Автоматическое пролистывание
            interval: 1000, // Интервал между пролистыванием элементов (мс)
            arrows: true, // Пролистывание стрелками
            dots: false // Индикаторные точки
        };

        Sim.prototype.elemPrev = function(num) {
            num = num || 1;

            let prevElement = this.currentElement;
            this.currentElement -= num;
            if (this.currentElement < 0) this.currentElement = this.elemCount - 1;

            if (!this.options.loop) {
                if (this.currentElement == 0) {
                    this.leftArrow.style.display = 'flex'
                };
                this.rightArrow.style.display = 'flex'
            };

            this.sldrElements[this.currentElement].style.display = 'flex';
            this.sldrElements[prevElement].style.display = 'none';

            if (this.options.dots) {
                this.dotOn(prevElement);
                this.dotOff(this.currentElement)
            }
        };

        Sim.prototype.elemNext = function(num) {
            num = num || 1;

            let prevElement = this.currentElement;
            this.currentElement += num;
            if (this.currentElement >= this.elemCount) this.currentElement = 0;

            if (!this.options.loop) {
                if (this.currentElement == this.elemCount - 1) {
                    this.rightArrow.style.display = 'flex'
                };
                this.leftArrow.style.display = 'flex'
            };

            this.sldrElements[this.currentElement].style.display = 'flex';
            this.sldrElements[prevElement].style.display = 'none';

            if (this.options.dots) {
                this.dotOn(prevElement);
                this.dotOff(this.currentElement)
            }
        };

        Sim.prototype.dotOn = function(num) {
            this.indicatorDotsAll[num].style.cssText = 'background-color:#BBB; cursor:pointer;'
        };

        Sim.prototype.dotOff = function(num) {
            this.indicatorDotsAll[num].style.cssText = 'background-color:#556; cursor:default;'
        };

        Sim.initialize = function(that) {

            // Constants
            that.elemCount = that.sldrElements.length; // Количество элементов

            // Variables
            that.currentElement = 0;
            let bgTime = getTime();

            // Functions
            function getTime() {
                return new Date().getTime();
            };

            function setAutoScroll() {
                that.autoScroll = setInterval(function() {
                    let fnTime = getTime();
                    if (fnTime - bgTime + 10 > that.options.interval) {
                        bgTime = fnTime;
                        that.elemNext()
                    }
                }, that.options.interval)
            };

            // Start initialization
            if (that.elemCount <= 1) { // Отключить навигацию
                that.options.auto = false;
                that.options.arrows = false;
                that.options.dots = false;
                that.leftArrow.style.display = 'flex';
                that.rightArrow.style.display = 'flex'
            };
            if (that.elemCount >= 1) { // показать первый элемент
                that.sldrElemFirst.style.display = 'flex';
            };

            if (!that.options.loop) {
                that.leftArrow.style.display = 'flex'; // отключить левую стрелку
                that.options.auto = false; // отключить автопркрутку
            } else if (that.options.auto) { // инициализация автопрокруки
                setAutoScroll();
                // Остановка прокрутки при наведении мыши на элемент
                that.sldrList.addEventListener('mouseenter', function() { clearInterval(that.autoScroll) }, false);
                that.sldrList.addEventListener('mouseleave', setAutoScroll, false)
            };

            if (that.options.arrows) { // инициализация стрелок
                that.leftArrow.addEventListener('click', function() {
                    let fnTime = getTime();
                    if (fnTime - bgTime > 1000) {
                        bgTime = fnTime;
                        that.elemPrev()
                    }
                }, false);
                that.rightArrow.addEventListener('click', function() {
                    let fnTime = getTime();
                    if (fnTime - bgTime > 1000) {
                        bgTime = fnTime;
                        that.elemNext()
                    }
                }, false)
            } else {
                that.leftArrow.style.display = 'flex';
                that.rightArrow.style.display = 'flex'
            };

            if (that.options.dots) { // инициализация индикаторных точек
                let sum = '',
                    diffNum;
                for (let i = 0; i < that.elemCount; i++) {
                    sum += '<span class="sim-dot"></span>'
                };
                that.indicatorDots.innerHTML = sum;
                that.indicatorDotsAll = that.sldrRoot.querySelectorAll('span.sim-dot');
                // Назначаем точкам обработчик события 'click'
                for (let n = 0; n < that.elemCount; n++) {
                    that.indicatorDotsAll[n].addEventListener('click', function() {
                        diffNum = Math.abs(n - that.currentElement);
                        if (n < that.currentElement) {
                            bgTime = getTime();
                            that.elemPrev(diffNum)
                        } else if (n > that.currentElement) {
                            bgTime = getTime();
                            that.elemNext(diffNum)
                        }
                        // Если n == that.currentElement ничего не делаем
                    }, false)
                };
                that.dotOff(0); // точка[0] выключена, остальные включены
                for (let i = 1; i < that.elemCount; i++) {
                    that.dotOn(i)
                }
            }
        };

        new Sim();
    }
    get_org.send(null);

}

function create_content(slider, page, content, total_el, letter, orgs_li) {
    new_block = content.cloneNode(true);
    new_block.getElementsByTagName("p")[0].innerHTML = letter.toUpperCase();

    total_el = total_el + 2;

    let content_inner = new_block.getElementsByClassName("content-inner")[0];
    let a = new_block.getElementsByTagName("a")[0].cloneNode(true);
    content_inner.innerHTML = ""

    for (i in orgs_li) {
        let a_tmp = a.cloneNode(true);
        a_tmp.getElementsByTagName("p")[0].innerHTML = orgs_li[i];
        a_tmp.href="/organization?org=" + orgs_li[i];
        content_inner.appendChild(a_tmp);

        total_el = total_el + 1;
    }
    page.appendChild(new_block);
    slider.appendChild(page);
    return total_el

}