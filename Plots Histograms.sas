/*question1
*/


data adoption;
infile "/home/u60672671/adoption.txt";
length country $ 12;
input country $ Year$ Adoptions;
run;


Proc Gchart data = adoption;
hbar year/sumvar = adoptions type = sum;
run;

Proc sort data = adoption;
by country;
run;
Proc Gchart data = adoption;
vbar year /sumvar = adoptions type =sum group = country;
Where country in ('China', 'Russia', 'Guatemala', 'Ethiopia');
run;

Proc Gchart data = adoption;
vbar year /sumvar = adoptions type =sum group = country;
Where country in ('South Korea', 'Colombia', 'Ukraine', 'Haiti', 'Vietnam');
run;



Proc gchart data = adoption;
pie year/sumvar = adoptions type = sum;
run;

Proc sort data = adoption;
by country;
run;

symbol1 value = "circle" color = blue I = join;
symbol2 value = "circle" color = red I = join;
symbol3 value = "circle" color = orange I = join;
symbol4 value = "circle" color = purple I = join;
Proc gPlot data = adoption;
plot adoptions * year = country;
Where country in ('China', 'Russia', 'Guatemala', 'Ethiopia');
run;

/*
question2
*/

Proc Import datafile= "/home/u60672671/Pyeongchang 2018 Winter Olympics.xlsx" out= work.olympic dbms = xlsx replace;
Getnames=Yes;
run;

Data olympicsdata;
Set olympic;
run;



Proc Gchart data = olympicsdata;
hbar country/group=medal discrete;
run;

/*question3
*/

Proc import datafile = "/home/u60672671/rollercoasters.csv" out = coasters dbms = csv;
Getnames=yes;
run;

Data rollercoasters;
Set coasters;
length excitement_rating $ 8 nausea_rating $ 8;
if excitement <5 then excitement_rating = "A_low";
if 5<= excitement< 7 then excitement_rating = "B_Medium";
if excitement >= 7 then excitement_rating = "C_High";
if nausea < 4 then nausea_rating = "A_Low";
if nausea >= 4 then nausea_rating = "B_High";
run;

Proc freq data = rollercoasters order = freq;
tables excitement_rating nausea_rating;
run;

Proc freq data = rollercoasters;
Tables excitement_rating * nausea_rating;
Title "2x2 of Excitement and Nausea Ratings";
run;