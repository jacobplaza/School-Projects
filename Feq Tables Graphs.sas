/*Question 1*/

data patientinfo; 
input ID$ 1-3 Gender$ 6 Race$ 8 - 24 CollegeEducated$ 29 - 31;
Datalines;
003  F Hispanic             Yes
008  F African American     Yes
007  M Hispanic             Yes
010  F Asian                No
006  M African American     No
004  M African American     Yes
002  M Asian                Yes
009  F Asian                Yes
005  F Hispanic             Yes
001  M White                Yes
;

Proc Sort data = patientinfo;
By ID;
Run;

Libname permdata "/home/u60672671/sasuser.v94";
run;

Proc Sort data = permdata.patientdata;
By ID;
Run;

Data patientvitals;
Set patientinfo permdata.patientdata;
weightkg = weight *(0.45359237);
heightm = height *(0.0254);
BMI = (weightkg)/(heightm)**2;
Averagebp = (1/3)*(sbp) + (2/3)*(dbp);
Run;

Proc means data = patientvitals Mean Median STD P95;
var BMI Averagebp;
run;

Proc Sort data = patientvitals;
By ID; 
Run;

Data merged;
Merge patientinfo patientvitals; 
By ID; 
Run;

Proc Print data=merged;
ID;
Run;

Proc Sort data = merged;
By Gender;
Run;

Proc boxplot data = merged;
plot BMI*gender;
run;

/*Question 2*/

Proc Import Out = boston
	datafile = "/home/u60672671/sasuser.v94/Boston.csv"
	DBMS = csv
	replace;
		Getnames = yes;
	run;
			
			
Proc means data = boston mean median std qrange skewness;
var crim tax medv;
where medv > 19;
run;

Proc means data = boston mean median std qrange skewness;
var crim tax medv;
where medv <= 19;
run;

data river;
set boston;
by chas; 
where chas = 1;
run;

data not_river;
set boston;
by chas;
where chas = 0;
run;

Proc Univariate data = river noprint;
Title("River-Bound Boston Neighborhoods by Crime Rate");
Histogram crim;
inset mean = 'Mean'(5.3) std = 'Std Dev' (5.3) kurtosis = 'Kurtosis'(5.3) skewness='Skewness'(5.3);
run;

Proc Univariate data = not_river noprint;
Title("Non-River-Bound Boston Neighborhoods by Crime Rate");
Histogram crim;
inset mean = 'Mean'(5.3) std = 'Std Dev' (5.3) kurtosis = 'Kurtosis'(5.3) skewness='Skewness'(5.3);
run;

/* Discuss the difference in skewness and kurtosis that you observe between the two graphs.
/* The second graph, showing the housing developments which are not river bound, have much higher skewness and kurtosis. 
/* Therefore, as far as skewness goes, the second graph is far more assymetrical, with the data leaning far more to the left.
/* The higher kurtosis value also suggests there are more outliers.
/* Therefore, both of these measures suggest that with non-river bound properties, crime rates are much more concentrated geographically
/* While in river-bound neighborhoods, crime rates are lower and more spread out. /*



