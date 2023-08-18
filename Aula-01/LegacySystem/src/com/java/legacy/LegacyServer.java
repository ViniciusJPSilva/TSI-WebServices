package com.java.legacy;

import java.io.ObjectOutputStream;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

import com.java.legacy.model.Student;

public class LegacyServer {
	
	public static final int SERVER_PORT = 14000;
	
	public static void main(String[] args) {
		startLegacyServer(SERVER_PORT);
	}

	public static void startLegacyServer(int serverPort) {
		try (ServerSocket serverSocket = new ServerSocket(serverPort)){
			System.out.printf("Servidor on-line - Ouvindo na porta %,d\n\nAguardando novas conexoes...", serverPort);
			
			com.java.legacy.model.Class testClass = createTestClass();
			
			while(true) {
				Socket client = serverSocket.accept();
				System.out.printf("\nCliente conectado: %s", client.getInetAddress().getHostAddress());
				ObjectOutputStream data = new ObjectOutputStream(client.getOutputStream());
				
				data.flush();
				
				PrintWriter writer = new PrintWriter(data, true);
//				String strJson = "{'message':'Heãllo World'}";
//                JSONObject jsonObj = new JSONObject(strJson);
//				writer.println(jsonObj.toString());
////				
				writer.println(testClass.toString());
				data.flush();
				data.close();
				client.close();
			}
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	private static com.java.legacy.model.Class createTestClass() {
		com.java.legacy.model.Class c = new com.java.legacy.model.Class("1", "Web Services", 2023);
		
		c.addStudent(new Student("12345", "Jão da Silva", 22));
		c.addStudent(new Student("45678", "Maria do Carmo", 18));
		c.addStudent(new Student("78912", "Paula d'Entro", 20));
		
		return c;
	}
	
}
