package br.com.vjps.webservice.legacysystem.socket;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.List;

import com.google.gson.Gson;
import com.google.gson.JsonObject;

import br.com.vjps.webservice.legacysystem.model.Student;
import br.com.vjps.webservice.legacysystem.test.JSONable;
import br.com.vjps.webservice.legacysystem.test.Test;

public class ClientHandler implements Runnable {

	private Socket clientSocket;
	private BufferedReader inputBuffer;
    private PrintWriter outputBuffer;
	
	public ClientHandler(Socket clientSocket) throws IOException{
		this.clientSocket = clientSocket;
		inputBuffer = new BufferedReader(new InputStreamReader(this.clientSocket.getInputStream()));
		outputBuffer = new PrintWriter(this.clientSocket.getOutputStream(), true);
	}
	
	private String receivMessage() throws IOException {
		return inputBuffer.readLine();
	}
	
	private void sendMessage(String message) {
		outputBuffer.println(message);
	}

	@Override
	public void run() {
		List<br.com.vjps.webservice.legacysystem.model.Class> testClass = Test.createTestClass();
		
		Gson gson = new Gson();
		String jsonInString = gson.toJson(testClass);
		sendMessage(jsonInString);
		
		
		try {
			JsonObject data = JSONable.stringToJson(receivMessage());
			System.out.printf("\nCliente %s diz:\n", clientSocket.getInetAddress().getHostAddress());
			data.keySet().forEach(key -> {
				JsonObject json = data.getAsJsonObject(key);
				System.out.printf("\tLider da turma %s: %s", key, new Student().createByJson(json.getAsJsonObject("leader")));
			});
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		System.out.printf("\nCliente %s desconectou!\n", clientSocket.getInetAddress().getHostAddress());
	}

}
