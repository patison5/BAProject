window.onload = function () {


	var counter = 0;
	var tmpArray = [];

	var http = new XMLHttpRequest();
	http.open('POST', '/organizations', true);

	//Send the proper header information along with the request
	http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

	http.onreadystatechange = function() {//Call a function when the state changes.
	    if(http.readyState == 4 && http.status == 200) {
	        var data = JSON.parse(http.responseText)
	        console.log(data)

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
	    }
	}
	http.send();

	

	function drawSwiperElements (data) {
		var mainCont = document.getElementsByClassName('sw-organization')[0];
		if (!mainCont)
			return;
		
		var container = mainCont.getElementsByClassName('swiper-wrapper')[0];
		var wraper = document.createElement('div');
			wraper.className = "organization-swiper swiper-slide";

		console.log(data)


		for (var i = 0; i < data.length; i++) {
			var href = document.createElement('a')
			href.setAttribute('href', "/organizations/"+data[i].id)

			if (typeof data[i] == 'string') {
				var swiper__letter = document.createElement('div');
				swiper__letter.className = 'swiper__letter';
				swiper__letter.innerHTML = data[i];

				wraper.appendChild(swiper__letter);
			} else {
				var swiper__element = document.createElement('div');
				swiper__element.className = 'swiper__element';
				swiper__element.innerHTML = data[i].text;


				href.appendChild(swiper__element)
				wraper.appendChild(href);
			}
		}

		container.appendChild(wraper);
	}
	
}