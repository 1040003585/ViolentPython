//--------------- �ļ�����Client.java ----------------------------------------------------------------
package _4_3Socket���ʾ��._4_4_2һ�Զ��ͨ��;
import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.net.UnknownHostException;

/**
 * _4_3Socket���ʾ��._4_4_2һ�Զ��ͨ��;
 * Copyright ? 2016 Authors. All rights reserved.
 *
 * FileName: .java
 * @author : Wu_Being <1040003585@qq.com>
 * Date/Time: 2016-6-8/����12:15:10
 * Description: �ͻ�������Բ�İ뾶�����͵��÷��������㣬���յ����
 */
public class Client {
	
	public static void main(String[] args) {
		
		try {
			//�������ӵ���������socket��������IP�Ͷ˿�����
			Socket connectToServerSocket = new Socket("localhost",9955);
			//������������������ӵ�socket��
			DataInputStream inFromServer = new DataInputStream(connectToServerSocket.getInputStream());
			DataOutputStream outToServer = new DataOutputStream(connectToServerSocket.getOutputStream());
			
			System.out.println("C����뾶��ֵ���͵�������������end����");
			boolean goon=true;
			//���ݴ��ն�����
			BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
			//�������û������ݲ�����
			while(goon){
				String outString=bf.readLine();		//���ݴ��ն�����
				outToServer.writeUTF(outString);			//д��Socket dos��
				outToServer.flush();						//��ջ���������������
				String inString=inFromServer.readUTF();		//��Socket dis�ж�����
				if(!inString.equals("end")){
					System.out.println("C�ӷ��������صĽ���ǣ���"+inString+"��");
				}else{
					goon=false;
					System.out.println("C�������������");
				}
			}
			//�ر�socket����
			connectToServerSocket.close();
			inFromServer.close();
			outToServer.close();
			
		} catch (UnknownHostException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
}
