/* Flash messages initialization */
$(document).ready(function(){
    $(".toast").toast('show');
});

/* Modal over modal trigger */

$('#edit_comment').click(function() {

    let comment_to_edit = $('#edit_comment').prev().text()

    let smodal_id = $('#edit_comment').prev("id")
    
    $('#edit_comment_modal').modal('show');

    $('#user_comment_smodal').text(comment_to_edit)  

    console.log(comment_to_edit)
    console.log(smodal_id)

});