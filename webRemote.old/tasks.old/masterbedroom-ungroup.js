//Group Bedroom+Bathroom Speakers
ipRemote.case.postCommand({"reference": "masterbedroom-wake", "action": "runSequence", "sequence": [
	{"sonos/unjoin": {"entity_id": "media_player.bathroom"}}
]});
