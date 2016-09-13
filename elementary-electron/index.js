var remote = require('electron').remote;
var fs = require('fs');
var image = require('lightning-image-poly');
var picture = require('cat-picture');
var src = picture.src;

// Remove the default cat picture.
picture.remove();

// Create the polygon editor, with the image.
var viz = new image('#visualization', null, [src], {hullAlgorithm: 'convex'});

function save() {
    // Electron magic to make a PDF?
    remote.getCurrentWindow().webContents.printToPDF({
        portrait: true,
    }, function(err, data) {
        // Use node file system module to create a file.
        fs.writeFile('annotation.pdf', data, function(err) {
            if (err) {
                window.alert('error generating pdf! ' + err.message);
            } else {
                window.alert('pdf saved!');
            }
        });
    });
}

window.addEventListener('keydown', function(e) {
    if (e.keyCode === 80) {
        save();
    }
});
