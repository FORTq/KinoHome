$(document).ready(function() {
    var form = $('#form_add_favorite');
    var form2 = $('#form_add_favorite2');
    var form3 = $('#form_add_plan');
    var form4 = $('#form_add_plan2');
    var form5 = $('#form_text_email');


        function KinoUpdateUser(kino_id, kino_delete, kino_plan){
        var data = {};
        data.kino_id = kino_id
        data.kino_delete = kino_delete
        data.kino_plan = kino_plan
        var csrf_token = $('#form_add_favorite [name="csrfmiddlewaretoken"]').val();
         data["csrfmiddlewaretoken"] = csrf_token;

        var url = form.attr("action");

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
            },
            error:function(){
                console.log("error")
            }
        })}


    function Add_email_sub(email){
        var data = {};
        data.email = email
        console.log(data.email)
        var csrf_token = $('#text_email234 [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr("action");

        $.ajax({
            url: url,
            type: 'POST',
            headers: {'X-CSRFToken': csrf_token},
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
                console.log(data.email)
            },
            error:function(){
                console.log("error")
            }
        })}

    form.on('submit', function (e) {
        e.preventDefault();
        var submit_btn = $('#submit_btn');
        var kino_id = submit_btn.data("kino_id");
        var kino_delete = "True";
        var kino_plan = "False";
        $('.padding-top-padding-bottom2').removeClass('hidden');
        $('.padding-top-padding-bottom').addClass('hidden');
        console.log(kino_id);
        KinoUpdateUser(kino_id, kino_delete, kino_plan)
    });

    form2.on('submit', function (e) {
        e.preventDefault();
        var submit_btn = $('#submit_btn2');
        var kino_id = submit_btn.data("kino_id");
        var kino_delete = "False";
        var kino_plan = "False";
        $('.padding-top-padding-bottom').removeClass('hidden');
        $('.padding-top-padding-bottom2').addClass('hidden');
        console.log(kino_id);
        KinoUpdateUser(kino_id, kino_delete, kino_plan)
    });

    form3.on('submit', function (e) {
        e.preventDefault();
        var submit_btn = $('#submit_btn3');
        var kino_id = submit_btn.data("kino_id");
        var kino_delete = "True";
        var kino_plan = "True";
        $('.padding-top-padding-bottom4').removeClass('hidden');
        $('.padding-top-padding-bottom3').addClass('hidden');
        console.log(kino_id);
        KinoUpdateUser(kino_id, kino_delete, kino_plan)
    });

    form4.on('submit', function (e) {
        e.preventDefault();
        var submit_btn = $('#submit_btn4');
        var kino_id = submit_btn.data("kino_id");
        var kino_delete = "False";
        var kino_plan = "True";
        $('.padding-top-padding-bottom3').removeClass('hidden');
        $('.padding-top-padding-bottom4').addClass('hidden');
        console.log(kino_id);
        KinoUpdateUser(kino_id, kino_delete, kino_plan)
    });


    form5.on('submit', function (e) {
        e.preventDefault();
        var email = $('#text_email').val();
        console.log(email)
        Add_email_sub(email)
    });



})




