package _4_3Socket���ʾ��._4_4_4�򵥵��������;

import java.awt.BorderLayout;
import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

/**
 * 
 * Copyright ? 2016 Authors. All rights reserved.
 *
 * FileName: .java
 * @author : Wu_Being <1040003585@qq.com>
 * Date/Time: 2016-6-9/����12:20:18
 * Description:
 */
public class ChatClient implements ActionListener, Runnable {

	JTextField msgTextField;
	JTextArea showTextArea;
	JFrame mainJFrame;
	JButton sentButton;
	JScrollPane jSPane;
	JPanel panel;// Ƕ��
	Container container;// ����

	Thread thread = null;
	ServerSocket serverSocket;
	Socket connectToClientSocket;
	DataInputStream inFromClient;
	DataOutputStream outToClient;

	public ChatClient() {
		// ���ý��棬��������
		mainJFrame = new JFrame("���졪���ͻ��ˣ������");
		container = mainJFrame.getContentPane();
		// ������Ϣչʾ��
		showTextArea = new JTextArea();
		showTextArea.setEditable(false); // ���ɱ༭
		showTextArea.setLineWrap(true); // �Զ�����
		jSPane = new JScrollPane(showTextArea);
		// ������Ϣ�����
		msgTextField = new JTextField();
		msgTextField.setColumns(30); // ����򳤶�
		msgTextField.addActionListener(this);/**/// ?
		// ���Ͱ���
		sentButton = new JButton("����");
		sentButton.addActionListener(this);/**/
		// Ƕ����������Ϣ�����ͷ��Ͱ���
		panel = new JPanel();
		panel.setLayout(new FlowLayout());
		panel.add(msgTextField);
		panel.add(sentButton);
		// ��������������Ϣչʾ���Ƕ��
		container.add(jSPane, BorderLayout.CENTER);
		container.add(panel, BorderLayout.SOUTH);
		// �����棬Ҫ�����ں���
		mainJFrame.setSize(500, 400);
		mainJFrame.setVisible(true);
		mainJFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		try {
			// �����׽������ӵ�������
			connectToClientSocket = new Socket("192.168.1.100", 9988);/**/
			inFromClient = new DataInputStream(connectToClientSocket
					.getInputStream());
			outToClient = new DataOutputStream(connectToClientSocket
					.getOutputStream());
			showTextArea.append("���ӳɹ�����˵��..." + getTime() + "\n");

			// �����߳��ں�̨�����նԷ�����Ϣ
			thread = new Thread(this);
			thread.setPriority(Thread.MAX_PRIORITY);
			thread.start();

		} catch (IOException e) {
			showTextArea.append("�Բ���û�����ӵ�������" + getTime() + "");
			msgTextField.setEditable(false); // ���ɱ༭
			msgTextField.setEnabled(false); // ���ɼ�
		}

	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new ChatClient();
	}

	// ��Ӧ��ť�¼���������Ϣ���Է�
	@Override
	public void actionPerformed(ActionEvent e) {

		String string = msgTextField.getText();
		if (string.length() > 0) {
			try {
				outToClient.writeUTF(string);
				outToClient.flush();
				showTextArea.append("���˵��" + string + "��" + getTime() + "\n");
				msgTextField.setText(null);
			} catch (IOException e1) {
				showTextArea.append("�����Ϣ��" + string + "��δ�ܷ��ͳ�ȥ" + getTime()
						+ "\n");
			}
		}
	}

	@Override
	public void run() {
		try {
			while (true) {
				showTextArea.append("��è˳˵��" + inFromClient.readUTF() + "��"
						+ getTime() + "\n");
				Thread.sleep(1000);
			}
		} catch (IOException e) {
		} catch (InterruptedException e) {
			thread.start();
		}
	}

	/**
	 * Java�����л�õ�ǰʱ��
	 * 
	 * @return ��ǰʱ��ʱ��
	 */
	private String getTime() {
		Date date = new Date();
		DateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		String time = format.format(date);
		return time;
	}
}
