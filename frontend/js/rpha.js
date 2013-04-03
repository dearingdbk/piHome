addDevice = function() {
    $('<div />')
        .append($('<form />')
            .append($('<fieldset />')
                .append($('<legend />')
                    .html('Controller properties'))
                .append($('<label />')
                    .attr('for', 'connection-point')
                    .html('Connection point'))
                .append($('<select />')
                    .attr('id', 'connection-point')
                    .attr('name', 'connection-point')
                    .append($('<option />')
                        .attr('value', '1')
                        .html('1'))))
            .append($('<fieldset />')
                .append($('<legend />')
                    .html('Device properties'))
                .append($('<label />')
                    .attr('for', 'device-type')
                    .html('Device type'))
                .append($('<select />')
                    .attr('id', 'device-type')
                    .attr('name', 'device-type')
                    .append($('<option />')
                        .attr('value', 'lightbulb')
                        .html('Lightbulb')))))
        .dialog({
            width: 400,
            height: 400,
            modal: true,
            buttons: {
                "Add device": function() {
                },
                "Cancel": function () {
                    $(this).dialog("close");
                }
            }
        });
}

addRoom = function() {
}

$(document).ready(function () {
    $('body').append(
        $('<ul />')
            .attr('id', 'toolbar')
            .append(
                $('<li />')
                    .append(
                        $('<a></a>')
                            .attr('href', '#')
                            .html('Add device')
                            .click(addDevice)))
            .append(
                $('<li />')
                    .append(
                        $('<a></a>')
                            .attr('href', '#')
                            .html('Add room')
                            .click(addRoom))));
});