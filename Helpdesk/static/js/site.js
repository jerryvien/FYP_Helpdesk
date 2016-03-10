/**
 * Created by Yee.Ch on 3/11/2016.
 */
$(document).ready(function () {
    $(document).on('click', '[name=setBtn]', function () {
        var userId = $(this).data('userId');
        var $this = $(this);
        $.ajax({
            type: 'POST',
            data: {"user": userId},
            url: '/set_superuser_ajax/',
            dataType: 'json',
            success: function (json) {
                checkActionStatus($this, json, userId)
            },
            error: function () {
                UnknownErrorPopup();
            }
        });
    });
});
function checkActionStatus($this, json, userId) {
    if (json.is_superuser == true) {
        $this.attr("class","btn btn-danger btn-xs fa fa-remove")
        $this.html("Unassign")
        var $role = $("#role"+userId)
        $role.attr("class", "label label-info label-mini")
        $role.html("Admin")
    } else {
        $this.attr("class","btn btn-success btn-xs fa fa-check")
        $this.html("Assign")
        var $role = $("#role"+userId)
        $role.attr("class", "label label-danger label-mini")
        $role.html("Customer")
    }
}

function UnknownErrorPopup() {
    alert("Unknown Error!")
    location.reload();
}