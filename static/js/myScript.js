$(function () {
    $("#slideshow > div:gt(0)").hide();
    setInterval(function () {
        $('#slideshow > div:first')
            .fadeOut(1000)
            .next()
            .fadeIn(1000)
            .end()
            .appendTo('#slideshow');
    }, 3000);

    $('#userDeleteBtn').click(function () {
        decision = confirm('Вы уверены, что хотите удалить свой аккаунт?\nВсе ваши котики будут удалены.');
        if (decision) {
            location.href = location.protocol + '//' + location.hostname + ':' + location.port + '/auth/user_delete';
        }
    });

    $('#addCatBtn').click(function () {
        location.href = location.protocol + '//' + location.hostname + ':' + location.port + '/api/addcat';
    });

    $('#addCatCancelBtn').click(function () {
        location.href = location.protocol + '//' + location.hostname + ':' + location.port + '/api/mycats';
    });

    $('td').click(function (event) {
        var td = $(event.target);
        var tr = td.parent();
        var name = $.trim(tr.children().first().text());
        location.href =
            location.protocol + '//' + location.hostname + ':' + location.port + '/api/setupcat?catName=' + name;
        event.stopImmediatePropagation();
        event.preventDefault();
    });

    $('#catDeleteBtn').click(function () {
        decision = confirm('Вы уверены, что хотите удалить котика?');
        if (decision) {
            var name = $('input[name="name"]').val();
            location.href =
                location.protocol + '//' + location.hostname + ':' + location.port + '/api/deletecat?catName=' + name;
        }
    });

    $('#catSetupCancelBtn').click(function () {
        location.href = location.protocol + '//' + location.hostname + ':' + location.port + '/api/mycats';
    });
});