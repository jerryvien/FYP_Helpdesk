var Script = function () {


    /* initialize the external events
     -----------------------------------------------------------------*/

    $('#external-events div.external-event').each(function() {

        // create an Event Object (http://arshaw.com/fullcalendar/docs/event_data/Event_Object/)
        // it doesn't need to have a start or end
        var eventObject = {
            title: $.trim($(this).text()) // use the element's text as the event title
        };

        // store the Event Object in the DOM element so we can get to it later
        $(this).data('eventObject', eventObject);

        // make the event draggable using jQuery UI
        $(this).draggable({
            zIndex: 999,
            revert: true,      // will cause the event to go back to its
            revertDuration: 0  //  original position after the drag
        });

    });

    /* initialize the calendar
     -----------------------------------------------------------------*/
    getCalender();
}();

function getCalender(){
    var date = new Date();
    var d = date.getDate();
    var m = date.getMonth();
    var y = date.getFullYear();
    var tests =""
    var titles =""
    var a = [];
    var b = [];
    $.ajax({
         type: 'GET',
         url: '/get_leave_calender/',
         dataType: 'json',
         success: function (json) {
             for (i = 0; i < json.length; i++){
                 a[i] = {
                     title: json[i].test,
                     start: new Date(y, m, json[i].date)
                 }
             }
             $('#leavecalendar').fullCalendar({
                events: a
             });
         },
         error: function () {
             UnknownErrorPopup();
         }
     });
    $.ajax({
         type: 'GET',
         url: '/get_calender/',
         dataType: 'json',
         success: function (json) {
             for (i = 0; i < json.length; i++){
                 tests = "http://127.0.0.1:9002/ticket_details/"+json[i].ticketNo
                 if ((json[i].hour <= 11))
                    if(json[i].minute >= 10)
                        titles = json[i].hour+":"+json[i].minute+" AM "+json[i].subject
                    if(json[i].minute <= 9)
                        titles = json[i].hour+":0"+json[i].minute+" AM "+json[i].subject
                 if ((json[i].hour >= 12))
                    if(json[i].minute >= 10)
                        titles = json[i].hour+":"+json[i].minute+" PM "+json[i].subject
                    if(json[i].minute <= 9)
                        titles = json[i].hour+":0"+json[i].minute+" PM "+json[i].subject
                 b[i] = {
                     title: titles,
                     start: new Date(y,json[i].month-1, json[i].date,json[i].hour,json[i].minute),
                     url: tests
                 }
             }
             $('#ticketcalendar').fullCalendar({
                 header: {
                    left: 'prev,next today',
                    center: 'title',
                    right: 'month,basicWeek,basicDay'
                    },
                 editable: true,
                events: b
             });
         },
         error: function () {
             UnknownErrorPopup();
         }
     });


}