package br.com.vjps.webservice.legacysystem;

import br.com.vjps.webservice.legacysystem.socket.ServerSocket;

public class LegacyServer {
	
	public static final int SERVER_PORT = 14000;
	
	public static void main(String[] args) {
		startLegacyServer(SERVER_PORT);
	}

	public static void startLegacyServer(int serverPort) {
		try (ServerSocket serverSocket = new ServerSocket(serverPort)){
			System.out.printf("Servidor on-line - Ouvindo na porta %,d\n\nAguardando novas conexoes...\n", serverPort);
			
			while(true) 
				System.out.printf("\nCliente %s conectado!\n", serverSocket.acceptClientConnection());
		} catch (Exception e) {
			System.err.println("Nao foi possivel iniciar o servidor!\nVerifique se o endereco e a porta estao disponiveis.");
		}
		
		System.exit(0);
	}
	
}
