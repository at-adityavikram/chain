# chain
found a weird number pattern randomly, HAD to make a quick-and-dirty script to confirm it

just run the allgch() function with any range of your choice, say 1-512 and start the program.

randomly thought of the following algorithm, which produced some interesting behaviour. im no mathematician, so not sure why exactly it does most of that. some numbers dont behave at all, starting somewhere in the low thousands. when it does behave the endpoint makes sense, but its almost always a number composed eniterly of 9s.

>take a random number preferably greater than 1 digit
>subtract the reverse of that number from  it, and keep repeating this step with the following constraints:

>if the result is negative, add the absolute value of reverse, else subtract it

>this sequence, when it ends, will always end in zero, with the value of the second last step being a number composed entirely of 9s, as long as the number has atleast 2 different digits.

>the length of this sequence follows a repetitive pattern for all (seems so, not sure) groups n-digit numbers

can somebody make sense of this
