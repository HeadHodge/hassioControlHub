                                       **** smartRemotes ****

<b>Overview:</b>

smartRemotes is a collection of modules to capture remote key codes and scan codes and interface the input to applications that need control input. The 1st interface written to date, captures key codes from usb hid devices (i.e. wireless usb keyboards) and interfaces the input to the Home-Assistant service bus to control smart home devices.

The main modules are loosely coupled to each other via network communications using websockets. This is a stateful communications protocol that is efficient for continuous data flow and is available on practically any platform you can think of. The ubiquitos nature of websockets along with the JSON standard for object serializaton, makes for an easy convient way to communicate between diverse systems. 
 
