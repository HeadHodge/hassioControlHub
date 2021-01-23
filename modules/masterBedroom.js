console.log('masterBedroom tasks loaded');

exports.wake = '{"action": "runSequence", "reference": "media-streaming-masterbedroom", "sequence": [{"remote/send_command": {"entity_id": "remote.rm4_ir_hub_remote", "device": "Vizio", "command": "On/Off"}}, {"androidtv/adb_command": {"entity_id": "media_player.firetv_masterbedroom", "command": "POWER"}}]}';
