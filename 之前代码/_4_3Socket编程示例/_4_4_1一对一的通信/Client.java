//--------------- �ļ�����Client.java ----------------------------------------------------------------
package _4_3Socket���ʾ��._4_4_1һ��һ��ͨ��;
import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.net.UnknownHostException;
/**
 * _4_3Socket���ʾ��._4_4_1һ��һ��ͨ��
 * Copyright ? 2016 Authors. All rights reserved.
 *
 * FileName: Client.java
 * @author : Wu_Being <1040003585@qq.com>
 * Date/Time: 2016-6-7/����02:07:58
 * Description: �ͻ�������Բ�İ뾶�����͵��÷��������㣬���յ����
 */
public class Client {
	
	public static void main(String[] args) {
		
		try {
			//�������ӵ���������socket��������IP�Ͷ˿�����
			Socket socket = new Socket("localhost",9955);
			//������������������ӵ�socket��
			DataInputStream dis = new DataInputStream(socket.getInputStream());
			DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
			
			System.out.println("C����뾶��ֵ���͵�������������end����");
			boolean goon=true;
			//���ݴ��ն�����
			BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
			//�������û������ݲ�����
			while(goon){
				String outString=bf.readLine();		//���ݴ��ն�����
				dos.writeUTF(outString);			//д��Socket dos��
				dos.flush();						//��ջ���������������
				String inString=dis.readUTF();		//��Socket dis�ж�����
				if(!inString.equals("end")){
					System.out.println("C�ӷ��������صĽ���ǣ�"+inString);
				}else{
					goon=false;
					System.out.println("C�������������");
				}
			}
			//�ر�socket����
			socket.close();
			dis.close();
			dos.close();
			
		} catch (UnknownHostException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
}
