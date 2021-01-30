//Turn TV On
ipRemote.case.keyPressed('['); //Open Menu
ipRemote.case.keyPressed('2'); //Select LivingRoom
ipRemote.case.keyPressed('1'); //Select Media
ipRemote.case.keyPressed('1'); //Select Satellite

//Open Shades
ipRemote.case.postCommand({"reference": "masterbedroom-wake", "action": "runSequence", "sequence": [
	{"cover/set_cover_position": {"entity_id": "cover.springs_window_fashions_graber_csz1_cellular_shade_level", "position": 55}}, //Open Livingroom Shade 60%
	{"cover/set_cover_position": {"entity_id": "cover.downstairs_slider", "position": 60}} //Open Dining Room Shade
//	{"switch/turn_on": {"entity_id": "switch.50702012ecfabc9cfc7a"}}, //Turn on Fireplace
//	{"input_select/select_option": {"entity_id": "input_select.livingroom_fireplace_duration", "option": "60 Minutes"}} //Turn on Fireplace
]});


