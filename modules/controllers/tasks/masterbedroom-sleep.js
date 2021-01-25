alert("hell no");
ipRemote.control.postCommand({"reference": "media-amazontv-livingroom", "action": "runSequence", "sequence": [{"remote/send_command": {"entity_id": "remote.hub_3911_living_room", "command": "VolumeUp", 		"device": "JBL Amp"}}]});
