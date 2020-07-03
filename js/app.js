window.onload = function () {

	var data = [
		{
			"variable": "A",
			"elements": [
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				},
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				},
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				},
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				},
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				}
			]
		},
		{
			"variable": "B",
			"elements": [
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				},
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				},
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				}
			]
		},
		{
			"variable": "C",
			"elements": [
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				},
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				},
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				},
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				},
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				},
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				}
			]
		},
		{
			"variable": "B",
			"elements": [
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				},
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				},
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				}
			]
		},
		{
			"variable": "B",
			"elements": [
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				},
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				},
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				}
			]
		},
		{
			"variable": "B",
			"elements": [
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				},
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				},
				{
					"text": 'Адвокат Березин МОСКОВСКАЯ КОЛЛЕГИЯ АДВОКАТОВ "ПРАВОВОЙ ЦЕНТР "АРБАТ"',
					"link": "#"
				}
			]
		},
	]


	var counter = 0;
	var tmpArray = [];

	for (var i = 0; i < data.length; i++) {

		if (counter < 16) {
			if (counter % 2 != 0)
				counter++;
			
			tmpArray.push(data[i].variable);
			counter+=2;
		} else {
			drawSwiperElements(tmpArray)
			tmpArray = [];
			counter = 0;
		}

		for (var j = 0; j < data[i].elements.length; j++) {
			var el = data[i].elements[j];
			tmpArray.push(el)
			counter++;

			if(counter >= 16) {
				drawSwiperElements(tmpArray);
				tmpArray = [];
				counter = 0;
			} 
		}
	}

	if (tmpArray.length > 0) {
		// if (tmpArray.length < 16) {
		// 	for (var i = 0; i < (16 -tmpArray.length) / 2 + 2; i++) {
		// 		tmpArray.push("")
		// 	}
		// }

		drawSwiperElements(tmpArray);
		tmpArray = [];
		counter = 0;
	}

	var swiper = new Swiper('.swiper-container', {
		direction: 'horizontal',
    	loop: true,
		navigation: {
			nextEl: '.swiper-button-next',
			prevEl: '.swiper-button-prev',
		},
	});

	function drawSwiperElements (data) {
		var container = document.getElementsByClassName('swiper-wrapper')[0];
		var wraper = document.createElement('div');
			wraper.className = "organization-swiper swiper-slide";

		console.log(data)


		for (var i = 0; i < data.length; i++) {
			if (typeof data[i] == 'string') {
				var swiper__letter = document.createElement('div');
				swiper__letter.className = 'swiper__letter';
				swiper__letter.innerHTML = data[i];

				wraper.appendChild(swiper__letter);
			} else {
				var swiper__element = document.createElement('div');
				swiper__element.className = 'swiper__element';
				swiper__element.innerHTML = data[i].text;

				wraper.appendChild(swiper__element);
			}
		}

		container.appendChild(wraper);
	}
	
}