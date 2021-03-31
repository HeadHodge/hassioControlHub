#name="Human Interface Device" sourceId="org.bluetooth.service.human_interface_device" type="primary" uuid="1812"
class HIDService(Service):
    SERVICE_UUID = '1812'
   
    def __init__(self, bus, index, application):
        Service.__init__(self, bus, index, self.SERVICE_UUID, True)
        
        self.parent = application
        self.protocolMode = ProtocolModeCharacteristic(bus, 0, self)
        self.hidInfo = HIDInfoCharacteristic(bus, 1, self)
        self.controlPoint = ControlPointCharacteristic(bus, 2, self)
        self.report = ReportCharacteristic(bus, 3, self)
        self.reportMap = ReportMapCharacteristic(bus, 4, self)
        
        self.add_characteristic(self.protocolMode)
        self.add_characteristic(self.hidInfo)
        self.add_characteristic(self.controlPoint)
        self.add_characteristic(self.report)
        self.add_characteristic(self.reportMap)
    
        self.protocolMode.ReadValue({})
        
#name="Protocol Mode" sourceId="org.bluetooth.characteristic.protocol_mode" uuid="2A4E"
class ProtocolModeCharacteristic(Characteristic):

    CHARACTERISTIC_UUID = '2A4E'

    def __init__(self, bus, index, service):
        
        Characteristic.__init__(
                self, bus, index,
                self.CHARACTERISTIC_UUID,
                ["read", "write-without-response"],
                service)
        
        #self.value = dbus.Array([1], signature=dbus.Signature('y'))
        self.parent = service
        self.value = dbus.Array(bytearray.fromhex('01'), signature=dbus.Signature('y'))
        print(f'***ProtocolMode value***: {self.value}')
        print('********', service.parent)

    def ReadValue(self, options):
        print(f'Read ProtocolMode: {self.value}')
        return self.value

    def WriteValue(self, value, options):
        print(f'Write ProtocolMode {value}')
        self.value = value

#sourceId="org.bluetooth.characteristic.hid_control_point" uuid="2A4C"
class ControlPointCharacteristic(Characteristic):

    CHARACTERISTIC_UUID = '2A4C'

    def __init__(self, bus, index, service):
        Characteristic.__init__(
                self, bus, index,
                self.CHARACTERISTIC_UUID,
                ["write-without-response"],
                service)
        
        self.value = dbus.Array(bytearray.fromhex('00'), signature=dbus.Signature('y'))
        print(f'***ControlPoint value***: {self.value}')

    def WriteValue(self, value, options):
        print(f'Write ControlPoint {value}')
        self.value = value


#id="hid_information" name="HID Information" sourceId="org.bluetooth.characteristic.hid_information" uuid="2A4A"
class HIDInfoCharacteristic(Characteristic):

    CHARACTERISTIC_UUID = '2A4A'

    def __init__(self, bus, index, service):
        Characteristic.__init__(
                self, bus, index,
                self.CHARACTERISTIC_UUID,
                ['read'],
                service)
                
        self.value = dbus.Array(bytearray.fromhex('01110002'), signature=dbus.Signature('y'))
        print(f'***HIDInformation value***: {self.value}')

    def ReadValue(self, options):
        print(f'Read HIDInformation: {self.value}')
        return self.value


#sourceId="org.bluetooth.characteristic.report_map" uuid="2A4B"
class ReportMapCharacteristic(Characteristic):

    CHARACTERISTIC_UUID = '2A4B'

    def __init__(self, bus, index, service):
        Characteristic.__init__(
                self, bus, index,
                self.CHARACTERISTIC_UUID,
                ['read'],
                service)
                
        self.parent = service
        #self.value = dbus.Array(bytearray.fromhex('05010906a101850175019508050719e029e715002501810295017508810395057501050819012905910295017503910395067508150026ff000507190029ff8100c0050C0901A101850275109501150126ff0719012Aff078100C005010906a101850375019508050719e029e715002501810295017508150026ff000507190029ff8100c0'), signature=dbus.Signature('y'))
        self.value = dbus.Array(bytearray.fromhex('05010906a101050719e029e71500250175019508810295017508810195067508150025650507190029658100c0'), signature=dbus.Signature('y'))
        print(f'***ReportMap value***: {self.value}')

    def ReadValue(self, options):
        print(f'Read ReportMap: {self.value}')
        return self.value


#id="report" name="Report" sourceId="org.bluetooth.characteristic.report" uuid="2A4D"        
class ReportCharacteristic(Characteristic):

    CHARACTERISTIC_UUID = '2A4D'

    def __init__(self, bus, index, service):
        Characteristic.__init__(
                self, bus, index,
                self.CHARACTERISTIC_UUID,
                ['read', 'notify'],
                service)
                
        #self.add_descriptor(ClientConfigurationDescriptor(bus, 0, self))
        self.add_descriptor(ReportReferenceDescriptor(bus, 1, self))
        
        #[ 0xA1, reportNum, 0, 0, 0, 0, 0, 0, 0, 0 ]
        #self.value = dbus.Array(bytearray.fromhex('00000000000000000000'), signature=dbus.Signature('y'))
        self.value = dbus.Array(bytearray.fromhex('0000000000000000'), signature=dbus.Signature('y'))
        print(f'***Report value***: {self.value}')
                
        self.notifying = False
        #self.battery_lvl = 100
        #GObject.timeout_add(5000, self.drain_battery)

    def send(self, value='Hey'):
        print(f'***send*** {value}');
        self.payload = dbus.Array(bytearray.fromhex('a100004800000000'))       
        self.PropertiesChanged(GATT_CHRC_IFACE, { 'Value': self.payload }, [])
                
        print(f'***sent***');
        

    def ReadValue(self, options):
        print(f'Read Report: {self.value}')
        return self.value

    def WriteValue(self, value, options):
        print(f'Write Report {self.value}')
        self.value = value

    def StartNotify(self):
        print(f'Start Notify')
        if self.notifying:
            print('Already notifying, nothing to do')
            return

        self.notifying = True
        self.notify_battery_level()

    def StopNotify(self):
        print(f'Stop Notify')
        if not self.notifying:
            print('Not notifying, nothing to do')
            return

        self.notifying = False
        
#name="Client Characteristic Configuration" sourceId="org.bluetooth.descriptor.gatt.client_characteristic_configuration" uuid="2902"
class ClientConfigurationDescriptor(Descriptor):

    DESCRIPTOR_UUID = '2902'

    def __init__(self, bus, index, characteristic):
        Descriptor.__init__(
                self, bus, index,
                self.DESCRIPTOR_UUID,
                ['read', 'write'],
                characteristic)
                
        self.value = dbus.Array(bytearray.fromhex('0100'), signature=dbus.Signature('y'))
        print(f'***ClientConfiguration***: {self.value}')

    def ReadValue(self, options):
        print(f'Read ClientConfiguration: {self.value}')
        return self.value

    def WriteValue(self, value, options):
        print(f'Write ClientConfiguration {self.value}')
        self.value = value

#type="org.bluetooth.descriptor.report_reference" uuid="2908"
class ReportReferenceDescriptor(Descriptor):

    DESCRIPTOR_UUID = '2908'

    def __init__(self, bus, index, characteristic):
        Descriptor.__init__(
                self, bus, index,
                self.DESCRIPTOR_UUID,
                ['read'],
                characteristic)
                
        self.value = dbus.Array(bytearray.fromhex('0001'), signature=dbus.Signature('y'))
        print(f'***ReportReference***: {self.value}')

    def ReadValue(self, options):
        print(f'Read ReportReference: {self.value}')
        return self.value
