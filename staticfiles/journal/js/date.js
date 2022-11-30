$('#stop-date-div').hide();

$('#period-btn').click(function (){
    if ($('#date-type').val()=='date'){
        $('#stop-date-div').show('fast');
        $('#date-type').val('period')
        $('.table_date_label[for=table_date_start]').text('Начало');
        $(this).text('Выбрать дату');
    }
    else{
        $('#stop-date-div').hide("fast");
        $('#date-type').val('date')
        $('.table_date_label[for=table_date_start]').text('Дата');
        $(this).text('Выбрать период');
    }

})

var today = new Date();

$('#table_date_stop').val(today.toISOString().substring(0, 10))

document.getElementById("table_date_start").setAttribute("max", today.toISOString().substring(0, 10));
document.getElementById("table_date_stop").setAttribute("max", today.toISOString().substring(0, 10));
document.getElementById("table_date_stop").setAttribute("min", $('#table_date_start').val());


$('#table_date_start').change(function() {
    document.getElementById("table_date_stop").setAttribute("min", $('#table_date_start').val());

    var start_date = new Date($('#table_date_start').val());
    var stop_date = new Date($('#table_date_stop').val());

    if (start_date > stop_date) {
        $('#table_date_stop').val(start_date.toISOString().substring(0, 10));
    }
});