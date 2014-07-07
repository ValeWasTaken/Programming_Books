public class PhraseOMatic
{
	public static void main(String[]args)
	{
		// Three sets of words to choose from
		String[] wordListOne = 
			{"24/7","mult-Tier","30,000 foot","B-to-B","win-win",
			"front-end","web-based","pervasive","smart","six-sigma",
			"critical-path","dynamic","back-end","revolutionary"};
		String[] wordListTwo = 
			{"empowered","sticky","value-added","oriented","centric",
			 "distributed","clustered","branded","outside-the-box",
			 "networked","focused","leveraged","aligned","targeted",
			 "shared","cooperative","accelerated","unique","cloud"};
		String[] wordListThree =
			{"process","tipping-point","solution","architecture",
			 "core competency","strategy","mindshare","portal",
			 "space","vision","paradigm","mission","goal","product"};
		
		// Find length of each list
		int oneLength = wordListOne.length;
		int twoLength = wordListTwo.length;
		int threeLength = wordListThree.length;
		
		// Generate random a random number (word position)
		int rand1 = (int) (Math.random() * oneLength);
		int rand2 = (int) (Math.random() * twoLength);
		int rand3 = (int) (Math.random() * threeLength);
		
		// Creates a combination of 3 words randomly chosen from above.
		String phrase = wordListOne[rand1] + " " + wordListTwo[rand2] + " " + wordListThree[rand3];
		
		System.out.println("What we need is a " + phrase);
		// Example output: "What we need is a win-win outside-the-box strategy"
	}
}
