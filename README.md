# SocketOverWAN

Sending and Receiving TCP data over the internet via NGROK or PortMap IO

## Why this project?
Why did I decide to make this? Plenty of reasons. For starters, have you watch Mr. Robot? The CLI Chat? That!
And I wanted to establish connection between different devices over WAN for remote command execution but NGROK's dynamic IP and lease-limit policy is a huge hindrance.

### This Has Been Done Already!
Honestly, that does not matter to me. I wanted to make this anyway and so I did. I might have reinvented the wheel or not acomplished anything at all but that's fine. I don't mind this.


### What's NGROK?
What ROK have you been living under? __o.O__
If you don't know of/don't have NGROK already, make sure you download it from [here](https://ngrok.com)!
Since the URL and PORTs can be a tad bit confusing if you are new to network programming with Python,
here's a comprehensible screenshot of how your ngrok window should look like! 


__NGROK Command__
`ngrok tcp <LocalPortToBeExposed>`

![Your NGROK Screen](https://raw.githubusercontent.com/tinshade/SocketOverWAN/master/NgrokSS.PNG)


### Running The Files
1. First run the _server.py_ in a new CMD window.
2. Open up a new CMD and run the _client.py_ file.

> The message transmission will be almost instantaneous. Make sure you have your server and NGROK running while the message is being transmitted. 

#### Things To Try
1. Try running the _client.py_ file via an android device using [termux](https://termux.com/)
2. Replace NGROK with a non-dynamic solution like [Heroku](https://www.heroku.com/)