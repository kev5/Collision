// Copyright 2017 Keval_Khara kevalk@bu.edu

#include <iostream> 
#include <string> 
#include <sstream> 
#include <vector>
#include <math.h>
//#include <typeinfo>

using namespace std; 

float col_time(float,float,float,float,float,float,float,float);

int main (int argcount, char **time) 
{ 
  string mystr,idi; 
  float xi,yi,vxi,vyi,ti;
  vector<string> id; 
  vector<float> x;
  vector<float> y;
  vector<float> vx;
  vector<float> vy;
  vector<float> t;
  stringstream ss;

  //loop for storing the time values
  for(int i=1;time[i]!=NULL;i++)
  {
  	ss<<time[i];
    ss>>ti;
  	if(ss.fail())
    	return 2;
    t.push_back(ti);
    ss.str("");
    ss.clear();
    
  }

  //loop for storing the ID, positions, velocities
  while(!cin.eof())
  {
  	getline (cin,mystr);
  	if(mystr.length()!=0)
  	{
    	stringstream ss;
    	ss<<mystr;
    	ss>>idi>>xi>>yi>>vxi>>vyi;
    	if(ss.fail())
      		return 1;
    id.push_back(idi);
    x.push_back(xi);
    y.push_back(yi);
    vx.push_back(vxi);
    vy.push_back(vyi);
  }  
}

float ct; 
ct = col_time(x[0], x[1], y[0], y[1], vx[0], vx[1], vy[0], vy[1]);

	
int main(){


	float p1x, p2x, p1y, p2y, v1x, v2x, v1y, v2y;
	cout<<"Enter p1x: ";
	cin>>p1x;

	cout<<"Enter p1y: ";
	cin>>p1y;

	cout<<"Enter v1x: ";
	cin>>v1x;

	cout<<"Enter v1y: ";
	cin>>v1y;

	cout<<"Enter p2x: ";
	cin>>p2x;

	cout<<"Enter p2y: ";
	cin>>p2y;

	cout<<"Enter v2x: ";
	cin>>v2x;

	cout<<"Enter v2y: ";
	cin>>v2y;


	//velocities chaning after collision
	float diffpos_x = p1x-p2x;
	float diffpos_y = p1y-p2y;

	float diffvel_x = v1x-v2x;
	float diffvel_y = v1y-v2y;

	float num1 = ((diffpos_x*diffvel_x)+(diffpos_y*diffvel_y));  
	float num2 = (num1 * diffpos_x);
	float num3 = (num1 * diffpos_y);
	float den = (diffpos_x + diffpos_y)*(diffpos_x + diffpos_y);
	float num4 = num2/den;
	float num5 = num3/den;

	float newv1x = v1x-num4;
	float newv1y = v1y-num5;

	float totalvx = v1x+v2x;
	float totalvy = v1y+v2y;

	float newv2x = totalvx - newv1x;
	float newv2y = totalvy - newv1y;

	cout<<newv1x<<'\n';
	cout<<newv1y<<'\n';
	cout<<newv2x<<'\n';
	cout<<newv2y<<'\n';


}
