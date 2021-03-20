#############################################
##            MODULE VARIABLES
#############################################
print('Load controller_livingRoom_entertainment')

eventNum = 5;
longPress = .75

adbEvents = {
	"Home"		: f'sendevent /dev/input/event{eventNum} 4 4 786979 && sendevent /dev/input/event{eventNum} 1 172 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 786979 && sendevent /dev/input/event{eventNum} 1 172 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Menu"		: f'sendevent /dev/input/event{eventNum} 4 4 786496 && sendevent /dev/input/event{eventNum} 1 139 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 786496 && sendevent /dev/input/event{eventNum} 1 139 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Back"		: f'sendevent /dev/input/event{eventNum} 4 4 458993 && sendevent /dev/input/event{eventNum} 1 158 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 458993 && sendevent /dev/input/event{eventNum} 1 158 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Up"		: f'sendevent /dev/input/event{eventNum} 4 4 458834 && sendevent /dev/input/event{eventNum} 1 103 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 458834 && sendevent /dev/input/event{eventNum} 1 103 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Down"		: f'sendevent /dev/input/event{eventNum} 4 4 458833 && sendevent /dev/input/event{eventNum} 1 108 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 458833 && sendevent /dev/input/event{eventNum} 1 108 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Left"		: f'sendevent /dev/input/event{eventNum} 4 4 458832 && sendevent /dev/input/event{eventNum} 1 105 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 458832 && sendevent /dev/input/event{eventNum} 1 105 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Right"		: f'sendevent /dev/input/event{eventNum} 4 4 458831 && sendevent /dev/input/event{eventNum} 1 106 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 458831 && sendevent /dev/input/event{eventNum} 1 106 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Ok"		: f'sendevent /dev/input/event{eventNum} 4 4 458840 && sendevent /dev/input/event{eventNum} 1 96 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 458840 && sendevent /dev/input/event{eventNum} 1 96 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"PlayToggle": f'sendevent /dev/input/event{eventNum} 4 4 786637 && sendevent /dev/input/event{eventNum} 1 164 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 786637 && sendevent /dev/input/event{eventNum} 1 164 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Backward"	: f'sendevent /dev/input/event{eventNum} 4 4 786612 && sendevent /dev/input/event{eventNum} 1 168 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 786612 && sendevent /dev/input/event{eventNum} 1 168 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Forward"	: f'sendevent /dev/input/event{eventNum} 4 4 786611 && sendevent /dev/input/event{eventNum} 1 208 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 786611 && sendevent /dev/input/event{eventNum} 1 208 0 && sendevent /dev/input/event{eventNum} 0 0 0'
};

name = 'MasterBedroom Entertainment Tasks';
zone = 'masterBedroom';
focus = 'Up';
tasks = {
	"Home": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "HOME"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Home"]}}
		{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 40, "hidMod": 12}}}
	],
	
	"Menu": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "MENU"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Menu"]}}
		{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 101, "hidMod": 0}}}
	],
		
	"Back": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "BACK"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Back"]}}
		{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 41, "hidMod": 0}}}
	],
	
	"Up": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "UP"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Up"]}}
		{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 82, "hidMod": 0}}}
	],
	
	"Down": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "DOWN"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Down"]}}
		{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 81, "hidMod": 0}}}
	],
	
	"Left": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "LEFT"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Left"]}}
		{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 80, "hidMod": 0}}}
	],
	
	"Right": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "RIGHT"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Right"]}}
		{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 79, "hidMod": 0}}}
	],
	
	"Ok": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "CENTER"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Ok"]}}
		{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 40, "hidMod": 0}}}
	],
	
	"Louder": [
		#{"media_player/volume_up": {"entity_id": "media_player.living_room"}},
		#{"media_player/volume_mute": {"entity_id": "media_player.living_room", "is_volume_muted": False}}
		{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 128, "hidMod": 0}}}
	],
	
	"Softer": [
		#{"media_player/volume_down": {"entity_id": "media_player.living_room"}},
		#{"media_player/volume_mute": {"entity_id": "media_player.living_room", "is_volume_muted": False}}
		{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 129, "hidMod": 0}}}
	],
    
	"SoundToggle": [
		#{"media_player/volume_mute": {"entity_id": "media_player.living_room", "is_volume_muted": True}}
		{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 127, "hidMod": 0}}}
	],
			
	"Sound": [
		{"media_player/volume_mute": {"entity_id": "media_player.living_room", "is_volume_muted": False}}
	],
			
	"Silence": [
		{"media_player/volume_mute": {"entity_id": "media_player.living_room", "is_volume_muted": True}}
	],
		
	"Forward": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "input keyevent --longpress 90"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Forward"]}}
		#{"script/publish_post": {"post": {"keyCode": "Forward", "hidCode": 235, "hidMod": 0, "hidWait": longPress}}}
		{"script/publish_post": {"post": {"keyCode": "Forward", "hidCode": 0xB3, "hidReport": 2, "hidWait": longPress, "hidRepeat": 1}}}
	],
	
	"Backward": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "input keyevent --longpress 89"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["Backward"]}}
		#{"script/publish_post": {"post": {"keyCode": "Backward", "hidCode": 234, "hidMod": 0, "hidWait": longPress}}}
		{"script/publish_post": {"post": {"keyCode": "Backward", "hidCode": 0xB4, "hidReport": 2, "hidWait": longPress, "hidRepeat": 1}}}
	],

	"PlayToggle": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "input keyevent 85"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": adbEvents["PlayToggle"]}}
		{"script/publish_post": {"post": {"keyCode": "PlayToggle", "hidCode": 232, "hidMod": 0}}}
	],
	
	"Open": [
		#{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_downstairs_remote", "device": "Insignia FireTV", "command": "On/Off"}}
		{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 102, "hidMod": 0}}}
	],
	
	"OnToggle": [
		#{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_downstairs_remote", "device": "Insignia FireTV", "command": "On/Off"}}	
		{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 102, "hidMod": 0}}}
	],
    
	"Space": [
		{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 40, "hidMod": 12}}}
	]
};

###########################################
#                MAIN
###########################################
