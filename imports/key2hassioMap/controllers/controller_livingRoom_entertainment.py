eventNum = 5;

adbEvents = {
	"Home"		: f'sendevent /dev/input/event{eventNum} 4 4 786979 && sendevent /dev/input/event{eventNum} 1 172 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 786979 && sendevent /dev/input/event{eventNum} 1 172 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Menu"		: f'sendevent /dev/input/event{eventNum} 4 4 786496 && sendevent /dev/input/event{eventNum} 1 139 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 786496 && sendevent /dev/input/event{eventNum} 1 139 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Exit"		: f'sendevent /dev/input/event{eventNum} 4 4 458993 && sendevent /dev/input/event{eventNum} 1 158 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 458993 && sendevent /dev/input/event{eventNum} 1 158 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Up"		: f'sendevent /dev/input/event{eventNum} 4 4 458834 && sendevent /dev/input/event{eventNum} 1 103 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 458834 && sendevent /dev/input/event{eventNum} 1 103 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Down"		: f'sendevent /dev/input/event{eventNum} 4 4 458833 && sendevent /dev/input/event{eventNum} 1 108 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 458833 && sendevent /dev/input/event{eventNum} 1 108 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Left"		: f'sendevent /dev/input/event{eventNum} 4 4 458832 && sendevent /dev/input/event{eventNum} 1 105 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 458832 && sendevent /dev/input/event{eventNum} 1 105 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Right"		: f'sendevent /dev/input/event{eventNum} 4 4 458831 && sendevent /dev/input/event{eventNum} 1 106 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 458831 && sendevent /dev/input/event{eventNum} 1 106 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Ok"		: f'sendevent /dev/input/event{eventNum} 4 4 458840 && sendevent /dev/input/event{eventNum} 1 96 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 458840 && sendevent /dev/input/event{eventNum} 1 96 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Stop/Start": f'sendevent /dev/input/event{eventNum} 4 4 786637 && sendevent /dev/input/event{eventNum} 1 164 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 786637 && sendevent /dev/input/event{eventNum} 1 164 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Backward"	: f'sendevent /dev/input/event{eventNum} 4 4 786612 && sendevent /dev/input/event{eventNum} 1 168 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 786612 && sendevent /dev/input/event{eventNum} 1 168 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Forward"	: f'sendevent /dev/input/event{eventNum} 4 4 786611 && sendevent /dev/input/event{eventNum} 1 208 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 786611 && sendevent /dev/input/event{eventNum} 1 208 0 && sendevent /dev/input/event{eventNum} 0 0 0'
};

name = 'MasterBedroom Entertainment Tasks';
zone = 'masterBedroom';
focus = 'Up';
tasks = {
	"Home": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "HOME"}}
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Home"]}}
	],
	
	"Menu": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "MENU"}}
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Menu"]}}
	],
		
	"Exit": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "BACK"}}
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Exit"]}}
	],
	
	"Up": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "UP"}}
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Up"]}}
	],
	
	"Down": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "DOWN"}}
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Down"]}}
	],
	
	"Left": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "LEFT"}}
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Left"]}}
	],
	
	"Right": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "RIGHT"}}
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Right"]}}
	],
	
	"Ok": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "CENTER"}}
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Ok"]}}
	],
	
	"Louder": [
		{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_downstairs_remote", "device": "JBL Soundbar", "command": "Louder"}}
	],
	
	"Softer": [
		{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_downstairs_remote", "device": "JBL Soundbar", "command": "Softer"}}
	],
			
	"Sound": [
		{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_downstairs_remote", "device": "JBL Soundbar", "command": "Silence/Sound"}}
	],
			
	"Silence": [
		{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_downstairs_remote", "device": "JBL Soundbar", "command": "Silence/Sound"}}
	],
	
	"Backward": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "input keyevent --longpress 89"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Backward"]}}
	],
	
	"Stop/Start": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "input keyevent 85"}}
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Stop/Start"]}}
	],
	
	"Forward": [
		{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "input keyevent --longpress 90"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Forward"]}}
	],
	
	"Open": [
		{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_downstairs_remote", "device": "Insignia FireTV", "command": "On/Off"}}
	],
	
	"Off/On": [
		{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_downstairs_remote", "device": "Insignia FireTV", "command": "On/Off"}}
	]
};

###########################################
#                MAIN
###########################################
print('Loaded controller.livingRoom.entertainment.py');
