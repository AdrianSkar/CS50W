
	function toggle() {
		let ele = document.getElementById("watchlist");
		if (ele.innerHTML === "Remove from watchlist") {
			ele.innerHTML = "Add to watchlist"
		} else {
			ele.innerHTML = "Remove from watchlist"
		}
	}
