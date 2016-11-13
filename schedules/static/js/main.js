$('#save-button').click(function() {
    var fileName = 'net-events.png';
    var cachedBlob = $(this).data('blob')
    if (cachedBlob === undefined) {
        var eventsWindow = $('#events-window')[0];
        domtoimage.toBlob(eventsWindow).then(function (blob) {
            FileSaver.saveAs(blob, fileName);
            $('#save-button').data('blob', blob);
            console.log("Cached blob.");
        }).catch(function(error) {
            console.log(error);
        });
    } else {
        console.log("Using cached blob.");
        FileSaver.saveAs(cachedBlob, fileName);
    }
});
