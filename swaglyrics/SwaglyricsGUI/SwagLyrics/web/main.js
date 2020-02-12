function getLyrics(){
	eel.artist_song()(setArtistSong)
    eel.show_cli()(setLyrics)
   // lyricss();
   setTimeout(getLyrics,7500);
}

function setLyrics(base64){
	document.getElementById("lyrics").innerHTML = base64; 
	
}

function setArtistSong(base64){
    document.getElementById("artist").innerHTML = base64 + "<br><br>";
    if(base64 == "Advertisement"){
        document.getElementById("lyrics").innerHTML = "";
    }
    else {
    if(document.getElementById("lyrics").innerHTML == ""){
        document.getElementById("lyrics").innerHTML = "Loading lyrics...";
    }
    }
}
/*function songchanged(){
    return eel.song_changed()(yes_no)
}

function yes_no(base64){
    if(base64 == "yes"){
        return true;
    }
    else{
        return false;
    }
}



function lyricss(){
    if(songchanged()){
        console.log("song changed");
        getLyrics();
        
    }
    setTimeout(lyricss,100);
}
*/
//getLyrics()

/*function fetch(){
    xhr.onreadystatechange = showScores;
    xhr.timeout = 100;
    xhr.ontimeout = backoff;
    xhr.open("GET","http://localhost/pr.php?department="+document.getElementById("department"),true);
    xhr.send();
}
function showScores(){
    if (xhr.readyState == 4 || xhr.status == 200){
        var res = xhr.responseText;
        var resArr = res.split(",");
        document.getElementById("score1").innerHTML = resArr[0];
        document.getElementById("score2").innerHTML = resArr[1];
        document.getElementById("score3").innerHTML = resArr[2];
        document.getElementById("score4").innerHTML = resArr[3];
    }
}
function backoff(){
    n = n*2;
    console.log(n);
    setTimeout(fetch, n*100);
}*/


