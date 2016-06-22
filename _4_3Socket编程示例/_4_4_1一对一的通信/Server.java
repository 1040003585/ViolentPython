//--------------- �ļ�����Server.java ----------------------------------------------------------------
package _4_3Socket���ʾ��._4_4_1һ��һ��ͨ��;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * _4_3Socket���ʾ��._4_4_1һ��һ��ͨ��
 * Copyright ? 2016 Authors. All rights reserved.
 *
 * FileName: Server.java
 * @author : Wu_Being <1040003585@qq.com>
 * Date/Time: 2016-6-7/����02:35:45
 * Description: �������˽��տͻ���Բ�뾶������Բ�����
 */
public class Server {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		System.out.println("S�ȴ�����......");
		try {
			//�����˿ں�9955�ķ������׽���
			ServerSocket serverSocket = new ServerSocket(9955);
			//���������ͻ�����������
			Socket socket=serverSocket.accept();
			System.out.println("S�����������ԣ�"+socket.getInetAddress().getHostAddress());
			//�����������������
			DataInputStream dis=new DataInputStream(socket.getInputStream());
			DataOutputStream dos=new DataOutputStream(socket.getOutputStream());
			
			boolean goon=true;
			while(goon){		
				String string=dis.readUTF();			//��socket�ж�ȡ����
				if(string.equals("end")==false){
					string=dealWith(string);			//������ִ���ض�����
					dos.writeUTF(string);				//��socket dosд����
					dos.flush();						//��ջ���������������
					System.out.println("S��������"+string+"���Ѿ�����");
				}else{
					goon=false;
					dos.writeUTF("end");
					dos.flush();
				}

			}

			//�ر�socket����
			serverSocket.close();
			dis.close();
			dos.close();

		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	
	/**
	 * ������ִ���ض����ܺ����������Ǹ�����Բ����Ĺ���
	 * @param string Բ�İ뾶
	 * @return Բ�����
	 */
	public static String dealWith(String string){
		System.out.print("S���յ��İ뾶ֵ��"+string+"����");	
		double radius=0.0;
		try {
			radius=Double.parseDouble(string);			
		} catch (NumberFormatException e) {
			return "�������ݸ�ʽ���ԣ�";
		}
		if(radius<0)return "�������ݲ���С��0��";
		double area=radius*radius*Math.PI;
		return Double.toString(area);
	}

}
