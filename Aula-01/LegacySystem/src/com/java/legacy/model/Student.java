package com.java.legacy.model;

public class Student {

	private String registration, name;
	private int age;
	
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
	
}
