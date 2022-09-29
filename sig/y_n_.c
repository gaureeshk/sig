#include <stdio.h>
#include <math.h>
int main() {
int x[6]={1,2,3,4,2,1};
float y[20];
y[0]=x[0];
y[1]=x[1]-y[0]/2;
for(int i=2;i<20;i++){
if(i<6){
	y[i]=x[i]+x[i-2]-y[i-1]/2;
}

else if(i>5 && i<8){
	y[i]=x[i-2]-y[i-1]/2;

}
else
{
	y[i]=-y[i-1]/2;
}
}
for(int j=0;j<20;j++){
printf("y[%d]=%f\n",j,y[j]);
}
FILE *f1=NULL;
FILE *f2=NULL;
f1=fopen("x.dat","w");
f2=fopen("y.dat","w");
for(int z=0;z<20;z++)
{
if(z<6)
{
fprintf(f1,"%d\n",x[z]);
}
fprintf(f2,"%f\n",y[z]);
}
}
