var element = "klava"

$("#" + element).click(function () {
    $("#keyboard").css('display', 'block');
})


$(function(){
    var $write = $('#'+element),
        shift = false,
        capslock = false;
     
    
    $('#keyboard .line__item .k_content').click(function(){
        var $this = $(this),
            character = $this.html(); // If it's a lowercase letter, nothing happens to this variable
        
        // Code for processing the key.

        // Shift keys
        if ($this.hasClass('shift') || $this.hasClass('shift')) {
            $('.letter').toggleClass('uppercase');
            $('.symbol span').toggle();
             
            shift = (shift === true) ? false : true;
            capslock = false;
            return false;
        }

        // Caps lock
        if ($this.hasClass('capslock')) {
            $('.letter').toggleClass('uppercase');
            capslock = true;
            return false;
        }

        // Delete
        if ($this.hasClass('delete')) {
            var html = $write.val();
             
            $write.val(html.substr(0, html.length - 1));
            return false;
        }

        // Special characters
        if ($this.hasClass('symbol')) character = $('span:visible', $this).html();
        if ($this.hasClass('space')) character = ' ';
        if ($this.hasClass('tab')) character = "\t";
        if ($this.hasClass('return')) character = "\n";

        if ($this.hasClass('enter')){
            console.log($write.val())
            return false;
        };

        // Uppercase letter
        if ($this.hasClass('uppercase')) character = character.toUpperCase();
         
        // Remove shift once a key is clicked.
        if (shift === true) {
            $('.symbol span').toggle();
            if (capslock === false) $('.letter').toggleClass('uppercase');
             
            shift = false;
        }

        // Add the character
        $write.val($write.val() + character);
    });
});


var specifiedElement = document.getElementById('keyboard');
var searchInput = document.getElementById(element)

//I'm using "click" but it works with any event
document.addEventListener('click', function(event) {
    var isClickInside = specifiedElement.contains(event.target);
    var isClickInsideSearchInput = searchInput.contains(event.target);

    if (!isClickInside && !isClickInsideSearchInput) {
        $("#keyboard").hide();
    }
});