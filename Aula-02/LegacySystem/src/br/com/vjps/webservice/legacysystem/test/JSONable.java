package br.com.vjps.webservice.legacysystem.test;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;

public interface JSONable<T> {

	T createByJson(JsonObject data) throws JsonParseException;
	
	public static JsonObject stringToJson(String jsonString) {
		return new Gson().fromJson(jsonString, JsonObject.class);
	}
	
}
