package br.com.vjps.webservice.legacysystem.model;

import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;

import br.com.vjps.webservice.legacysystem.test.JSONable;

public class Student implements JSONable<Student> {

	private String registration, name;
	private int age;
	
	public Student() {
	}

	public Student(String registration, String name, int age) {
		this.registration = registration;
		this.name = name;
		this.age = age;
	}

	public String getRegistration() {
		return registration;
	}

	public void setRegistration(String registration) {
		this.registration = registration;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	@Override
	public String toString() {
		return String.format("- %s, %d anos, matricula %s\n", name, age, registration);
	}

	@Override
	public Student createByJson(JsonObject data) throws JsonParseException {
		try {
			registration = data.get("registration").getAsString();
			name = data.get("name").getAsString();
			age = data.get("age").getAsInt();
			
			return this;
		} catch (Exception e) {
			throw new JsonParseException("Impossível instanciar um objeto Student.");
		}
	}
	
}
