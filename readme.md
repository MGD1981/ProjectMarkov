Two ways of generating Markov language chains (plus an html text scraper)!
==========================================================================
markov_in_line.py
-----------------
Without first having researched methods of creating a Markov language chain, my first idea was to convert the source text into a long string, choose the first word at random, and then move the string's index to any of the instances of the first word (chosen at random), plus one.  This worked rather well, as far as I was initially concerned, although it was later pointed out to me that my method of finding every instance of that word in the string for every jump was relatively slow.  A timestamp clocking the execution was added later for comparison.

The program does not run on its own at this point, but contains the primary chain generation function (`def genchain(textsource, length=500)` where textsource is a string), which returns a string `length` words long.

markov_hashed.py
----------------
For much greater efficiency, this Markov chain generator first iterates over the source text and creates a hash table, where every unique word in the source is a key and every word found ever found after that word is a value.  The generation function then uses that hash table to determine the next word in the new text, rather than re-iterating over the string.

Unlike markov_in_line.py, this program is executable from the command prompt, taking the source text file as an argument.

markov_launcher.py
------------------
A way to launch markov_in_line.py from the command prompt, taking the source text file as an argument.

markov_url.py
-------------
Another method of launching markov_in_line.py from the terminal, retreiving the source text from a url rather than a file.  The url may be given as an argument in the command line, but the program will ask for it if none is given (defaults to my personal blog).  Content retrieved is then parsed by htmlslicer.py, then run through markov_in_line.py.

htmlslicer.py
-------------
A very hack-y way to parse content intended to be read from an html file, the program contains a number of functions which slices out unwanted text using various criteria (e.g. text enclosed between `<` and `>`).
