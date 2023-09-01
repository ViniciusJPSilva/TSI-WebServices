package br.com.vjps.webservice.legacysystem.socket;

import java.io.IOException;
import java.net.Socket;

public class ServerSocket implements AutoCloseable {
	
	private int port;
	private java.net.ServerSocket socket;
	
	public ServerSocket(int port) throws IOException {
		this.port = port;
		socket = new java.net.ServerSocket(port);
	}

	public int getPort() {
		return port;
	}
	
	public String acceptClientConnection() throws IOException {
		Socket clientSocket = socket.accept();
		
		ClientHandler clientHandler = new ClientHandler(clientSocket);
		new Thread(clientHandler).start();
		
		return clientSocket.getInetAddress().getHostAddress();
	}

	@Override
	public void close() throws Exception {
		socket.close();
	}
	
	public boolean isOnline() {
		return !socket.isClosed();
	}
}
