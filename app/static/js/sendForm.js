function sendAjaxForm(form_ajax) {
    var form = $("#" + form_ajax)
    console.log(form_ajax)
    console.log("click in" + form.attr('action'))
    $.ajax({
        type: form.attr('method'),
        url: form.attr('action'),
        success: (res) => {
            console.log('DELETED')
        },
        error: (err) => {
            console.log("err: ", err)
        }
    })
}

$(document).ready(() => {
        $("#delete_form").submit((event) => {
            sendAjaxForm("delete_form")
            event.preventDefault()
        })
    })