# websocket-ping-py 
A websocket program, that is reciving timestamp , to know when to send a message and then disconnects! 
Used for headless Windows/Linux machines to know if they are online!

The script is functioning in the next order.
1. On start check if there is a internet connection by ping www.google.com.
2. Check if config.cfg exist.
3. Compare local and remote time.
4. If times are +-10 seconds, the program will consider itself synced and it will continue the execution.
5. Send the unique identifier with "|online"
6. Recives the timestamp in the future when to send the message.

For the backend i used Node-Red:
1. The websocket input node gets connected to the websocket
2. The change node is used , so it is easier to configure delay between client pings, using msg.time.
3. In the function node i configured if recieved message conatin "gettime" current timestamp will be sent to first output , else if message contain "|online" the current timestamp gets sumed with msg.time and then outputed to websocket out node.
4. Change node is used to delete the msg._session and msg._msgid ,this could be done in the function node but i wanted to keep simplicity.
5. After the change node of msg.time , i used function node to see if every message contain Machine identifier , and then for every Identifier there is one output.
6. Output for each Machine identifier is a mytimeout node , witch is preconfigured with the same time as in change node of msg.time , but it could easly be setup to programaticly change using JSON input.



<p align="center">
  <img src="https://raw.githubusercontent.com/lizzardguki/websocket-ping-py/master/Node-red.png" width="800" title="hover text">

</p>


In near future i will be building a Node-Red node and push it to NPM.
