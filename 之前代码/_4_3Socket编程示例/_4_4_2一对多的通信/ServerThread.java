//------------------- �ļ���ServerThread.java ------------------------------------------------
package _4_3Socket���ʾ��._4_4_2һ�Զ��ͨ��;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

/**
 * _4_3Socket���ʾ��._4_4_2һ�Զ��ͨ��;
 * Copyright ? 2016 Authors. All rights reserved.
 *
 * FileName: ServerThread.java
 * @author : Wu_Being <1040003585@qq.com>
 * Date/Time: 2016-6-7/����11:11:32
 * Description: ���ñ��߳�����ɷ�������ͻ��˵�ͨ�Ź���
 */
public class ServerThread extends Thread {

	private Socket connectToClientSocket;
	private DataInputStream inFromClient;
	private DataOutputStream outToClient;
	private int clientname=1;	//������static�����������̻߳Ṳ��clienti����
	
	/**
	 * ���캯��1
	 * @param socket
	 * @throws IOException
	 */
	public ServerThread(Socket socket) throws IOException {
		super();
		connectToClientSocket=socket;
		inFromClient=new DataInputStream(connectToClientSocket.getInputStream());
		outToClient=new DataOutputStream(connectToClientSocket.getOutputStream());
		System.out.println("S�����������ԣ�"+connectToClientSocket.getInetAddress().getHostAddress());
		start();		//����run()����
	}
	/**
	 * ���캯��2
	 * @param socket
	 * @param ci ���ӵĵ�i���ͻ���
	 * @throws IOException
	 */
	public ServerThread(Socket socket,int cname) throws IOException {
		super();
		connectToClientSocket=socket;
		clientname=cname;
		inFromClient=new DataInputStream(connectToClientSocket.getInputStream());
		outToClient=new DataOutputStream(connectToClientSocket.getOutputStream());
		System.out.println("S������������"+clientname+"��"+connectToClientSocket.getInetAddress().getHostAddress());
		start();		//����run()����
	}
	
	/**
	 * ��run()������ͻ���ͨ��
	 */
	@Override
	public void run() {
		// TODO Auto-generated method stub
		super.run();
		System.out.println("S����Clinet"+clientname+"......");
		try {
			boolean goon=true;
			while(goon){		
				String string=inFromClient.readUTF();			//��socket�ж�ȡ����
				if(string.equals("end")==false){
					string=dealWith(string,clientname);					//������ִ���ض�����
					outToClient.writeUTF(string);				//��socket dosд����
					outToClient.flush();						//��ջ���������������
					System.out.println("SC"+clientname+"��������"+string+"���Ѿ�����");
				}else{
					goon=false;
					outToClient.writeUTF("end");
					outToClient.flush();
					System.out.println("SC"+clientname+"�������������");
				}

			}

			//�ر�socket����
			connectToClientSocket.close();
			inFromClient.close();
			outToClient.close();

		} catch (IOException e) {
			e.printStackTrace();
		}

	}
	
	/**
	 * ������ִ���ض����ܺ����������Ǹ�����Բ����Ĺ���
	 * @param string Բ�İ뾶
	 * @return Բ�����
	 */
	public static String dealWith(String string,int ci){
		System.out.print("SC"+ci+"���յ��İ뾶ֵ��"+string+"����");	
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

