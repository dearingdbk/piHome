var BACKEND = 'http://localhost/piHome/backend-mockup/';

var DEVICE_TYPES = {
    onoff: {
        name: 'On/off',
        activate: function(el) {
            if ($(this).hasClass('on'))
                $(this).removeClass('on');
            else
                $(this).addClass('on');
        }
    },
    dimmer: {
        name: 'Dimmer',
        activate: function(el) {
        }
    },
    sensor: {
        name: 'Sensor',
        activate: function(el) {
        }
    }
};

var addTrashcan = function() {
    $('body').append($('<div />')
        .attr('id', 'trashcan')
        .addClass('device')
        .droppable({
            tolerance: 'pointer',
            hoverClass: 'hover',
            drop: function(event, ui) {
                event.preventDefault();

                if ($(ui.draggable).hasClass('room'))
                    url = BACKEND + 'rooms/' + $(ui.draggable).attr('data-room-id');
                else
                    url = BACKEND + 'devices/' + $(ui.draggable).attr('data-device-id');

                $.ajax({
                    type: 'DELETE',
                    url: url,
                    success: function(response) {
                        if (!response.success)
                            alert(response.message);
                        else
                            $(ui.draggable).remove();
                    }
                });
            }
        }));
}

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

    $('<div />')
        .append($('<form />')
            .append($('<fieldset />')
                .append($('<legend />')
                    .html('Controller properties'))
                .append($('<label />')
                    .attr('for', 'controller')
                    .html('Controller'))
                .append(controllerSelect)
                .append($('<label />')
                    .attr('for', 'connection')
                    .html('Connection'))
                .append($('<select />')
                    .attr('id', 'connection')
                    .attr('name', 'connection'))
                .append($('<label />')
                    .attr('for', 'active-high-low')
                    .html('Active'))
                .append($('<select />')
                    .attr('id', 'active-high-low')
                    .attr('name', 'active-high-low')
                    .append($('<option />')
                        .val('high')
                        .html('High'))
                    .append($('<option />')
                        .val('low')
                        .html('Low'))))
            .append($('<fieldset />')
                .append($('<legend />')
                    .html('Device properties'))
                .append($('<label />')
                    .attr('for', 'device-type')
                    .html('Device type'))
                .append(typeSelect)))
        .dialog({
            width: 400,
            height: 400,
            modal: true,
            buttons: {
                'Add device': function() {
                    $.ajax({
                        type: 'PUT',
                        url: BACKEND + 'devices',
                        data: {
                            controller: $('#controller').val(),
                            connection: $('#connection').val(),
                            active: $('#active-high-low').val(),
                            type: $('#device-type').val()
                        },
                        success: function() {
                            loadDevices();
                        }
                    });
                },
                'Cancel': function () {
                    $(this).dialog('close');
                }
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
    $.ajax({
        type: 'PUT',
        url: BACKEND + 'rooms',
        success: function() {
            loadRooms();
        }
    });
}

var loadDevices = function() {
    $('.device').not('#trashcan').remove();
    $.getJSON(BACKEND + 'devices', function(devices) {
        $.each(devices, function(index, device) {
            var position = getPositionOnPage({x: device.x, y: device.y});
            $('body').append($('<div />')
                .attr('data-device-id', device.id)
                .addClass('device')
                .addClass(device.type)
                .addClass(device.state)
                .css('left', position.x)
                .css('top', position.y)
                .draggable({
                    revert: 'valid',
                    stop: function() {
                        offset = $(this).offset();
                        $.ajax({
                            type: 'POST',
                            url: BACKEND + 'devices/' + $(this).attr('data-device-id'),
                            data: {
                                x: offset.left - $(window).width() / 2,
                                y: offset.top - $(window).height() / 2
                            }
                        });
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
            $('body').append($('<div />')
                .attr('data-room-id', room.id)
                .addClass('room')
                .css('width', room.width + 'px')
                .css('height', room.height + 'px')
                .css('left', position.x)
                .css('top', position.y)
                .draggable({
                    revert: 'valid',
                    stop: function() {
                        offset = $(this).offset();
                        $.ajax({
                            type: 'POST',
                            url: BACKEND + 'rooms/' + $(this).attr('data-room-id'),
                            data: {
                                x: offset.left - $(window).width() / 2,
                                y: offset.top - $(window).height() / 2
                            }
                        });
                    }
                })
                .resizable({
                    handles: 'se',
                    stop: function() {
                        offset = $(this).offset();
                        $.ajax({
                            type: 'POST',
                            url: BACKEND + 'rooms/' + $(this).attr('data-room-id'),
                            data: {
                                width: $(this).width(),
                                height: $(this).height()
                            }
                        });
                    }
                }));
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

    addTrashcan();
    loadDevices();
    loadRooms();
});