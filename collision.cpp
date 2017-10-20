// Copyright 2017 Keval_Khara kevalk@bu.edu

#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

vector<int> inputs;

//int main(int argc, char* argv[])
//{



	// int time[argc-1];
	// //stringstream ss(argv);
	// string x;

	// for(int i=0;i<(argc-1);i++)			//loop to store all the input time values
	// {
	// 	time[i]=atoi(argv[i+1]);
	// }

	// while(cin>>x)
	// {
	// 	inputs.push_back(x);
	// }

	// if(argv!=NULL)
	// {
	// 	while(getline(ss,inputs,'\n')){
	// 		cout<<inputs<<endl;
	// 	}
	// }

	// //new positions when they are not colliding
	// for(int j=0;j<(argc-1);j++)
	// {
	// 	for(int i=0;i<(time[j]);i++)
	// 	{
	// 		newp1x[j]=v1x*time[j];
	// 		newp2x[j]=v2x*time[j];

	// 		newp1y[j]=v1y*time[j];
	// 		newp2y[j]=v2y*time[j];
	// 	}

	// 	//velocities remain same
	// }
	
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
