#############################################
##            MODULE VARIABLES
#############################################
print('Load zone_masterBedroom')

focus = 'Up'
primaryController = {}
primaryModule = None
isFocusSet = None
isTaskSet = None
isSilent = None
eventNum = 4

controllers = {
	"Home" 			: "controller_masterBedroom_entertainment",
	"Softer" 		: "controller_masterBedroom_video",
	"SoundToggle"	: "controller_masterBedroom_sound",
	"Louder" 		: "controller_masterBedroom_entertainment",
	"Backward"		: "controller_masterBedroom_fireplace",
	"PlayToggle"	: "controller_masterBedroom_covers",
	"Forward"		: "controller_masterBedroom_entertainment"
}

adbEvents = {
	"Home"		: f'sendevent /dev/input/event{eventNum} 4 4 786979 && sendevent /dev/input/event{eventNum} 1 172 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 786979 && sendevent /dev/input/event{eventNum} 1 172 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Menu"		: f'sendevent /dev/input/event{eventNum} 4 4 786496 && sendevent /dev/input/event{eventNum} 1 139 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 786496 && sendevent /dev/input/event{eventNum} 1 139 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Exit"		: f'sendevent /dev/input/event{eventNum} 4 4 458993 && sendevent /dev/input/event{eventNum} 1 158 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 458993 && sendevent /dev/input/event{eventNum} 1 158 0 && sendevent /dev/input/event{eventNum} 0 0 0',
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

tasks = {
		#Keep FireTV awake	
		"Ping"  : [
			{"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "PING"}}
		],
		
		#Wake Up	
		"Left"  : [
			#Turn Music On
			{"sonos/clear_sleep_timer": {"entity_id": "media_player.master_bedroom"}},
			{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "Blues"}},
			{"media_player/volume_set": {"entity_id": "media_player.master_bedroom", "volume_level": 0.25}},

			#Turn Fireplace On
			{"input_select/select_option": {"entity_id": "input_select.masterbedroom_fireplace_duration", "option": "90 Minutes"}},

			#Open Shade
			{"cover/open_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"cover/open_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"sleep": 10},

			{"cover/close_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"sleep": 3.2},

			{"cover/stop_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"cover/stop_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}}
		],
	
		#Morning	
		"Up"  : [
            #Turn TV On	
			{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_upstairs_remote", "device": "Vizio", "command": "On/Off"}},
            {"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 40, "hidMod": 12}}},
			{"media_player/select_source": {"entity_id": "media_player.firetv_masterbedroom", "source": "com.att.tv"}},
	
            #Turn Sond On and link bathroom speaker	
			{"sonos/clear_sleep_timer": {"entity_id": "media_player.master_bedroom"}},
			{"sonos/join": {"entity_id": "media_player.bathroom", "master": "media_player.master_bedroom"}},
			{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "TV"}},
			{"media_player/volume_set": {"entity_id": "media_player.bathroom", "volume_level": 0.45}},
			{"media_player/volume_set": {"entity_id": "media_player.master_bedroom", "volume_level": 0.3}}
		],
	
		#Daytime	
		"Right"  : [
			#Turn TV Off
			{"remote/send_command" : {"entity_id": "remote.broadlink_ir_hub_upstairs_remote", "device": "Vizio", "command": "On/Off"}},
            {"script/publish_post": {"post": {"keyCode": "OnToggle", "hidCode": 248, "hidMod": 0}}},

			#Turn Music On
			{"sonos/unjoin": {"entity_id": "media_player.bathroom"}},
			{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "Blues"}},
			{"media_player/volume_set": {"entity_id": "media_player.master_bedroom", "volume_level": 0.3}}
		],
	
		#Night	
		"Down"  : [
			#Turn Fireplace On
			{"input_select/select_option": {"entity_id": "input_select.masterbedroom_fireplace_duration", "option": "90 Minutes"}},

			#Turn TV On
			{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_upstairs_remote", "device": "Vizio", "command": "On/Off"}},
            {"script/publish_post": {"post": {"keyCode": "Home", "hidCode": 40, "hidMod": 12}}},
            {"media_player/select_source": {"entity_id": "media_player.firetv_masterbedroom", "source": "com.att.tv"}},
            #{"script/publish_post": {"post": {"keyCode": "OnToggle", "hidCode": 102, "hidMod": 0}}},

			#Turn Sound On
			{"sonos/unjoin": {"entity_id": "media_player.bathroom"}},
			{"sonos/clear_sleep_timer": {"entity_id": "media_player.master_bedroom"}},
			{"media_player/select_source": {"entity_id": "media_player.master_bedroom", "source": "TV"}},
			{"media_player/volume_set": {"entity_id": "media_player.master_bedroom", "volume_level": 0.45}},

			#Close Shades
			{"cover/close_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			#{"cover/close_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"sleep": 10},
			
			{"cover/open_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			#{"cover/open_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"sleep": 1},
			
			#{"cover/stop_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
			{"cover/stop_cover": {"entity_id": "cover.somfy_unknown_type_5a52_id_5401_level"}},
 		]
}

#######################################
#                MAIN
#######################################

primaryModule = controllers['Home']