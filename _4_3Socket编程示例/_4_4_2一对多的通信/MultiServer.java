//------------------- �ļ���MultiServer.java ------------------------------------------------
package _4_3Socket���ʾ��._4_4_2һ�Զ��ͨ��;

import java.net.ServerSocket;
import java.net.Socket;

/**
 * _4_3Socket���ʾ��._4_4_2һ�Զ��ͨ��;
 * Copyright ? 2016 Authors. All rights reserved.
 *
 * FileName: MultiServer.java
 * @author : Wu_Being <1040003585@qq.com>
 * Date/Time: 2016-6-7/����11:12:51
 * Description: ������������ֻҪ�򵥵������߳̾Ϳ����ˡ�
 */
public class MultiServer {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("S����......");
		try {
			ServerSocket serverSocket = new ServerSocket(9955);
			Socket connectToClientSocket=null;
			int i=0;
			while(++i!=0){
				//�ȴ��ͻ��˵�����
				connectToClientSocket=serverSocket.accept();
				//ÿ����������һ���߳�������
				new ServerThread(connectToClientSocket,i);
			}
		}
		catch (Exception e) {
		}
	
	}
}
