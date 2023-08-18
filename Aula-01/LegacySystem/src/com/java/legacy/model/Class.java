package com.java.legacy.model;

public class Class {
	
	public static final int STD_NUMBER_STUDENTS = 5;
	
	private String id, name;
	private int year;
	
	private Student students[]; 
	private int currentStudent = 0, maxNumberOfStudents;
	
	
	public Class(String id, String name, int year) {
		this.id = id;
		this.name = name;
		this.year = year;
		students = new Student[STD_NUMBER_STUDENTS];
		maxNumberOfStudents = STD_NUMBER_STUDENTS;
	}
	
	public Class(String id, String name, int year, int numberOfStudents) {
		super();
		this.id = id;
		this.name = name;
		this.year = year;
		this.students = new Student[numberOfStudents];
		maxNumberOfStudents = numberOfStudents;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getYear() {
		return year;
	}

	public void setYear(int year) {
		this.year = year;
	}

	public boolean addStudent(Student student) {
		if(currentStudent >= maxNumberOfStudents) return false;
		students[currentStudent++] = student;
		return true;
	}
	
	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder(String.format("Turma %s (id = %s) (%d)\n", name, id, year));
		
		for(int i = 0; i < currentStudent; i++)
			builder.append(students[i]);
		
		return builder.toString();
	}
	
}
