$(function () {
    var firstName = '', lastName = '';
    $('input[name=first_name]').on('keyup keypress blur change', function () {
        firstName = $(this).val();
        updateFullName()
    });
    $('input[name=last_name]').on('keyup keypress blur change', function () {
        lastName = $(this).val();
        updateFullName()
    });
    function updateFullName() {
        if ($('input[name=first_name]').val() === '' && $('input[name=last_name]').val() === '') {
            $('input[name=full_name]').val('');
        } else {
            $('input[name=full_name]').val(firstName + ' ' + lastName);
        }
    }


    // var vals = ['', ''];
    // $('input[name="first_name"]').on('keyup keypress blur change', function(){
    //   vals[0] = $(this).val();
    //   updateFullName();
    // });
    // $('input[name="last_name"]').on('keyup keypress blur change', function(){
    //   vals[1] = $(this).val();
    //   updateFullName();
    // });
    // function updateFullName(){
    //   // $('input[name="full_name"]').val( vals.join(' ') );
    //   if ($('input[name="first_name"]').val() === '' && $('input[name="last_name"]').val() === '') {
    //       $('input[name="full_name"]').val('');
    //   } else {
    //       $('input[name="full_name"]').val( vals.join(' ') );
    //   }
    // }



    // $('input[name=first_name]').on('keyup keypress blur change', function () {
    //     // $('input[name=full_name]').val($(this).val());
    // }, function () {
    //     $('input[name=last_name]').on('keyup keypress blur change', function () {
    //         var lastName = $('input[name=last_name]').val();
    //         $('input[name=full_name]').val($('input[name=first_name]').val() + ' ' + lastName);
    //         // $('input[name=full_name]').val($('input[name=first_name]').val() + ' ' + $('input[name=last_name]').val());
    //     });
    // });

});


