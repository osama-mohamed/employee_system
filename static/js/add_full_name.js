$(function () {
    $('input[name=first_name]').on('keyup', function () {
        $('input[name=full_name]').val($(this).val());
    }, function () {
        $('input[name=last_name]').on('keyup', function () {
            $('input[name=full_name]').val($('input[name=first_name]').val() + ' ' + $('input[name=last_name]').val());
        });
    });
    // var lastName = '';
    // $('input[name=last_name]').keyup(function () {
    //     var lastName = $('input[name=last_name]').val();
    //     $('input[name=full_name]').val(firstName + lastName);
    // });
});