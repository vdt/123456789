# Crazy Sequential Representation for Numbers

Paper: [Crazy Sequential Representation: Numbers from 0 to 11111 in terms of Increasing and Decreasing Orders of 1 to 9](https://arxiv.org/abs/1302.1479)

The paper gives a sequential representation for the first 11111 numbers. A
sequential representation is one in which the digits `1, 2, 3, 3, 4, 5, 6, 7, 8, 9`
appear in ascending order (or descending order).

For example:

    1^2 - 34*5 + 6789    = 6620
    (1^2)*3*4*5*6*7 - 89 = 4950

While the paper gives representation for all of the first 11,111 numbers,
I thought I could write a quick python program to do this.

And I found representations for about 6,280 numbers. I don't have the entire list
probably because I haven't included parantheses?

Check out the [output](output) file.
