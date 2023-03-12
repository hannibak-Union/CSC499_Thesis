* Encoding: UTF-8.

*repeat this for each of the 10 aCOMPUTE rTIPI6 = 8 - Tipi6.

COMPUTE rTIPI2 = 8 - Tipi2.
EXECUTE.
COMPUTE rTIPI8 = 8 - TIPI8.
EXECUTE.
COMPUTE rTIPI4 = 8 - Tipi4.
EXECUTE.
COMPUTE rTIPI10 = 8 - Tipi10.
EXECUTE.

***Extrav =Extraversion. 
    *Agree = Agreeableness.  
   *Consc = Conscientiousness. 
   *Neur= Neuroticism. 
   *Open = Openness.***.

COMPUTE Extrav = (Tipi1+rTIPI6)/2.
EXECUTE.
COMPUTE Agree = (rTIPI2+Tipi7)/2. 
EXECUTE.
COMPUTE Consc = (TIPI3+rTIPI8)/2.
EXECUTE.
COMPUTE Neur = (rTIPI4+TIPI9)/2. 
EXECUTE.
COMPUTE Open = (TIPI5+rTIPI10)/2.
EXECUTE.

*Articles coding.

COMPUTE PosSelection = 0.
COMPUTE NegSelection = 0.
COMPUTE NeuSelection = 0.
COMPUTE CompSelection = 0.
EXECUTE.

if(Articles#1=1) PosSelection=PosSelection+1.
if(Articles#1=2) NegSelection=NegSelection+1.
if(Articles#1=3) CompSelection=CompSelection+1.
if(Articles#1=4) NeuSelection=NeuSelection+1.
EXECUTE.

if(Articles#2=1) PosSelection=PosSelection+1.
if(Articles#2=2) NegSelection=NegSelection+1.
if(Articles#2=3) CompSelection=CompSelection+1.
if(Articles#2=4) NeuSelection=NeuSelection+1.
EXECUTE.

if(Articles#3=1) PosSelection=PosSelection+1.
if(Articles#3=2) NegSelection=NegSelection+1.
if(Articles#3=3) CompSelection=CompSelection+1.
if(Articles#3=4) NeuSelection=NeuSelection+1.
EXECUTE.

if(Articles#4=1) PosSelection=PosSelection+1.
if(Articles#4=2) NegSelection=NegSelection+1.
if(Articles#4=3) CompSelection=CompSelection+1.
if(Articles#4=4) NeuSelection=NeuSelection+1.
EXECUTE.

if(Articles#5=1) PosSelection=PosSelection+1.
if(Articles#5=2) NegSelection=NegSelection+1.
if(Articles#5=3) CompSelection=CompSelection+1.
if(Articles#5=4) NeuSelection=NeuSelection+1.
EXECUTE.

if(Articles#6=1) PosSelection=PosSelection+1.
if(Articles#6=2) NegSelection=NegSelection+1.
if(Articles#6=3) CompSelection=CompSelection+1.
if(Articles#6=4) NeuSelection=NeuSelection+1.
EXECUTE.

if(Articles#7=1) PosSelection=PosSelection+1.
if(Articles#7=2) NegSelection=NegSelection+1.
if(Articles#7=3) CompSelection=CompSelection+1.
if(Articles#7=4) NeuSelection=NeuSelection+1.
EXECUTE.

if(Articles#8=1) PosSelection=PosSelection+1.
if(Articles#8=2) NegSelection=NegSelection+1.
if(Articles#8=3) CompSelection=CompSelection+1.
if(Articles#8=4) NeuSelection=NeuSelection+1.
EXECUTE.

if(Articles#9=1) PosSelection=PosSelection+1.
if(Articles#9=2) NegSelection=NegSelection+1.
if(Articles#9=3) CompSelection=CompSelection+1.
if(Articles#9=4) NeuSelection=NeuSelection+1.
EXECUTE.

if(Articles#10=1) PosSelection=PosSelection+1.
if(Articles#10=2) NegSelection=NegSelection+1.
if(Articles#10=3) CompSelection=CompSelection+1.
if(Articles#10=4) NeuSelection=NeuSelection+1.
EXECUTE.

compute xxduco=durationinseconds*compselection.
execute.

DATASET ACTIVATE DataSet1.
CORRELATIONS
  /VARIABLES=NegSelection PosSelection NeuSelection CompSelection with Extrav Agree Consc Open Neur
  /PRINT=TWOTAIL NOSIG FULL
  /MISSING=PAIRWISE.
