class DebugChannel {
	constructor() {
		this.socket = io();

		// compute bindings
		this.handleServerMessage.bind(this);
		this.hotreload.bind(this);

		// socket handler
		this.socket.on('debug', this.handleServerMessage);
	}
	hotreload() {
		console.log('should hot reload now');
	}

	handleServerMessage(data) {
		switch (data.directive) {
			case 'reload':
				location.reload();
				break;
			default:
				console.log(data);
		}
	}
}

var dbgchannel = new DebugChannel();
