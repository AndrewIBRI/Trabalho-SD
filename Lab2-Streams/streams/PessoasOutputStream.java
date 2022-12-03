package streams;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.EOFException;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.io.PrintStream;
import java.net.Socket;
import java.net.UnknownHostException;

import entidades.Pessoa;

public class PessoasOutputStream extends OutputStream {
	
	private OutputStream op;
	private Pessoa[] pessoas;
	
	public PessoasOutputStream() {}
	
	public PessoasOutputStream(Pessoa[] p, OutputStream os) {
		this.pessoas = p;
		this.op = os;
	}

	public void writeSystem() {
		
		PrintStream opLocal = new PrintStream(op);
		
		//envia quantidade de pessoas;
		int qtdpessoa = pessoas.length;
		opLocal.println("Quantidade de pessoas: "+qtdpessoa);
		
		//envia os dados de um conjunto (array) de Pessoas
		for (Pessoa pessoa : pessoas) {
			if (pessoa != null) {
				int tamanhoNomePessoa = pessoa.getNome().getBytes().length;
				String nome = pessoa.getNome();
				double cpf = pessoa.getCpf();
				int idade = pessoa.getIdade();
							
				opLocal.println(" tamanhoNomePessoa: "+tamanhoNomePessoa+ "\n"+
								" nomePessoa: "+nome+ "\n"+
								" cpf: "+cpf+ "\n"+
								" idade: "+idade);
			}
		}
	}

	public void writeFile() {
		   
        FileOutputStream fout = null;
		try {
			fout = new FileOutputStream("D:\\testout.txt");
		} catch (FileNotFoundException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}    
        for (Pessoa pessoa : pessoas) {
			if (pessoa != null) {
				int tamanhoNomePessoa = pessoa.getNome().getBytes().length;
				String nome = pessoa.getNome();
				long cpf = pessoa.getCpf();
				int idade = pessoa.getIdade();
							
				String s=" tamanhoNomePessoa: "+tamanhoNomePessoa+ "\n"+
						" nomePessoa: "+nome+ "\n"+
						" cpf: "+cpf+ "\n"+
						" idade: "+idade;    
		        byte b[]=s.getBytes();//converting string into byte array    
		        
		        try {
					fout.write(b);
					fout.close();
					System.out.println("successo");   
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}    
		        
			}
		}
                
	}
	
	public void writeTCP() {  
		Socket socket = null;
        for (Pessoa pessoa : pessoas) {
			if (pessoa != null) {
				int tamanhoNomePessoa = pessoa.getNome().getBytes().length;
				String nome = pessoa.getNome();
				long cpf = pessoa.getCpf();
				int idade = pessoa.getIdade();
		        try {
		        	int serverPort = 7896;
					socket = new Socket("localhost", serverPort);
					DataInputStream in = new DataInputStream(socket.getInputStream());
					DataOutputStream out = new DataOutputStream(socket.getOutputStream());
					String envio = " tamanhoNomePessoa: "+tamanhoNomePessoa+ "\n"+
							" nomePessoa: "+nome+ "\n"+
							" cpf: "+cpf+ "\n"+
							" idade: "+idade;
					System.out.println("Sent: "+envio);
					out.writeUTF(envio); // UTF is a string encoding see Sn. 4.4
					String data = in.readUTF(); // read a line of data from the stream
					System.out.println("Received: " + data);
					System.out.println("successo");   
				} catch (UnknownHostException e) {
					System.out.println("Socket:" + e.getMessage());
				} catch (EOFException e) {
					System.out.println("EOF:" + e.getMessage());
				} catch (IOException e) {
					System.out.println("readline:" + e.getMessage());
				} finally {
					if (socket != null)
						try {
							socket.close();
						} catch (IOException e) {
							System.out.println("close:" + e.getMessage());
						}
				}  
		        
			}
		}
	}		
	
	@Override
	public void write(int b) throws IOException {
		// TODO Auto-generated method stub
	}

	@Override
	public String toString() {
		return "Ola, mundo! Estamos sobrescrevendo o método toString()!\n"
				+ " PessoasOutputStream [ \n"
				+ " getClass()=" + getClass() +",\n"
				+ " hashCode()=" + hashCode() +",\n"
				+ " toString()="+ super.toString() + "]";
	}
}

