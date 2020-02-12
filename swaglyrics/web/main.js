function getLyrics(){
    eel.getLyric()(setLyrics)
}

function setLyrics(base64){
    document.getElementById("lyrics").innerHTML = base64; 
}