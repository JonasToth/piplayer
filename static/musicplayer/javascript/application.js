/***
 Javascript functionaltiy for the player.

*/

function updateVolume(value)
{
	//alert("Volume ist " + value);
	console.log("Set Volume to " + value);
	$.get("/musicplayer/control/vol/" + value + "/");
}

function next()
{
	console.log("Next Title");
	$.get(PLAYER_URL_NEXT);
	
	updateCurrentlyPlaying();
}

function previous()
{
	console.log("Previous Title");
	$.get(PLAYER_URL_PREVIOUS);
	
	updateCurrentlyPlaying();
}

function updateCurrentlyPlaying()
{
	console.log("Get Current Title");
	$.get("/musicplayer/control/getCurrentlyPlaying/", function(data) {
		$("#currently_playing").text(data["currently_playing"]);
	});
}


function play()
{
	console.log("Play mpc");
	$.get(PLAYER_URL_PLAY);
	
	updateCurrentlyPlaying()
}

function stop()
{
	console.log("Stop mpc");
	$.get(PLAYER_URL_STOP);
	
	updateCurrentlyPlaying()
}

function shuffle()
{
	console.log("Shuffle Playlist");
	$.get(PLAYER_URL_SHUFFLE);
	
	updateCurrentlyPlaying()
}

setInterval(updateCurrentlyPlaying, 5000);
