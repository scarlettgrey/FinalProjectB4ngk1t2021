package testin;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLConnection;
import java.nio.charset.StandardCharsets;

public class SendPost {
	
	public static void main(String[] args) throws Exception {
		URL Cloud = new URL("https://asia-southeast2-rational-logic-308203.cloudfunctions.net/model-caller-py");
		URLConnection con = Cloud.openConnection();
		HttpURLConnection http = (HttpURLConnection)con;
		http.setRequestMethod("POST"); // PUT is another valid option
		http.setRequestProperty("Content-Type", "application/json; charset=UTF-8");
		http.setRequestProperty("Accept", "application/json");
		http.setDoOutput(true);
		
		String out = "{\"symptoms\": [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}";
		try(OutputStream os = con.getOutputStream()) {
		    byte[] input = out.getBytes("utf-8");
		    os.write(input, 0, input.length);			
		}
		
		try(BufferedReader br = new BufferedReader(
			new InputStreamReader(con.getInputStream(), "utf-8"))) {
		    StringBuilder response = new StringBuilder();
		    String responseLine = null;
		    while ((responseLine = br.readLine()) != null) {
		        response.append(responseLine.trim());
		    }
		    System.out.println(response.toString());
		}
	}

}
