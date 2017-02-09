
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;


public class Server {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		System.out.println("Swait for connect......");
		try {
			ServerSocket serverSocket = new ServerSocket(5000);
			Socket socket=serverSocket.accept();
			System.out.println("S connet from:"+socket.getInetAddress().getHostAddress());
			DataInputStream dis=new DataInputStream(socket.getInputStream());
			DataOutputStream dos=new DataOutputStream(socket.getOutputStream());

			dos.writeUTF(" hello, I am server.  ");	
			dos.flush();	
			System.out.println("S result sent...");

			serverSocket.close();
			dis.close();
			dos.close();

		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	

}
