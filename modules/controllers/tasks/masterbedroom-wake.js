//Turn TV On
ipRemote.case.keyPressed('['); //Open Menu
ipRemote.case.keyPressed('3'); //Select Bedrom
ipRemote.case.keyPressed('1'); //Select Media
ipRemote.case.keyPressed('5'); //Select Audio

//Open Shades
ipRemote.case.postCommand({"reference": "masterbedroom-wake", "action": "runSequence", "sequence": [
	{"cover/open_cover": {"entity_id": "cover.upstairs_slider"}},
	{"cover/close_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
	{"sleep": 15},
	{"cover/open_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
	{"sonos/join": {"entity_id": "media_player.bathroom", "master": "media_player.master_bedroom"}},
	{"sleep": 6.4},
	{"cover/stop_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
        {"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "Blues"}},
	{"media_player/volume_set": {"entity_id": "media_player.bathroom", "volume_level": 0.4}},
	{"media_player/volume_set": {"entity_id": "media_player.master_bedroom", "volume_level": 0.4}}
]});
