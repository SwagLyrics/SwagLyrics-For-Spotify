function songChanged() {
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "/songChanged", true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                if (xhr.responseText === 'yes') {
                    location.reload(true)
                }
                setTimeout(songChanged, 5000)
            }
        };
        xhr.send();
    }
    songChanged();