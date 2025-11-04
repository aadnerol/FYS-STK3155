**Evaluation of project number:** 1

**Name:** Bror Johannes Tidemand Ruud (640394), Egil Furnes (693784) & Ã…dne Rolstad (693783)

## Abstract
*Abstract: accurate and informative? Total number of possible points: 5*

Mark and comments: 5
Great title! And very good abstract - could perhaps have mentioned the implications more, but overall good. 

## Introduction
*Introduction: status of problem and the major objectives. Total number of
possible points: 10*

Mark and comments: 9
Overall very good, but you could have motivated GD/SGD and resampeling better (-1p) - what is the point of this part of the project?

## Formalism
*Formalism/methods: Discussion of the methods used and their basis/suitability.
Total number of possible points 20*

Mark and comments: 18
* Scaling is not criticaly discussed: how does it affect the different regression models? (-1p)
* Regularization is minially discussed: what is the purpose of driving coefficiencts to zero (-1p)
* Good description of GD and learning rate and adaptive methods


## Code, implementation and testing
*Code/Implementations/test: Readability of code, implementation, testing and
discussion of benchmarks. Total number of possible points 20*

Mark and comments: 18
Well documented and clean, but there is quite a lot of repetition. It would have been better to make one GD function that where you can pass the gradient and method of tuning (-1p). It would have reduced 750 lines to 50. You could also made the same model work as a SGD (-1p). The functions are not very generalizable when the tuning and gradient are hardcoded in. 
Good testing!

## Analysis
*Analysis: of results and the effectiveness of their selection and presentation.
Are the results well understood and discussed? Total number of possible points:
20*

Mark and comments: 20
Very good work! 
* You did not define number of datapoints - data should be better explained 
* I like how you use Figure 4 and 6 in your discussion

## Conclusions
*Conclusions, discussions and critical comments: on what was learned about the
method used and on the results obtained. Possible directions and future
improvements? Total number of possible points: 10*

Mark and comments: 9
Very good. You could have been clearer on the motivation of using GD and SGD (-1p), i.e. with a different number o f datapoints or size of noise they could have compared better

## Overall presentation:
*Clarity of figures, tables, algorithms  and overall presentation. Too much or too little? Total number of possible points: 10*

Mark and comments: 10
Great!

## Referencing
*Referencing: relevant works cited accurately? Total number of possible points 5*

Mark and comments: 4
* Not cited: Runge, adaptive methods, Ridge, Lasso

## Overall 95
*Overall mark in points (maximum number of points per project is 100) and final possible final comments*

