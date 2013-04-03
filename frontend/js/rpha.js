<<<<<<< HEAD
addDevice = function() {
=======
var BACKEND = 'http://localhost/piHome/backend-mockup/';

var DEVICE_TYPES = {
    onoff: {
        name: "On/off",
        activate: function(el) {
            if ($(this).hasClass('on'))
                $(this).removeClass('on');
            else
                $(this).addClass('on');
        }
    },
    dimmer: {
        name: "Dimmer",
        activate: function(el) {
        }
    },
    sensor: {
        name: "Sensor",
        activate: function(el) {
        }
    }
};

var addDevice = function() {
    $.getJSON(BACKEND + 'controllers', addDeviceDialog);
}

var addDeviceDialog = function(controllers) {
    var controllerSelect = $('<select />')
        .attr('id', 'controller')
        .attr('name', 'controller')
        .change(function() {
            populateConnections(controllers, $(this).val());
        });
    $.each(controllers, function(index, controller) {
        controllerSelect.append($('<option />')
            .val(controller.id)
            .html(controller.name));
    });

    var typeSelect = $('<select />')
        .attr('id', 'device-type')
        .attr('name', 'device-type');
    $.each(DEVICE_TYPES, function(type, properties) {
        typeSelect.append($('<option />')
            .val(type)
            .html(properties.name));
    })

>>>>>>> Added some UI elements.
    $('<div />')
        .append($('<form />')
            .append($('<fieldset />')
                .append($('<legend />')
                    .html('Controller properties'))
                .append($('<label />')
<<<<<<< HEAD
                    .attr('for', 'connection-point')
                    .html('Connection point'))
                .append($('<select />')
                    .attr('id', 'connection-point')
                    .attr('name', 'connection-point')
                    .append($('<option />')
                        .attr('value', '1')
                        .html('1'))))
=======
                    .attr('for', 'controller')
                    .html('Controller'))
                .append(controllerSelect)
                .append($('<label />')
                    .attr('for', 'connection')
                    .html('Connection'))
                .append($('<select />')
                    .attr('id', 'connection')
                    .attr('name', 'connection')))
>>>>>>> Added some UI elements.
            .append($('<fieldset />')
                .append($('<legend />')
                    .html('Device properties'))
                .append($('<label />')
                    .attr('for', 'device-type')
                    .html('Device type'))
<<<<<<< HEAD
                .append($('<select />')
                    .attr('id', 'device-type')
                    .attr('name', 'device-type')
                    .append($('<option />')
                        .attr('value', 'lightbulb')
                        .html('Lightbulb')))))
=======
                .append(typeSelect)))
>>>>>>> Added some UI elements.
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
<<<<<<< HEAD
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
=======
            },
            open: function() {
                populateConnections(controllers, controllers[0].id);
            },
            close: function() {
                $(this).dialog('destroy');
            }});
}

var populateConnections = function(controllers, selectedControllerId)
{
    $.each(controllers, function(index, controller) {
        if (controller.id == selectedControllerId)
        {
            $('#connection').empty();
            $.each(controller.connections, function(index, connection) {
                $('#connection')
                    .append($('<option />')
                    .val(connection.id)
                    .html(connection.name));
            });
            return;
        }
    });
}

var addRoom = function() {
}

var loadDevices = function() {
    $.getJSON(BACKEND + 'devices', function(devices) {
        $.each(devices, function(index, device) {
            var position = getPositionOnPage({x: device.x, y: device.y});
            $('body').append($('<div />')
                .addClass('device')
                .addClass(device.type)
                .addClass(device.state)
                .css('left', position.x)
                .css('top', position.y)
                .draggable({
                    stop: function() {
                        console.log('done dragging');
                    }
                })
                .click(DEVICE_TYPES[device.type].activate));
        });
    });
}

var loadRooms = function() {
    $.getJSON(BACKEND + 'rooms', function(rooms) {
        $.each(rooms, function(index, room) {
            var position = getPositionOnPage({x: room.x, y: room.y});
            var roomEl = $('<div />')
                .addClass('room')
                .css('width', room.width + 'px')
                .css('height', room.height + 'px')
                .css('left', position.x)
                .css('top', position.y);
            $('body').append(roomEl);
            roomEl.draggable();
        });
    });
}

var getPositionOnPage = function(position = {x: 0, y: 0}) {
    return {
        x: $(window).width() / 2 + position.x,
        y: $(window).height() / 2 + position.y
    };
}

var getPositionRelativeToCenter = function(position = {x: 0, y: 0}) {
    return {
        x: position.x - $(window).width() / 2,
        y: position.y - $(window).height() / 2
    }
}

$(document).ready(function () {
    $('body').append($('<ul />')
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

    loadDevices();
    loadRooms();
>>>>>>> Added some UI elements.
});