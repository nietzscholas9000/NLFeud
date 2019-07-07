This game was created for a SEIS 603: foundations of software development.
I plan to continue developing this project, so any and all feedback is welcome.

THanks for checking this out! =)

..............GAMEPLAY....
This game is played with output of questions and input of answers by user to the interpreter window.

To play, just follow the prompts displayed from the program when it is run.

This is a Family Feud style game. The game asks for two teams,
but you may run the program by yourself,
inputting whichever team you desire between rounds (1 or 2).

During each round, a new question is displayed.
The current team will be able to guess until there are
no answers left or they have guessed three wrong answers to the question.
If there are three "strikes", the opposing team gets a chance to steal the round points.


~DEPENDENCIES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To use this game, you will need NLTK module (natural language tool kit),
including the wordnet corpus. NLTK wordnet may require numpy to be installed (dependency for some of NLTK).

    in your terminal run the command:

        conda install nltk

    in your python console:

        import nltk
        nltk.download()

    nltk.download() will open a GUI window from you python console. Here you should click on the corpora tab,
    scroll down and select WordNet, then hit Download.

This program also uses the CSV module, should be included with your python distribution.


______DATA_________________
the questions and answers for this game are taken from csv files.
There are several csv files included with this program, each containing questions with a different
number of answers.

This program can accept any csv file with the following column format (up through 7),
where "#N" contains the points assigned to Answer N

(  Question, Answer 1, #1, ..., Answer N, #N  )




----Potential issues & future improvements----------

I did not make the questions/answers myself so there there may be errors in spelling.
Some issues with answers including "a" (e.g., a cell phone) or plural answers in csv files.
I have not yet created a way to handle multi-word answers.
Reformatting game_round(), which is a very long function. Or some inner loops/tests into functions.
I will likely create a proper object-oriented structure once ironed out my comparison method in game_round().
More robust comparison method: currently testing for membership, previously used the intersection of sets.
Consider other tools from wordnet such as similar_tos().




/////////acknowledgements////////////////////////////////////////////////////////

Special thanks to Prof. Eric V. Level for his wonderful teaching and inspiration.

Thanks to Lawrence Aderinkomi for giving me the original idea.

Also, S/O to u/007craft on reddit for creating the excel file that I've included with this project.

    https://www.reddit.com/r/trivia/comments/3wzpvt/free_database_of_50000_trivia_questions/