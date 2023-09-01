package br.com.vjps.webservice.legacysystem.test;

import java.util.ArrayList;
import java.util.List;

import br.com.vjps.webservice.legacysystem.model.Student;

public class Test {
	public static List<br.com.vjps.webservice.legacysystem.model.Class> createTestClass() {
		br.com.vjps.webservice.legacysystem.model.Class c1 = new br.com.vjps.webservice.legacysystem.model.Class("1", "Web Services", 2023);
		br.com.vjps.webservice.legacysystem.model.Class c2 = new br.com.vjps.webservice.legacysystem.model.Class("2", "Turma 45", 2023, 2);
		
		c1.addStudent(new Student("12345", "Jão da Silva", 22));
		c1.addStudent(new Student("45678", "Maria do Carmo", 18));
		c1.addStudent(new Student("78912", "Paula d'Entro", 20));
		c1.addStudent(new Student("4845", "Manga 2", 19));
		c1.addStudent(new Student("666", "Capiroto", 44));
		
		c2.addStudent(new Student("1", "Aluno 1", 10));
		c2.addStudent(new Student("2", "Aluno 2", 20));
		c2.addStudent(new Student("3", "Aluno 3", 30));
		
		List<br.com.vjps.webservice.legacysystem.model.Class> list = new ArrayList<>();
		list.add(c1);
		list.add(c2);
		
		return list;
	}
}
