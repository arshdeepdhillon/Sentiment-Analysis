import java.io.*;

public class splitSentiment {
	public static void main(String[] args){
		splitSentiment ss = new splitSentiment();
		ss.doWork();
	}

	private void doWork(){

		try{
			BufferedReader br1 = new BufferedReader(new FileReader("reviews.txt"));
			BufferedReader br2 = new BufferedReader(new FileReader("labels.txt"));
			BufferedWriter bw1 = new BufferedWriter(new FileWriter("negative.txt"));
			BufferedWriter bw2 = new BufferedWriter(new FileWriter("positive.txt"));

			String rLine;
			String lLine;
			while((rLine = br1.readLine()) != null){
				if ((lLine = br2.readLine()) != null){
					if (lLine.equals("negative")){
						bw1.write(rLine);
						bw1.newLine();
					} else if (lLine.equals("positive")){
						bw2.write(rLine);
						bw2.newLine();
					}
				}
			}
			br1.close();
			br2.close();
			bw1.close();
			bw2.close();
		} catch (Exception e){
			System.out.println("IO ERROR");
		}

	}
}