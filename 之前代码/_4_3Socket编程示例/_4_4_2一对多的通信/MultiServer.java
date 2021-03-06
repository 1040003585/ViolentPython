//------------------- 文件名MultiServer.java ------------------------------------------------
package _4_3Socket编程示例._4_4_2一对多的通信;

import java.net.ServerSocket;
import java.net.Socket;

/**
 * _4_3Socket编程示例._4_4_2一对多的通信;
 * Copyright ? 2016 Authors. All rights reserved.
 *
 * FileName: MultiServer.java
 * @author : Wu_Being <1040003585@qq.com>
 * Date/Time: 2016-6-7/下午11:12:51
 * Description: 这是主程序，它只要简单地启动线程就可以了。
 */
public class MultiServer {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("S启动......");
		try {
			ServerSocket serverSocket = new ServerSocket(9955);
			Socket connectToClientSocket=null;
			int i=0;
			while(++i!=0){
				//等待客户端的请求
				connectToClientSocket=serverSocket.accept();
				//每次请求都启动一个线程来处理
				new ServerThread(connectToClientSocket,i);
			}
		}
		catch (Exception e) {
		}
	
	}
}
