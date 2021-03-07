#############################################
##            MODULE VARIABLES
#############################################
print('Load zone_livingRoom')

focus = 'Up'
primaryController = {}
primaryModule = None
isFocusSet = None
isTaskSet = None
isSilent = None
eventNum = 4

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
	"Forward"	: f'sendevent /dev/input/event{eventNum} 4 4 786611 && sendevent /dev/input/event{eventNum} 1 208 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 786611 && sendevent /dev/input/event{eventNum} 1 208 0 && sendevent /dev/input/event{eventNum} 0 0 0',
	"Off/On"	: f'sendevent /dev/input/event{eventNum} 4 4 458854 && sendevent /dev/input/event{eventNum} 1 116 1 && sendevent /dev/input/event{eventNum} 0 0 0 && sendevent /dev/input/event{eventNum} 4 4 458854 && sendevent /dev/input/event{eventNum} 1 116 0 && sendevent /dev/input/event{eventNum} 0 0 0'
}

controllers = {
	"Home" 			: "controller_livingRoom_entertainment",
	"Softer" 		: "controller_livingRoom_video",
	"Silence/Sound"	: "controller_livingRoom_sound",
	"Louder" 		: "controller_livingRoom_entertainment",
	"Backward"		: "controller_livingRoom_fireplace",
	"Stop/Start"	: "controller_livingRoom_covers",
	"Forward"		: "controller_livingRoom_entertainment"
}

tasks = {
		#Keep FireTV awake	
		"xPing"  : [
			{"androidtv/adb_command": {"entity_id": "media_player.firetv_livingroom", "command": "WAKEUP"}}
		],
		
		#Wake Up	
		"Left"  : [
			{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_downstairs_remote", "device": "Insignia FireTV", "command": "On/Off"}}, #Turn TV On
			{"cover/set_cover_position": {"entity_id": "cover.springs_window_fashions_graber_csz1_cellular_shade_level", "position": 45}}, #Partial Open Livingroom Shade
			{"cover/set_cover_position": {"entity_id": "cover.downstairs_slider", "position": 40}}, #Partial Open Dining Room Shade
			{"input_select/select_option": {"entity_id": "input_select.livingroom_fireplace_duration", "option": "90 Minutes"}}, #Turn Fireplace On
			{"media_player/select_source": {"entity_id": "media_player.firetv_livingroom", "source": "com.att.tv"}}
		],

		#Morning	
		"Up"  : [
			{"remote/send_command": {"entity_id": "remote.broadlink_ir_hub_downstairs_remote", "device": "Insignia FireTV", "command": "On/Off"}}, #Turn TV On
			{"cover/set_cover_position": {"entity_id": "cover.springs_window_fashions_graber_csz1_cellular_shade_level", "position": 45}}, #Partial Open Livingroom Shade
			{"cover/set_cover_position": {"entity_id": "cover.downstairs_slider", "position": 40}}, #Partial Open Dining Room Shade
			{"input_select/select_option": {"entity_id": "input_select.livingroom_fireplace_duration", "option": "90 Minutes"}}, #Turn Fireplace On
			{"media_player/select_source": {"entity_id": "media_player.firetv_livingroom", "source": "com.att.tv"}}
		],
	
		#Daytime	
		"Right"  : [
		],
	
		#Night	
		"Down"  : [
		]
}

########################################
#               MAIN
########################################

primaryModule = controllers['Home']