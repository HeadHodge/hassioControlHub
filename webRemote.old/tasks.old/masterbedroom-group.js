//Group Bedroom+Bathroom Speakers
ipRemote.case.postCommand({"reference": "masterbedroom-wake", "action": "runSequence", "sequence": [
	{"sonos/join": {"entity_id": "media_player.bathroom", "master": "media_player.master_bedroom"}},
	{"media_player/volume_set": {"entity_id": "media_player.bathroom", "volume_level": 0.5}}
]});
