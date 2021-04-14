#############################################
##            MODULE VARIABLES
#############################################
print('Load controller_masterBedroom_entertainment')

eventNum = 4
longPress = .5

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
	"Forward"	: f'sendevent /dev/input/event{eventNum} 4 4 786611 && sendevent /dev/input/event{eventNum} 1 208 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 786611 && sendevent /dev/input/event{eventNum} 1 208 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"OnToggle"	: f'sendevent /dev/input/event{eventNum} 4 4 458854 && sendevent /dev/input/event{eventNum} 1 116 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 458854 && sendevent /dev/input/event{eventNum} 1 116 0 && sendevent /dev/input/event{eventNum} 0 0 0'
}

name = 'MasterBedroom Entertainment Tasks'
zone = 'masterBedroom'
focus = 'Up'
tasks = {
	"Home": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "HOME"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Home"]}}
		#{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 40, "hidMod": 12}}}
		{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 0x223, "hidReport": 2}}}
	],
	
	"Menu": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "MENU"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Menu"]}}
		#{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 101, "hidMod": 0}}}
		{"script/publish_post": {"post": {"keyCode": "Menu", "hidCode": 0x40, "hidReport": 2}}}
	],
		
	"Back": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "BACK"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Back"]}}
		#{"script/publish_post": {"post": {"keyCode": "Back", "hidCode": 41, "hidMod": 0}}}
		{"script/publish_post": {"post": {"keyCode": "Back", "hidCode": 0x46, "hidReport": 2}}}
	],
	
	"Up": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "UP"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Up"]}}
		#{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 82, "hidMod": 0}}}
		{"script/publish_post": {"post": {"keyCode": "Up", "hidCode": 0x42, "hidReport": 2}}}
	],
	
	"Down": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "DOWN"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Down"]}}
		#{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 81, "hidMod": 0}}}
		{"script/publish_post": {"post": {"keyCode": "Down", "hidCode": 0x43, "hidReport": 2}}}
	],
	
	"Left": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "LEFT"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Left"]}}
		#{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 80, "hidMod": 0}}}
		{"script/publish_post": {"post": {"keyCode": "Left", "hidCode": 0x44, "hidReport": 2}}}
	],
	
	"Right": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "RIGHT"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Right"]}}
		#{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 79, "hidMod": 0}}}
		{"script/publish_post": {"post": {"keyCode": "Right", "hidCode": 0x45, "hidReport": 2}}}
	],
	
	"Ok": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "CENTER"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Ok"]}}
		#{"script/publish_post": {"post": {"keyCode": "Ok", "hidCode": 40, "hidMod": 0}}}
		{"script/publish_post": {"post": {"keyCode": "Ok", "hidCode": 0x41, "hidReport": 2}}}
	],
	
	"Louder": [
		{"media_player/volume_up"  : {"entity_id": "media_player.master_bedroom"}},
		#{"media_player/volume_mute": {"entity_id": "media_player.master_bedroom", "is_volume_muted": False}}
		#{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 128, "hidMod": 0}}}
		#{"script/publish_post": {"post": {"keyCode": "Louder", "hidCode": 0xE9, "hidReport": 2}}}
	],
	
	"Softer": [
		{"media_player/volume_down": {"entity_id": "media_player.master_bedroom"}},
		#{"media_player/volume_mute": {"entity_id": "media_player.master_bedroom", "is_volume_muted": False}}
		#{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 129, "hidMod": 0}}}
		#{"script/publish_post": {"post": {"keyCode": "Softer", "hidCode": 0xEA, "hidReport": 2}}}
	],
			
	"SoundToggle": [
		#{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 127, "hidMod": 0}}}
		{"script/publish_post": {"post": {"keyCode": "SoundToggle", "hidCode": 0xE2, "hidReport": 2}}}
	],
			
	"Sound": [
		{"media_player/volume_mute": {"entity_id": "media_player.master_bedroom", "is_volume_muted": False}}
	],
			
	"Silence": [
		{"media_player/volume_mute": {"entity_id": "media_player.master_bedroom", "is_volume_muted": True}}
	],
	
	"Forward": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "input keyevent --longpress 90"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Forward"]}}
		#{"script/publish_post": {"post": {"keyCode": "Forward", "hidCode": 235, "hidMod": 0, "hidRepeat": 1}}}
		#{"script/publish_post": {"post": {"keyCode": "Forward", "hidCode": 0xB3, "hidReport": 2, "hidMod": 0, "hidRepeat": 1}}}
		{"script/publish_post": {"post": {"keyCode": "Forward", "hidCode": 0xB3, "hidReport": 2, "hidWait": longPress, "hidRepeat": 1}}}
	],
	
	"Backward": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "input keyevent --longpress 89"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["Backward"]}}
		#{"script/publish_post": {"post": {"keyCode": "Backward", "hidCode": 234, "hidMod": 0, "hidRepeat": 1}}}
		#{"script/publish_post": {"post": {"keyCode": "Backward", "hidCode": 0xB4, "hidReport": 2, "hidMod": 0, "hidRepeat": 1}}}
		{"script/publish_post": {"post": {"keyCode": "Backward", "hidCode": 0xB4, "hidReport": 2, "hidWait": longPress, "hidRepeat": 1}}}
	],
	
	"PlayToggle": [
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "input keyevent 85"}}
		#{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": adbEvents["PlayToggle"]}}
		#{"script/publish_post": {"post": {"keyCode": "PlayToggle", "hidCode": 232, "hidMod": 0}}}
		{"script/publish_post": {"post": {"keyCode": "PlayToggle", "hidCode": 0xCD, "hidReport": 2}}}
	],
	
	"Open": [
		#Turn on TV
		{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_upstairs_remote", "device": "Vizio", "command": "On/Off"}},
		{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 0x223, "hidReport": 2}}},
		{"media_player/select_source": {"entity_id": "media_player.firetv_masterbedroom", "source": "com.att.tv"}},
		#{"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 40, "hidMod": 12}}},
	    {"sleep": 2},

		#Turn on Sound
		{"sonos/unjoin": {"entity_id": "media_player.bathroom"}},
		{"sonos/clear_sleep_timer": {"entity_id": "media_player.master_bedroom"}},
		{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "TV"}},
		{"media_player/volume_set": {"entity_id": "media_player.master_bedroom", "volume_level": 0.45}}
	],
		
	"OnToggle": [
		#Turn off TV
		{"script/publish_post": {"post": {"keyCode": "OnToggle", "hidCode": 0x30, "hidReport": 2}}},
		{"remote/send_command" : {"entity_id": "remote.broadlink_ir_hub_upstairs_remote", "device": "Vizio", "command": "On/Off"}},
	    {"sleep": 2},

		#Turn on Sleep Timer with Music
		{"sonos/unjoin": {"entity_id": "media_player.bathroom"}},
		{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "Blues"}},
		{"media_player/volume_set": {"entity_id": "media_player.master_bedroom", "volume_level": 0.18}},
		{"sonos/set_sleep_timer": {"entity_id": "media_player.master_bedroom", "sleep_time": 3600}}
	]
}

#########################################
#                MAIN
#########################################
