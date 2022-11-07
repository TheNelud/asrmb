$(document).ready( function () {
    $('#table').DataTable();

    $('#submit').on('click', function(){
        $date = $('#date').val();
     
        if($date == "" ){
            alert("Please complete field");
        }else{
            $.ajax({
                type: "POST",
                url: "insert",
                data:{
                    date: $date,
                    
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(){
                    alert('Save Data');
                    $('#date').val('');
                    window.location = "/";
                }
            });
        }
    });
} );