$(function() {
    $('.generate-button').click(function() {
      console.log('asdfasd');
        // var user = $('#txtUsername').val();
        // var pass = $('#txtPassword').val();
        $.ajax({
            url: '/generate',
            // data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                console.log($('#text'))
                $('#text').text(response)
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
