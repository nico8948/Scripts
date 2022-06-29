# Scripts
Build Scripts
Thanks to the script creator Benedikt Bayer who created it for smseagle, Carlo Kleinloog only changed it for MessageBird
This script is created to send and SMS to a device that should reboot when receiving the SMS. It can also be used for notifications.


1. Place the files in the proper locations. See Script location in the script. Add to monitoring configuration... X Make this variable available in notifications (enabled)
2. Create 3 Custom User Attribute in Setup/Users/Custom user attributes.
	 access_key	_ACCESS_KEY	   Simple Text
	 body	      _BODY	         Simple Text
	 originator	_ORIGINATOR	   Simple Text
3. Create 1 Custom host attribute in Setup/Hosts/Custom host attributes and enable Show in host tables and Add to monitoring configuration.
   Show in host tables...X Show this attribute in host tables of the setup menu.
   Add to monitoring configuration...X Make this custom attribute available to check commands, notifications and the status GUI.
   NOTIFY_PHONE	Notify through SMS	Simple Text
   
4. Add phone number to host or person to send sms to.
5. Create Notification rule in Setup/Events/Notification configuration.
   In the notification method field select MessaeBird in Hostname/IP fill in rest.messagebird.com or personal URL.
   In the body field you can type the message. In my usecase Reboot.
   In the originator field you can type the sender of the message.
   In the access_key field you can type the API key, somthing like GVIaBS65l464SGSiGSuX
   Choose your conditions and save.
6. Now it should work!   
