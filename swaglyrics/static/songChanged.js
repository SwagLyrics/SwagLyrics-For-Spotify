const songChanged = async () => {
    const resp = await fetch("/songChanged")
    if (resp.ok && await resp.text() === "yes") location.reload(true) 
}

setInterval(songChanged, 5000);
